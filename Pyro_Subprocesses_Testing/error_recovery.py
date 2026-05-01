"""
Flex error-recovery QA: pipette overpressure, plate reader + gripper, TC + concurrent
pipette activity, heater-shaker, and stacker + LLD with P50 8-channel.

Deck layout matches
``Flex_S_2_2_P200_96_GRIP_HS_MB_TC_TM_Overrides_SmokeTestWith2Stackers (9).py``:
TC (A1/B1), magnetic block A3, lid stack A4, tip adapter A2, absorbance B3,
HS C1, plate C2, stacker C4 + D4, reservoir D2, temperature module D1.

Uses API 2.27 so ``thermocycler.start_execute_profile`` and ``ctx.wait_for_tasks``
can overlap with pipette mixing (concurrent hardware). Docstring originally
requested 2.26; bump to 2.27 is required for that concurrent block.
"""

from opentrons import protocol_api

metadata = {
    "protocolName": "Pyro / Error recovery QA tour",
    "author": "QA",
}

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.27",
}

HEATER_SHAKER_ADAPTER_NAME = "opentrons_96_pcr_adapter"
HEATER_SHAKER_NAME = "heaterShakerModuleV1"
MAGNETIC_BLOCK_NAME = "magneticBlockV1"
TEMPERATURE_MODULE_ADAPTER_NAME = "opentrons_96_well_aluminum_block"
TEMPERATURE_MODULE_NAME = "temperature module gen2"
THERMOCYCLER_NAME = "thermocycler module gen2"
ABSORBANCE_READER = "absorbanceReaderV1"
DECK_RISER_NAME = "opentrons_flex_deck_riser"
TC_LID = "opentrons_tough_pcr_auto_sealing_lid"
TIPRACK_96_ADAPTER_NAME = "opentrons_flex_96_tiprack_adapter"
TIPRACK_96_1000 = "opentrons_flex_96_tiprack_1000ul"
TIPRACK_96_50 = "opentrons_flex_96_tiprack_50ul"
FLEX_STACKER = "flexStackerModuleV1"

WELL_PLATE_STARTING_POSITION = "C2"
RESERVOIR_STARTING_POSITION = "D2"
RESERVOIR_LOAD_NAME = "nest_1_reservoir_290ml"
WELL_PLATE_LOAD_NAME = "opentrons_96_wellplate_200ul_pcr_full_skirt"


