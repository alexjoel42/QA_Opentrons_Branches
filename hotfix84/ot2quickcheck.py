from opentrons import protocol_api, types

metadata = {
    "protocolName": "OT-2 smoke test ",
    "description": "This will go through each step of the OT-2 "
}

requirements = {
    "robotType": "OT-2",
    "apiLevel": "2.23",
}

def run(protocol: protocol_api.ProtocolContext) -> None:
    # Load Modules:
    thermocycler_module_1 = protocol.load_module("thermocyclerModuleV2", "7")
    magnetic_module_1 = protocol.load_module("magneticModuleV2", "9")
    temperature_module_1 = protocol.load_module("temperatureModuleV2", "3")
    heater_shaker_module_1 = protocol.load_module("heaterShakerModuleV1", "1")

    # Load Adapters:
    adapter_1 = temperature_module_1.load_adapter(
        "opentrons_96_deep_well_temp_mod_adapter",
        namespace="opentrons",
        version=1,
    )
    adapter_2 = heater_shaker_module_1.load_adapter(
        "opentrons_96_flat_bottom_adapter",
        namespace="opentrons",
        version=1,
    )

    # Load Labware:
    tip_rack_1 = protocol.load_labware(
        "opentrons_96_tiprack_300ul",
        location="5",
        namespace="opentrons",
        version=1,
    )
    tip_rack_2 = protocol.load_labware(
        "opentrons_96_filtertiprack_200ul",
        location="6",
        namespace="opentrons",
        version=1,
    )
    well_plate_1 = thermocycler_module_1.load_labware(
        "opentrons_96_wellplate_200ul_pcr_full_skirt",
        namespace="opentrons",
        version=2,
    )
    well_plate_2 = magnetic_module_1.load_labware(
        "nest_96_wellplate_2ml_deep",
        namespace="opentrons",
        version=2,
    )
    well_plate_3 = adapter_1.load_labware(
        "nest_96_wellplate_2ml_deep",
        namespace="opentrons",
        version=2,
    )
    well_plate_4 = adapter_2.load_labware(
        "nest_96_wellplate_200ul_flat",
        namespace="opentrons",
        version=2,
    )

    # Load Pipettes:
    pipette_left = protocol.load_instrument("p300_single_gen2", "left", tip_racks=[tip_rack_1])
    pipette_right = protocol.load_instrument("p50_single", "right", tip_racks=[tip_rack_2])

    # Define Liquids:
    liquid_1 = protocol.define_liquid(
        "H20",
        display_color="#b925ff",
    )
    liquid_2 = protocol.define_liquid(
        "Potato",
        display_color="#ffd600",
    )

    # Load Liquids:
    well_plate_2["A1"].load_liquid(liquid_1, 1234)
    well_plate_2["B1"].load_liquid(liquid_1, 1234)
    well_plate_2["C1"].load_liquid(liquid_1, 1234)
    well_plate_2["D1"].load_liquid(liquid_1, 1234)
    well_plate_2["E1"].load_liquid(liquid_1, 1234)
    well_plate_2["F1"].load_liquid(liquid_1, 1234)
    well_plate_2["G1"].load_liquid(liquid_1, 1234)
    well_plate_2["H1"].load_liquid(liquid_1, 1234)
    well_plate_2["A2"].load_liquid(liquid_1, 1234)
    well_plate_2["B2"].load_liquid(liquid_1, 1234)
    well_plate_2["C2"].load_liquid(liquid_1, 1234)
    well_plate_2["D2"].load_liquid(liquid_1, 1234)
    well_plate_2["E2"].load_liquid(liquid_1, 1234)
    well_plate_2["F2"].load_liquid(liquid_1, 1234)
    well_plate_2["G2"].load_liquid(liquid_1, 1234)
    well_plate_2["H2"].load_liquid(liquid_1, 1234)
    well_plate_2["A3"].load_liquid(liquid_1, 1234)
    well_plate_2["B3"].load_liquid(liquid_1, 1234)
    well_plate_2["C3"].load_liquid(liquid_1, 1234)
    well_plate_2["D3"].load_liquid(liquid_1, 1234)
    well_plate_2["E3"].load_liquid(liquid_1, 1234)
    well_plate_2["F3"].load_liquid(liquid_1, 1234)
    well_plate_2["G3"].load_liquid(liquid_1, 1234)
    well_plate_2["H3"].load_liquid(liquid_1, 1234)
    well_plate_2["A4"].load_liquid(liquid_1, 1234)
    well_plate_2["B4"].load_liquid(liquid_1, 1234)
    well_plate_2["C4"].load_liquid(liquid_1, 1234)
    well_plate_2["D4"].load_liquid(liquid_1, 1234)
    well_plate_2["E4"].load_liquid(liquid_1, 1234)
    well_plate_2["F4"].load_liquid(liquid_1, 1234)
    well_plate_2["G4"].load_liquid(liquid_1, 1234)
    well_plate_2["H4"].load_liquid(liquid_1, 1234)
    well_plate_2["E5"].load_liquid(liquid_1, 1234)
    well_plate_2["F5"].load_liquid(liquid_1, 1234)
    well_plate_2["G5"].load_liquid(liquid_1, 1234)
    well_plate_2["H5"].load_liquid(liquid_1, 1234)
    well_plate_2["E6"].load_liquid(liquid_1, 1234)
    well_plate_2["F6"].load_liquid(liquid_1, 1234)
    well_plate_2["G6"].load_liquid(liquid_1, 1234)
    well_plate_2["H6"].load_liquid(liquid_1, 1234)
    well_plate_2["E7"].load_liquid(liquid_1, 1234)
    well_plate_2["F7"].load_liquid(liquid_1, 1234)
    well_plate_2["G7"].load_liquid(liquid_1, 1234)
    well_plate_2["H7"].load_liquid(liquid_1, 1234)
    well_plate_2["E8"].load_liquid(liquid_1, 1234)
    well_plate_2["F8"].load_liquid(liquid_1, 1234)
    well_plate_2["G8"].load_liquid(liquid_1, 1234)
    well_plate_2["H8"].load_liquid(liquid_1, 1234)
    well_plate_2["E9"].load_liquid(liquid_1, 1234)
    well_plate_2["F9"].load_liquid(liquid_1, 1234)
    well_plate_2["G9"].load_liquid(liquid_1, 1234)
    well_plate_2["H9"].load_liquid(liquid_1, 1234)
    well_plate_2["E10"].load_liquid(liquid_1, 1234)
    well_plate_2["F10"].load_liquid(liquid_1, 1234)
    well_plate_2["G10"].load_liquid(liquid_1, 1234)
    well_plate_2["H10"].load_liquid(liquid_1, 1234)
    well_plate_2["E11"].load_liquid(liquid_1, 1234)
    well_plate_2["F11"].load_liquid(liquid_1, 1234)
    well_plate_2["G11"].load_liquid(liquid_1, 1234)
    well_plate_2["H11"].load_liquid(liquid_1, 1234)
    well_plate_2["E12"].load_liquid(liquid_1, 1234)

    # PROTOCOL STEPS

    # Step 1:
    heater_shaker_module_1.close_labware_latch()
    heater_shaker_module_1.deactivate_heater()

    # Step 2:
    thermocycler_module_1.open_lid()
    thermocycler_module_1.set_block_temperature(33)
    thermocycler_module_1.set_lid_temperature(110)

    # Step 3:
    pipette_left.pick_up_tip(location=tip_rack_1)
    pipette_left.move_to(well_plate_2["A1"].top(z=2))
    pipette_left.prepare_to_aspirate()
    pipette_left.move_to(well_plate_2["A1"].top())
    pipette_left.move_to(well_plate_2["A1"].bottom(), speed=125)
    pipette_left.mix(
        repetitions=1,
        volume=123,
        aspirate_flow_rate=46.4,
        dispense_flow_rate=46.4,
        aspirate_delay=1,
        dispense_delay=1,
        final_push_out=0,
    )
    pipette_left.aspirate(volume=123, flow_rate=46.4)
    protocol.delay(seconds=1)
    pipette_left.move_to(well_plate_2["A1"].top(), speed=125)
    pipette_left.touch_tip(well_plate_2["A1"], v_offset=-1, speed=400, mm_from_edge=0)
    pipette_left.move_to(well_plate_2["A1"].top())
    pipette_left.air_gap(volume=111, in_place=True, flow_rate=46.4)
    protocol.delay(seconds=1)
    pipette_left.move_to(well_plate_4["A1"].top())
    pipette_left.dispense(volume=111, flow_rate=46.4, push_out=0)
    protocol.delay(seconds=1)
    pipette_left.move_to(well_plate_4["A1"].bottom(), speed=125)
    pipette_left.dispense(volume=123, flow_rate=46.4, push_out=0)
    protocol.delay(seconds=1)
    pipette_left.mix(
        repetitions=2,
        volume=111,
        aspirate_flow_rate=46.4,
        dispense_flow_rate=46.4,
        aspirate_delay=1,
        dispense_delay=1,
        final_push_out=0,
    )
    pipette_left.move_to(well_plate_4["A1"].bottom(), speed=125)
    pipette_left.flow_rate.blow_out = 46.43
    pipette_left.blow_out()
    pipette_left.touch_tip(well_plate_4["A1"], v_offset=-1, speed=400, mm_from_edge=0)
    pipette_left.move_to(well_plate_4["A1"].bottom())
    pipette_left.air_gap(volume=200, in_place=True, flow_rate=46.4)
    protocol.delay(seconds=1)
    pipette_left.drop_tip()
    pipette_left.pick_up_tip(location=tip_rack_1)
    pipette_left.move_to(well_plate_2["B1"].top(z=2))
    pipette_left.prepare_to_aspirate()
    pipette_left.move_to(well_plate_2["B1"].top())
    pipette_left.move_to(well_plate_2["B1"].bottom(), speed=125)
    pipette_left.mix(
        repetitions=1,
        volume=123,
        aspirate_flow_rate=46.4,
        dispense_flow_rate=46.4,
        aspirate_delay=1,
        dispense_delay=1,
        final_push_out=0,
    )
    pipette_left.aspirate(volume=123, flow_rate=46.4)
    protocol.delay(seconds=1)
    pipette_left.move_to(well_plate_2["B1"].top(), speed=125)
    pipette_left.touch_tip(well_plate_2["B1"], v_offset=-1, speed=400, mm_from_edge=0)
    pipette_left.move_to(well_plate_2["B1"].top())
    pipette_left.air_gap(volume=111, in_place=True, flow_rate=46.4)
    protocol.delay(seconds=1)
    pipette_left.move_to(well_plate_4["A1"].top())
    pipette_left.dispense(volume=111, flow_rate=46.4, push_out=0)
    protocol.delay(seconds=1)
    pipette_left.move_to(well_plate_4["A1"].bottom(), speed=125)
    pipette_left.dispense(volume=123, flow_rate=46.4, push_out=0)
    protocol.delay(seconds=1)
    pipette_left.mix(
        repetitions=2,
        volume=111,
        aspirate_flow_rate=46.4,
        dispense_flow_rate=46.4,
        aspirate_delay=1,
        dispense_delay=1,
        final_push_out=0,
    )
    pipette_left.move_to(well_plate_4["A1"].bottom(), speed=125)
    pipette_left.flow_rate.blow_out = 46.43
    pipette_left.blow_out()
    pipette_left.touch_tip(well_plate_4["A1"], v_offset=-1, speed=400, mm_from_edge=0)
    pipette_left.move_to(well_plate_4["A1"].bottom())
    pipette_left.air_gap(volume=200, in_place=True, flow_rate=46.4)
    protocol.delay(seconds=1)
    pipette_left.drop_tip()
    pipette_left.pick_up_tip(location=tip_rack_1)
    pipette_left.move_to(well_plate_2["C1"].top(z=2))
    pipette_left.prepare_to_aspirate()
    pipette_left.move_to(well_plate_2["C1"].top())
    pipette_left.move_to(well_plate_2["C1"].bottom(), speed=125)
    pipette_left.mix(
        repetitions=1,
        volume=123,
        aspirate_flow_rate=46.4,
        dispense_flow_rate=46.4,
        aspirate_delay=1,
        dispense_delay=1,
        final_push_out=0,
    )
    pipette_left.aspirate(volume=123, flow_rate=46.4)
    protocol.delay(seconds=1)
    pipette_left.move_to(well_plate_2["C1"].top(), speed=125)
    pipette_left.touch_tip(well_plate_2["C1"], v_offset=-1, speed=400, mm_from_edge=0)
    pipette_left.move_to(well_plate_2["C1"].top())
    pipette_left.air_gap(volume=111, in_place=True, flow_rate=46.4)
    protocol.delay(seconds=1)
    pipette_left.move_to(well_plate_4["A1"].top())
    pipette_left.dispense(volume=111, flow_rate=46.4, push_out=0)
    protocol.delay(seconds=1)
    pipette_left.move_to(well_plate_4["A1"].bottom(), speed=125)
    pipette_left.dispense(volume=123, flow_rate=46.4, push_out=0)
    protocol.delay(seconds=1)
    pipette_left.mix(
        repetitions=2,
        volume=111,
        aspirate_flow_rate=46.4,
        dispense_flow_rate=46.4,
        aspirate_delay=1,
        dispense_delay=1,
        final_push_out=0,
    )
    pipette_left.move_to(well_plate_4["A1"].bottom(), speed=125)
    pipette_left.flow_rate.blow_out = 46.43
    pipette_left.blow_out()
    pipette_left.touch_tip(well_plate_4["A1"], v_offset=-1, speed=400, mm_from_edge=0)
    pipette_left.move_to(well_plate_4["A1"].bottom())
    pipette_left.air_gap(volume=200, in_place=True, flow_rate=46.4)
    protocol.delay(seconds=1)
    pipette_left.drop_tip()
    pipette_left.pick_up_tip(location=tip_rack_1)
    pipette_left.move_to(well_plate_2["D1"].top(z=2))
    pipette_left.prepare_to_aspirate()
    pipette_left.move_to(well_plate_2["D1"].top())
    pipette_left.move_to(well_plate_2["D1"].bottom(), speed=125)
    pipette_left.mix(
        repetitions=1,
        volume=123,
        aspirate_flow_rate=46.4,
        dispense_flow_rate=46.4,
        aspirate_delay=1,
        dispense_delay=1,
        final_push_out=0,
    )
    pipette_left.aspirate(volume=123, flow_rate=46.4)
    protocol.delay(seconds=1)
    pipette_left.move_to(well_plate_2["D1"].top(), speed=125)
    pipette_left.touch_tip(well_plate_2["D1"], v_offset=-1, speed=400, mm_from_edge=0)
    pipette_left.move_to(well_plate_2["D1"].top())
    pipette_left.air_gap(volume=111, in_place=True, flow_rate=46.4)
    protocol.delay(seconds=1)
    pipette_left.move_to(well_plate_4["A1"].top())
    pipette_left.dispense(volume=111, flow_rate=46.4, push_out=0)
    protocol.delay(seconds=1)
    pipette_left.move_to(well_plate_4["A1"].bottom(), speed=125)
    pipette_left.dispense(volume=123, flow_rate=46.4, push_out=0)
    protocol.delay(seconds=1)
    pipette_left.mix(
        repetitions=2,
        volume=111,
        aspirate_flow_rate=46.4,
        dispense_flow_rate=46.4,
        aspirate_delay=1,
        dispense_delay=1,
        final_push_out=0,
    )
    pipette_left.move_to(well_plate_4["A1"].bottom(), speed=125)
    pipette_left.flow_rate.blow_out = 46.43
    pipette_left.blow_out()
    pipette_left.touch_tip(well_plate_4["A1"], v_offset=-1, speed=400, mm_from_edge=0)
    pipette_left.move_to(well_plate_4["A1"].bottom())
    pipette_left.air_gap(volume=200, in_place=True, flow_rate=46.4)
    protocol.delay(seconds=1)
    pipette_left.drop_tip()

    # Step 4:
    pipette_left.pick_up_tip(location=tip_rack_1)
    pipette_left.move_to(well_plate_2["A2"].top(z=2))
    pipette_left.prepare_to_aspirate()
    pipette_left.move_to(well_plate_2["A2"].top())
    pipette_left.move_to(well_plate_2["A2"].bottom(), speed=125)
    pipette_left.mix(
        repetitions=11,
        volume=11,
        aspirate_flow_rate=46.4,
        dispense_flow_rate=46.4,
        aspirate_delay=1,
        dispense_delay=1,
        final_push_out=0,
    )
    pipette_left.mix(
        repetitions=1,
        volume=123,
        aspirate_flow_rate=46.4,
        dispense_flow_rate=46.4,
        aspirate_delay=1,
        dispense_delay=1,
        final_push_out=0,
    )
    pipette_left.aspirate(volume=123, flow_rate=46.4)
    protocol.delay(seconds=1)
    pipette_left.move_to(well_plate_2["A2"].top(), speed=125)
    pipette_left.touch_tip(well_plate_2["A2"], v_offset=-1, speed=400, mm_from_edge=0)
    pipette_left.move_to(well_plate_2["A2"].top())
    pipette_left.air_gap(volume=111, in_place=True, flow_rate=46.4)
    protocol.delay(seconds=1)
    pipette_left.move_to(well_plate_1["A12"].top())
    pipette_left.dispense(volume=111, flow_rate=46.4, push_out=0)
    protocol.delay(seconds=1)
    pipette_left.move_to(well_plate_1["A12"].bottom(), speed=125)
    pipette_left.dispense(volume=123, flow_rate=46.4, push_out=0)
    protocol.delay(seconds=1)
    pipette_left.mix(
        repetitions=2,
        volume=11,
        aspirate_flow_rate=46.4,
        dispense_flow_rate=46.4,
        aspirate_delay=1,
        dispense_delay=1,
        final_push_out=0,
    )
    pipette_left.move_to(well_plate_1["A12"].bottom(), speed=125)
    pipette_left.flow_rate.blow_out = 46.43
    pipette_left.blow_out()
    pipette_left.air_gap(volume=200, in_place=True, flow_rate=46.4)
    protocol.delay(seconds=1)
    pipette_left.drop_tip()

    # Step 5:
    thermocycler_module_1.close_lid()
    thermocycler_module_1.set_lid_temperature(100)
    thermocycler_module_1.execute_profile(
        [
            {"temperature": 33, "hold_time_seconds": 2},
            {"temperature": 22, "hold_time_seconds": 2},
        ],
        2,
        block_max_volume=11,
    )
    thermocycler_module_1.set_block_temperature(90)
    thermocycler_module_1.set_lid_temperature(110)

    # Step 6:
    magnetic_module_1.engage(height_from_base=20)

    # Step 7:
    protocol.pause("Hi! ")

    # Step 8:
    protocol.delay(seconds=10)