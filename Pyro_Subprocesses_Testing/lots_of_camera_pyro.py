"""
Flex Pyro/IPC stress: camera bursts, gripper, Temperature Module Gen2 concurrent tasks,
on-robot CSV I/O, and Absorbance Plate Reader single→multi (initialize each phase).

Deck (matches common QA patterns like Template plate_reader_Smoke + temp on D1):
- A3: waste chute
- B2: 50 µL tip rack
- C2: nest_96_wellplate_200ul_flat (staging + reader path)
- C3: absorbanceReaderV1
- D1: temperatureModuleV2 + aluminum block adapter

Flow:
- Five identical “rich” loops (camera + pipette motion + gripper to temp + concurrent temp task
  + CSV append + plate reader single/multi with intiialize).
- Then ``photo_burst_count`` captures with ``home_before=False`` (set RTP to 10000 for the
  soak described in older notes).

Additional Pyro IPC angles exercised here: large camera command volume, FlexGripper moves,
``start_set_temperature`` :class:``Task`` + ``wait_for_tasks``, filesystem CSV read/write on the
robot OS, and absorbance reader JSON-ish result dicts crossing the protocol boundary.
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import cast

from opentrons import protocol_api
from opentrons.protocol_api.module_contexts import AbsorbanceReaderContext

metadata = {
    "protocolName": "Lots of camera + peripherals (Pyro IPC Flex)",
    "author": "QA",
}

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.28",
}

CSV_PATH = Path("/tmp/pyro_ipc_qa_metrics.csv")


def add_parameters(parameters: protocol_api.Parameters) -> None:
    parameters.add_int(
        display_name="Burst captures (home_before=False)",
        variable_name="photo_burst_count",
        default=100,
        minimum=1,
        maximum=20000,
        description=(
            "Camera soak after the five main loops. Use ~10000 on hardware for Pyro/IPC stress; "
            "lower for dry runs. Simulation caps this automatically."
        ),
    )


def _plate_reader_single_then_multi(
    protocol: protocol_api.ProtocolContext,
    mod: AbsorbanceReaderContext,
    plate: protocol_api.Labware,
    pipette: protocol_api.InstrumentContext,
    tip_rack: protocol_api.Labware,
    waste: protocol_api.WasteChute,
    tip_index_first: int,
    loop_ix: int,
) -> None:
    """Initialize single read, then re-init for multi — same idea as plate_reader_Smoke."""
    tips = tip_rack.wells()
    pipette.pick_up_tip(tips[tip_index_first])
    pipette.aspirate(30, plate.wells_by_name()["A1"])
    pipette.dispense(30, plate.wells_by_name()["A1"])
    pipette.drop_tip(waste)

    mod.close_lid()
    mod.initialize("single", [600], reference_wavelength=450)

    mod.open_lid()
    protocol.move_labware(plate, mod, use_gripper=True)
    mod.close_lid()

    result_single = mod.read()
    protocol.comment(msg=f"loop {loop_ix} plate reader single: {result_single!s}"[:300])
    mod.read(export_filename=f"loop{loop_ix}_single")

    protocol.comment(msg="Perform multi read")
    mod.open_lid()
    protocol.move_labware(plate, "C2", use_gripper=True)
    mod.close_lid()

    mod.initialize("multi", [450, 562, 600])

    mod.open_lid()
    protocol.move_labware(plate, mod, use_gripper=True)

    pipette.pick_up_tip(tips[tip_index_first + 1])
    pipette.aspirate(30, plate.wells_by_name()["A1"])
    pipette.dispense(30, plate.wells_by_name()["A1"])
    pipette.drop_tip(waste)

    mod.close_lid()
    result_multi = mod.read()
    protocol.comment(msg=f"loop {loop_ix} plate reader multi: {result_multi!s}"[:300])
    mod.read(export_filename=f"loop{loop_ix}_multi")

    mod.open_lid()
    protocol.move_labware(plate, "C2", use_gripper=True)
    mod.close_lid()


def run(protocol: protocol_api.ProtocolContext) -> None:
    burst_total = protocol.params.photo_burst_count
    if protocol.is_simulating():
        burst_total = min(int(burst_total), 20)

    waste = protocol.load_waste_chute()
    tip_rack = protocol.load_labware("opentrons_flex_96_tiprack_50ul", "B2")
    plate = protocol.load_labware("nest_96_wellplate_200ul_flat", "C2")
    temp_mod = protocol.load_module("temperatureModuleV2", "D1")
    temp_adapter = temp_mod.load_adapter(
        "opentrons_96_well_aluminum_block",
        namespace="opentrons",
        version=1,
    )
    reader = cast(
        AbsorbanceReaderContext,
        protocol.load_module("absorbanceReaderV1", "C3"),
    )
    pipette = protocol.load_instrument(
        "flex_8channel_50",
        "right",
        tip_racks=[tip_rack],
    )

    main_loops = 5
    tips = tip_rack.wells()

    for loop in range(1, main_loops + 1):
        protocol.comment(msg=f"========== Pyro IPC main loop {loop}/{main_loops} ==========")

        # Three tips per loop: camera moves, reader pre-single, reader pre-multi.
        tip_base = (loop - 1) * 3

        protocol.capture_image(home_before=True, filename=f"L{loop}a_prehome")
        protocol.home()
        protocol.delay(seconds=1)

        pipette.pick_up_tip(tips[tip_base])
        pipette.move_to(plate.wells_by_name()["A4"].top())
        protocol.capture_image(home_before=True, filename=f"L{loop}b_after_move1")

        protocol.home()
        protocol.delay(seconds=1)

        pipette.move_to(plate.wells_by_name()["G8"].top())
        protocol.capture_image(home_before=True, filename=f"L{loop}c_after_move2")
        pipette.drop_tip(waste)

        # FlexGripper: hardware path to Temperature Module (stresses USB/CAN + Pyro-adjacent orchestration).
        protocol.move_labware(plate, temp_adapter, use_gripper=True)

        # Concurrent Temperature Module: async ramp while other commands run (API 2.27+ Task).
        td_task = temp_mod.start_set_temperature(celsius=30.0)
        protocol.delay(seconds=0.25)
        protocol.capture_image(home_before=True, filename=f"L{loop}d_temp_concurrent")
        protocol.wait_for_tasks([td_task])
        temp_mod.deactivate()

        protocol.move_labware(plate, "C2", use_gripper=True)

        # On-robot CSV: real filesystem I/O (path is on Linux robot; App run files also appear in UI for reader exports).
        write_header = not CSV_PATH.exists()
        with CSV_PATH.open("a", newline="") as fh:
            w = csv.writer(fh)
            if write_header:
                w.writerow(["loop", "note", "plate_slot"])
            w.writerow([loop, "post_temp_move", "C2"])
        csv_preview = CSV_PATH.read_text()[-800:]
        protocol.comment(msg=f"CSV tail ({CSV_PATH}): {csv_preview}")
        print(csv_preview)

        _plate_reader_single_then_multi(
            protocol,
            reader,
            plate,
            pipette,
            tip_rack,
            waste,
            tip_index_first=tip_base + 1,
            loop_ix=loop,
        )

    protocol.comment(msg=f"========== Burst capture: {burst_total} × capture_image(home_before=False) ==========")
    for i in range(burst_total):
        if i % 1000 == 0 and i > 0:
            protocol.comment(msg=f"Burst progress {i}/{burst_total}")
        protocol.capture_image(
            home_before=False,
            filename=f"b{i:05d}",
            zoom=2.0,
            contrast=10,
        )

    temp_mod.deactivate()
    protocol.comment("lots_of_camera_pyro: complete")