def run(ctx: protocol_api.ProtocolContext) -> None:
    waste_chute = ctx.load_waste_chute()

    # --- Stackers (2-stack pattern from Flex_protocol_viz smoke) ---
    # Index 0 = first stacker (C4), index 1 = second stacker (D4).
    stacker_C4 = ctx.load_module(FLEX_STACKER, "C4")
    stacker_C4.set_stored_labware(TIPRACK_96_1000, count=0)

    stacker_D4 = ctx.load_module(FLEX_STACKER, "D4")
    stacker_D4.set_stored_labware(
        TIPRACK_96_1000, count=4, lid="opentrons_flex_tiprack_lid"
    )
    stackers = (stacker_C4, stacker_D4)
    second_stacker = stackers[1]

    # --- Modules ---
    thermocycler = ctx.load_module(THERMOCYCLER_NAME)
    ctx.load_module(MAGNETIC_BLOCK_NAME, "A3")
    heater_shaker = ctx.load_module(HEATER_SHAKER_NAME, "C1")
    temperature_module = ctx.load_module(TEMPERATURE_MODULE_NAME, "D1")
    absorbance_module = ctx.load_module(ABSORBANCE_READER, "B3")
    ctx.load_lid_stack(
        load_name=TC_LID,
        location="A4",
        quantity=5,
        adapter=DECK_RISER_NAME,
    )

    thermocycler.open_lid()
    heater_shaker.open_labware_latch()
    absorbance_module.close_lid()

    temperature_module.load_adapter(TEMPERATURE_MODULE_ADAPTER_NAME)
    heater_shaker_adapter = heater_shaker.load_adapter(HEATER_SHAKER_ADAPTER_NAME)

    # --- Labware ---
    pcr_plate = ctx.load_labware(WELL_PLATE_LOAD_NAME, WELL_PLATE_STARTING_POSITION)
    source_reservoir = ctx.load_labware(
        RESERVOIR_LOAD_NAME, RESERVOIR_STARTING_POSITION
    )
    pcr_plate.load_empty(pcr_plate.wells())

    tip_rack_adapter = ctx.load_adapter(TIPRACK_96_ADAPTER_NAME, "A2")
    tip_rack_50_on_deck = ctx.load_labware(TIPRACK_96_50, "C3")

    water = ctx.define_liquid(
        name="water", description="Aqueous", display_color="#42AB2D"
    )
    source_reservoir.wells_by_name()["A1"].load_liquid(liquid=water, volume=20000)

    tip_racks_1000: list = []
    p1000 = ctx.load_instrument(
        "flex_1channel_1000",
        mount="left",
        tip_racks=tip_racks_1000,
    )
    p1000.trash_container = waste_chute

    tip_racks_50: list[protocol_api.Labware] = [tip_rack_50_on_deck]
    p50 = ctx.load_instrument(
        "flex_8channel_50",
        mount="right",
        tip_racks=tip_racks_50,
        liquid_presence_detection=True,
    )
    p50.trash_container = waste_chute

    # --- Tips for P1000 (1000 µL rack from second stacker, slot D4) ---
    tip_rack_1000 = second_stacker.retrieve()
    ctx.move_lid(tip_rack_1000, waste_chute, use_gripper=True)
    ctx.move_labware(tip_rack_1000, tip_rack_adapter, use_gripper=True)
    tip_racks_1000.append(tip_rack_1000)
    p1000.reset_tipracks()

    # 1) P1000: pick up, aspirate 500, dispense 250 into single-well reservoir
    ctx.comment("Step 1: P1000 aspirate 500 µL, dispense 250 µL into reservoir A1")
    p1000.pick_up_tip(tip_rack_1000["A1"])
    p1000.aspirate(500, source_reservoir["A1"].bottom(z=1))
    p1000.dispense(250, source_reservoir["A1"].top(z=-2))
    # Keep ~250 µL in tip for step 3 (overpressure); avoid blow_out here so volume remains

    # 2) Pause: swap reservoir for calibration block (overpressure path)
    ctx.pause(
        msg=(
            "If you have not already, cause an overpressure scenario: remove the "
            "reservoir from D2 and place a calibration block (or obstructing labware) "
            "in the same position so the next dispense hits a closed/obstructed surface."
        )
    )

    # 3) Remaining 250 µL dispense — expect overpressure / error recovery
    ctx.comment("Step 3: Dispense remaining ~250 µL (overpressure if block in place)")
    p1000.dispense(250, source_reservoir["A1"].top(z=-2))
    p1000.blow_out(source_reservoir["A1"].top())
    p1000.drop_tip(waste_chute)

    # 4–5) Plate reader: initialize single band, open lid
    ctx.comment("Steps 4–5: Plate reader single band + open lid")
    absorbance_module.initialize("single", [600], 450)
    absorbance_module.open_lid()

    # 6) Pause: remove tough plate for gripper failure (if not already)
    ctx.pause(
        msg=(
            "If you have not already, remove the Opentrons Tough 96-well plate from "
            f"{WELL_PLATE_STARTING_POSITION} so the next gripper move can fail; then "
            "replace it on-deck before resuming."
        )
    )

    # 7) Gripper to plate reader, read, open lid
    ctx.comment("Step 7: Move plate to absorbance reader, read, open lid")
    ctx.move_labware(pcr_plate, absorbance_module, use_gripper=True)
    absorbance_module.close_lid()
    result = absorbance_module.read(export_filename="error_recovery_abs.csv")
    ctx.comment(f"Absorbance read: {result}")
    absorbance_module.open_lid()

    # 8–9) Open TC, move plate into thermocycler
    ctx.comment("Steps 8–9: Open thermocycler, move plate into TC")
    thermocycler.open_lid()
    ctx.move_labware(pcr_plate, thermocycler, use_gripper=True)

    # 10) Manual TC lid placement (incorrect on purpose for QA)
    ctx.pause(
        msg=(
            "MANUAL: Place an Opentrons Tough PCR auto-sealing TC lid on the "
            "thermocycler incorrectly (mis-seated / wrong orientation) if you have "
            "not already. Fix it after any error-recovery prompt before the run "
            "continues past close_lid."
        )
    )

    # 11) Concurrent TC profile + P50 mix in reservoir
    ctx.comment(
        "Step 11: Start TC profile (async) while mixing in reservoir with P50 8-ch"
    )
    p50.pick_up_tip(tip_rack_50_on_deck.wells_by_name()["A1"])
    thermocycler.close_lid()
    tc_profile_steps = [
        {"temperature": 55, "hold_time_seconds": 20},
        {"temperature": 40, "hold_time_seconds": 20},
        {"temperature": 20, "hold_time_seconds": 45},
    ]
    tc_task = thermocycler.start_execute_profile(
        steps=tc_profile_steps,
        repetitions=1,
        block_max_volume=50,
    )
    p50.mix(repetitions=10, volume=40, location=source_reservoir["A1"])
    ctx.wait_for_tasks([tc_task])
    p50.drop_tip(waste_chute)

    # 12–13) HS to 40 °C while waiting for TC (TC already waited); heat HS concurrently
    ctx.comment("Steps 12–13: Heat heater-shaker to 40 °C (async); ensure TC is idle")
    hs_task = heater_shaker.set_target_temperature(celsius=40.0)
    ctx.wait_for_tasks([hs_task])

    # 14–17) Open TC, remove lid from plate if present, move plate to HS
    ctx.comment("Steps 14–17: Open TC, strip lid, move plate to heater-shaker")
    thermocycler.open_lid()
    ctx.pause(
        msg=(
            "If a Tough PCR auto-sealing lid is on the plate, remove it manually "
            "(gripper lid strip optional). Then resume for gripper move to heater-shaker."
        )
    )
    heater_shaker.open_labware_latch()
    ctx.move_labware(pcr_plate, heater_shaker_adapter, use_gripper=True)

    # 17–18) Pause manual latch, close latch, shake 500 rpm for 30 s
    ctx.pause(
        msg=(
            "MANUAL: On first run, intentionally do not seat the plate on the "
            "heater-shaker perfectly; after recovery, close the latch on-deck. "
            "When ready, resume so the protocol can close the latch and shake."
        )
    )
    heater_shaker.close_labware_latch()
    ctx.comment("Step 18: Shake 500 rpm for 30 s")
    heater_shaker.set_shake_speed(500)
    ctx.delay(seconds=30)
    heater_shaker.deactivate_shaker()

    # 19–22) Stacker: user loads 50 µL rack, retrieve, deck placement, LLD transfer
    ctx.pause(
        msg=(
            "Step 19–20: Physically load stacker D4 with ONE 50 µL tip rack "
            "(opentrons_flex_96_tiprack_50ul). On first dry run you may skip loading — "
            "the next fill/retrieve will fail until racks are present."
        )
    )
    stacker_D4.empty("Clear D4 stacker of any leftover labware before continuing.")
    stacker_D4.set_stored_labware(
        TIPRACK_96_50,
        count=1,
        lid="opentrons_flex_tiprack_lid",
    )
    stacker_D4.fill(
        count=1,
        message="Place one 50 µL Flex tip rack into stacker D4, then resume.",
    )
    tip_rack_50_from_stacker = stacker_D4.retrieve()
    ctx.move_lid(tip_rack_50_from_stacker, waste_chute, use_gripper=True)
    ctx.move_labware(tip_rack_50_from_stacker, "D3", use_gripper=True)
    tip_racks_50.append(tip_rack_50_from_stacker)

    ctx.comment(
        "Step 22: LLD in reservoir with P50 8-ch, 50 µL to column 1 of PCR plate"
    )
    p50.reset_tipracks()
    p50.pick_up_tip(tip_rack_50_from_stacker.wells_by_name()["A1"])
    if not ctx.is_simulating():
        p50.detect_liquid_presence(source_reservoir["A1"])
    p50.aspirate(
        50,
        source_reservoir["A1"].meniscus(target="dynamic", z=-1),
    )
    dest_column = pcr_plate.columns()[0]
    p50.dispense(50, dest_column[0].bottom(z=1))
    p50.drop_tip(waste_chute)

    ctx.comment("Error recovery QA tour: protocol steps complete.")
    heater_shaker.deactivate_heater()
    temperature_module.deactivate()
