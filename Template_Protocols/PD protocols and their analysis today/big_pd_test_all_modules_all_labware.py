import json
from opentrons import protocol_api, types

metadata = {
    "protocolName": "DuoSeq_FFPE_v.1",
    "created": "2026-01-30T20:12:54.419Z",
    "internalAppBuildDate": "Tue, 24 Mar 2026 15:51:09 GMT",
    "lastModified": "2026-04-20T20:50:02.673Z",
    "protocolDesigner": "8.9.1",
    "source": "Protocol Designer",
}

requirements = {"robotType": "Flex", "apiLevel": "2.27"}

def run(protocol: protocol_api.ProtocolContext) -> None:
    # Load Modules:
    thermocycler_module_1 = protocol.load_module("thermocyclerModuleV2", "B1")
    temperature_module_1 = protocol.load_module("temperatureModuleV2", "C1")
    temperature_module_2 = protocol.load_module("temperatureModuleV2", "D1")
    magnetic_block_1 = protocol.load_module("magneticBlockV1", "D2")

    # Load Adapters:
    aluminum_block_1 = temperature_module_1.load_adapter(
        "opentrons_96_well_aluminum_block",
        namespace="opentrons",
        version=1,
    )

    # Load Labware:
    tip_rack_1 = protocol.load_labware(
        "opentrons_flex_96_filtertiprack_1000ul",
        location="A3",
        namespace="opentrons",
        version=1,
    )
    tip_rack_2 = protocol.load_labware(
        "opentrons_flex_96_filtertiprack_200ul",
        location="B3",
        namespace="opentrons",
        version=1,
    )
    tip_rack_3 = protocol.load_labware(
        "opentrons_flex_96_filtertiprack_200ul",
        location="C3",
        label="Opentrons Flex 96 Filter Tip Rack 200 µL (1)",
        namespace="opentrons",
        version=1,
    )
    tip_rack_4 = protocol.load_labware(
        "opentrons_flex_96_filtertiprack_200ul",
        location="A4",
        label="Opentrons Flex 96 Filter Tip Rack 200 µL (2)",
        namespace="opentrons",
        version=1,
    )
    tip_rack_5 = protocol.load_labware(
        "opentrons_flex_96_filtertiprack_200ul",
        location="B4",
        label="Opentrons Flex 96 Filter Tip Rack 200 µL (3)",
        namespace="opentrons",
        version=1,
    )
    tip_rack_6 = protocol.load_labware(
        "opentrons_flex_96_filtertiprack_200ul",
        location="C4",
        label="Opentrons Flex 96 Filter Tip Rack 200 µL (4)",
        namespace="opentrons",
        version=1,
    )
    tip_rack_7 = protocol.load_labware(
        "opentrons_flex_96_filtertiprack_200ul",
        location="D4",
        label="Opentrons Flex 96 Filter Tip Rack 200 µL (5)",
        namespace="opentrons",
        version=1,
    )
    well_plate_1 = protocol.load_labware(
        "nest_96_wellplate_100ul_pcr_full_skirt",
        location=protocol_api.OFF_DECK,
        label="Plate 1",
        namespace="opentrons",
        version=5,
    )
    tube_rack_1 = protocol.load_labware(
        "opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical",
        location=protocol_api.OFF_DECK,
        label="Conical Tube Rack",
        namespace="opentrons",
        version=3,
    )
    reservoir_1 = protocol.load_labware(
        "nest_12_reservoir_15ml",
        location=protocol_api.OFF_DECK,
        label="12 Well Reservoir",
        namespace="opentrons",
        version=3,
    )
    well_plate_2 = protocol.load_labware(
        "nest_96_wellplate_100ul_pcr_full_skirt",
        location=protocol_api.OFF_DECK,
        label="Plate 2",
        namespace="opentrons",
        version=5,
    )
    aluminum_block_2 = temperature_module_2.load_labware(
        "opentrons_24_aluminumblock_generic_2ml_screwcap",
        namespace="opentrons",
        version=3,
    )

    # Load Pipettes:
    pipette_left = protocol.load_instrument("flex_1channel_1000", "left")
    pipette_right = protocol.load_instrument("flex_8channel_1000", "right")

    # Load Waste Chute:
    waste_chute = protocol.load_waste_chute()

    # Define Liquids:
    liquid_1 = protocol.define_liquid(
        "Input",
        display_color="#b925ff",
    )
    liquid_2 = protocol.define_liquid(
        "P1-P8",
        display_color="#a973c7ff",
    )
    liquid_3 = protocol.define_liquid(
        "8A",
        display_color="#ff0000ff",
    )
    liquid_4 = protocol.define_liquid(
        "2A",
        display_color="#d9d9d9ff",
    )
    liquid_5 = protocol.define_liquid(
        "2B",
        display_color="#d9d9d9ff",
    )
    liquid_6 = protocol.define_liquid(
        "3A",
        display_color="#ffe699ff",
    )
    liquid_7 = protocol.define_liquid(
        "3B",
        display_color="#ffe699ff",
    )
    liquid_8 = protocol.define_liquid(
        "4A",
        display_color="#a9d08eff",
    )
    liquid_9 = protocol.define_liquid(
        "4B",
        display_color="#a9d08eff",
    )
    liquid_10 = protocol.define_liquid(
        "5A",
        display_color="#ed7c37ff",
    )
    liquid_11 = protocol.define_liquid(
        "5B",
        display_color="#ed7c37ff",
    )
    liquid_12 = protocol.define_liquid(
        "6A",
        display_color="#a973c7ff",
    )
    liquid_13 = protocol.define_liquid(
        "6B",
        display_color="#a973c7ff",
    )
    liquid_14 = protocol.define_liquid(
        "7A",
        display_color="#2f75b5ff",
    )
    liquid_15 = protocol.define_liquid(
        "7B",
        display_color="#2f75b5ff",
    )
    liquid_16 = protocol.define_liquid(
        "8B",
        display_color="#ff0000ff",
    )
    liquid_17 = protocol.define_liquid(
        "8C",
        display_color="#ff0000ff",
    )
    liquid_18 = protocol.define_liquid(
        "9A",
        display_color="#48d0ffff",
    )
    liquid_19 = protocol.define_liquid(
        "9B",
        display_color="#48d0ffff",
    )
    liquid_20 = protocol.define_liquid(
        "9C",
        display_color="#48d0ffff",
    )
    liquid_21 = protocol.define_liquid(
        "CB",
        display_color="#48d0ffff",
    )
    liquid_22 = protocol.define_liquid(
        "10A",
        display_color="#38e85aff",
    )
    liquid_23 = protocol.define_liquid(
        "10B",
        display_color="#38e85aff",
    )
    liquid_24 = protocol.define_liquid(
        "80% Ethanol",
        display_color="#1b0994ff",
    )
    liquid_25 = protocol.define_liquid(
        "SB",
        display_color="#311e0aff",
    )
    liquid_26 = protocol.define_liquid(
        "H2O",
        display_color="#9dffd8ff",
    )
    liquid_27 = protocol.define_liquid(
        "LTE",
        display_color="#9dffd8",
    )

    # Load Liquids:
    well_plate_1.load_liquid(
        wells=[
            "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1"
        ],
        liquid=liquid_1,
        volume=10,
    )
    tube_rack_1.load_liquid(
        wells=["A1"],
        liquid=liquid_27,
        volume=5000,
    )
    tube_rack_1.load_liquid(
        wells=["A2"],
        liquid=liquid_18,
        volume=4000,
    )
    tube_rack_1.load_liquid(
        wells=["B2"],
        liquid=liquid_19,
        volume=4000,
    )
    tube_rack_1.load_liquid(
        wells=["C2"],
        liquid=liquid_20,
        volume=4000,
    )
    tube_rack_1.load_liquid(
        wells=["A3"],
        liquid=liquid_24,
        volume=25000,
    )
    well_plate_2.load_liquid(
        wells=[
            "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5"
        ],
        liquid=liquid_2,
        volume=1,
    )
    well_plate_2.load_liquid(
        wells=[
            "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7"
        ],
        liquid=liquid_3,
        volume=1,
    )
    aluminum_block_2.load_liquid(
        wells=["A1"],
        liquid=liquid_4,
        volume=75,
    )
    aluminum_block_2.load_liquid(
        wells=["B1"],
        liquid=liquid_5,
        volume=15,
    )
    aluminum_block_2.load_liquid(
        wells=["A2"],
        liquid=liquid_6,
        volume=180,
    )
    aluminum_block_2.load_liquid(
        wells=["B2"],
        liquid=liquid_7,
        volume=36,
    )
    aluminum_block_2.load_liquid(
        wells=["A3"],
        liquid=liquid_8,
        volume=230,
    )
    aluminum_block_2.load_liquid(
        wells=["B3"],
        liquid=liquid_9,
        volume=30,
    )
    aluminum_block_2.load_liquid(
        wells=["A4"],
        liquid=liquid_10,
        volume=120,
    )
    aluminum_block_2.load_liquid(
        wells=["B4"],
        liquid=liquid_11,
        volume=18,
    )
    aluminum_block_2.load_liquid(
        wells=["A5"],
        liquid=liquid_12,
        volume=250,
    )
    aluminum_block_2.load_liquid(
        wells=["B5"],
        liquid=liquid_13,
        volume=10,
    )
    aluminum_block_2.load_liquid(
        wells=["A6"],
        liquid=liquid_14,
        volume=70,
    )
    aluminum_block_2.load_liquid(
        wells=["B6"],
        liquid=liquid_15,
        volume=250,
    )
    aluminum_block_2.load_liquid(
        wells=["C1"],
        liquid=liquid_16,
        volume=450,
    )
    aluminum_block_2.load_liquid(
        wells=["C2"],
        liquid=liquid_17,
        volume=350,
    )
    aluminum_block_2.load_liquid(
        wells=["C3"],
        liquid=liquid_25,
        volume=1900,
    )
    aluminum_block_2.load_liquid(
        wells=["C4"],
        liquid=liquid_21,
        volume=250,
    )
    aluminum_block_2.load_liquid(
        wells=["C5"],
        liquid=liquid_22,
        volume=70,
    )
    aluminum_block_2.load_liquid(
        wells=["C6"],
        liquid=liquid_23,
        volume=250,
    )
    aluminum_block_2.load_liquid(
        wells=["D1"],
        liquid=liquid_26,
        volume=500,
    )

    # Load Liquid Classes:
    glycerol_50_base_class = protocol.get_liquid_class("glycerol_50")
    ethanol_80_base_class = protocol.get_liquid_class("ethanol_80")
    water_base_class = protocol.get_liquid_class("water")

    # PROTOCOL STEPS

    # Step 1: Module Set up
    protocol.capture_image()

    # Step 2: Temp D1 4 C
    temperature_module_2.start_set_temperature(4)

    # Step 3: Temp C1 12 C
    temperature_module_1.start_set_temperature(12)

    # Step 4: Open Cycler
    thermocycler_module_1.open_lid()

    # Step 5: Replace Lid Seal
    # Remove old lid seal and replace with the new seal provided in the Duoseq kit.
    protocol.pause("Remove the used lid seal and replace with the new seal provided in the Duoseq kit.")

    # Step 6: Step 2 Cycler Prep
    thermocycler_module_1.set_block_temperature(37)
    thermocycler_module_1.set_lid_temperature(75)

    # Step 7: Conical Tube Rack to slot A2
    # Put Conical tube rack at position A2 on the deck.
    protocol.move_labware(tube_rack_1, "A2")

    # Step 8: Reservoir to B2
    # Put Reservoir at position B2 on the deck.
    protocol.move_labware(reservoir_1, "B2")

    # Step 9: Plate 1 to C2
    # Place plate 1 on the temperature block located at position C1 on the deck.
    protocol.move_labware(well_plate_1, aluminum_block_1)

    # Step 10: Plate 2 to Temp at C1
    # Place Plate 2 at position C2 on the deck.
    protocol.move_labware(well_plate_2, "C2")

    # Step 11: 2 mL tubes to 24-well Aluminum block
    # Remove old lid seal and replace with the new seal provided in the Duoseq kit.
    protocol.pause("Place all 2 mL tubes from DuoSeq Kit to indicated position on the 24-well Aluminum Block located at position D1 on the deck")

    # Step 12: Labware Set UP
    protocol.capture_image()

    # Step 13: Cap Removal
    # Remove all caps from all 2 ml tubes and conical tubes.
    protocol.pause("Remove all caps from all 2 ml tubes and conical tubes.")

    # Step 14: Full Deck Set Up
    protocol.capture_image()

    # Step 15: 2A + 2B Mix
    pipette_left.transfer_with_liquid_class(
        volume=60,
        source=[aluminum_block_2["A1"]],
        dest=[aluminum_block_2["B1"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_15",
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "destination", "flow_rate": 250},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 10, "volume": 50},
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 16: Mix 2 Disperse
    pipette_left.distribute_with_liquid_class(
        volume=6,
        source=[aluminum_block_2["B1"]],
        dest=[well_plate_2["A2"], well_plate_2["B2"], well_plate_2["C2"], well_plate_2["D2"], well_plate_2["E2"], well_plate_2["F2"], well_plate_2["G2"], well_plate_2["H2"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_16",
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 1, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 716},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 1, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 716},
                    },
                    "correction_by_volume": [(0, 0)],
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 10)],
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 17: Mix 2 RxN
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=5,
        source=[well_plate_2["A2"]],
        dest=[well_plate_1["A1"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_17",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 5, "volume": 8},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 18: P1 to Cycler
    protocol.move_labware(well_plate_1, thermocycler_module_1, use_gripper=True)

    # Step 19: Step 2 Start
    thermocycler_module_1.close_lid()
    thermocycler_module_1_task_1 = thermocycler_module_1.start_execute_profile(
        [
            {"temperature": 37, "hold_time_seconds": 720},
            {"temperature": 65, "hold_time_seconds": 900},
        ],
        1,
        block_max_volume=15,
    )

    # Step 20: Step 2A Delay
    protocol.delay(seconds=1140)

    # Step 21: P2 to Temp C1
    protocol.move_labware(well_plate_2, aluminum_block_1, use_gripper=True)

    # Step 22: LTE to Res
    pipette_left.transfer_with_liquid_class(
        volume=5000,
        source=[tube_rack_1["A1"]],
        dest=[reservoir_1["A1"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_22",
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_1000ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 716)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 716)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 23: H2O to P2
    pipette_left.distribute_with_liquid_class(
        volume=50,
        source=[aluminum_block_2["D1"]],
        dest=[well_plate_2["A10"], well_plate_2["B10"], well_plate_2["C10"], well_plate_2["D10"], well_plate_2["E10"], well_plate_2["F10"], well_plate_2["G10"], well_plate_2["H10"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_23",
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_1000ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 500)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 100)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 716},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 100)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 716},
                    },
                    "correction_by_volume": [(0, 0)],
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 5)],
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 24: 3A + 3B Mix
    pipette_left.transfer_with_liquid_class(
        volume=144,
        source=[aluminum_block_2["A2"]],
        dest=[aluminum_block_2["B2"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_24",
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 150)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 150)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 50)],
                    "mix": {"enabled": True, "repetitions": 10, "volume": 125},
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 25: Mix 3 Disperse
    pipette_left.distribute_with_liquid_class(
        volume=17,
        source=[aluminum_block_2["B2"]],
        dest=[well_plate_2["A3"], well_plate_2["B3"], well_plate_2["C3"], well_plate_2["D3"], well_plate_2["E3"], well_plate_2["F3"], well_plate_2["G3"], well_plate_2["H3"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_25",
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 20)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 716},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 20)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 716},
                    },
                    "correction_by_volume": [(0, 0)],
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 5)],
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 26: pause
    protocol.wait_for_tasks([thermocycler_module_1_task_1])

    # Step 27: Step 2 End
    thermocycler_module_1.open_lid()
    thermocycler_module_1.set_block_temperature(12)
    thermocycler_module_1.set_lid_temperature(85)

    # Step 28: Mix 3 RxN
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=15,
        source=[well_plate_2["A3"]],
        dest=[well_plate_1["A1"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_28",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 10, "volume": 20},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 29: Step 3 Start
    thermocycler_module_1.close_lid()
    thermocycler_module_1_task_2 = thermocycler_module_1.start_execute_profile(
        [
            {"temperature": 25, "hold_time_seconds": 600},
            {"temperature": 42, "hold_time_seconds": 900},
            {"temperature": 75, "hold_time_seconds": 1200},
        ],
        1,
        block_max_volume=30,
    )

    # Step 30: Step 3 Delay
    protocol.delay(seconds=2400)

    # Step 31: SB Disperse 1
    pipette_left.distribute_with_liquid_class(
        volume=55,
        source=[aluminum_block_2["C3"]],
        dest=[well_plate_2["A1"], well_plate_2["B1"], well_plate_2["C1"], well_plate_2["D1"], well_plate_2["E1"], well_plate_2["F1"], well_plate_2["G1"], well_plate_2["H1"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_31",
            base_liquid_class=glycerol_50_base_class,
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_1000ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 20},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (10, -0.2), (100, -0.1), (1000, 12)],
                    "delay": {"enabled": True, "duration": 1},
                    "mix": {"enabled": True, "repetitions": 3, "volume": 250},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {
                            "enabled": True,
                            "z_offset": -10,
                            "mm_from_edge": 0.5,
                            "speed": 30,
                        },
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 1, "y": 0, "z": 5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "delay": {"enabled": True, "duration": 1},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "source", "flow_rate": 250},
                    },
                    "correction_by_volume": [(0, 0), (10, -0.2), (100, -0.1), (1000, 12)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 1, "y": 0, "z": 5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "delay": {"enabled": True, "duration": 1},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "source", "flow_rate": 250},
                    },
                    "correction_by_volume": [(0, 0), (10, -0.2), (100, -0.1), (1000, 12)],
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 5)],
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 32: 4A+4B Mix
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[aluminum_block_2["A3"]],
        dest=[aluminum_block_2["B3"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_32",
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 75)],
                    "mix": {"enabled": True, "repetitions": 10, "volume": 150},
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 33: Mix 4 Disperse
    pipette_left.distribute_with_liquid_class(
        volume=22,
        source=[aluminum_block_2["B3"]],
        dest=[well_plate_2["A4"], well_plate_2["B4"], well_plate_2["C4"], well_plate_2["D4"], well_plate_2["E4"], well_plate_2["F4"], well_plate_2["G4"], well_plate_2["H4"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_33",
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 1},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 20)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 716},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 20)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 716},
                    },
                    "correction_by_volume": [(0, 0)],
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 5)],
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 34: pause
    protocol.wait_for_tasks([thermocycler_module_1_task_2])

    # Step 35: Step 3 Incubation
    thermocycler_module_1.open_lid()
    thermocycler_module_1.set_block_temperature(16)
    thermocycler_module_1.set_lid_temperature(37)

    # Step 36: Mix 4 RxN
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=20,
        source=[well_plate_2["A4"]],
        dest=[well_plate_1["A1"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_36",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 40)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 3},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 40)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 10, "volume": 40},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 37: Temp C1 24 C
    temperature_module_1.start_set_temperature(24)

    # Step 38: Step 4 cycler Set Up
    thermocycler_module_1.close_lid()

    # Step 39: Step 4 Incubation
    protocol.delay(seconds=1800)

    # Step 40: Step 4 End
    thermocycler_module_1.open_lid()
    thermocycler_module_1.set_lid_temperature(75)

    # Step 41: P1 to Deck C2
    protocol.move_labware(well_plate_1, "C2", use_gripper=True)

    # Step 42: SB + Sample 1
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=50,
        source=[well_plate_2["A1"]],
        dest=[well_plate_1["A1"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_42",
            base_liquid_class=glycerol_50_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.2), (50, -0.3), (200, -0.8)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": True, "repetitions": 3, "volume": 45},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 3},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 75)],
                    "delay": {"enabled": True, "duration": 1},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.2), (50, -0.3), (200, -0.8)],
                    "push_out_by_volume": [(0, 50)],
                    "mix": {"enabled": True, "repetitions": 5, "volume": 75},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 43: Bead 1 Start
    thermocycler_module_1.close_lid()
    thermocycler_module_1_task_3 = thermocycler_module_1.start_execute_profile(
        [
            {"temperature": 20, "hold_time_seconds": 240},
        ],
        1,
        block_max_volume=50,
    )

    # Step 44: EtOH to Res 1
    pipette_left.transfer_with_liquid_class(
        volume=4000,
        source=[tube_rack_1["A3"]],
        dest=[reservoir_1["A2"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_44",
            base_liquid_class=ethanol_80_base_class,
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_1000ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 30},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 500)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (10, -0.9), (100, -2.6), (1000, -32.2)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 300)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (10, -0.9), (100, -2.6), (1000, -32.2)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 45: pause
    protocol.wait_for_tasks([thermocycler_module_1_task_3])

    # Step 46: Bead 1 End
    thermocycler_module_1.open_lid()

    # Step 47: P1 to Mag
    protocol.move_labware(well_plate_1, magnetic_block_1, use_gripper=True)

    # Step 48: Bead Bind 1
    protocol.delay(seconds=120)

    # Step 49: Rem Sup 1
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[well_plate_1["A1"]],
        dest=[reservoir_1["A12"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_49",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 100)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 50: Add EtOH 1.1
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=150,
        source=[reservoir_1["A2"]],
        dest=[well_plate_1["A1"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_50",
            base_liquid_class=ethanol_80_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 100)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 10)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 10},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 51: Rem EtOH 1.1
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_1["A1"]],
        dest=[reservoir_1["A12"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_51",
            base_liquid_class=ethanol_80_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 4},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 150)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 52: Add EtOH 1.2
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=150,
        source=[reservoir_1["A2"]],
        dest=[well_plate_1["A1"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_52",
            base_liquid_class=ethanol_80_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 100)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 10)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 10},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 53: Rem EtOH 1.2
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_1["A1"]],
        dest=[reservoir_1["A12"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_53",
            base_liquid_class=ethanol_80_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 6},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 150)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 54: P1 to Deck C2
    protocol.move_labware(well_plate_1, "C2", use_gripper=True)

    # Step 55: Elute 1
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=22,
        source=[reservoir_1["A1"]],
        dest=[well_plate_1["A1"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_55",
            base_liquid_class=water_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 20)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 10, "volume": 15},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 56: 5A + 5B Mix
    pipette_left.transfer_with_liquid_class(
        volume=102,
        source=[aluminum_block_2["A4"]],
        dest=[aluminum_block_2["B4"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_56",
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 100)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 100)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 50)],
                    "mix": {"enabled": True, "repetitions": 10, "volume": 70},
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 57: Mix 5 Disperse
    pipette_left.distribute_with_liquid_class(
        volume=10,
        source=[aluminum_block_2["B4"]],
        dest=[well_plate_1["A2"], well_plate_1["B2"], well_plate_1["C2"], well_plate_1["D2"], well_plate_1["E2"], well_plate_1["F2"], well_plate_1["G2"], well_plate_1["H2"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_57",
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 100)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 20)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 716},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 20)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 716},
                    },
                    "correction_by_volume": [(0, 0)],
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 5)],
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 58: P1 to Mag
    protocol.move_labware(well_plate_1, magnetic_block_1, use_gripper=True)

    # Step 59: P2 to Deck C2
    protocol.move_labware(well_plate_2, "C2", use_gripper=True)

    # Step 60: Temp C1 to 50C
    temperature_module_1.start_set_temperature(50)

    # Step 61: Prep P1-P8
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=7,
        source=[well_plate_2["A10"]],
        dest=[well_plate_2["A5"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_61",
            base_liquid_class=water_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 3, "volume": 4},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 62: Mix 5 RxN
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=20,
        source=[well_plate_1["A1"]],
        dest=[well_plate_1["A2"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_62",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 20)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 10, "volume": 20},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 63: P1 to Cycler
    protocol.move_labware(well_plate_1, thermocycler_module_1, use_gripper=True)

    # Step 64: Step 5 Start
    thermocycler_module_1.close_lid()
    thermocycler_module_1_task_4 = thermocycler_module_1.start_execute_profile(
        [
            {"temperature": 20, "hold_time_seconds": 900},
            {"temperature": 65, "hold_time_seconds": 900},
        ],
        1,
        block_max_volume=30,
    )

    # Step 65: P2 to Temp C1
    protocol.move_labware(well_plate_2, aluminum_block_1, use_gripper=True)

    # Step 66: Step 5 Delay 1
    protocol.delay(seconds=1080)

    # Step 67: P2 to Deck C2
    protocol.move_labware(well_plate_2, "C2", use_gripper=True)

    # Step 68: Temp C1 to 24C
    temperature_module_1.start_set_temperature(24)

    # Step 69: Step 5 Delay 2
    protocol.delay(seconds=300)

    # Step 70: SB Disperse 2
    pipette_left.distribute_with_liquid_class(
        volume=55,
        source=[aluminum_block_2["C3"]],
        dest=[well_plate_2["A1"], well_plate_2["B1"], well_plate_2["C1"], well_plate_2["D1"], well_plate_2["E1"], well_plate_2["F1"], well_plate_2["G1"], well_plate_2["H1"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_70",
            base_liquid_class=glycerol_50_base_class,
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_1000ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 10},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 600)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (10, -0.2), (100, -0.1), (1000, 12)],
                    "delay": {"enabled": True, "duration": 1},
                    "mix": {"enabled": True, "repetitions": 5, "volume": 600},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {
                            "enabled": True,
                            "z_offset": -10,
                            "mm_from_edge": 0.5,
                            "speed": 30,
                        },
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 1, "y": 0, "z": 5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "delay": {"enabled": True, "duration": 1},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "source", "flow_rate": 250},
                    },
                    "correction_by_volume": [(0, 0), (10, -0.2), (100, -0.1), (1000, 12)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 1, "y": 0, "z": 5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "delay": {"enabled": True, "duration": 1},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "source", "flow_rate": 250},
                    },
                    "correction_by_volume": [(0, 0), (10, -0.2), (100, -0.1), (1000, 12)],
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 5)],
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 71: 6A + 6B Mix
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[aluminum_block_2["A5"]],
        dest=[aluminum_block_2["B5"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_71",
            base_liquid_class=glycerol_50_base_class,
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 150)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.2), (50, -0.3), (200, -0.8)],
                    "delay": {"enabled": True, "duration": 1},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 150)],
                    "delay": {"enabled": True, "duration": 0.5},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {
                            "enabled": True,
                            "z_offset": -10,
                            "mm_from_edge": 0.5,
                            "speed": 30,
                        },
                        "blowout": {"enabled": True, "location": "destination", "flow_rate": 250},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.2), (50, -0.3), (200, -0.8)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 10, "volume": 150},
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 72: Mix 6 Disperse
    pipette_left.distribute_with_liquid_class(
        volume=22,
        source=[aluminum_block_2["B5"]],
        dest=[well_plate_2["A6"], well_plate_2["B6"], well_plate_2["C6"], well_plate_2["D6"], well_plate_2["E6"], well_plate_2["F6"], well_plate_2["G6"], well_plate_2["H6"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_72",
            base_liquid_class=glycerol_50_base_class,
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 100)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.2), (50, -0.3), (200, -0.8)],
                    "delay": {"enabled": True, "duration": 1},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 20)],
                    "delay": {"enabled": True, "duration": 0.5},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 716},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.2), (50, -0.3), (200, -0.8)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 20)],
                    "delay": {"enabled": True, "duration": 0.5},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 716},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.2), (50, -0.3), (200, -0.8)],
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 5)],
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 73: pause
    protocol.wait_for_tasks([thermocycler_module_1_task_4])

    # Step 74: Step 5 End
    thermocycler_module_1.open_lid()
    thermocycler_module_1.set_block_temperature(12)

    # Step 75: P1-P8 RxN
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=15,
        source=[well_plate_2["A5"]],
        dest=[well_plate_1["A2"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_75",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": True, "repetitions": 3, "volume": 4},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 3},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 3, "volume": 15},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 76: Mix 6 RxN
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=20,
        source=[well_plate_2["A6"]],
        dest=[well_plate_1["A2"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_76",
            base_liquid_class=glycerol_50_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.2), (50, -0.3), (200, -0.8)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 3},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 40)],
                    "delay": {"enabled": True, "duration": 1},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.2), (50, -0.3), (200, -0.8)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 15, "volume": 40},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 77: Step 6 Start
    thermocycler_module_1.set_block_temperature(20)

    # Step 78: Step 6 Incubation
    protocol.delay(seconds=900)

    # Step 79: Step 6 End
    thermocycler_module_1.set_block_temperature(12)
    thermocycler_module_1.set_lid_temperature(105)

    # Step 80: P2 to Temp C1
    protocol.move_labware(well_plate_2, aluminum_block_1, use_gripper=True)

    # Step 81: P1 to Deck C2
    protocol.move_labware(well_plate_1, "C2", use_gripper=True)

    # Step 82: SB + Sample 2
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=55,
        source=[well_plate_2["A1"]],
        dest=[well_plate_1["A2"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_82",
            base_liquid_class=glycerol_50_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.2), (50, -0.3), (200, -0.8)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": True, "repetitions": 3, "volume": 45},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 3},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 75)],
                    "delay": {"enabled": True, "duration": 1},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.2), (50, -0.3), (200, -0.8)],
                    "push_out_by_volume": [(0, 50)],
                    "mix": {"enabled": True, "repetitions": 5, "volume": 75},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 83: Bead 2 Start
    thermocycler_module_1.close_lid()
    thermocycler_module_1_task_5 = thermocycler_module_1.start_execute_profile(
        [
            {"temperature": 98, "hold_time_seconds": 210},
        ],
        1,
        block_max_volume=50,
    )

    # Step 84: EtOH to Res 2
    pipette_left.transfer_with_liquid_class(
        volume=4000,
        source=[tube_rack_1["A3"]],
        dest=[reservoir_1["A2"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_84",
            base_liquid_class=ethanol_80_base_class,
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_1000ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 15},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 500)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (10, -0.9), (100, -2.6), (1000, -32.2)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 300)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (10, -0.9), (100, -2.6), (1000, -32.2)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 85: pause
    protocol.wait_for_tasks([thermocycler_module_1_task_5])

    # Step 86: Bead 2 End
    thermocycler_module_1.open_lid()

    # Step 87: P1 to Mag
    protocol.move_labware(well_plate_1, magnetic_block_1, use_gripper=True)

    # Step 88: Bind Beads to Mag 2
    protocol.delay(seconds=180)

    # Step 89: Rem Sup 2
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=110,
        source=[well_plate_1["A2"]],
        dest=[reservoir_1["A11"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_89",
            base_liquid_class=glycerol_50_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.2), (50, -0.3), (200, -0.8)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 100)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.2), (50, -0.3), (200, -0.8)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 90: Add EtOH 2.1
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=150,
        source=[reservoir_1["A2"]],
        dest=[well_plate_1["A2"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_90",
            base_liquid_class=ethanol_80_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 100)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 10)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 10},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 91: Rem EtOH 2.1
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_1["A2"]],
        dest=[reservoir_1["A11"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_91",
            base_liquid_class=ethanol_80_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 4},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 150)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 92: Add EtOH 2.2
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=150,
        source=[reservoir_1["A2"]],
        dest=[well_plate_1["A2"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_92",
            base_liquid_class=ethanol_80_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 100)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 10)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 10},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 93: Rem EtOH 2.2
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_1["A2"]],
        dest=[reservoir_1["A11"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_93",
            base_liquid_class=ethanol_80_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 6},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 150)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 94: P1 to Deck C2
    protocol.move_labware(well_plate_1, "C2", use_gripper=True)

    # Step 95: Elute 2
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=22,
        source=[reservoir_1["A1"]],
        dest=[well_plate_1["A2"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_95",
            base_liquid_class=water_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 20)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 10, "volume": 15},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 96: 7A + 7B Mix
    pipette_left.transfer_with_liquid_class(
        volume=50,
        source=[aluminum_block_2["A6"]],
        dest=[aluminum_block_2["B6"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_96",
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 100)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 75)],
                    "mix": {"enabled": True, "repetitions": 10, "volume": 200},
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 97: Mix 7 Disperse
    pipette_left.distribute_with_liquid_class(
        volume=30,
        source=[aluminum_block_2["B6"]],
        dest=[well_plate_1["A3"], well_plate_1["B3"], well_plate_1["C3"], well_plate_1["D3"], well_plate_1["E3"], well_plate_1["F3"], well_plate_1["G3"], well_plate_1["H3"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_97",
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_1000ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 716},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 716},
                    },
                    "correction_by_volume": [(0, 0)],
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 5)],
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 98: P1 to Mag
    protocol.move_labware(well_plate_1, magnetic_block_1, use_gripper=True)

    # Step 99: Elute 2 Min
    protocol.delay(seconds=60)

    # Step 100: Mix 7 RxN
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=20,
        source=[well_plate_1["A2"]],
        dest=[well_plate_1["A3"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_6, tip_rack_5, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_100",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 20)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 3},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 40)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 10, "volume": 40},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 101: Temp D1 to 24C
    temperature_module_2.start_set_temperature(24)

    # Step 102: P1 to Cycler
    protocol.move_labware(well_plate_1, thermocycler_module_1, use_gripper=True)

    # Step 103: Step 7 Incubation
    thermocycler_module_1.close_lid()
    thermocycler_module_1_task_6 = thermocycler_module_1.start_execute_profile(
        [
            {"temperature": 98, "hold_time_seconds": 30},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 60, "hold_time_seconds": 30},
            {"temperature": 72, "hold_time_seconds": 30},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 60, "hold_time_seconds": 30},
            {"temperature": 72, "hold_time_seconds": 30},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 60, "hold_time_seconds": 30},
            {"temperature": 72, "hold_time_seconds": 30},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 60, "hold_time_seconds": 30},
            {"temperature": 72, "hold_time_seconds": 30},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 60, "hold_time_seconds": 30},
            {"temperature": 72, "hold_time_seconds": 30},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 60, "hold_time_seconds": 30},
            {"temperature": 72, "hold_time_seconds": 30},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 60, "hold_time_seconds": 30},
            {"temperature": 72, "hold_time_seconds": 30},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 60, "hold_time_seconds": 30},
            {"temperature": 72, "hold_time_seconds": 30},
            {"temperature": 72, "hold_time_seconds": 60},
        ],
        1,
        block_max_volume=50,
    )

    # Step 104: SB Disperse 3
    pipette_left.distribute_with_liquid_class(
        volume=55,
        source=[aluminum_block_2["C3"]],
        dest=[well_plate_2["A1"], well_plate_2["B1"], well_plate_2["C1"], well_plate_2["D1"], well_plate_2["E1"], well_plate_2["F1"], well_plate_2["G1"], well_plate_2["H1"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_104",
            base_liquid_class=glycerol_50_base_class,
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_1000ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 400)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (10, -0.2), (100, -0.1), (1000, 12)],
                    "delay": {"enabled": True, "duration": 1},
                    "mix": {"enabled": True, "repetitions": 5, "volume": 500},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {
                            "enabled": True,
                            "z_offset": -10,
                            "mm_from_edge": 0.5,
                            "speed": 30,
                        },
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 1, "y": 0, "z": 5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "delay": {"enabled": True, "duration": 1},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "source", "flow_rate": 250},
                    },
                    "correction_by_volume": [(0, 0), (10, -0.2), (100, -0.1), (1000, 12)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 1, "y": 0, "z": 5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "delay": {"enabled": True, "duration": 1},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "source", "flow_rate": 250},
                    },
                    "correction_by_volume": [(0, 0), (10, -0.2), (100, -0.1), (1000, 12)],
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 5)],
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 105: Box0 B3 Off
    protocol.move_labware(tip_rack_2, waste_chute, use_gripper=True)

    # Step 106: Box2 A4 to B3
    protocol.move_labware(tip_rack_4, "B3", use_gripper=True)

    # Step 107: Box1 C3 to A4
    protocol.move_labware(tip_rack_3, "A4", use_gripper=True)

    # Step 108: Box3 B4 to C3
    protocol.move_labware(tip_rack_5, "C3", use_gripper=True)

    # Step 109: Step 7 Delay
    protocol.delay(seconds=600)

    # Step 110: 8B Disperse
    pipette_left.distribute_with_liquid_class(
        volume=45,
        source=[aluminum_block_2["C1"]],
        dest=[well_plate_2["A11"], well_plate_2["B11"], well_plate_2["C11"], well_plate_2["D11"], well_plate_2["E11"], well_plate_2["F11"], well_plate_2["G11"], well_plate_2["H11"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_110",
            base_liquid_class=glycerol_50_base_class,
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_1000ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 100)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (10, -0.2), (100, -0.1), (1000, 12)],
                    "delay": {"enabled": True, "duration": 1},
                    "mix": {"enabled": True, "repetitions": 3, "volume": 200},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 20)],
                    "delay": {"enabled": True, "duration": 1},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 716},
                    },
                    "correction_by_volume": [(0, 0), (10, -0.2), (100, -0.1), (1000, 12)],
                    "push_out_by_volume": [(0, 35)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 20)],
                    "delay": {"enabled": True, "duration": 1},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 716},
                    },
                    "correction_by_volume": [(0, 0), (10, -0.2), (100, -0.1), (1000, 12)],
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 10)],
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 111: pause
    protocol.wait_for_tasks([thermocycler_module_1_task_6])

    # Step 112: Step 7 Incubation
    thermocycler_module_1.open_lid()
    thermocycler_module_1.set_block_temperature(24)
    thermocycler_module_1.set_lid_temperature(56)

    # Step 113: P1 to Deck C2
    protocol.move_labware(well_plate_1, "C2", use_gripper=True)

    # Step 114: Temp C1 to 65C
    temperature_module_1.start_set_temperature(65)

    # Step 115: Temp D1 to 4C
    temperature_module_2.start_set_temperature(4)

    # Step 116: SB + Sample 3
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=50,
        source=[well_plate_2["A1"]],
        dest=[well_plate_1["A3"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_4, tip_rack_5, tip_rack_6, tip_rack_3, tip_rack_7],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_116",
            base_liquid_class=glycerol_50_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.2), (50, -0.3), (200, -0.8)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": True, "repetitions": 3, "volume": 45},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 3},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 75)],
                    "delay": {"enabled": True, "duration": 1},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.2), (50, -0.3), (200, -0.8)],
                    "push_out_by_volume": [(0, 50)],
                    "mix": {"enabled": True, "repetitions": 5, "volume": 75},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 117: Bind Beads
    protocol.delay(seconds=300)

    # Step 118: P1 to Mag
    protocol.move_labware(well_plate_1, magnetic_block_1, use_gripper=True)

    # Step 119: EtOH to Res 3
    pipette_left.transfer_with_liquid_class(
        volume=4000,
        source=[tube_rack_1["A3"]],
        dest=[reservoir_1["A2"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_119",
            base_liquid_class=ethanol_80_base_class,
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_1000ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 500)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (10, -0.9), (100, -2.6), (1000, -32.2)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 300)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (10, -0.9), (100, -2.6), (1000, -32.2)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 120: Step 8.1 Cycler Prep
    thermocycler_module_1.set_block_temperature(48)

    # Step 121: Rem Sup 3
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[well_plate_1["A3"]],
        dest=[reservoir_1["A10"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_4, tip_rack_5, tip_rack_6, tip_rack_3, tip_rack_7],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_121",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 100)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 122: Add EtOH 3.1
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=150,
        source=[reservoir_1["A2"]],
        dest=[well_plate_1["A3"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_4, tip_rack_5, tip_rack_6, tip_rack_3, tip_rack_7],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_122",
            base_liquid_class=ethanol_80_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 100)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 10)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 10},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 123: Rem EtOH 3.1
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_1["A3"]],
        dest=[reservoir_1["A10"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_4, tip_rack_5, tip_rack_6, tip_rack_3, tip_rack_7],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_123",
            base_liquid_class=ethanol_80_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 4},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 150)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 124: Add EtOH 3.2
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=150,
        source=[reservoir_1["A2"]],
        dest=[well_plate_1["A3"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_4, tip_rack_5, tip_rack_6, tip_rack_3, tip_rack_7],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_124",
            base_liquid_class=ethanol_80_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 100)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 10)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 10},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 125: Rem EtOH 3.2
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_1["A3"]],
        dest=[reservoir_1["A10"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_4, tip_rack_5, tip_rack_6, tip_rack_3, tip_rack_7],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_125",
            base_liquid_class=ethanol_80_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 6},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 150)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 126: P1 to Deck C2
    protocol.move_labware(well_plate_1, "C2", use_gripper=True)

    # Step 127: 8B Elute 1
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=35,
        source=[well_plate_2["A11"]],
        dest=[well_plate_1["A3"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_4, tip_rack_5, tip_rack_6, tip_rack_3, tip_rack_7],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_127",
            base_liquid_class=glycerol_50_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.2), (50, -0.3), (200, -0.8)],
                    "delay": {"enabled": True, "duration": 1},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 2, "y": -2, "z": 3},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 15)],
                    "delay": {"enabled": True, "duration": 1},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.2), (50, -0.3), (200, -0.8)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 128: 8B Elute 2
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=15,
        source=[well_plate_1["A3"]],
        dest=[well_plate_1["A3"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_4, tip_rack_5, tip_rack_6, tip_rack_3, tip_rack_7],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_128",
            base_liquid_class=glycerol_50_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.2), (50, -0.3), (200, -0.8)],
                    "delay": {"enabled": True, "duration": 1},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 2, "y": 2, "z": 3},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 15)],
                    "delay": {"enabled": True, "duration": 1},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.2), (50, -0.3), (200, -0.8)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 129: 8B Elute 3
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=15,
        source=[well_plate_1["A3"]],
        dest=[well_plate_1["A3"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_4, tip_rack_5, tip_rack_6, tip_rack_3, tip_rack_7],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_129",
            base_liquid_class=glycerol_50_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.2), (50, -0.3), (200, -0.8)],
                    "delay": {"enabled": True, "duration": 1},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": -2, "y": 2, "z": 3},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 15)],
                    "delay": {"enabled": True, "duration": 1},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.2), (50, -0.3), (200, -0.8)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 130: 8B Elute 4
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=15,
        source=[well_plate_1["A3"]],
        dest=[well_plate_1["A3"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_4, tip_rack_5, tip_rack_6, tip_rack_3, tip_rack_7],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_130",
            base_liquid_class=glycerol_50_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.2), (50, -0.3), (200, -0.8)],
                    "delay": {"enabled": True, "duration": 1},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": -2, "y": -2, "z": 3},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 15)],
                    "delay": {"enabled": True, "duration": 1},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.2), (50, -0.3), (200, -0.8)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 131: P1 to Cycler
    protocol.move_labware(well_plate_1, thermocycler_module_1, use_gripper=True)

    # Step 132: 8B Mix
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.pick_up_tip(location=tip_rack_4)
    pipette_right.mix(
        repetitions=10,
        volume=15,
        location=well_plate_1["A3"].bottom(z=3),
        aspirate_flow_rate=25,
        dispense_flow_rate=15,
        dispense_delay=1,
        final_push_out=0,
    )
    pipette_right.drop_tip(waste_chute)

    # Step 133: P1 to Mag
    protocol.move_labware(well_plate_1, magnetic_block_1, use_gripper=True)

    # Step 134: P2 to Deck C2
    protocol.move_labware(well_plate_2, "C2", use_gripper=True)

    # Step 135: Step 8 Set Up 2
    thermocycler_module_1.set_block_temperature(95)

    # Step 136: 8C Disperse
    pipette_left.distribute_with_liquid_class(
        volume=25,
        source=[aluminum_block_2["C2"]],
        dest=[well_plate_2["A12"], well_plate_2["B12"], well_plate_2["C12"], well_plate_2["D12"], well_plate_2["E12"], well_plate_2["F12"], well_plate_2["G12"], well_plate_2["H12"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_136",
            base_liquid_class=glycerol_50_base_class,
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_1000ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (10, -0.2), (100, -0.1), (1000, 12)],
                    "delay": {"enabled": True, "duration": 1},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 20)],
                    "delay": {"enabled": True, "duration": 0.5},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "source", "flow_rate": 250},
                    },
                    "correction_by_volume": [(0, 0), (10, -0.2), (100, -0.1), (1000, 12)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 20)],
                    "delay": {"enabled": True, "duration": 0.5},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "source", "flow_rate": 250},
                    },
                    "correction_by_volume": [(0, 0), (10, -0.2), (100, -0.1), (1000, 12)],
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 20)],
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 137: Bind Beads to Mag 3
    protocol.delay(seconds=60)

    # Step 138: 8B Add
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=25,
        source=[well_plate_1["A3"]],
        dest=[well_plate_2["A7"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_4, tip_rack_5, tip_rack_6, tip_rack_3, tip_rack_7],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_138",
            base_liquid_class=glycerol_50_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 15)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.2), (50, -0.3), (200, -0.8)],
                    "delay": {"enabled": True, "duration": 0.5},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "delay": {"enabled": True, "duration": 0.5},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.2), (50, -0.3), (200, -0.8)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 15, "volume": 15},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 139: P2 to Temp C1
    protocol.move_labware(well_plate_2, aluminum_block_1, use_gripper=True)

    # Step 140: P2 to Deck C2
    protocol.move_labware(well_plate_2, "C2", use_gripper=True)

    # Step 141: temperature
    temperature_module_1.start_set_temperature(24)

    # Step 142: 8C Add
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=15,
        source=[well_plate_2["A12"]],
        dest=[well_plate_2["A7"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_4, tip_rack_5, tip_rack_6, tip_rack_3, tip_rack_7],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_142",
            base_liquid_class=glycerol_50_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 15)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.2), (50, -0.3), (200, -0.8)],
                    "delay": {"enabled": True, "duration": 1},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 12},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 15)],
                    "delay": {"enabled": True, "duration": 0.5},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {
                            "enabled": True,
                            "z_offset": -2,
                            "mm_from_edge": 0.5,
                            "speed": 30,
                        },
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.2), (50, -0.3), (200, -0.8)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 143: P2 to Cycler
    protocol.move_labware(well_plate_2, thermocycler_module_1, use_gripper=True)

    # Step 144: Step 8 Incubation
    thermocycler_module_1.close_lid()
    thermocycler_module_1_task_7 = thermocycler_module_1.start_execute_profile(
        [
            {"temperature": 95, "hold_time_seconds": 300},
            {"temperature": 60, "hold_time_seconds": 3600},
        ],
        1,
        block_max_volume=60,
    )

    # Step 145: Step 8 Delay
    protocol.delay(seconds=2880)

    # Step 146: 9A to Res
    pipette_left.transfer_with_liquid_class(
        volume=4000,
        source=[tube_rack_1["A2"]],
        dest=[reservoir_1["A3"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_146",
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_1000ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 500)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 500)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 147: 9B to Res
    pipette_left.transfer_with_liquid_class(
        volume=4000,
        source=[tube_rack_1["B2"]],
        dest=[reservoir_1["A4"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_147",
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_1000ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 500)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 500)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 148: 9C to Res
    pipette_left.transfer_with_liquid_class(
        volume=5000,
        source=[tube_rack_1["C2"]],
        dest=[reservoir_1["A5"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_148",
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_1000ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 500)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 500)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 149: P1 to Deck
    protocol.move_labware(well_plate_1, "C2", use_gripper=True)

    # Step 150: Temp C1 to 60C
    temperature_module_1.start_set_temperature(60)

    # Step 151: CB Mix
    pipette_left.pick_up_tip(location=tip_rack_1)
    pipette_left.mix(
        repetitions=10,
        volume=230,
        location=aluminum_block_2["C4"].bottom(z=2),
        aspirate_flow_rate=200,
        dispense_flow_rate=500,
        final_push_out=0,
    )
    pipette_left.flow_rate.blow_out = 250
    pipette_left.blow_out(aluminum_block_2["C4"].top(z=-10))
    pipette_left.drop_tip(waste_chute)

    # Step 152: CB Disperse
    pipette_left.distribute_with_liquid_class(
        volume=25,
        source=[aluminum_block_2["C4"]],
        dest=[well_plate_1["A4"], well_plate_1["B4"], well_plate_1["C4"], well_plate_1["D4"], well_plate_1["E4"], well_plate_1["F4"], well_plate_1["G4"], well_plate_1["H4"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_152",
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_1000ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "source", "flow_rate": 250},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "source", "flow_rate": 250},
                    },
                    "correction_by_volume": [(0, 0)],
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 5)],
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 153: P1 to Mag
    protocol.move_labware(well_plate_1, magnetic_block_1, use_gripper=True)

    # Step 154: Rem CB
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=25,
        source=[well_plate_1["A4"]],
        dest=[reservoir_1["A9"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_4, tip_rack_5, tip_rack_6, tip_rack_3, tip_rack_7],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_154",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 100)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 155: P1 to Deck C2
    protocol.move_labware(well_plate_1, "C2", use_gripper=True)

    # Step 156: Add 9A 1
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=150,
        source=[reservoir_1["A3"]],
        dest=[well_plate_1["A4"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_4, tip_rack_5, tip_rack_6, tip_rack_3, tip_rack_7],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_156",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 100)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 3},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 10, "volume": 100},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 157: P1 to Mag
    protocol.move_labware(well_plate_1, magnetic_block_1, use_gripper=True)

    # Step 158: Bind Beads
    protocol.delay(seconds=30)

    # Step 159: Rem 9A 1
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=150,
        source=[well_plate_1["A4"]],
        dest=[reservoir_1["A9"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_4, tip_rack_5, tip_rack_6, tip_rack_3, tip_rack_7],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_159",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 100)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 3},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 160: P1 to Deck C2
    protocol.move_labware(well_plate_1, "C2", use_gripper=True)

    # Step 161: Add 9A 2
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_1["A3"]],
        dest=[well_plate_1["A4"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_4, tip_rack_5, tip_rack_6, tip_rack_3, tip_rack_7],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_161",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 100)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 3},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 10, "volume": 75},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 162: P1 to Temp C1
    protocol.move_labware(well_plate_1, aluminum_block_1, use_gripper=True)

    # Step 163: pause
    protocol.wait_for_tasks([thermocycler_module_1_task_7])

    # Step 164: Step 8 End
    thermocycler_module_1.open_lid()

    # Step 165: 9A to RxN 8
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[well_plate_1["A4"]],
        dest=[well_plate_2["A7"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_4, tip_rack_5, tip_rack_6, tip_rack_3, tip_rack_7],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_165",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": True, "repetitions": 3, "volume": 75},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 4},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 75)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 5, "volume": 75},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 166: Temp C1 to 68C
    temperature_module_1.start_set_temperature(68)

    # Step 167: 9A Start
    thermocycler_module_1.close_lid()
    thermocycler_module_1_task_8 = thermocycler_module_1.start_execute_profile(
        [
            {"temperature": 48, "hold_time_seconds": 600},
        ],
        1,
        block_max_volume=100,
    )

    # Step 168: Box2 B3 to B4
    protocol.move_labware(tip_rack_4, "B4", use_gripper=True)

    # Step 169: Box4 C4 to B3
    protocol.move_labware(tip_rack_6, "B3", use_gripper=True)

    # Step 170: 9B Disperse
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.distribute_with_liquid_class(
        volume=170,
        source=[reservoir_1["A4"]],
        dest=[well_plate_1["A5"], well_plate_1["A6"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_170",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_1000ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 100)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 12},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 716},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 12},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 716},
                    },
                    "correction_by_volume": [(0, 0)],
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 10)],
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 171: pause
    protocol.wait_for_tasks([thermocycler_module_1_task_8])

    # Step 172: 9A End
    thermocycler_module_1.open_lid()
    thermocycler_module_1.set_block_temperature(24)

    # Step 173: P2 to Mag
    protocol.move_labware(well_plate_2, magnetic_block_1, use_gripper=True)

    # Step 174: 9B cycler Prep
    thermocycler_module_1.set_block_temperature(68)
    thermocycler_module_1.set_lid_temperature(75)

    # Step 175: P1 to Cycler
    protocol.move_labware(well_plate_1, thermocycler_module_1, use_gripper=True)

    # Step 176: Rem 9A 2
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_2["A7"]],
        dest=[reservoir_1["A9"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_5, tip_rack_6, tip_rack_3, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_176",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 8},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 177: Add 9B 1
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=150,
        source=[well_plate_1["A5"]],
        dest=[well_plate_2["A7"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_5, tip_rack_6, tip_rack_3, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_177",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 1},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 12},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 178: P2 to Temp C1
    protocol.move_labware(well_plate_2, aluminum_block_1, use_gripper=True)

    # Step 179: Mix 9B 1
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.pick_up_tip(location=tip_rack_5)
    pipette_right.mix(
        repetitions=10,
        volume=100,
        location=well_plate_2["A7"].bottom(z=4),
        aspirate_flow_rate=150,
        dispense_flow_rate=150,
        final_push_out=0,
    )
    pipette_right.drop_tip(waste_chute)

    # Step 180: P2 to Mag
    protocol.move_labware(well_plate_2, magnetic_block_1, use_gripper=True)

    # Step 181: Rem 9B 1
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_2["A7"]],
        dest=[reservoir_1["A8"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_5, tip_rack_6, tip_rack_3, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_181",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 182: Add 9B 2
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=150,
        source=[well_plate_1["A6"]],
        dest=[well_plate_2["A7"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_5, tip_rack_6, tip_rack_3, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_182",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 1},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 12},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 183: P2 to Temp C1
    protocol.move_labware(well_plate_2, aluminum_block_1, use_gripper=True)

    # Step 184: Mix 9B 2
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.pick_up_tip(location=tip_rack_5)
    pipette_right.mix(
        repetitions=10,
        volume=100,
        location=well_plate_2["A7"].bottom(z=4),
        aspirate_flow_rate=150,
        dispense_flow_rate=150,
        final_push_out=0,
    )
    pipette_right.drop_tip(waste_chute)

    # Step 185: 9C Cycler Set Up
    thermocycler_module_1.set_block_temperature(48)
    thermocycler_module_1.set_lid_temperature(85)

    # Step 186: 9C Disperse
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.distribute_with_liquid_class(
        volume=170,
        source=[reservoir_1["A5"]],
        dest=[well_plate_1["A7"], well_plate_1["A8"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_186",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_1000ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 100)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 12},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 716},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 12},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 716},
                    },
                    "correction_by_volume": [(0, 0)],
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 10)],
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 187: 9B Incubation
    protocol.delay(seconds=60)

    # Step 188: Temp C1 to 48
    temperature_module_1.start_set_temperature(48)

    # Step 189: RxN Transfer
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=150,
        source=[well_plate_2["A7"]],
        dest=[well_plate_2["A8"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_5, tip_rack_6, tip_rack_3, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_189",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": True, "repetitions": 1, "volume": 75},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 10},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 190: P2 to Mag
    protocol.move_labware(well_plate_2, magnetic_block_1, use_gripper=True)

    # Step 191: Rem 9B 2
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_2["A8"]],
        dest=[reservoir_1["A8"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_5, tip_rack_6, tip_rack_3, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_191",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 4},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 192: Add 9C 1
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=150,
        source=[well_plate_1["A7"]],
        dest=[well_plate_2["A8"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_5, tip_rack_6, tip_rack_3, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_192",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 1},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 12},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 193: P2 to Temp C1
    protocol.move_labware(well_plate_2, aluminum_block_1, use_gripper=True)

    # Step 194: Mix 9C 1
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.pick_up_tip(location=tip_rack_6)
    pipette_right.mix(
        repetitions=10,
        volume=100,
        location=well_plate_2["A8"].bottom(z=4),
        aspirate_flow_rate=150,
        dispense_flow_rate=150,
        final_push_out=0,
    )
    pipette_right.drop_tip(waste_chute)

    # Step 195: P2 to Mag
    protocol.move_labware(well_plate_2, magnetic_block_1, use_gripper=True)

    # Step 196: Rem 9C 1
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_2["A8"]],
        dest=[reservoir_1["A7"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_5, tip_rack_6, tip_rack_3, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_196",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 197: Add 9C 2
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=150,
        source=[well_plate_1["A8"]],
        dest=[well_plate_2["A8"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_5, tip_rack_6, tip_rack_3, tip_rack_7, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_197",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 1},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 12},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 198: P2 to Temp C1
    protocol.move_labware(well_plate_2, aluminum_block_1, use_gripper=True)

    # Step 199: Mix 9C 2
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.pick_up_tip(location=tip_rack_6)
    pipette_right.mix(
        repetitions=10,
        volume=100,
        location=well_plate_2["A8"].bottom(z=4),
        aspirate_flow_rate=150,
        dispense_flow_rate=150,
        final_push_out=0,
    )
    pipette_right.drop_tip(waste_chute)

    # Step 200: Box 3 C3 to C4
    protocol.move_labware(tip_rack_5, "C4", use_gripper=True)

    # Step 201: Box 5 D4 to C3
    protocol.move_labware(tip_rack_7, "C3", use_gripper=True)

    # Step 202: P1 to Deck C2
    protocol.move_labware(well_plate_1, "C2", use_gripper=True)

    # Step 203: Step 10 Cycler Prep
    thermocycler_module_1.set_block_temperature(98)
    thermocycler_module_1.set_lid_temperature(105)

    # Step 204: 9C Incubation
    protocol.delay(seconds=5)

    # Step 205: P2 to Mag
    protocol.move_labware(well_plate_2, magnetic_block_1, use_gripper=True)

    # Step 206: Temp C1 to 24C
    temperature_module_1.start_set_temperature(24)

    # Step 207: P1 to Temp C1
    protocol.move_labware(well_plate_1, aluminum_block_1, use_gripper=True)

    # Step 208: Rem 9C 2
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_2["A8"]],
        dest=[reservoir_1["A7"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_6, tip_rack_7, tip_rack_5, tip_rack_3, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_208",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 209: Add LTE
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=50,
        source=[reservoir_1["A1"]],
        dest=[well_plate_2["A8"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_6, tip_rack_7, tip_rack_5, tip_rack_3, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_209",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 1, "y": 0, "z": 5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 210: Box 4 B3 to D4
    protocol.move_labware(tip_rack_6, "D4", use_gripper=True)

    # Step 211: Box1 A4 to B3
    protocol.move_labware(tip_rack_3, "B3", use_gripper=True)

    # Step 212: Rem LTE
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=50,
        source=[well_plate_2["A8"]],
        dest=[reservoir_1["A7"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_7, tip_rack_6, tip_rack_5, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_212",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 6},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 100)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 213: P2 to Deck C2
    protocol.move_labware(well_plate_2, "C2", use_gripper=True)

    # Step 214: Elute 3
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=20,
        source=[reservoir_1["A1"]],
        dest=[well_plate_2["A8"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_7, tip_rack_6, tip_rack_5, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_214",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 20)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 20)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 5, "volume": 15},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 215: 10A + 10B Mix
    pipette_left.transfer_with_liquid_class(
        volume=50,
        source=[aluminum_block_2["C5"]],
        dest=[aluminum_block_2["C6"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_7, tip_rack_6, tip_rack_5, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_215",
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 100)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 75)],
                    "mix": {"enabled": True, "repetitions": 10, "volume": 200},
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 216: Mix 10 Disperse
    pipette_left.distribute_with_liquid_class(
        volume=32,
        source=[aluminum_block_2["C6"]],
        dest=[well_plate_2["A9"], well_plate_2["B9"], well_plate_2["C9"], well_plate_2["D9"], well_plate_2["E9"], well_plate_2["F9"], well_plate_2["G9"], well_plate_2["H9"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_216",
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_1000ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 716},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 716},
                    },
                    "correction_by_volume": [(0, 0)],
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 5)],
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 217: Temp D1 Deactivate
    temperature_module_2.deactivate()

    # Step 218: Mix 10 RxN
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=30,
        source=[well_plate_2["A9"]],
        dest=[well_plate_2["A8"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_7, tip_rack_6, tip_rack_5, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_218",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 20)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 3},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 40)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 10, "volume": 40},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 219: P2 to Cycler
    protocol.move_labware(well_plate_2, thermocycler_module_1, use_gripper=True)

    # Step 220: Step 10 Incubation
    thermocycler_module_1.close_lid()
    thermocycler_module_1_task_9 = thermocycler_module_1.start_execute_profile(
        [
            {"temperature": 98, "hold_time_seconds": 30},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 60, "hold_time_seconds": 30},
            {"temperature": 72, "hold_time_seconds": 30},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 60, "hold_time_seconds": 30},
            {"temperature": 72, "hold_time_seconds": 30},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 60, "hold_time_seconds": 30},
            {"temperature": 72, "hold_time_seconds": 30},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 60, "hold_time_seconds": 30},
            {"temperature": 72, "hold_time_seconds": 30},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 60, "hold_time_seconds": 30},
            {"temperature": 72, "hold_time_seconds": 30},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 60, "hold_time_seconds": 30},
            {"temperature": 72, "hold_time_seconds": 30},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 60, "hold_time_seconds": 30},
            {"temperature": 72, "hold_time_seconds": 30},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 60, "hold_time_seconds": 30},
            {"temperature": 72, "hold_time_seconds": 30},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 60, "hold_time_seconds": 30},
            {"temperature": 72, "hold_time_seconds": 30},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 60, "hold_time_seconds": 30},
            {"temperature": 72, "hold_time_seconds": 30},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 60, "hold_time_seconds": 30},
            {"temperature": 72, "hold_time_seconds": 30},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 60, "hold_time_seconds": 30},
            {"temperature": 72, "hold_time_seconds": 30},
            {"temperature": 72, "hold_time_seconds": 60},
        ],
        1,
        block_max_volume=50,
    )

    # Step 221: SB Disperse 4
    pipette_left.distribute_with_liquid_class(
        volume=55,
        source=[aluminum_block_2["C3"]],
        dest=[well_plate_1["A10"], well_plate_1["B10"], well_plate_1["C10"], well_plate_1["D10"], well_plate_1["E10"], well_plate_1["F10"], well_plate_1["G10"], well_plate_1["H10"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_221",
            base_liquid_class=glycerol_50_base_class,
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_1000ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 300)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (10, -0.2), (100, -0.1), (1000, 12)],
                    "delay": {"enabled": True, "duration": 0.7},
                    "mix": {"enabled": True, "repetitions": 5, "volume": 300},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {
                            "enabled": True,
                            "z_offset": -10,
                            "mm_from_edge": 0.5,
                            "speed": 30,
                        },
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 1, "y": 0, "z": 5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "delay": {"enabled": True, "duration": 1},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "source", "flow_rate": 250},
                    },
                    "correction_by_volume": [(0, 0), (10, -0.2), (100, -0.1), (1000, 12)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 1, "y": 0, "z": 5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "delay": {"enabled": True, "duration": 1},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "source", "flow_rate": 250},
                    },
                    "correction_by_volume": [(0, 0), (10, -0.2), (100, -0.1), (1000, 12)],
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 5)],
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 222: EtOH to Res 4
    pipette_left.transfer_with_liquid_class(
        volume=4000,
        source=[tube_rack_1["A3"]],
        dest=[reservoir_1["A2"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_222",
            base_liquid_class=ethanol_80_base_class,
            properties={"flex_1channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_1000ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 500)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (10, -0.9), (100, -2.6), (1000, -32.2)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 300)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (10, -0.9), (100, -2.6), (1000, -32.2)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_left.drop_tip(waste_chute)

    # Step 223: pause
    protocol.wait_for_tasks([thermocycler_module_1_task_9])

    # Step 224: Step 10 Incubation
    thermocycler_module_1.open_lid()
    thermocycler_module_1.set_block_temperature(4)
    thermocycler_module_1.deactivate_lid()

    # Step 225: P2 to Deck C2
    protocol.move_labware(well_plate_2, "C2", use_gripper=True)

    # Step 226: SB + Sample 4
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=50,
        source=[well_plate_1["A10"]],
        dest=[well_plate_2["A8"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_7, tip_rack_6, tip_rack_5, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_226",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": True, "repetitions": 3, "volume": 45},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 3},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 75)],
                    "delay": {"enabled": True, "duration": 1},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 50,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 50)],
                    "mix": {"enabled": True, "repetitions": 5, "volume": 75},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 227: Bead Incubation 4
    protocol.delay(seconds=300)

    # Step 228: P2 to Mag
    protocol.move_labware(well_plate_2, magnetic_block_1, use_gripper=True)

    # Step 229: Pause 2 min
    protocol.delay(seconds=120)

    # Step 230: Rem Sup 4
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[well_plate_2["A8"]],
        dest=[reservoir_1["A6"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_7, tip_rack_6, tip_rack_5, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_230",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 100)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 231: Add EtOH 4.1
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=150,
        source=[reservoir_1["A2"]],
        dest=[well_plate_2["A8"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_7, tip_rack_6, tip_rack_5, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_231",
            base_liquid_class=ethanol_80_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 150)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 10)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 10},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 232: Rem EtOH 4.1
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_2["A8"]],
        dest=[reservoir_1["A6"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_7, tip_rack_6, tip_rack_5, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_232",
            base_liquid_class=ethanol_80_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 4},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 150)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 233: Add EtOH 4.2
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=150,
        source=[reservoir_1["A2"]],
        dest=[well_plate_2["A8"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_7, tip_rack_6, tip_rack_5, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_233",
            base_liquid_class=ethanol_80_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 150)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 10)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 10},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 234: Rem EtOH 4.2
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_2["A8"]],
        dest=[reservoir_1["A6"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_7, tip_rack_6, tip_rack_5, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_234",
            base_liquid_class=ethanol_80_base_class,
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 6},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 150)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (5, -0.5), (50, -0.2), (200, -4.9)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 235: P2 to Deck C2
    protocol.move_labware(well_plate_2, "C2", use_gripper=True)

    # Step 236: Elute 4
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=17,
        source=[reservoir_1["A1"]],
        dest=[well_plate_2["A8"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_7, tip_rack_6, tip_rack_5, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_236",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 20)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 5, "volume": 13},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 237: Pause 2 min
    protocol.delay(seconds=120)

    # Step 238: P2 to Mag
    protocol.move_labware(well_plate_2, magnetic_block_1, use_gripper=True)

    # Step 239: Pause 2 min
    protocol.delay(seconds=120)

    # Step 240: Final Lib Elute
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=16,
        source=[well_plate_2["A8"]],
        dest=[well_plate_1["A12"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2, tip_rack_3, tip_rack_7, tip_rack_6, tip_rack_5, tip_rack_4],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_240",
            properties={"flex_8channel_1000": {"opentrons/opentrons_flex_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 20)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 20)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 500,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 500,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 241: Temp C1 Deactivate
    temperature_module_1.deactivate()

    # Step 242: P1 to Cycler
    protocol.move_labware(well_plate_1, thermocycler_module_1, use_gripper=True)

    # Step 243: Close Cycler
    thermocycler_module_1.close_lid()

    # Step 244: pause
    protocol.pause("Library ready")

    # Step 245: Temp C1 to 4C
    temperature_module_1.start_set_temperature(4)

    # Step 246: Open Cycler
    thermocycler_module_1.open_lid()
    thermocycler_module_1.deactivate_block()

    # Step 247: P1 to Temp C1
    protocol.move_labware(well_plate_1, aluminum_block_1, use_gripper=True)

    # Step 248: Take Libraries off
    protocol.pause("Take samples and place on ice. ")

    # Step 249: Temp C1 Deactivate
    temperature_module_1.deactivate()

    # Step 250: Deactivate Cycler
    thermocycler_module_1.close_lid()

DESIGNER_APPLICATION = """{"robot":{"model":"OT-3 Standard"},"designerApplication":{"name":"opentrons/protocol-designer","version":"8.9.0","data":{"pipetteTiprackAssignments":{"155ded0a-0639-45fb-b83f-df0574691c2f":["opentrons/opentrons_flex_96_filtertiprack_1000ul/1","opentrons/opentrons_flex_96_filtertiprack_200ul/1"],"2141dc88-dedc-41c1-8ebc-1a8868fa9069":["opentrons/opentrons_flex_96_filtertiprack_200ul/1","opentrons/opentrons_flex_96_filtertiprack_1000ul/1"]},"dismissedWarnings":{"form":[],"timeline":[]},"ingredients":{"0":{"displayName":"Input","displayColor":"#b925ff","description":null,"liquidGroupId":"0"},"1":{"displayName":"P1-P8","displayColor":"#a973c7ff","description":null,"liquidGroupId":"1"},"2":{"displayName":"8A","displayColor":"#ff0000ff","description":null,"liquidGroupId":"2"},"3":{"displayName":"2A","displayColor":"#d9d9d9ff","description":null,"liquidGroupId":"3"},"4":{"displayName":"2B","displayColor":"#d9d9d9ff","description":null,"liquidGroupId":"4"},"5":{"displayName":"3A","displayColor":"#ffe699ff","description":null,"liquidGroupId":"5"},"6":{"displayName":"3B","displayColor":"#ffe699ff","description":null,"liquidGroupId":"6"},"7":{"displayName":"4A","displayColor":"#a9d08eff","description":null,"liquidGroupId":"7"},"8":{"displayName":"4B","displayColor":"#a9d08eff","description":null,"liquidGroupId":"8"},"9":{"displayName":"5A","displayColor":"#ed7c37ff","description":null,"liquidGroupId":"9"},"10":{"displayName":"5B","displayColor":"#ed7c37ff","description":null,"liquidGroupId":"10"},"11":{"displayName":"6A","displayColor":"#a973c7ff","description":null,"liquidGroupId":"11"},"12":{"displayName":"6B","displayColor":"#a973c7ff","description":null,"liquidGroupId":"12"},"13":{"displayName":"7A","displayColor":"#2f75b5ff","description":null,"liquidGroupId":"13"},"14":{"displayName":"7B","displayColor":"#2f75b5ff","description":null,"liquidGroupId":"14"},"15":{"displayName":"8B","displayColor":"#ff0000ff","description":null,"liquidGroupId":"15"},"16":{"displayName":"8C","displayColor":"#ff0000ff","description":null,"liquidGroupId":"16"},"17":{"displayName":"9A","displayColor":"#48d0ffff","description":null,"liquidGroupId":"17"},"18":{"displayName":"9B","displayColor":"#48d0ffff","description":null,"liquidGroupId":"18"},"19":{"displayName":"9C","displayColor":"#48d0ffff","description":null,"liquidGroupId":"19"},"20":{"displayName":"CB","displayColor":"#48d0ffff","description":null,"liquidGroupId":"20"},"21":{"displayName":"10A","displayColor":"#38e85aff","description":null,"liquidGroupId":"21"},"22":{"displayName":"10B","displayColor":"#38e85aff","description":null,"liquidGroupId":"22"},"23":{"displayName":"80% Ethanol","displayColor":"#1b0994ff","description":null,"liquidGroupId":"23"},"24":{"displayName":"SB","displayColor":"#311e0aff","description":null,"liquidGroupId":"24"},"25":{"displayName":"H2O","displayColor":"#9dffd8ff","description":null,"liquidGroupId":"25"},"26":{"displayName":"LTE","displayColor":"#9dffd8","description":null,"liquidGroupId":"26"}},"ingredLocations":{"4a3bea46-728a-498c-9c2e-a5caf006f10b:opentrons/opentrons_flex_96_filtertiprack_200ul/1":{},"f1d18a33-99d2-4f9d-bdd6-3d4fe1f15b4a:opentrons/opentrons_flex_96_filtertiprack_200ul/1":{},"2d19a470-70c5-4006-9b83-85dd5572f12a:opentrons/opentrons_flex_96_filtertiprack_200ul/1":{},"2bd3ba52-6320-4739-b104-ef168e2e144a:opentrons/opentrons_flex_96_filtertiprack_200ul/1":{},"7be17658-efe0-4c22-a4a4-9c50c70e566a:opentrons/opentrons_flex_96_filtertiprack_200ul/1":{},"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5":{"A1":{"0":{"volume":10}},"B1":{"0":{"volume":10}},"C1":{"0":{"volume":10}},"D1":{"0":{"volume":10}},"E1":{"0":{"volume":10}},"F1":{"0":{"volume":10}},"G1":{"0":{"volume":10}},"H1":{"0":{"volume":10}}},"6db7eb96-52b3-489e-805e-010e35d88119:opentrons/opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical/3":{"A1":{"26":{"volume":5000}},"A2":{"17":{"volume":4000}},"B2":{"18":{"volume":4000}},"C2":{"19":{"volume":4000}},"A3":{"23":{"volume":25000}}},"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5":{"A5":{"1":{"volume":1}},"B5":{"1":{"volume":1}},"C5":{"1":{"volume":1}},"D5":{"1":{"volume":1}},"E5":{"1":{"volume":1}},"F5":{"1":{"volume":1}},"G5":{"1":{"volume":1}},"H5":{"1":{"volume":1}},"A7":{"2":{"volume":1}},"B7":{"2":{"volume":1}},"C7":{"2":{"volume":1}},"D7":{"2":{"volume":1}},"E7":{"2":{"volume":1}},"F7":{"2":{"volume":1}},"G7":{"2":{"volume":1}},"H7":{"2":{"volume":1}}},"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3":{"A1":{"3":{"volume":75}},"B1":{"4":{"volume":15}},"A2":{"5":{"volume":180}},"B2":{"6":{"volume":36}},"A3":{"7":{"volume":230}},"B3":{"8":{"volume":30}},"A4":{"9":{"volume":120}},"B4":{"10":{"volume":18}},"A5":{"11":{"volume":250}},"B5":{"12":{"volume":10}},"A6":{"13":{"volume":70}},"B6":{"14":{"volume":250}},"C1":{"15":{"volume":450}},"C2":{"16":{"volume":350}},"C3":{"24":{"volume":1900}},"C4":{"20":{"volume":250}},"C5":{"21":{"volume":70}},"C6":{"22":{"volume":250}},"D1":{"25":{"volume":500}}}},"savedStepForms":{"__INITIAL_DECK_SETUP_STEP__":{"stepType":"manualIntervention","id":"__INITIAL_DECK_SETUP_STEP__","labwareLocationUpdate":{"b474f89a-f894-48b8-ae4e-dee6cbae8d7c:opentrons/opentrons_flex_96_filtertiprack_1000ul/1":"A3","271a7505-3035-4be2-8204-80a7546b6512:opentrons/opentrons_flex_96_filtertiprack_200ul/1":"B3","4a3bea46-728a-498c-9c2e-a5caf006f10b:opentrons/opentrons_flex_96_filtertiprack_200ul/1":"C3","f1d18a33-99d2-4f9d-bdd6-3d4fe1f15b4a:opentrons/opentrons_flex_96_filtertiprack_200ul/1":"A4","2d19a470-70c5-4006-9b83-85dd5572f12a:opentrons/opentrons_flex_96_filtertiprack_200ul/1":"B4","2bd3ba52-6320-4739-b104-ef168e2e144a:opentrons/opentrons_flex_96_filtertiprack_200ul/1":"C4","7be17658-efe0-4c22-a4a4-9c50c70e566a:opentrons/opentrons_flex_96_filtertiprack_200ul/1":"D4","594810cf-69c3-4e9c-8f82-a8f9b38ad79d:opentrons/opentrons_96_well_aluminum_block/1":"033331ec-47f1-4f9a-9c01-ca09a87b9ac1:temperatureModuleType","3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5":"offDeck","6db7eb96-52b3-489e-805e-010e35d88119:opentrons/opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical/3":"offDeck","b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3":"offDeck","6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5":"offDeck","09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3":"65263cf9-315d-4e77-a59d-5e60ac83f781:temperatureModuleType"},"pipetteLocationUpdate":{"155ded0a-0639-45fb-b83f-df0574691c2f":"left","2141dc88-dedc-41c1-8ebc-1a8868fa9069":"right"},"moduleLocationUpdate":{"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType":"B1","033331ec-47f1-4f9a-9c01-ca09a87b9ac1:temperatureModuleType":"C1","65263cf9-315d-4e77-a59d-5e60ac83f781:temperatureModuleType":"D1","561cc9e8-ae90-49c1-bccf-75a85989930b:magneticBlockType":"D2"},"trashBinLocationUpdate":{},"wasteChuteLocationUpdate":{"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute":"cutoutD3"},"stagingAreaLocationUpdate":{"33419948-a850-4e7f-8ebb-4691cc6707f0:stagingArea":"cutoutA3","d2945620-4da1-45e7-a628-c4eb94e4d2a6:stagingArea":"cutoutB3","7ad11239-9ba8-4ca7-949b-565612f7adee:stagingArea":"cutoutC3","3f82d2f9-7619-435c-9ad6-900f4cf9bebf:stagingArea":"cutoutD3"},"gripperLocationUpdate":{"156a112d-16e9-4507-b6e0-1bd16080be0a:gripper":"mounted"},"moduleStateUpdate":{}},"82ff0816-ea0c-4e4f-a55d-f8d452cec89d":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"82ff0816-ea0c-4e4f-a55d-f8d452cec89d","stepType":"pause","stepName":"pause","stepDetails":""},"10ecbb35-df45-4c7f-86c3-b05938ec35d2":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"10ecbb35-df45-4c7f-86c3-b05938ec35d2","stepType":"pause","stepName":"pause","stepDetails":""},"b0c16a14-9d8b-4c1c-8c3f-4fb80a559d02":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"b0c16a14-9d8b-4c1c-8c3f-4fb80a559d02","stepType":"pause","stepName":"pause","stepDetails":""},"d14d2741-709f-4f0b-8d8d-b4c794619d19":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"d14d2741-709f-4f0b-8d8d-b4c794619d19","stepType":"pause","stepName":"pause","stepDetails":""},"6f19fec9-bed6-45f1-9d9a-f3e9232b733b":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"6f19fec9-bed6-45f1-9d9a-f3e9232b733b","stepType":"pause","stepName":"pause","stepDetails":""},"0a349f6f-82b3-482b-bdb1-36d78d622323":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"0a349f6f-82b3-482b-bdb1-36d78d622323","stepType":"pause","stepName":"pause","stepDetails":""},"f9ac1247-149f-45fb-9c3d-469a569b2266":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"f9ac1247-149f-45fb-9c3d-469a569b2266","stepType":"pause","stepName":"pause","stepDetails":""},"fb55ebcb-995b-401c-861c-ee5664d76979":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"fb55ebcb-995b-401c-861c-ee5664d76979","stepType":"pause","stepName":"pause","stepDetails":""},"27f244fb-9345-4837-9684-5070a8d14431":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"27f244fb-9345-4837-9684-5070a8d14431","stepType":"pause","stepName":"pause","stepDetails":""},"85fa5fb6-144e-4465-9e17-775a6f52d4ee":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"85fa5fb6-144e-4465-9e17-775a6f52d4ee","stepType":"pause","stepName":"pause","stepDetails":""},"a27b1b3b-4704-420f-8be1-5ebe9081accd":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"a27b1b3b-4704-420f-8be1-5ebe9081accd","stepType":"pause","stepName":"pause","stepDetails":""},"d6f77157-9364-4787-b07c-2aa726c53864":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"d6f77157-9364-4787-b07c-2aa726c53864","stepType":"pause","stepName":"pause","stepDetails":""},"8c2df33c-23dc-4659-992c-f887b9e8e83f":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"8c2df33c-23dc-4659-992c-f887b9e8e83f","stepType":"pause","stepName":"pause","stepDetails":""},"8bc9f620-2822-4d26-9cc9-c46a5092d359":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"8bc9f620-2822-4d26-9cc9-c46a5092d359","stepType":"pause","stepName":"pause","stepDetails":""},"d59aebd9-2881-42b5-8f75-a5bf05420258":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"d59aebd9-2881-42b5-8f75-a5bf05420258","stepType":"pause","stepName":"pause","stepDetails":""},"c33af065-aa1e-4bc5-941e-324324e0dd0d":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"c33af065-aa1e-4bc5-941e-324324e0dd0d","stepType":"pause","stepName":"pause","stepDetails":""},"cfe38fc8-4f78-4af2-b12a-b85636421c0b":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"cfe38fc8-4f78-4af2-b12a-b85636421c0b","stepType":"pause","stepName":"pause","stepDetails":""},"28619e82-cbfd-4dcd-b6c4-c43429eeeb84":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"28619e82-cbfd-4dcd-b6c4-c43429eeeb84","stepType":"pause","stepName":"pause","stepDetails":""},"19359c0c-3cdc-4f89-a41d-092d9a22d068":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"19359c0c-3cdc-4f89-a41d-092d9a22d068","stepType":"pause","stepName":"pause","stepDetails":""},"8eeeb323-fd2f-4e1e-8bf5-a9b035de1721":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"8eeeb323-fd2f-4e1e-8bf5-a9b035de1721","stepType":"pause","stepName":"pause","stepDetails":""},"22b1a196-ea6c-4aa1-96f4-d1054408a0ce":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"22b1a196-ea6c-4aa1-96f4-d1054408a0ce","stepType":"pause","stepName":"pause","stepDetails":""},"336ab6d4-029c-4519-9bc1-30ab14840f95":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"336ab6d4-029c-4519-9bc1-30ab14840f95","stepType":"pause","stepName":"pause","stepDetails":""},"7bd8f168-ed36-449d-9b72-f6564e0d0848":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"7bd8f168-ed36-449d-9b72-f6564e0d0848","stepType":"pause","stepName":"pause","stepDetails":""},"4391562a-238d-4af6-b89c-2b7ba08c763f":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"4391562a-238d-4af6-b89c-2b7ba08c763f","stepType":"pause","stepName":"pause","stepDetails":""},"9fe5174c-0f4c-4351-992c-c7780f6b301f":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"9fe5174c-0f4c-4351-992c-c7780f6b301f","stepType":"pause","stepName":"pause","stepDetails":""},"8d6fe45c-ea19-4239-97a4-0a7b3a39dca5":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"8d6fe45c-ea19-4239-97a4-0a7b3a39dca5","stepType":"pause","stepName":"pause","stepDetails":""},"904c0748-27fb-4479-aa8a-289b4ab97cbe":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"904c0748-27fb-4479-aa8a-289b4ab97cbe","stepType":"pause","stepName":"pause","stepDetails":""},"b29493c9-d771-4c9a-9a10-e66c2d071fb4":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"b29493c9-d771-4c9a-9a10-e66c2d071fb4","stepType":"pause","stepName":"pause","stepDetails":""},"2b2f8049-a470-4c3d-9ce7-dc93e7965b50":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"2b2f8049-a470-4c3d-9ce7-dc93e7965b50","stepType":"pause","stepName":"pause","stepDetails":""},"62b241a1-4c56-4bb7-a4f9-65ff602937c4":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"62b241a1-4c56-4bb7-a4f9-65ff602937c4","stepType":"pause","stepName":"pause","stepDetails":""},"6d7fdee5-bbee-48fd-871c-79b56fceaccb":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"6d7fdee5-bbee-48fd-871c-79b56fceaccb","stepType":"pause","stepName":"pause","stepDetails":""},"8f84a863-693d-4e81-bd36-390a0b85d4f8":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"8f84a863-693d-4e81-bd36-390a0b85d4f8","stepType":"pause","stepName":"pause","stepDetails":""},"9d36b42c-1cca-443f-b322-92c8bcfd9779":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"9d36b42c-1cca-443f-b322-92c8bcfd9779","stepType":"pause","stepName":"pause","stepDetails":""},"7485f815-e767-4dbd-996a-2ee026c5f141":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"7485f815-e767-4dbd-996a-2ee026c5f141","stepType":"pause","stepName":"pause","stepDetails":""},"db7c9d99-fbf9-4e5d-bd85-f28fe885de01":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"db7c9d99-fbf9-4e5d-bd85-f28fe885de01","stepType":"pause","stepName":"pause","stepDetails":""},"9146303c-2c15-4290-be5f-fbaf49b300e0":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"9146303c-2c15-4290-be5f-fbaf49b300e0","stepType":"pause","stepName":"pause","stepDetails":""},"42ecec27-c1db-4359-8667-838c61df94e2":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"42ecec27-c1db-4359-8667-838c61df94e2","stepType":"pause","stepName":"pause","stepDetails":""},"5f9d3d44-f3b0-497e-a240-0989649e47ab":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"5f9d3d44-f3b0-497e-a240-0989649e47ab","stepType":"pause","stepName":"pause","stepDetails":""},"f7f8d8a4-ec78-4516-b402-e42da5136a85":{"home_before":false,"filename":null,"resolution":null,"zoom":null,"contrast":null,"brightness":null,"saturation":null,"id":"f7f8d8a4-ec78-4516-b402-e42da5136a85","stepType":"camera","stepName":"Module Set up","stepDetails":"","stepNumber":0},"3189d4da-e030-49de-9f7e-b0730c3c4d73":{"moduleId":"65263cf9-315d-4e77-a59d-5e60ac83f781:temperatureModuleType","setTemperature":"true","targetTemperature":"4","id":"3189d4da-e030-49de-9f7e-b0730c3c4d73","stepType":"temperature","stepName":"Temp D1 4 C","stepDetails":"","stepNumber":0},"eb470c8d-e040-4d88-a53a-b77c01db6d5b":{"moduleId":"033331ec-47f1-4f9a-9c01-ca09a87b9ac1:temperatureModuleType","setTemperature":"true","targetTemperature":"12","id":"eb470c8d-e040-4d88-a53a-b77c01db6d5b","stepType":"temperature","stepName":"Temp C1 12 C","stepDetails":"","stepNumber":0},"5ecf8966-038a-44e2-8ae3-69aa45dc2fe3":{"blockIsActive":false,"blockTargetTemp":"","lidIsActive":false,"lidOpen":true,"lidTargetTemp":"","moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":[],"profileItemsById":{},"profileTargetLidTemp":null,"profileVolume":null,"thermocyclerFormType":"thermocyclerState","blockIsActiveHold":false,"blockTargetTempHold":null,"lidIsActiveHold":false,"lidOpenHold":null,"lidTargetTempHold":null,"id":"5ecf8966-038a-44e2-8ae3-69aa45dc2fe3","stepType":"thermocycler","stepName":"Open Cycler","stepDetails":"","stepNumber":0},"1e1f2b3d-2658-4c64-8190-432863878537":{"moduleId":null,"pauseAction":"untilResume","pauseMessage":"Remove the used lid seal and replace with the new seal provided in the Duoseq kit.","pauseTemperature":null,"pauseTime":null,"id":"1e1f2b3d-2658-4c64-8190-432863878537","stepType":"pause","stepName":"Replace Lid Seal","stepDetails":"Remove old lid seal and replace with the new seal provided in the Duoseq kit.","stepNumber":0},"93745cb0-644f-439d-aa1a-4e038f1097b3":{"blockIsActive":true,"blockTargetTemp":"37","lidIsActive":true,"lidOpen":true,"lidTargetTemp":"75","moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":[],"profileItemsById":{},"profileTargetLidTemp":null,"profileVolume":null,"thermocyclerFormType":"thermocyclerState","blockIsActiveHold":false,"blockTargetTempHold":null,"lidIsActiveHold":false,"lidOpenHold":null,"lidTargetTempHold":null,"id":"93745cb0-644f-439d-aa1a-4e038f1097b3","stepType":"thermocycler","stepName":"Step 2 Cycler Prep","stepDetails":"","stepNumber":0},"ec46e4a0-c689-4a20-9838-320b3b83165a":{"labware":"6db7eb96-52b3-489e-805e-010e35d88119:opentrons/opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical/3","newLocation":"A2","useGripper":false,"id":"ec46e4a0-c689-4a20-9838-320b3b83165a","stepType":"moveLabware","stepName":"Conical Tube Rack to slot A2","stepDetails":"Put Conical tube rack at position A2 on the deck.","stepNumber":0},"886936bf-210f-4e9f-bfc6-41e8e8e36aa4":{"labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","newLocation":"B2","useGripper":false,"id":"886936bf-210f-4e9f-bfc6-41e8e8e36aa4","stepType":"moveLabware","stepName":"Reservoir to B2","stepDetails":"Put Reservoir at position B2 on the deck.","stepNumber":0},"7b2834b6-8bba-43c0-9020-3863f6988cca":{"labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"594810cf-69c3-4e9c-8f82-a8f9b38ad79d:opentrons/opentrons_96_well_aluminum_block/1","useGripper":false,"id":"7b2834b6-8bba-43c0-9020-3863f6988cca","stepType":"moveLabware","stepName":"Plate 1 to C2","stepDetails":"Place plate 1 on the temperature block located at position C1 on the deck.","stepNumber":0},"b3ba6306-9ce0-4252-b76c-b751400875b0":{"labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"C2","useGripper":false,"id":"b3ba6306-9ce0-4252-b76c-b751400875b0","stepType":"moveLabware","stepName":"Plate 2 to Temp at C1","stepDetails":"Place Plate 2 at position C2 on the deck.","stepNumber":0},"b2d27fd1-e137-418c-a983-4f2afb0787fe":{"moduleId":null,"pauseAction":"untilResume","pauseMessage":"Place all 2 mL tubes from DuoSeq Kit to indicated position on the 24-well Aluminum Block located at position D1 on the deck","pauseTemperature":null,"pauseTime":null,"id":"b2d27fd1-e137-418c-a983-4f2afb0787fe","stepType":"pause","stepName":"2 mL tubes to 24-well Aluminum block","stepDetails":"Remove old lid seal and replace with the new seal provided in the Duoseq kit.","stepNumber":0},"8ab7c733-f380-498c-b756-e6b7d67140c3":{"home_before":false,"filename":null,"resolution":null,"zoom":null,"contrast":null,"brightness":null,"saturation":null,"id":"8ab7c733-f380-498c-b756-e6b7d67140c3","stepType":"camera","stepName":"Labware Set UP","stepDetails":"","stepNumber":0},"869f366b-90af-4459-9839-a08f9df5042c":{"moduleId":null,"pauseAction":"untilResume","pauseMessage":"Remove all caps from all 2 ml tubes and conical tubes.","pauseTemperature":null,"pauseTime":null,"id":"869f366b-90af-4459-9839-a08f9df5042c","stepType":"pause","stepName":"Cap Removal","stepDetails":"Remove all caps from all 2 ml tubes and conical tubes.","stepNumber":0},"9db89d6f-3c0a-40a2-b975-11e5b3c7b218":{"home_before":false,"filename":null,"resolution":null,"zoom":null,"contrast":null,"brightness":null,"saturation":null,"id":"9db89d6f-3c0a-40a2-b975-11e5b3c7b218","stepType":"camera","stepName":"Full Deck Set Up","stepDetails":"","stepNumber":0},"a08d8754-fb66-484b-bc0a-7e01c4d26985":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":0.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":true,"blowout_flowRate":"250","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"50","dispense_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","dispense_mix_checkbox":true,"dispense_mix_times":"10","dispense_mix_volume":"50","dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["B1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"single","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"60","id":"a08d8754-fb66-484b-bc0a-7e01c4d26985","stepType":"moveLiquid","stepName":"2A + 2B Mix","stepDetails":"","stepNumber":0},"d7a992d4-ad3b-4c2b-a85d-bbbf061b0090":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":0.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["B1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dispense_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A2","B2","C2","D2","E2","F2","G2","H2"],"dispense_x_position":1,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"10","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"multiDispense","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"15","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"6","id":"d7a992d4-ad3b-4c2b-a85d-bbbf061b0090","stepType":"moveLiquid","stepName":"Mix 2 Disperse","stepDetails":"","stepNumber":0},"92fd55db-ddb2-4820-b2bb-8303db043f83":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"10","aspirate_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":true,"dispense_mix_times":"5","dispense_mix_volume":"8","dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"10","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"5","id":"92fd55db-ddb2-4820-b2bb-8303db043f83","stepType":"moveLiquid","stepName":"Mix 2 RxN","stepDetails":"","stepNumber":0},"c8f7ddf9-f232-44d9-a686-cd861d693341":{"labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","useGripper":true,"id":"c8f7ddf9-f232-44d9-a686-cd861d693341","stepType":"moveLabware","stepName":"P1 to Cycler","stepDetails":"","stepNumber":0},"803f90b2-4f50-4838-af63-292ba8ea44dc":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:19:00","id":"803f90b2-4f50-4838-af63-292ba8ea44dc","stepType":"pause","stepName":"Step 2A Delay","stepDetails":"","stepNumber":0},"7dd38451-c1fc-4845-a128-0a43408b57ea":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"716","aspirate_labware":"6db7eb96-52b3-489e-805e-010e35d88119:opentrons/opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"716","dispense_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":"","dispense_mmFromBottom":5,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"single","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_1000ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"5000","id":"7dd38451-c1fc-4845-a128-0a43408b57ea","stepType":"moveLiquid","stepName":"LTE to Res","stepDetails":"","stepNumber":0},"f5abc40d-72f1-498e-ab60-efe9bc8e4680":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"500","aspirate_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["D1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"100","dispense_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A10","B10","C10","D10","E10","F10","G10","H10"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"5","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"multiDispense","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_1000ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"50","id":"f5abc40d-72f1-498e-ab60-efe9bc8e4680","stepType":"moveLiquid","stepName":"H2O to P2","stepDetails":"","stepNumber":0},"c090a7a1-1c8e-4963-af89-99ed5ab2f89d":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"150","aspirate_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":0.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"250","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"150","dispense_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","dispense_mix_checkbox":true,"dispense_mix_times":"10","dispense_mix_volume":"125","dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["B2"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"single","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"50","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"144","id":"c090a7a1-1c8e-4963-af89-99ed5ab2f89d","stepType":"moveLiquid","stepName":"3A + 3B Mix","stepDetails":"","stepNumber":0},"e1aa0d6f-4de9-44b5-ae3b-40ca0d0b5912":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":0.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["B2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"20","dispense_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3","B3","C3","D3","E3","F3","G3","H3"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"5","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"multiDispense","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"15","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"17","id":"e1aa0d6f-4de9-44b5-ae3b-40ca0d0b5912","stepType":"moveLiquid","stepName":"Mix 3 Disperse","stepDetails":"","stepNumber":0},"1c964a84-b27e-4de6-9f94-483831289e77":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"1c964a84-b27e-4de6-9f94-483831289e77","stepType":"pause","stepName":"pause","stepDetails":""},"9eba86f9-bb30-412d-ba62-9adf3128b015":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"30","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":true,"dispense_mix_times":"10","dispense_mix_volume":"20","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"15","id":"9eba86f9-bb30-412d-ba62-9adf3128b015","stepType":"moveLiquid","stepName":"Mix 3 RxN","stepDetails":"","stepNumber":0},"d0e6a43e-f30b-4994-b7b0-8e1c7ebe778d":{"blockIsActive":false,"blockTargetTemp":null,"lidIsActive":false,"lidOpen":false,"lidTargetTemp":null,"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":["4ba6d73d-44fe-47d9-bb29-1b096658a33b","10c9355e-d47f-48b1-90aa-ec23241c5793","31f347e5-5697-4104-8ead-ac1637c48706"],"profileItemsById":{"4ba6d73d-44fe-47d9-bb29-1b096658a33b":{"durationMinutes":"10","durationSeconds":"00","id":"4ba6d73d-44fe-47d9-bb29-1b096658a33b","temperature":"25","title":"1","type":"profileStep"},"10c9355e-d47f-48b1-90aa-ec23241c5793":{"durationMinutes":"15","durationSeconds":"00","id":"10c9355e-d47f-48b1-90aa-ec23241c5793","temperature":"42","title":"2","type":"profileStep"},"31f347e5-5697-4104-8ead-ac1637c48706":{"durationMinutes":"20","durationSeconds":"00","id":"31f347e5-5697-4104-8ead-ac1637c48706","temperature":"75","title":"3","type":"profileStep"}},"profileTargetLidTemp":"85","profileVolume":"30","thermocyclerFormType":"thermocyclerProfile","id":"d0e6a43e-f30b-4994-b7b0-8e1c7ebe778d","stepType":"thermocycler","stepName":"Step 3 Start","stepDetails":""},"156fc5c3-6141-4012-8c4e-3d3308d3c386":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"156fc5c3-6141-4012-8c4e-3d3308d3c386","stepType":"pause","stepName":"pause","stepDetails":""},"6b34a55f-e41e-4e34-867b-bd6a1ab638ec":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:40:00","id":"6b34a55f-e41e-4e34-867b-bd6a1ab638ec","stepType":"pause","stepName":"Step 3 Delay","stepDetails":"","stepNumber":0},"470f8d7a-5548-4dac-9cb2-374e8b57859a":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"1","aspirate_flowRate":"200","aspirate_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","aspirate_mix_checkbox":true,"aspirate_mix_times":"3","aspirate_mix_volume":"250","aspirate_mmFromBottom":20,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"1","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":true,"aspirate_touchTip_mmFromTop":-10,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["C3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"250","blowout_location":"source_well","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":true,"dispense_delay_seconds":"1","dispense_flowRate":"200","dispense_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":5,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1","B1","C1","D1","E1","F1","G1","H1"],"dispense_x_position":1,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"5","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"glycerol_50","nozzles":null,"path":"multiDispense","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_1000ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"55","id":"470f8d7a-5548-4dac-9cb2-374e8b57859a","stepType":"moveLiquid","stepName":"SB Disperse 1","stepDetails":"","stepNumber":0},"26115080-470c-4811-85a4-bd748d5fdc4f":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"200","aspirate_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":0.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"250","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"200","dispense_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","dispense_mix_checkbox":true,"dispense_mix_times":"10","dispense_mix_volume":"150","dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["B3"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"single","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"75","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","id":"26115080-470c-4811-85a4-bd748d5fdc4f","stepType":"moveLiquid","stepName":"4A+4B Mix","stepDetails":"","stepNumber":0},"d20a9cdc-2ecb-450c-80e1-d7fa8fcbda69":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"1","aspirate_flowRate":"200","aspirate_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":0.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["B3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"20","dispense_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A4","B4","C4","D4","E4","F4","G4","H4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"5","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"multiDispense","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"15","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"22","id":"d20a9cdc-2ecb-450c-80e1-d7fa8fcbda69","stepType":"moveLiquid","stepName":"Mix 4 Disperse","stepDetails":"","stepNumber":0},"22a69388-b106-42a5-9cce-12f7ceb2609b":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"22a69388-b106-42a5-9cce-12f7ceb2609b","stepType":"pause","stepName":"pause","stepDetails":""},"041f07a1-5ab0-4a68-a2dc-3a138804b088":{"blockIsActive":true,"blockTargetTemp":"16","lidIsActive":true,"lidOpen":true,"lidTargetTemp":"37","moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":[],"profileItemsById":{},"profileTargetLidTemp":null,"profileVolume":null,"thermocyclerFormType":"thermocyclerState","id":"041f07a1-5ab0-4a68-a2dc-3a138804b088","stepType":"thermocycler","stepName":"Step 3 Incubation","stepDetails":""},"9fcfdacd-6205-4cf2-803b-cc1ccc4c44a7":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"40","aspirate_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A4"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"40","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":true,"dispense_mix_times":"10","dispense_mix_volume":"40","dispense_mmFromBottom":3,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"20","id":"9fcfdacd-6205-4cf2-803b-cc1ccc4c44a7","stepType":"moveLiquid","stepName":"Mix 4 RxN","stepDetails":"","stepNumber":0},"31aa158c-d167-4bd1-bb01-9586065b6edc":{"blockIsActive":true,"blockTargetTemp":"16","lidIsActive":true,"lidOpen":false,"lidTargetTemp":"37","moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":[],"profileItemsById":{},"profileTargetLidTemp":null,"profileVolume":null,"thermocyclerFormType":"thermocyclerState","blockIsActiveHold":false,"blockTargetTempHold":null,"lidIsActiveHold":false,"lidOpenHold":null,"lidTargetTempHold":null,"id":"31aa158c-d167-4bd1-bb01-9586065b6edc","stepType":"thermocycler","stepName":"Step 4 cycler Set Up","stepDetails":"","stepNumber":0},"ee130f51-993f-44d2-8c7b-fd02475414d4":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:30:00","id":"ee130f51-993f-44d2-8c7b-fd02475414d4","stepType":"pause","stepName":"Step 4 Incubation","stepDetails":"","stepNumber":0},"d3e00fc1-d353-4a63-ac05-eea9fd0fb43b":{"blockIsActive":true,"blockTargetTemp":"16","lidIsActive":true,"lidOpen":true,"lidTargetTemp":"75","moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":[],"profileItemsById":{},"profileTargetLidTemp":null,"profileVolume":null,"thermocyclerFormType":"thermocyclerState","blockIsActiveHold":false,"blockTargetTempHold":null,"lidIsActiveHold":false,"lidOpenHold":null,"lidTargetTempHold":null,"id":"d3e00fc1-d353-4a63-ac05-eea9fd0fb43b","stepType":"thermocycler","stepName":"Step 4 End","stepDetails":"","stepNumber":0},"441bfc07-aa25-4198-9ee5-47e960e3d619":{"labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"594810cf-69c3-4e9c-8f82-a8f9b38ad79d:opentrons/opentrons_96_well_aluminum_block/1","useGripper":true,"id":"441bfc07-aa25-4198-9ee5-47e960e3d619","stepType":"moveLabware","stepName":"P2 to Temp C1","stepDetails":"","stepNumber":0},"35cbdeeb-0475-4364-9602-afa936d7462b":{"labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"C2","useGripper":true,"id":"35cbdeeb-0475-4364-9602-afa936d7462b","stepType":"moveLabware","stepName":"P1 to Deck C2","stepDetails":"","stepNumber":0},"4efa6455-d70c-4cf4-bfe4-30f4b724d4d5":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":true,"aspirate_mix_times":"3","aspirate_mix_volume":"45","aspirate_mmFromBottom":1.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"1","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"50","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":true,"dispense_delay_seconds":"1","dispense_flowRate":"75","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":true,"dispense_mix_times":"5","dispense_mix_volume":"75","dispense_mmFromBottom":3,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"50","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"glycerol_50","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"50","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"50","id":"4efa6455-d70c-4cf4-bfe4-30f4b724d4d5","stepType":"moveLiquid","stepName":"SB + Sample 1","stepDetails":"","stepNumber":0},"c030b267-9047-46dc-9e20-12b6d8f7561c":{"blockIsActive":false,"blockTargetTemp":null,"lidIsActive":false,"lidOpen":false,"lidTargetTemp":null,"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":["ce258417-8eea-41be-be1b-8f717a42fc70"],"profileItemsById":{"ce258417-8eea-41be-be1b-8f717a42fc70":{"durationMinutes":"04","durationSeconds":"00","id":"ce258417-8eea-41be-be1b-8f717a42fc70","temperature":"20","title":"1","type":"profileStep"}},"profileTargetLidTemp":"75","profileVolume":"50","thermocyclerFormType":"thermocyclerProfile","blockIsActiveHold":false,"blockTargetTempHold":null,"lidIsActiveHold":false,"lidOpenHold":null,"lidTargetTempHold":null,"id":"c030b267-9047-46dc-9e20-12b6d8f7561c","stepType":"thermocycler","stepName":"Bead 1 Start","stepDetails":"","stepNumber":0},"f2efca7d-696e-4cf2-a436-f9c5c69d2033":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"500","aspirate_labware":"6db7eb96-52b3-489e-805e-010e35d88119:opentrons/opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":30,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"300","blowout_location":"dest_well","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"12","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"300","dispense_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":5,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A2"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"ethanol_80","nozzles":null,"path":"single","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"","tipRack":"opentrons/opentrons_flex_96_filtertiprack_1000ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"4000","id":"f2efca7d-696e-4cf2-a436-f9c5c69d2033","stepType":"moveLiquid","stepName":"EtOH to Res 1","stepDetails":"","stepNumber":0},"92998ae9-bf8a-47f7-8bf9-4058c09e9262":{"labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"561cc9e8-ae90-49c1-bccf-75a85989930b:magneticBlockType","useGripper":true,"id":"92998ae9-bf8a-47f7-8bf9-4058c09e9262","stepType":"moveLabware","stepName":"P1 to Mag","stepDetails":"","stepNumber":0},"0000e7c0-bf27-4bf7-8ff6-cd609ff06142":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"25","aspirate_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"100","dispense_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":"","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","id":"0000e7c0-bf27-4bf7-8ff6-cd609ff06142","stepType":"moveLiquid","stepName":"Rem Sup 1","stepDetails":"","stepNumber":0},"34b1c83a-e57c-4af9-92fb-7b33586a647f":{"aspirate_airGap_checkbox":true,"aspirate_airGap_volume":"10","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"100","aspirate_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0.5","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"100","blowout_location":"dest_well","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"10","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"50","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":10,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"ethanol_80","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"150","id":"34b1c83a-e57c-4af9-92fb-7b33586a647f","stepType":"moveLiquid","stepName":"Add EtOH 1.1","stepDetails":"","stepNumber":0},"6856b413-c500-4e1e-bbaa-3975badf4a2e":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"25","aspirate_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0.5","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"100","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"10","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"150","dispense_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":4,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"ethanol_80","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","id":"6856b413-c500-4e1e-bbaa-3975badf4a2e","stepType":"moveLiquid","stepName":"Rem EtOH 1.1","stepDetails":"","stepNumber":0},"54774486-843d-45bd-a8fd-c5a5c67d9d61":{"aspirate_airGap_checkbox":true,"aspirate_airGap_volume":"10","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"100","aspirate_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0.5","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"100","blowout_location":"dest_well","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"10","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"50","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":10,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"ethanol_80","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"150","id":"54774486-843d-45bd-a8fd-c5a5c67d9d61","stepType":"moveLiquid","stepName":"Add EtOH 1.2","stepDetails":"","stepNumber":0},"1fd56567-fc34-40d5-8cd7-e6fb007f9cbd":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"25","aspirate_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":0.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0.5","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"100","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"10","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"150","dispense_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":6,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"ethanol_80","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","id":"1fd56567-fc34-40d5-8cd7-e6fb007f9cbd","stepType":"moveLiquid","stepName":"Rem EtOH 1.2","stepDetails":"","stepNumber":0},"d7c8fd93-eaac-428a-a75d-c97b245d60fc":{"labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"C2","useGripper":true,"id":"d7c8fd93-eaac-428a-a75d-c97b245d60fc","stepType":"moveLabware","stepName":"P1 to Deck C2","stepDetails":"","stepNumber":0},"2653b82b-3e88-40d4-847f-3d87dc044ffd":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"5","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"0.5","aspirate_flowRate":"20","aspirate_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"5","dispense_delay_checkbox":false,"dispense_delay_seconds":"0","dispense_flowRate":"50","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":true,"dispense_mix_times":"10","dispense_mix_volume":"15","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"water","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"22","id":"2653b82b-3e88-40d4-847f-3d87dc044ffd","stepType":"moveLiquid","stepName":"Elute 1","stepDetails":"","stepNumber":0},"be1d53b9-199f-486b-83c3-b6bbc192f9e3":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"100","aspirate_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":0.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A4"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"250","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"100","dispense_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","dispense_mix_checkbox":true,"dispense_mix_times":"10","dispense_mix_volume":"70","dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["B4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"single","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"50","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"102","id":"be1d53b9-199f-486b-83c3-b6bbc192f9e3","stepType":"moveLiquid","stepName":"5A + 5B Mix","stepDetails":"","stepNumber":0},"d9564769-82e4-4a83-9adc-75f07feb6f9c":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"100","aspirate_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":0.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["B4"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"20","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A2","B2","C2","D2","E2","F2","G2","H2"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"5","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"multiDispense","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"15","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","id":"d9564769-82e4-4a83-9adc-75f07feb6f9c","stepType":"moveLiquid","stepName":"Mix 5 Disperse","stepDetails":"","stepNumber":0},"2823cf89-b0c8-4e41-a3ee-932f3136215f":{"labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"561cc9e8-ae90-49c1-bccf-75a85989930b:magneticBlockType","useGripper":true,"id":"2823cf89-b0c8-4e41-a3ee-932f3136215f","stepType":"moveLabware","stepName":"P1 to Mag","stepDetails":"","stepNumber":0},"a8b6ac49-7601-4e24-b300-5d76f656235b":{"labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"C2","useGripper":true,"id":"a8b6ac49-7601-4e24-b300-5d76f656235b","stepType":"moveLabware","stepName":"P2 to Deck C2","stepDetails":"","stepNumber":0},"6d4000a6-cd41-4640-a975-260addd3cebe":{"moduleId":"033331ec-47f1-4f9a-9c01-ca09a87b9ac1:temperatureModuleType","setTemperature":"true","targetTemperature":"50","id":"6d4000a6-cd41-4640-a975-260addd3cebe","stepType":"temperature","stepName":"Temp C1 to 50C","stepDetails":"","stepNumber":0},"2e04f225-f5c2-4fcc-b1ce-a5d269644616":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","aspirate_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"3","aspirate_mix_volume":"4","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A10"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"10","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dispense_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":true,"dispense_mix_times":"3","dispense_mix_volume":"4","dispense_mmFromBottom":0.5,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A5"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"water","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"7","id":"2e04f225-f5c2-4fcc-b1ce-a5d269644616","stepType":"moveLiquid","stepName":"Prep P1-P8","stepDetails":"","stepNumber":0},"41fe1efc-b5ea-4850-be65-74feeffd9d14":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"20","aspirate_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":0.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"30","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":true,"dispense_mix_times":"10","dispense_mix_volume":"20","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A2"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"20","id":"41fe1efc-b5ea-4850-be65-74feeffd9d14","stepType":"moveLiquid","stepName":"Mix 5 RxN","stepDetails":"","stepNumber":0},"9d01c0b3-213d-4bf3-9411-c3eb38c5ae36":{"labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","useGripper":true,"id":"9d01c0b3-213d-4bf3-9411-c3eb38c5ae36","stepType":"moveLabware","stepName":"P1 to Cycler","stepDetails":"","stepNumber":0},"22952fc3-db6a-43fa-a4f9-31cf85207a05":{"blockIsActive":false,"blockTargetTemp":null,"lidIsActive":false,"lidOpen":false,"lidTargetTemp":null,"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":["ee96e2f2-3922-454f-a178-b140a446e090","05fedfc0-c522-47a8-a5fb-2118e9a6380a"],"profileItemsById":{"ee96e2f2-3922-454f-a178-b140a446e090":{"durationMinutes":"15","durationSeconds":"00","id":"ee96e2f2-3922-454f-a178-b140a446e090","temperature":"20","title":"1","type":"profileStep"},"05fedfc0-c522-47a8-a5fb-2118e9a6380a":{"durationMinutes":"15","durationSeconds":"00","id":"05fedfc0-c522-47a8-a5fb-2118e9a6380a","temperature":"65","title":"2","type":"profileStep"}},"profileTargetLidTemp":"75","profileVolume":"30","thermocyclerFormType":"thermocyclerProfile","id":"22952fc3-db6a-43fa-a4f9-31cf85207a05","stepType":"thermocycler","stepName":"Step 5 Start","stepDetails":""},"7f3bc144-d1a5-4291-8b5b-1f8919245267":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"7f3bc144-d1a5-4291-8b5b-1f8919245267","stepType":"pause","stepName":"pause","stepDetails":""},"e49bde28-4791-4955-ac5b-18cc0658a1b3":{"labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"594810cf-69c3-4e9c-8f82-a8f9b38ad79d:opentrons/opentrons_96_well_aluminum_block/1","useGripper":true,"id":"e49bde28-4791-4955-ac5b-18cc0658a1b3","stepType":"moveLabware","stepName":"P2 to Temp C1","stepDetails":"","stepNumber":0},"e264b32b-68ed-49e0-88aa-820560e95c3b":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:18:00","id":"e264b32b-68ed-49e0-88aa-820560e95c3b","stepType":"pause","stepName":"Step 5 Delay 1","stepDetails":"","stepNumber":0},"6c7584f1-72c8-4082-aa12-2029f8210e50":{"labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"C2","useGripper":true,"id":"6c7584f1-72c8-4082-aa12-2029f8210e50","stepType":"moveLabware","stepName":"P2 to Deck C2","stepDetails":"","stepNumber":0},"5563f1be-4fc8-454d-b136-d98570ccce12":{"moduleId":"033331ec-47f1-4f9a-9c01-ca09a87b9ac1:temperatureModuleType","setTemperature":"true","targetTemperature":"24","id":"5563f1be-4fc8-454d-b136-d98570ccce12","stepType":"temperature","stepName":"Temp C1 to 24C","stepDetails":"","stepNumber":0},"e9e20c47-0064-4a55-b958-418cd6aa56af":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:05:00","id":"e9e20c47-0064-4a55-b958-418cd6aa56af","stepType":"pause","stepName":"Step 5 Delay 2","stepDetails":"","stepNumber":0},"4165fdc2-49b6-43d8-890d-467e1fb8c69c":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":true,"aspirate_delay_seconds":"1","aspirate_flowRate":"600","aspirate_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","aspirate_mix_checkbox":true,"aspirate_mix_times":"5","aspirate_mix_volume":"600","aspirate_mmFromBottom":10,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"1","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":true,"aspirate_touchTip_mmFromTop":-10,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["C3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"250","blowout_location":"source_well","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":true,"dispense_delay_seconds":"1","dispense_flowRate":"200","dispense_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":5,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1","B1","C1","D1","E1","F1","G1","H1"],"dispense_x_position":1,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"5","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"glycerol_50","nozzles":null,"path":"multiDispense","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"35","tipRack":"opentrons/opentrons_flex_96_filtertiprack_1000ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"55","id":"4165fdc2-49b6-43d8-890d-467e1fb8c69c","stepType":"moveLiquid","stepName":"SB Disperse 2","stepDetails":"","stepNumber":0},"9ff89971-903e-4a7d-b0a0-5da2074d777f":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":true,"aspirate_delay_seconds":"1","aspirate_flowRate":"150","aspirate_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":null,"aspirate_mmFromBottom":0.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"50","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A5"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":true,"blowout_flowRate":"250","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":true,"dispense_delay_seconds":"0.5","dispense_flowRate":"150","dispense_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","dispense_mix_checkbox":true,"dispense_mix_times":"10","dispense_mix_volume":"150","dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"50","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":true,"dispense_touchTip_mmFromTop":-10,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["B5"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"glycerol_50","nozzles":null,"path":"single","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"75","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","id":"9ff89971-903e-4a7d-b0a0-5da2074d777f","stepType":"moveLiquid","stepName":"6A + 6B Mix","stepDetails":"","stepNumber":0},"7074ea38-a3ae-4601-ad2d-387d3a797b26":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":true,"aspirate_delay_seconds":"1","aspirate_flowRate":"100","aspirate_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":null,"aspirate_mmFromBottom":0.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"50","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["B5"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":true,"dispense_delay_seconds":"0.5","dispense_flowRate":"20","dispense_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"50","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A6","B6","C6","D6","E6","F6","G6","H6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"5","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"glycerol_50","nozzles":null,"path":"multiDispense","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"35","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"22","id":"7074ea38-a3ae-4601-ad2d-387d3a797b26","stepType":"moveLiquid","stepName":"Mix 6 Disperse","stepDetails":"","stepNumber":0},"0fbb3d5e-95a5-43d1-bc11-fba87f13ff21":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"0fbb3d5e-95a5-43d1-bc11-fba87f13ff21","stepType":"pause","stepName":"pause","stepDetails":""},"1553aead-bcfd-4b0f-be34-e401001333ef":{"blockIsActive":true,"blockTargetTemp":"20","lidIsActive":true,"lidOpen":true,"lidTargetTemp":"75","moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":[],"profileItemsById":{},"profileTargetLidTemp":null,"profileVolume":null,"thermocyclerFormType":"thermocyclerState","id":"1553aead-bcfd-4b0f-be34-e401001333ef","stepType":"thermocycler","stepName":"Bead 1 End","stepDetails":""},"f4803e9b-9f0d-4a4a-b771-85d9375f0e23":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","aspirate_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":true,"aspirate_mix_times":"3","aspirate_mix_volume":"4","aspirate_mmFromBottom":0.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A5"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":true,"dispense_mix_times":"3","dispense_mix_volume":"15","dispense_mmFromBottom":3,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A2"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"15","id":"f4803e9b-9f0d-4a4a-b771-85d9375f0e23","stepType":"moveLiquid","stepName":"P1-P8 RxN","stepDetails":"","stepNumber":0},"71837b00-b6e5-4228-a346-0c36f08d08e7":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"25","aspirate_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"50","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"50","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":true,"dispense_delay_seconds":"1","dispense_flowRate":"40","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":true,"dispense_mix_times":"15","dispense_mix_volume":"40","dispense_mmFromBottom":3,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"50","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A2"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"glycerol_50","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"20","id":"71837b00-b6e5-4228-a346-0c36f08d08e7","stepType":"moveLiquid","stepName":"Mix 6 RxN","stepDetails":"","stepNumber":0},"12d666f2-8d58-40fe-afc6-4d54babe13d9":{"blockIsActive":true,"blockTargetTemp":"20","lidIsActive":true,"lidOpen":true,"lidTargetTemp":"75","moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":[],"profileItemsById":{},"profileTargetLidTemp":null,"profileVolume":null,"thermocyclerFormType":"thermocyclerState","blockIsActiveHold":false,"blockTargetTempHold":null,"lidIsActiveHold":false,"lidOpenHold":null,"lidTargetTempHold":null,"id":"12d666f2-8d58-40fe-afc6-4d54babe13d9","stepType":"thermocycler","stepName":"Step 6 Start","stepDetails":"","stepNumber":0},"3ebccc2a-97f4-44c0-af78-e88bdbb5bb85":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:15:00","id":"3ebccc2a-97f4-44c0-af78-e88bdbb5bb85","stepType":"pause","stepName":"Step 6 Incubation","stepDetails":"","stepNumber":0},"70bfc436-5af2-4608-a2f1-b66fa327f9cc":{"blockIsActive":true,"blockTargetTemp":"12","lidIsActive":true,"lidOpen":true,"lidTargetTemp":"105","moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":[],"profileItemsById":{},"profileTargetLidTemp":null,"profileVolume":null,"thermocyclerFormType":"thermocyclerState","blockIsActiveHold":false,"blockTargetTempHold":null,"lidIsActiveHold":false,"lidOpenHold":null,"lidTargetTempHold":null,"id":"70bfc436-5af2-4608-a2f1-b66fa327f9cc","stepType":"thermocycler","stepName":"Step 6 End","stepDetails":"","stepNumber":0},"0c12ea3f-5291-4a52-b951-cf35df48ed48":{"labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"594810cf-69c3-4e9c-8f82-a8f9b38ad79d:opentrons/opentrons_96_well_aluminum_block/1","useGripper":true,"id":"0c12ea3f-5291-4a52-b951-cf35df48ed48","stepType":"moveLabware","stepName":"P2 to Temp C1","stepDetails":"","stepNumber":0},"96469258-d0e8-4f14-9831-3fdc161a860f":{"labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"C2","useGripper":true,"id":"96469258-d0e8-4f14-9831-3fdc161a860f","stepType":"moveLabware","stepName":"P1 to Deck C2","stepDetails":"","stepNumber":0},"8ec21f63-f7e0-4d65-9883-37a8b9ce2591":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":true,"aspirate_mix_times":"3","aspirate_mix_volume":"45","aspirate_mmFromBottom":1.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"1","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"50","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"50","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":true,"dispense_delay_seconds":"1","dispense_flowRate":"75","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":true,"dispense_mix_times":"5","dispense_mix_volume":"75","dispense_mmFromBottom":3,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"50","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A2"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"glycerol_50","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"50","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"55","id":"8ec21f63-f7e0-4d65-9883-37a8b9ce2591","stepType":"moveLiquid","stepName":"SB + Sample 2","stepDetails":"","stepNumber":0},"626ba193-3c88-4e91-a041-49e096f60331":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"500","aspirate_labware":"6db7eb96-52b3-489e-805e-010e35d88119:opentrons/opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":15,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"300","blowout_location":"dest_well","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"12","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"300","dispense_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":5,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A2"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"ethanol_80","nozzles":null,"path":"single","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"","tipRack":"opentrons/opentrons_flex_96_filtertiprack_1000ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"4000","id":"626ba193-3c88-4e91-a041-49e096f60331","stepType":"moveLiquid","stepName":"EtOH to Res 2","stepDetails":"","stepNumber":0},"ef05de48-d9f7-4b0d-bf37-d50ceb7e1771":{"blockIsActive":false,"blockTargetTemp":null,"lidIsActive":false,"lidOpen":false,"lidTargetTemp":null,"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":["fc2b2c9b-3731-4008-9514-d905e5da614d"],"profileItemsById":{"fc2b2c9b-3731-4008-9514-d905e5da614d":{"durationMinutes":"03","durationSeconds":"30","id":"fc2b2c9b-3731-4008-9514-d905e5da614d","temperature":"98","title":"1","type":"profileStep"}},"profileTargetLidTemp":"105","profileVolume":"50","thermocyclerFormType":"thermocyclerProfile","blockIsActiveHold":false,"blockTargetTempHold":null,"lidIsActiveHold":false,"lidOpenHold":null,"lidTargetTempHold":null,"id":"ef05de48-d9f7-4b0d-bf37-d50ceb7e1771","stepType":"thermocycler","stepName":"Bead 2 Start","stepDetails":"","stepNumber":0},"aefe376d-b858-4368-ad89-3efc7c95da05":{"labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"561cc9e8-ae90-49c1-bccf-75a85989930b:magneticBlockType","useGripper":true,"id":"aefe376d-b858-4368-ad89-3efc7c95da05","stepType":"moveLabware","stepName":"P1 to Mag","stepDetails":"","stepNumber":0},"a1fe84f0-edd8-4d72-afcf-283f326e52ea":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:03:00","id":"a1fe84f0-edd8-4d72-afcf-283f326e52ea","stepType":"pause","stepName":"Bind Beads to Mag 2","stepDetails":"","stepNumber":0},"702f6690-e012-4280-b959-d88ffa7819d5":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"25","aspirate_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"100","dispense_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":"","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A11"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"glycerol_50","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"110","id":"702f6690-e012-4280-b959-d88ffa7819d5","stepType":"moveLiquid","stepName":"Rem Sup 2","stepDetails":"","stepNumber":0},"edac41ea-88da-4f2e-a7e9-02991725dfb7":{"aspirate_airGap_checkbox":true,"aspirate_airGap_volume":"10","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"100","aspirate_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0.5","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"100","blowout_location":"dest_well","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"10","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"50","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":10,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A2"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"ethanol_80","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"150","id":"edac41ea-88da-4f2e-a7e9-02991725dfb7","stepType":"moveLiquid","stepName":"Add EtOH 2.1","stepDetails":"","stepNumber":0},"ffc9c3b1-0afd-47d4-bda9-fc2846110406":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"25","aspirate_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0.5","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"100","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"10","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"150","dispense_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":4,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A11"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"ethanol_80","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","id":"ffc9c3b1-0afd-47d4-bda9-fc2846110406","stepType":"moveLiquid","stepName":"Rem EtOH 2.1","stepDetails":"","stepNumber":0},"677857b1-2c23-40e4-99e0-61540d64026f":{"aspirate_airGap_checkbox":true,"aspirate_airGap_volume":"10","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"100","aspirate_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0.5","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"100","blowout_location":"dest_well","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"10","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"50","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":10,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A2"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"ethanol_80","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"150","id":"677857b1-2c23-40e4-99e0-61540d64026f","stepType":"moveLiquid","stepName":"Add EtOH 2.2","stepDetails":"","stepNumber":0},"46ae79c9-590d-486d-84a3-7384f11a7eea":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"25","aspirate_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":0.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0.5","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"100","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"10","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"150","dispense_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":6,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A11"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"ethanol_80","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","id":"46ae79c9-590d-486d-84a3-7384f11a7eea","stepType":"moveLiquid","stepName":"Rem EtOH 2.2","stepDetails":"","stepNumber":0},"ed25af81-d3dd-467a-881c-48136fb724f0":{"labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"C2","useGripper":true,"id":"ed25af81-d3dd-467a-881c-48136fb724f0","stepType":"moveLabware","stepName":"P1 to Deck C2","stepDetails":"","stepNumber":0},"7cf4faab-326c-4fe1-a98d-e3e2e2337552":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"20","aspirate_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"50","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":true,"dispense_mix_times":"10","dispense_mix_volume":"15","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A2"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"water","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"22","id":"7cf4faab-326c-4fe1-a98d-e3e2e2337552","stepType":"moveLiquid","stepName":"Elute 2","stepDetails":"","stepNumber":0},"7d0ec1ae-06cf-42e5-9c8e-f44273a9990f":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:01:00","id":"7d0ec1ae-06cf-42e5-9c8e-f44273a9990f","stepType":"pause","stepName":"Elute 2 Min","stepDetails":"","stepNumber":0},"cca199c0-778d-416a-ac3f-8dbfbd6ed970":{"labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"561cc9e8-ae90-49c1-bccf-75a85989930b:magneticBlockType","useGripper":true,"id":"cca199c0-778d-416a-ac3f-8dbfbd6ed970","stepType":"moveLabware","stepName":"P1 to Mag","stepDetails":"","stepNumber":0},"7b2b54a5-8852-49c6-9ea5-5d71ccf1032b":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"100","aspirate_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":0.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"250","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"200","dispense_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","dispense_mix_checkbox":true,"dispense_mix_times":"10","dispense_mix_volume":"200","dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["B6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"single","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"75","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"50","id":"7b2b54a5-8852-49c6-9ea5-5d71ccf1032b","stepType":"moveLiquid","stepName":"7A + 7B Mix","stepDetails":"","stepNumber":0},"0554afaa-ab39-4e01-83e9-3ce9b201b6a4":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"200","aspirate_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":0.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["B6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"30","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3","B3","C3","D3","E3","F3","G3","H3"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"5","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"multiDispense","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_1000ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"30","id":"0554afaa-ab39-4e01-83e9-3ce9b201b6a4","stepType":"moveLiquid","stepName":"Mix 7 Disperse","stepDetails":"","stepNumber":0},"03fe6045-dab5-4f9b-8df2-aed4c306b5aa":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"20","aspirate_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"10","aspirate_mix_volume":"40","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"40","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":true,"dispense_mix_times":"10","dispense_mix_volume":"40","dispense_mmFromBottom":3,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"20","id":"03fe6045-dab5-4f9b-8df2-aed4c306b5aa","stepType":"moveLiquid","stepName":"Mix 7 RxN","stepDetails":"","stepNumber":0},"1e790a52-0d5c-48ca-8beb-955894ca4a5f":{"moduleId":"65263cf9-315d-4e77-a59d-5e60ac83f781:temperatureModuleType","setTemperature":"true","targetTemperature":"24","id":"1e790a52-0d5c-48ca-8beb-955894ca4a5f","stepType":"temperature","stepName":"Temp D1 to 24C","stepDetails":"","stepNumber":0},"0c65b540-99ba-4cc3-be12-f66cb3f7026c":{"labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","useGripper":true,"id":"0c65b540-99ba-4cc3-be12-f66cb3f7026c","stepType":"moveLabware","stepName":"P1 to Cycler","stepDetails":"","stepNumber":0},"e1c17946-b9d4-4aba-a088-b33d0a495a36":{"blockIsActive":false,"blockTargetTemp":null,"lidIsActive":false,"lidOpen":false,"lidTargetTemp":null,"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":["3b0f3ad0-4fb1-42a3-a316-26dbe78ec2d8","adf4d471-11b0-4426-9231-ff9bc7c62883","fa9834db-35e9-44ef-a7e4-3c7713865f12"],"profileItemsById":{"3b0f3ad0-4fb1-42a3-a316-26dbe78ec2d8":{"durationMinutes":"00","durationSeconds":"30","id":"3b0f3ad0-4fb1-42a3-a316-26dbe78ec2d8","temperature":"98","title":"1","type":"profileStep"},"adf4d471-11b0-4426-9231-ff9bc7c62883":{"id":"adf4d471-11b0-4426-9231-ff9bc7c62883","title":"","steps":[{"durationMinutes":"00","durationSeconds":"10","id":"effb2efa-ebf9-4b46-b556-84bfcb20226c","temperature":"98","title":"2.1","type":"profileStep"},{"durationMinutes":"00","durationSeconds":"30","id":"c6c39636-48bf-40f9-b060-7dad520189c6","temperature":"60","title":"2.2","type":"profileStep"},{"durationMinutes":"00","durationSeconds":"30","id":"4b28c3b0-003f-4180-9804-6eabfd367c2f","temperature":"72","title":"2.3","type":"profileStep"}],"type":"profileCycle","repetitions":"8"},"fa9834db-35e9-44ef-a7e4-3c7713865f12":{"durationMinutes":"01","durationSeconds":"00","id":"fa9834db-35e9-44ef-a7e4-3c7713865f12","temperature":"72","title":"3","type":"profileStep"}},"profileTargetLidTemp":"105","profileVolume":"50","thermocyclerFormType":"thermocyclerProfile","id":"e1c17946-b9d4-4aba-a088-b33d0a495a36","stepType":"thermocycler","stepName":"Step 7 Incubation","stepDetails":""},"e18e56f1-dcf0-4524-b709-2b0f39799716":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"e18e56f1-dcf0-4524-b709-2b0f39799716","stepType":"pause","stepName":"pause","stepDetails":""},"1c410b4a-4454-48fe-b78a-96f9cd127fb0":{"labware":"271a7505-3035-4be2-8204-80a7546b6512:opentrons/opentrons_flex_96_filtertiprack_200ul/1","newLocation":"cutoutD3","useGripper":true,"id":"1c410b4a-4454-48fe-b78a-96f9cd127fb0","stepType":"moveLabware","stepName":"Box0 B3 Off","stepDetails":"","stepNumber":0},"297ddfc3-b603-4ad2-bbf0-e049af302915":{"labware":"f1d18a33-99d2-4f9d-bdd6-3d4fe1f15b4a:opentrons/opentrons_flex_96_filtertiprack_200ul/1","newLocation":"B3","useGripper":true,"id":"297ddfc3-b603-4ad2-bbf0-e049af302915","stepType":"moveLabware","stepName":"Box2 A4 to B3","stepDetails":"","stepNumber":0},"02bf3807-760d-44a5-a4b8-017cf8176df5":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":true,"aspirate_delay_seconds":"1","aspirate_flowRate":"400","aspirate_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","aspirate_mix_checkbox":true,"aspirate_mix_times":"5","aspirate_mix_volume":"500","aspirate_mmFromBottom":5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"1","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":true,"aspirate_touchTip_mmFromTop":-10,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["C3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"250","blowout_location":"source_well","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":true,"dispense_delay_seconds":"1","dispense_flowRate":"200","dispense_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":5,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1","B1","C1","D1","E1","F1","G1","H1"],"dispense_x_position":1,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"5","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"glycerol_50","nozzles":null,"path":"multiDispense","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"35","tipRack":"opentrons/opentrons_flex_96_filtertiprack_1000ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"55","id":"02bf3807-760d-44a5-a4b8-017cf8176df5","stepType":"moveLiquid","stepName":"SB Disperse 3","stepDetails":"","stepNumber":0},"16df3755-4ca4-4e1b-8eba-4b3e3633e35e":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"16df3755-4ca4-4e1b-8eba-4b3e3633e35e","stepType":"pause","stepName":"pause","stepDetails":""},"cb785a74-ef4a-4f92-9964-52a9f8e30754":{"blockIsActive":true,"blockTargetTemp":"98","lidIsActive":true,"lidOpen":true,"lidTargetTemp":"105","moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":[],"profileItemsById":{},"profileTargetLidTemp":null,"profileVolume":null,"thermocyclerFormType":"thermocyclerState","id":"cb785a74-ef4a-4f92-9964-52a9f8e30754","stepType":"thermocycler","stepName":"Bead 2 End","stepDetails":""},"73fa53c8-6f93-483d-944e-266e5eda5201":{"labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"C2","useGripper":true,"id":"73fa53c8-6f93-483d-944e-266e5eda5201","stepType":"moveLabware","stepName":"P1 to Deck C2","stepDetails":"","stepNumber":0},"84083ef9-f900-4b5d-ab8f-1c48530888eb":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":true,"aspirate_mix_times":"3","aspirate_mix_volume":"45","aspirate_mmFromBottom":1.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"1","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"50","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"50","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":true,"dispense_delay_seconds":"1","dispense_flowRate":"75","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":true,"dispense_mix_times":"5","dispense_mix_volume":"75","dispense_mmFromBottom":3,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"50","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"glycerol_50","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"50","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"50","id":"84083ef9-f900-4b5d-ab8f-1c48530888eb","stepType":"moveLiquid","stepName":"SB + Sample 3","stepDetails":"","stepNumber":0},"edaa1587-ad6a-48c3-8a6d-d24acbbf954d":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":true,"aspirate_delay_seconds":"1","aspirate_flowRate":"100","aspirate_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","aspirate_mix_checkbox":true,"aspirate_mix_times":"3","aspirate_mix_volume":"200","aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"50","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["C1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":true,"dispense_delay_seconds":"1","dispense_flowRate":"20","dispense_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"50","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A11","B11","C11","D11","E11","F11","G11","H11"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"10","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"glycerol_50","nozzles":null,"path":"multiDispense","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"35","tipRack":"opentrons/opentrons_flex_96_filtertiprack_1000ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"45","id":"edaa1587-ad6a-48c3-8a6d-d24acbbf954d","stepType":"moveLiquid","stepName":"8B Disperse","stepDetails":"","stepNumber":0},"8d9a4467-8ff3-449c-98c3-e01e5abfd80d":{"moduleId":"033331ec-47f1-4f9a-9c01-ca09a87b9ac1:temperatureModuleType","setTemperature":"true","targetTemperature":"65","id":"8d9a4467-8ff3-449c-98c3-e01e5abfd80d","stepType":"temperature","stepName":"Temp C1 to 65C","stepDetails":"","stepNumber":0},"dc7bece4-3fff-4182-9566-5edce83cc425":{"moduleId":"65263cf9-315d-4e77-a59d-5e60ac83f781:temperatureModuleType","setTemperature":"true","targetTemperature":"4","id":"dc7bece4-3fff-4182-9566-5edce83cc425","stepType":"temperature","stepName":"Temp D1 to 4C","stepDetails":"","stepNumber":0},"d89f8be9-2314-4b66-b2b5-53110fa1b73b":{"labware":"4a3bea46-728a-498c-9c2e-a5caf006f10b:opentrons/opentrons_flex_96_filtertiprack_200ul/1","newLocation":"A4","useGripper":true,"id":"d89f8be9-2314-4b66-b2b5-53110fa1b73b","stepType":"moveLabware","stepName":"Box1 C3 to A4","stepDetails":"","stepNumber":0},"4efecefd-69e2-48a3-b51c-6b63d9aa786d":{"labware":"2d19a470-70c5-4006-9b83-85dd5572f12a:opentrons/opentrons_flex_96_filtertiprack_200ul/1","newLocation":"C3","useGripper":true,"id":"4efecefd-69e2-48a3-b51c-6b63d9aa786d","stepType":"moveLabware","stepName":"Box3 B4 to C3","stepDetails":"","stepNumber":0},"98aa17e5-bf28-4525-8587-914fe28f2efa":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:10:00","id":"98aa17e5-bf28-4525-8587-914fe28f2efa","stepType":"pause","stepName":"Step 7 Delay","stepDetails":"","stepNumber":0},"fa1e579a-b348-4af7-afc9-30dfee5e8c9f":{"labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"561cc9e8-ae90-49c1-bccf-75a85989930b:magneticBlockType","useGripper":true,"id":"fa1e579a-b348-4af7-afc9-30dfee5e8c9f","stepType":"moveLabware","stepName":"P1 to Mag","stepDetails":"","stepNumber":0},"e3c5c90b-2104-4ad5-9b6e-74ee3a274a17":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"500","aspirate_labware":"6db7eb96-52b3-489e-805e-010e35d88119:opentrons/opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"300","blowout_location":"dest_well","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"12","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"300","dispense_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":5,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A2"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"ethanol_80","nozzles":null,"path":"single","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"","tipRack":"opentrons/opentrons_flex_96_filtertiprack_1000ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"4000","id":"e3c5c90b-2104-4ad5-9b6e-74ee3a274a17","stepType":"moveLiquid","stepName":"EtOH to Res 3","stepDetails":"","stepNumber":0},"8f0b4880-2ad3-402c-a5d9-036ef7d3c20f":{"blockIsActive":true,"blockTargetTemp":"48","lidIsActive":true,"lidOpen":true,"lidTargetTemp":56,"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":[],"profileItemsById":{},"profileTargetLidTemp":null,"profileVolume":null,"thermocyclerFormType":"thermocyclerState","blockIsActiveHold":false,"blockTargetTempHold":null,"lidIsActiveHold":false,"lidOpenHold":null,"lidTargetTempHold":null,"id":"8f0b4880-2ad3-402c-a5d9-036ef7d3c20f","stepType":"thermocycler","stepName":"Step 8.1 Cycler Prep","stepDetails":"","stepNumber":0},"ceea5d2d-d3be-43e2-9ded-7d6d412fb848":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"25","aspirate_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"100","dispense_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":"","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A10"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","id":"ceea5d2d-d3be-43e2-9ded-7d6d412fb848","stepType":"moveLiquid","stepName":"Rem Sup 3","stepDetails":"","stepNumber":0},"c5574468-5135-4148-8968-fddd1c1b6877":{"aspirate_airGap_checkbox":true,"aspirate_airGap_volume":"10","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"100","aspirate_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0.5","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"100","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"10","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"50","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":10,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"ethanol_80","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"150","id":"c5574468-5135-4148-8968-fddd1c1b6877","stepType":"moveLiquid","stepName":"Add EtOH 3.1","stepDetails":"","stepNumber":0},"50ea8e7d-a8b8-496a-bf19-ddd6f97818d7":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"25","aspirate_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0.5","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"100","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"10","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"150","dispense_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":4,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A10"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"ethanol_80","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","id":"50ea8e7d-a8b8-496a-bf19-ddd6f97818d7","stepType":"moveLiquid","stepName":"Rem EtOH 3.1","stepDetails":"","stepNumber":0},"fee907be-071b-4a48-8d86-51c4a95687d4":{"aspirate_airGap_checkbox":true,"aspirate_airGap_volume":"10","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"100","aspirate_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0.5","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"100","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"10","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"50","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":10,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"ethanol_80","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"150","id":"fee907be-071b-4a48-8d86-51c4a95687d4","stepType":"moveLiquid","stepName":"Add EtOH 3.2","stepDetails":"","stepNumber":0},"e45933c8-b509-4f6d-899d-0212c54ba6dc":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"25","aspirate_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":0.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0.5","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"100","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"10","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"150","dispense_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":6,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A10"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"ethanol_80","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","id":"e45933c8-b509-4f6d-899d-0212c54ba6dc","stepType":"moveLiquid","stepName":"Rem EtOH 3.2","stepDetails":"","stepNumber":0},"dd2b4be2-0338-4dd7-ad15-522853de4ec7":{"labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"C2","useGripper":true,"id":"dd2b4be2-0338-4dd7-ad15-522853de4ec7","stepType":"moveLabware","stepName":"P1 to Deck C2","stepDetails":"","stepNumber":0},"c88aaf0d-3089-4ab6-ab11-b5c0aa156187":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"1","aspirate_flowRate":"25","aspirate_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"50","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A11"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"50","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":true,"dispense_delay_seconds":"1","dispense_flowRate":"15","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":3,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"50","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3"],"dispense_x_position":2,"dispense_y_position":-2,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"glycerol_50","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"35","id":"c88aaf0d-3089-4ab6-ab11-b5c0aa156187","stepType":"moveLiquid","stepName":"8B Elute 1","stepDetails":"","stepNumber":0},"525a75df-bdeb-4442-a273-0aafaffc703f":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"1","aspirate_flowRate":"25","aspirate_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"50","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"50","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":true,"dispense_delay_seconds":"1","dispense_flowRate":"15","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":3,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"50","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3"],"dispense_x_position":2,"dispense_y_position":2,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"glycerol_50","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"15","id":"525a75df-bdeb-4442-a273-0aafaffc703f","stepType":"moveLiquid","stepName":"8B Elute 2","stepDetails":"","stepNumber":0},"67766d8d-402f-406e-8e04-bde10210ae42":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"1","aspirate_flowRate":"25","aspirate_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"50","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"50","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":true,"dispense_delay_seconds":"1","dispense_flowRate":"15","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":3,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"50","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3"],"dispense_x_position":-2,"dispense_y_position":2,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"glycerol_50","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"15","id":"67766d8d-402f-406e-8e04-bde10210ae42","stepType":"moveLiquid","stepName":"8B Elute 3","stepDetails":"","stepNumber":0},"8f8b3918-1079-4116-ac3c-40b562bbc214":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"1","aspirate_flowRate":"25","aspirate_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"50","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"50","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":true,"dispense_delay_seconds":"1","dispense_flowRate":"15","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":3,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"50","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3"],"dispense_x_position":-2,"dispense_y_position":-2,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"glycerol_50","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"15","id":"8f8b3918-1079-4116-ac3c-40b562bbc214","stepType":"moveLiquid","stepName":"8B Elute 4","stepDetails":"","stepNumber":0},"7bd0b730-7dfb-46c3-bef8-b3722aedf519":{"labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","useGripper":true,"id":"7bd0b730-7dfb-46c3-bef8-b3722aedf519","stepType":"moveLabware","stepName":"P1 to Cycler","stepDetails":"","stepNumber":0},"d1545ccd-bb13-4f57-8e56-462b6dc1f69d":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"25","blowout_checkbox":false,"blowout_flowRate":"50","blowout_location":"dest_well","blowout_z_offset":0,"changeTip":"always","dispense_delay_checkbox":true,"dispense_delay_seconds":"1","dispense_flowRate":"15","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","liquidClassesSupported":true,"liquidClass":"glycerol_50","mix_mmFromBottom":3,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","pushOut_checkbox":false,"pushOut_volume":"20","times":"10","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"15","wells":["A3"],"id":"d1545ccd-bb13-4f57-8e56-462b6dc1f69d","stepType":"mix","stepName":"8B Mix","stepDetails":"","stepNumber":0},"433fff8c-8d4f-4b4d-816c-66aefe4e7171":{"labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"C2","useGripper":true,"id":"433fff8c-8d4f-4b4d-816c-66aefe4e7171","stepType":"moveLabware","stepName":"P2 to Deck C2","stepDetails":"","stepNumber":0},"34c0364d-a594-415f-8557-b46d7b266d94":{"labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"561cc9e8-ae90-49c1-bccf-75a85989930b:magneticBlockType","useGripper":true,"id":"34c0364d-a594-415f-8557-b46d7b266d94","stepType":"moveLabware","stepName":"P1 to Mag","stepDetails":"","stepNumber":0},"74dd0828-3c87-4905-9e04-c79c87cf88e7":{"blockIsActive":true,"blockTargetTemp":"95","lidIsActive":true,"lidOpen":true,"lidTargetTemp":56,"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":[],"profileItemsById":{},"profileTargetLidTemp":null,"profileVolume":null,"thermocyclerFormType":"thermocyclerState","blockIsActiveHold":false,"blockTargetTempHold":null,"lidIsActiveHold":false,"lidOpenHold":null,"lidTargetTempHold":null,"id":"74dd0828-3c87-4905-9e04-c79c87cf88e7","stepType":"thermocycler","stepName":"Step 8 Set Up 2","stepDetails":"","stepNumber":0},"7ad92f96-27c1-4510-a434-b095be7983b7":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":true,"aspirate_delay_seconds":"1","aspirate_flowRate":"200","aspirate_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":null,"aspirate_mmFromBottom":0.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"50","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["C2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"250","blowout_location":"source_well","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":true,"dispense_delay_seconds":"0.5","dispense_flowRate":"20","dispense_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"50","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A12","B12","C12","D12","E12","F12","G12","H12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"glycerol_50","nozzles":null,"path":"multiDispense","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"35","tipRack":"opentrons/opentrons_flex_96_filtertiprack_1000ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"25","id":"7ad92f96-27c1-4510-a434-b095be7983b7","stepType":"moveLiquid","stepName":"8C Disperse","stepDetails":"","stepNumber":0},"3dd3172b-cc1d-4ad9-83d3-2f527279bfcd":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:01:00","id":"3dd3172b-cc1d-4ad9-83d3-2f527279bfcd","stepType":"pause","stepName":"Bind Beads to Mag 3","stepDetails":"","stepNumber":0},"1f2823fd-4038-43d2-b281-6f0864178e47":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"0.5","aspirate_flowRate":"15","aspirate_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":0.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"50","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"50","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":true,"dispense_delay_seconds":"0.5","dispense_flowRate":"50","dispense_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":true,"dispense_mix_times":"15","dispense_mix_volume":"15","dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"50","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A7"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"glycerol_50","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"25","id":"1f2823fd-4038-43d2-b281-6f0864178e47","stepType":"moveLiquid","stepName":"8B Add","stepDetails":"","stepNumber":0},"4f6e9a4e-9884-41b3-b79b-6b7b156cbdb9":{"labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"594810cf-69c3-4e9c-8f82-a8f9b38ad79d:opentrons/opentrons_96_well_aluminum_block/1","useGripper":true,"id":"4f6e9a4e-9884-41b3-b79b-6b7b156cbdb9","stepType":"moveLabware","stepName":"P2 to Temp C1","stepDetails":"","stepNumber":0},"7e2051d4-509e-4cf6-a8fc-e64426ecc8db":{"labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"C2","useGripper":true,"id":"7e2051d4-509e-4cf6-a8fc-e64426ecc8db","stepType":"moveLabware","stepName":"P2 to Deck C2","stepDetails":"","stepNumber":0},"5e6b81e7-55ea-4ebc-99af-00b943707c17":{"moduleId":"033331ec-47f1-4f9a-9c01-ca09a87b9ac1:temperatureModuleType","setTemperature":"true","targetTemperature":"24","id":"5e6b81e7-55ea-4ebc-99af-00b943707c17","stepType":"temperature","stepName":"temperature","stepDetails":"","stepNumber":0},"e2259737-faba-416d-b1cc-fd4bb8461d01":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"1","aspirate_flowRate":"15","aspirate_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"50","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"50","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":true,"dispense_delay_seconds":"0.5","dispense_flowRate":"15","dispense_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":12,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"50","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":true,"dispense_touchTip_mmFromTop":-2,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A7"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"glycerol_50","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"15","id":"e2259737-faba-416d-b1cc-fd4bb8461d01","stepType":"moveLiquid","stepName":"8C Add","stepDetails":"","stepNumber":0},"965c3b34-6ca7-4942-804e-7efcddfba656":{"labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","useGripper":true,"id":"965c3b34-6ca7-4942-804e-7efcddfba656","stepType":"moveLabware","stepName":"P2 to Cycler","stepDetails":"","stepNumber":0},"d8a209bc-5e3b-48c3-bf0a-cd04d7cef980":{"blockIsActive":false,"blockTargetTemp":null,"lidIsActive":false,"lidOpen":false,"lidTargetTemp":null,"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":["0c82ecf8-34bd-4336-8a79-a92a7bcda8bc","e85ecc48-4af7-4572-ac65-c1a9d927e624"],"profileItemsById":{"0c82ecf8-34bd-4336-8a79-a92a7bcda8bc":{"durationMinutes":"05","durationSeconds":"00","id":"0c82ecf8-34bd-4336-8a79-a92a7bcda8bc","temperature":"95","title":"1","type":"profileStep"},"e85ecc48-4af7-4572-ac65-c1a9d927e624":{"durationMinutes":"60","durationSeconds":"00","id":"e85ecc48-4af7-4572-ac65-c1a9d927e624","temperature":"60","title":"2","type":"profileStep"}},"profileTargetLidTemp":"56","profileVolume":"60","thermocyclerFormType":"thermocyclerProfile","id":"d8a209bc-5e3b-48c3-bf0a-cd04d7cef980","stepType":"thermocycler","stepName":"Step 8 Incubation","stepDetails":""},"3a97c77e-ca29-43eb-b35d-849fe928bb2b":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"3a97c77e-ca29-43eb-b35d-849fe928bb2b","stepType":"pause","stepName":"pause","stepDetails":""},"3f9850f0-8002-479e-8647-2f8990b6e976":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"3f9850f0-8002-479e-8647-2f8990b6e976","stepType":"pause","stepName":"pause","stepDetails":""},"0991ee7d-2cf7-4ce7-9479-7bbed23a38c1":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"500","aspirate_labware":"6db7eb96-52b3-489e-805e-010e35d88119:opentrons/opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"500","dispense_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":"","dispense_mmFromBottom":5,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"single","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_1000ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"4000","id":"0991ee7d-2cf7-4ce7-9479-7bbed23a38c1","stepType":"moveLiquid","stepName":"9A to Res","stepDetails":"","stepNumber":0},"317b3b80-9bda-409c-8b90-fa34df75eb7c":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"500","aspirate_labware":"6db7eb96-52b3-489e-805e-010e35d88119:opentrons/opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["B2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"500","dispense_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":"","dispense_mmFromBottom":5,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"single","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_1000ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"4000","id":"317b3b80-9bda-409c-8b90-fa34df75eb7c","stepType":"moveLiquid","stepName":"9B to Res","stepDetails":"","stepNumber":0},"69692c76-504c-4dc8-ab39-60c180422590":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"500","aspirate_labware":"6db7eb96-52b3-489e-805e-010e35d88119:opentrons/opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["C2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"500","dispense_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":"","dispense_mmFromBottom":5,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A5"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"single","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_1000ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"5000","id":"69692c76-504c-4dc8-ab39-60c180422590","stepType":"moveLiquid","stepName":"9C to Res","stepDetails":"","stepNumber":0},"862cd5d9-67c1-44af-b5f3-0ab3c7361501":{"labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"C2","useGripper":true,"id":"862cd5d9-67c1-44af-b5f3-0ab3c7361501","stepType":"moveLabware","stepName":"P1 to Deck","stepDetails":"","stepNumber":0},"5a564527-44f3-4811-a0fa-2f5e70dabf02":{"blockIsActive":true,"blockTargetTemp":"60","lidIsActive":true,"lidOpen":true,"lidTargetTemp":"56","moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":[],"profileItemsById":{},"profileTargetLidTemp":null,"profileVolume":null,"thermocyclerFormType":"thermocyclerState","id":"5a564527-44f3-4811-a0fa-2f5e70dabf02","stepType":"thermocycler","stepName":"Step 8 End","stepDetails":""},"8d291db6-a2eb-4b93-8153-0273187621f3":{"moduleId":"033331ec-47f1-4f9a-9c01-ca09a87b9ac1:temperatureModuleType","setTemperature":"true","targetTemperature":"60","id":"8d291db6-a2eb-4b93-8153-0273187621f3","stepType":"temperature","stepName":"Temp C1 to 60C","stepDetails":"","stepNumber":0},"bfa6f714-93e8-4f7b-8a76-6f8c5f5d173f":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"200","blowout_checkbox":true,"blowout_flowRate":"250","blowout_location":"dest_well","blowout_z_offset":-10,"changeTip":"once","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"500","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","liquidClassesSupported":true,"liquidClass":"none","mix_mmFromBottom":2,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":null,"pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","pushOut_checkbox":false,"pushOut_volume":"20","times":"10","tipRack":"opentrons/opentrons_flex_96_filtertiprack_1000ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"230","wells":["C4"],"id":"bfa6f714-93e8-4f7b-8a76-6f8c5f5d173f","stepType":"mix","stepName":"CB Mix","stepDetails":"","stepNumber":0},"b5722d10-0871-4709-8b87-9f15b9b8eab9":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"200","aspirate_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":0.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["C4"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"250","blowout_location":"source_well","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"50","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A4","B4","C4","D4","E4","F4","G4","H4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"5","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"multiDispense","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_1000ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"25","id":"b5722d10-0871-4709-8b87-9f15b9b8eab9","stepType":"moveLiquid","stepName":"CB Disperse","stepDetails":"","stepNumber":0},"5216b76f-3e59-4c1e-b1bd-2a650787bace":{"labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"561cc9e8-ae90-49c1-bccf-75a85989930b:magneticBlockType","useGripper":true,"id":"5216b76f-3e59-4c1e-b1bd-2a650787bace","stepType":"moveLabware","stepName":"P1 to Mag","stepDetails":"","stepNumber":0},"7e7ea0c5-ed4d-4f3e-917e-b7970e506f21":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"25","aspirate_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A4"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"100","dispense_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":"","dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A9"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"25","id":"7e7ea0c5-ed4d-4f3e-917e-b7970e506f21","stepType":"moveLiquid","stepName":"Rem CB","stepDetails":"","stepNumber":0},"6be88374-e7e8-49fc-bef1-82fa7422a6c6":{"labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"C2","useGripper":true,"id":"6be88374-e7e8-49fc-bef1-82fa7422a6c6","stepType":"moveLabware","stepName":"P1 to Deck C2","stepDetails":"","stepNumber":0},"8d11d5ad-b9ab-4795-9100-4ba024ea66e0":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"100","aspirate_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"200","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":true,"dispense_mix_times":"10","dispense_mix_volume":"100","dispense_mmFromBottom":3,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"150","id":"8d11d5ad-b9ab-4795-9100-4ba024ea66e0","stepType":"moveLiquid","stepName":"Add 9A 1","stepDetails":"","stepNumber":0},"cd2738d9-e67d-4d57-bc2a-571746846ff6":{"labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"561cc9e8-ae90-49c1-bccf-75a85989930b:magneticBlockType","useGripper":true,"id":"cd2738d9-e67d-4d57-bc2a-571746846ff6","stepType":"moveLabware","stepName":"P1 to Mag","stepDetails":"","stepNumber":0},"98f991cb-b1b2-422a-95d6-2c607fda90bd":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:48:00","id":"98f991cb-b1b2-422a-95d6-2c607fda90bd","stepType":"pause","stepName":"Step 8 Delay","stepDetails":"","stepNumber":0},"777bb889-245c-44fa-82f3-20014c5301ed":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"100","aspirate_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A4"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"200","dispense_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":"","dispense_mmFromBottom":3,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A9"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"150","id":"777bb889-245c-44fa-82f3-20014c5301ed","stepType":"moveLiquid","stepName":"Rem 9A 1","stepDetails":"","stepNumber":0},"0c6693f6-d4cf-44b1-911f-8d48a164ea9c":{"labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"C2","useGripper":true,"id":"0c6693f6-d4cf-44b1-911f-8d48a164ea9c","stepType":"moveLabware","stepName":"P1 to Deck C2","stepDetails":"","stepNumber":0},"54656a37-8bf4-44b7-9005-eff753fb0a4a":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"100","aspirate_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"200","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":true,"dispense_mix_times":"10","dispense_mix_volume":"75","dispense_mmFromBottom":3,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","id":"54656a37-8bf4-44b7-9005-eff753fb0a4a","stepType":"moveLiquid","stepName":"Add 9A 2","stepDetails":"","stepNumber":0},"6e2471bc-b27f-46f7-9aee-4acc4698dc5f":{"labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"594810cf-69c3-4e9c-8f82-a8f9b38ad79d:opentrons/opentrons_96_well_aluminum_block/1","useGripper":true,"id":"6e2471bc-b27f-46f7-9aee-4acc4698dc5f","stepType":"moveLabware","stepName":"P1 to Temp C1","stepDetails":"","stepNumber":0},"29c2555d-1688-4863-9c43-37aeb388aaff":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":true,"aspirate_mix_times":"3","aspirate_mix_volume":"75","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"50","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A4"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"75","dispense_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":true,"dispense_mix_times":"5","dispense_mix_volume":"75","dispense_mmFromBottom":4,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"50","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A7"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","id":"29c2555d-1688-4863-9c43-37aeb388aaff","stepType":"moveLiquid","stepName":"9A to RxN 8","stepDetails":"","stepNumber":0},"a1edded1-056e-47a5-8045-353904199f79":{"moduleId":"033331ec-47f1-4f9a-9c01-ca09a87b9ac1:temperatureModuleType","setTemperature":"true","targetTemperature":"68","id":"a1edded1-056e-47a5-8045-353904199f79","stepType":"temperature","stepName":"Temp C1 to 68C","stepDetails":"","stepNumber":0},"c35012c6-9596-4708-8f9f-3cbd0e0a60db":{"blockIsActive":false,"blockTargetTemp":null,"lidIsActive":false,"lidOpen":false,"lidTargetTemp":null,"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":["b4e89ed0-5073-4947-9bc6-1914840723d2"],"profileItemsById":{"b4e89ed0-5073-4947-9bc6-1914840723d2":{"durationMinutes":"10","durationSeconds":"00","id":"b4e89ed0-5073-4947-9bc6-1914840723d2","temperature":"48","title":"1","type":"profileStep"}},"profileTargetLidTemp":"56","profileVolume":"100","thermocyclerFormType":"thermocyclerProfile","id":"c35012c6-9596-4708-8f9f-3cbd0e0a60db","stepType":"thermocycler","stepName":"9A Start","stepDetails":""},"f9556003-fc64-49b6-8630-3bb1025e1337":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"f9556003-fc64-49b6-8630-3bb1025e1337","stepType":"pause","stepName":"pause","stepDetails":""},"2693278c-e37c-474d-906e-f9b2bda59c1d":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"2693278c-e37c-474d-906e-f9b2bda59c1d","stepType":"pause","stepName":"pause","stepDetails":""},"7163c588-9e28-4108-acc5-095ec820c5ae":{"blockIsActive":true,"blockTargetTemp":"24","lidIsActive":true,"lidOpen":true,"lidTargetTemp":"56","moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":[],"profileItemsById":{},"profileTargetLidTemp":null,"profileVolume":null,"thermocyclerFormType":"thermocyclerState","id":"7163c588-9e28-4108-acc5-095ec820c5ae","stepType":"thermocycler","stepName":"9A End","stepDetails":""},"94e477b9-879f-41a0-8e7d-0bfcdb6615c2":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"100","aspirate_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A4"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"200","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":12,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A5","A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"10","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"multiDispense","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_1000ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"170","id":"94e477b9-879f-41a0-8e7d-0bfcdb6615c2","stepType":"moveLiquid","stepName":"9B Disperse","stepDetails":"","stepNumber":0},"f25ebae4-5b7f-4c59-a66b-b90fdddb6ac5":{"labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"561cc9e8-ae90-49c1-bccf-75a85989930b:magneticBlockType","useGripper":true,"id":"f25ebae4-5b7f-4c59-a66b-b90fdddb6ac5","stepType":"moveLabware","stepName":"P2 to Mag","stepDetails":"","stepNumber":0},"b35f945f-dc93-4c88-8a85-fe00b4352208":{"blockIsActive":true,"blockTargetTemp":"68","lidIsActive":true,"lidOpen":true,"lidTargetTemp":"75","moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":[],"profileItemsById":{},"profileTargetLidTemp":null,"profileVolume":null,"thermocyclerFormType":"thermocyclerState","blockIsActiveHold":false,"blockTargetTempHold":null,"lidIsActiveHold":false,"lidOpenHold":null,"lidTargetTempHold":null,"id":"b35f945f-dc93-4c88-8a85-fe00b4352208","stepType":"thermocycler","stepName":"9B cycler Prep","stepDetails":"","stepNumber":0},"401d0c97-8efa-4eb9-86d6-4f28e27af441":{"labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","useGripper":true,"id":"401d0c97-8efa-4eb9-86d6-4f28e27af441","stepType":"moveLabware","stepName":"P1 to Cycler","stepDetails":"","stepNumber":0},"42bfc236-a318-4749-b03e-bb39175af7d1":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":0.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A7"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"200","dispense_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":"","dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A9"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","id":"42bfc236-a318-4749-b03e-bb39175af7d1","stepType":"moveLiquid","stepName":"Rem 9A 2","stepDetails":"","stepNumber":0},"f51935e7-2729-43d9-b434-75a7cd24eb9c":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A5"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"50","dispense_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":"10","dispense_mix_volume":"100","dispense_mmFromBottom":12,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A7"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"150","id":"f51935e7-2729-43d9-b434-75a7cd24eb9c","stepType":"moveLiquid","stepName":"Add 9B 1","stepDetails":"","stepNumber":0},"4956a732-c1da-497d-b0d3-fb58e6978ce1":{"labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"594810cf-69c3-4e9c-8f82-a8f9b38ad79d:opentrons/opentrons_96_well_aluminum_block/1","useGripper":true,"id":"4956a732-c1da-497d-b0d3-fb58e6978ce1","stepType":"moveLabware","stepName":"P2 to Temp C1","stepDetails":"","stepNumber":0},"5d7e914e-e00a-49f5-88f9-46b64b1a1012":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"150","blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"blowout_z_offset":0,"changeTip":"always","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"150","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","liquidClassesSupported":true,"liquidClass":"none","mix_mmFromBottom":4,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":-1,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","pushOut_checkbox":false,"pushOut_volume":"20","times":"10","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","wells":["A7"],"id":"5d7e914e-e00a-49f5-88f9-46b64b1a1012","stepType":"mix","stepName":"Mix 9B 1","stepDetails":"","stepNumber":0},"111a5d9d-47c2-4e88-8df4-ad8e1c61ef35":{"labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"561cc9e8-ae90-49c1-bccf-75a85989930b:magneticBlockType","useGripper":true,"id":"111a5d9d-47c2-4e88-8df4-ad8e1c61ef35","stepType":"moveLabware","stepName":"P2 to Mag","stepDetails":"","stepNumber":0},"85c028ad-e72d-4934-ad6f-db7b43319181":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A7"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"200","dispense_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":"","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A8"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","id":"85c028ad-e72d-4934-ad6f-db7b43319181","stepType":"moveLiquid","stepName":"Rem 9B 1","stepDetails":"","stepNumber":0},"c333f046-1efe-4e14-b4db-c456bba6a3fa":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"50","dispense_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":"10","dispense_mix_volume":"100","dispense_mmFromBottom":12,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A7"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"150","id":"c333f046-1efe-4e14-b4db-c456bba6a3fa","stepType":"moveLiquid","stepName":"Add 9B 2","stepDetails":"","stepNumber":0},"0800bb1c-744a-4209-9cf6-cb25ad79e754":{"labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"594810cf-69c3-4e9c-8f82-a8f9b38ad79d:opentrons/opentrons_96_well_aluminum_block/1","useGripper":true,"id":"0800bb1c-744a-4209-9cf6-cb25ad79e754","stepType":"moveLabware","stepName":"P2 to Temp C1","stepDetails":"","stepNumber":0},"1f3abe18-9a03-4866-8156-693d1165ce19":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"150","blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"blowout_z_offset":0,"changeTip":"always","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"150","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","liquidClassesSupported":true,"liquidClass":"none","mix_mmFromBottom":4,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":-1,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","pushOut_checkbox":false,"pushOut_volume":"20","times":"10","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","wells":["A7"],"id":"1f3abe18-9a03-4866-8156-693d1165ce19","stepType":"mix","stepName":"Mix 9B 2","stepDetails":"","stepNumber":0},"69dcf1b5-7dd8-447a-8ef4-d0fb02ab86bb":{"blockIsActive":true,"blockTargetTemp":"48","lidIsActive":true,"lidOpen":true,"lidTargetTemp":"85","moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":[],"profileItemsById":{},"profileTargetLidTemp":null,"profileVolume":null,"thermocyclerFormType":"thermocyclerState","blockIsActiveHold":false,"blockTargetTempHold":null,"lidIsActiveHold":false,"lidOpenHold":null,"lidTargetTempHold":null,"id":"69dcf1b5-7dd8-447a-8ef4-d0fb02ab86bb","stepType":"thermocycler","stepName":"9C Cycler Set Up","stepDetails":"","stepNumber":0},"918ad838-c887-41d2-8039-179f267ab37e":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"100","aspirate_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A5"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"200","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":12,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A7","A8"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"10","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"multiDispense","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_1000ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"170","id":"918ad838-c887-41d2-8039-179f267ab37e","stepType":"moveLiquid","stepName":"9C Disperse","stepDetails":"","stepNumber":0},"b0f7e2b8-6076-4da0-9eca-a8b4d322947c":{"labware":"f1d18a33-99d2-4f9d-bdd6-3d4fe1f15b4a:opentrons/opentrons_flex_96_filtertiprack_200ul/1","newLocation":"B4","useGripper":true,"id":"b0f7e2b8-6076-4da0-9eca-a8b4d322947c","stepType":"moveLabware","stepName":"Box2 B3 to B4","stepDetails":"","stepNumber":0},"95e77349-e268-4183-a389-87e2ea1f6d8b":{"labware":"2bd3ba52-6320-4739-b104-ef168e2e144a:opentrons/opentrons_flex_96_filtertiprack_200ul/1","newLocation":"B3","useGripper":true,"id":"95e77349-e268-4183-a389-87e2ea1f6d8b","stepType":"moveLabware","stepName":"Box4 C4 to B3","stepDetails":"","stepNumber":0},"969ef19b-27e1-4cfe-9b47-c1d50698513a":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:01:00","id":"969ef19b-27e1-4cfe-9b47-c1d50698513a","stepType":"pause","stepName":"9B Incubation","stepDetails":"","stepNumber":0},"e064752b-b811-460f-b00d-6039e820768b":{"moduleId":"033331ec-47f1-4f9a-9c01-ca09a87b9ac1:temperatureModuleType","setTemperature":"true","targetTemperature":"48","id":"e064752b-b811-460f-b00d-6039e820768b","stepType":"temperature","stepName":"Temp C1 to 48","stepDetails":"","stepNumber":0},"76b3a9f2-d032-48f8-a43b-d1d40ecaa800":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":true,"aspirate_mix_times":"1","aspirate_mix_volume":"75","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A7"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"50","dispense_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":"","dispense_mmFromBottom":10,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A8"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"150","id":"76b3a9f2-d032-48f8-a43b-d1d40ecaa800","stepType":"moveLiquid","stepName":"RxN Transfer","stepDetails":"","stepNumber":0},"9adbca06-96e9-4655-bed5-50facdd713bc":{"labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"561cc9e8-ae90-49c1-bccf-75a85989930b:magneticBlockType","useGripper":true,"id":"9adbca06-96e9-4655-bed5-50facdd713bc","stepType":"moveLabware","stepName":"P2 to Mag","stepDetails":"","stepNumber":0},"55ac0a98-c66a-4a43-8359-19e8d40d0b57":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":0.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A8"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"200","dispense_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":"","dispense_mmFromBottom":4,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A8"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","id":"55ac0a98-c66a-4a43-8359-19e8d40d0b57","stepType":"moveLiquid","stepName":"Rem 9B 2","stepDetails":"","stepNumber":0},"cd582b08-577f-4b56-86b5-86d00ed56762":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":true,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A7"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"50","dispense_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":"10","dispense_mix_volume":null,"dispense_mmFromBottom":12,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A8"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"150","id":"cd582b08-577f-4b56-86b5-86d00ed56762","stepType":"moveLiquid","stepName":"Add 9C 1","stepDetails":"","stepNumber":0},"ac86ba5d-38ae-4b91-8656-bd743859e273":{"labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"594810cf-69c3-4e9c-8f82-a8f9b38ad79d:opentrons/opentrons_96_well_aluminum_block/1","useGripper":true,"id":"ac86ba5d-38ae-4b91-8656-bd743859e273","stepType":"moveLabware","stepName":"P2 to Temp C1","stepDetails":"","stepNumber":0},"d7b5494b-4324-43a3-8716-85a1b3334e46":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"150","blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"blowout_z_offset":0,"changeTip":"always","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"150","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","liquidClassesSupported":true,"liquidClass":"none","mix_mmFromBottom":4,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":-1,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","pushOut_checkbox":false,"pushOut_volume":"20","times":"10","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","wells":["A8"],"id":"d7b5494b-4324-43a3-8716-85a1b3334e46","stepType":"mix","stepName":"Mix 9C 1","stepDetails":"","stepNumber":0},"7c3023af-c4c3-4757-9c23-a92e522806c2":{"labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"561cc9e8-ae90-49c1-bccf-75a85989930b:magneticBlockType","useGripper":true,"id":"7c3023af-c4c3-4757-9c23-a92e522806c2","stepType":"moveLabware","stepName":"P2 to Mag","stepDetails":"","stepNumber":0},"36b9e12a-eece-43e5-a70b-d82bb173bfe8":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A8"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"200","dispense_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":"","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A7"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","id":"36b9e12a-eece-43e5-a70b-d82bb173bfe8","stepType":"moveLiquid","stepName":"Rem 9C 1","stepDetails":"","stepNumber":0},"6f8f8767-fa71-41d8-8100-b428a8072707":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A8"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"50","dispense_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":"10","dispense_mix_volume":"100","dispense_mmFromBottom":12,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A8"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"150","id":"6f8f8767-fa71-41d8-8100-b428a8072707","stepType":"moveLiquid","stepName":"Add 9C 2","stepDetails":"","stepNumber":0},"036f94b6-27d4-46f7-8743-3b8b32e9ef98":{"labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"594810cf-69c3-4e9c-8f82-a8f9b38ad79d:opentrons/opentrons_96_well_aluminum_block/1","useGripper":true,"id":"036f94b6-27d4-46f7-8743-3b8b32e9ef98","stepType":"moveLabware","stepName":"P2 to Temp C1","stepDetails":"","stepNumber":0},"dfa403fe-09bd-42ba-96a2-196151485275":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"150","blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"blowout_z_offset":0,"changeTip":"always","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"150","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","liquidClassesSupported":true,"liquidClass":"none","mix_mmFromBottom":4,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":-1,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","pushOut_checkbox":false,"pushOut_volume":"20","times":"10","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","wells":["A8"],"id":"dfa403fe-09bd-42ba-96a2-196151485275","stepType":"mix","stepName":"Mix 9C 2","stepDetails":"","stepNumber":0},"49460001-4c24-42dc-87cf-df2340af1411":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A8"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"200","dispense_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":"","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A7"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","id":"49460001-4c24-42dc-87cf-df2340af1411","stepType":"moveLiquid","stepName":"Rem 9C 2","stepDetails":"","stepNumber":0},"c5ef0835-ac0e-49d1-8b58-da0a85c3694c":{"labware":"2d19a470-70c5-4006-9b83-85dd5572f12a:opentrons/opentrons_flex_96_filtertiprack_200ul/1","newLocation":"C4","useGripper":true,"id":"c5ef0835-ac0e-49d1-8b58-da0a85c3694c","stepType":"moveLabware","stepName":"Box 3 C3 to C4","stepDetails":"","stepNumber":0},"9a00210e-5114-49f0-9b6e-6c636931cd44":{"labware":"7be17658-efe0-4c22-a4a4-9c50c70e566a:opentrons/opentrons_flex_96_filtertiprack_200ul/1","newLocation":"C3","useGripper":true,"id":"9a00210e-5114-49f0-9b6e-6c636931cd44","stepType":"moveLabware","stepName":"Box 5 D4 to C3","stepDetails":"","stepNumber":0},"01897ea5-7cdd-4210-a608-ef4172381385":{"labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"C2","useGripper":true,"id":"01897ea5-7cdd-4210-a608-ef4172381385","stepType":"moveLabware","stepName":"P1 to Deck C2","stepDetails":"","stepNumber":0},"2df9bac7-93b8-4a47-a132-52c3838ca551":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:00:05","id":"2df9bac7-93b8-4a47-a132-52c3838ca551","stepType":"pause","stepName":"9C Incubation","stepDetails":"","stepNumber":0},"971a608d-3a7d-4f27-bc4c-b7b6d4fdf4a5":{"labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"561cc9e8-ae90-49c1-bccf-75a85989930b:magneticBlockType","useGripper":true,"id":"971a608d-3a7d-4f27-bc4c-b7b6d4fdf4a5","stepType":"moveLabware","stepName":"P2 to Mag","stepDetails":"","stepNumber":0},"5b22c515-c378-4649-b385-af550cb6d080":{"blockIsActive":true,"blockTargetTemp":"98","lidIsActive":true,"lidOpen":true,"lidTargetTemp":"105","moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":[],"profileItemsById":{},"profileTargetLidTemp":null,"profileVolume":null,"thermocyclerFormType":"thermocyclerState","blockIsActiveHold":false,"blockTargetTempHold":null,"lidIsActiveHold":false,"lidOpenHold":null,"lidTargetTempHold":null,"id":"5b22c515-c378-4649-b385-af550cb6d080","stepType":"thermocycler","stepName":"Step 10 Cycler Prep","stepDetails":"","stepNumber":0},"36fa013f-d7e0-4f41-832d-4302126812ab":{"moduleId":"033331ec-47f1-4f9a-9c01-ca09a87b9ac1:temperatureModuleType","setTemperature":"true","targetTemperature":"24","id":"36fa013f-d7e0-4f41-832d-4302126812ab","stepType":"temperature","stepName":"Temp C1 to 24C","stepDetails":"","stepNumber":0},"d098280c-6076-4bff-b2e5-71d0f6a72eeb":{"labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"594810cf-69c3-4e9c-8f82-a8f9b38ad79d:opentrons/opentrons_96_well_aluminum_block/1","useGripper":true,"id":"d098280c-6076-4bff-b2e5-71d0f6a72eeb","stepType":"moveLabware","stepName":"P1 to Temp C1","stepDetails":"","stepNumber":0},"8bbb5161-70cb-4176-9fae-cfffdce25161":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"25","dispense_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":"","dispense_mmFromBottom":5,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A8"],"dispense_x_position":1,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"50","id":"8bbb5161-70cb-4176-9fae-cfffdce25161","stepType":"moveLiquid","stepName":"Add LTE","stepDetails":"","stepNumber":0},"51ab1e21-2b5f-46ad-a8a0-fbd7fad13c95":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"25","aspirate_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":0.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A8"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"100","dispense_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":"","dispense_mmFromBottom":6,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A7"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"50","id":"51ab1e21-2b5f-46ad-a8a0-fbd7fad13c95","stepType":"moveLiquid","stepName":"Rem LTE","stepDetails":"","stepNumber":0},"92f181b9-69cf-46ed-a03e-1f8df266dbc3":{"labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"C2","useGripper":true,"id":"92f181b9-69cf-46ed-a03e-1f8df266dbc3","stepType":"moveLabware","stepName":"P2 to Deck C2","stepDetails":"","stepNumber":0},"f779ddd5-65b3-4d6d-b4fd-8b24074411a2":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"20","aspirate_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"20","dispense_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":true,"dispense_mix_times":"5","dispense_mix_volume":"15","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A8"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"20","id":"f779ddd5-65b3-4d6d-b4fd-8b24074411a2","stepType":"moveLiquid","stepName":"Elute 3","stepDetails":"","stepNumber":0},"658f472d-0d5c-4c51-ab44-c53d0216ecfb":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":true,"aspirate_delay_seconds":"0.7","aspirate_flowRate":"300","aspirate_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","aspirate_mix_checkbox":true,"aspirate_mix_times":"5","aspirate_mix_volume":"300","aspirate_mmFromBottom":0.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"1","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":true,"aspirate_touchTip_mmFromTop":-10,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["C3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"250","blowout_location":"source_well","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"5","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":true,"dispense_delay_seconds":"1","dispense_flowRate":"200","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":5,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A10","B10","C10","D10","E10","F10","G10","H10"],"dispense_x_position":1,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"5","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"glycerol_50","nozzles":null,"path":"multiDispense","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"35","tipRack":"opentrons/opentrons_flex_96_filtertiprack_1000ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"55","id":"658f472d-0d5c-4c51-ab44-c53d0216ecfb","stepType":"moveLiquid","stepName":"SB Disperse 4","stepDetails":"","stepNumber":0},"49a5d69f-8c67-4c41-9703-5a9e95611993":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"100","aspirate_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":0.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["C5"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"250","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"200","dispense_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","dispense_mix_checkbox":true,"dispense_mix_times":"10","dispense_mix_volume":"200","dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["C6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"single","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"75","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"50","id":"49a5d69f-8c67-4c41-9703-5a9e95611993","stepType":"moveLiquid","stepName":"10A + 10B Mix","stepDetails":"","stepNumber":0},"0f02e4fe-4301-4619-b3f8-63e4496ac852":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"200","aspirate_labware":"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":0.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["C6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"30","dispense_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A9","B9","C9","D9","E9","F9","G9","H9"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"5","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"multiDispense","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_1000ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"32","id":"0f02e4fe-4301-4619-b3f8-63e4496ac852","stepType":"moveLiquid","stepName":"Mix 10 Disperse","stepDetails":"","stepNumber":0},"60e6a51f-0f26-4294-937b-2dff74bd1bcf":{"moduleId":"65263cf9-315d-4e77-a59d-5e60ac83f781:temperatureModuleType","setTemperature":null,"targetTemperature":null,"id":"60e6a51f-0f26-4294-937b-2dff74bd1bcf","stepType":"temperature","stepName":"Temp D1 Deactivate","stepDetails":"","stepNumber":0},"26fe086f-a731-41f6-b631-60627ab61232":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"20","aspirate_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A9"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"40","dispense_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":true,"dispense_mix_times":"10","dispense_mix_volume":"40","dispense_mmFromBottom":3,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A8"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"30","id":"26fe086f-a731-41f6-b631-60627ab61232","stepType":"moveLiquid","stepName":"Mix 10 RxN","stepDetails":"","stepNumber":0},"2b1d3ba2-659c-420f-a6a3-c9147d37e89b":{"labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","useGripper":true,"id":"2b1d3ba2-659c-420f-a6a3-c9147d37e89b","stepType":"moveLabware","stepName":"P2 to Cycler","stepDetails":"","stepNumber":0},"77324879-de62-49a9-bf51-5c031ec6cbbe":{"blockIsActive":false,"blockTargetTemp":null,"lidIsActive":false,"lidOpen":false,"lidTargetTemp":null,"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":["3b0f3ad0-4fb1-42a3-a316-26dbe78ec2d8","adf4d471-11b0-4426-9231-ff9bc7c62883","fa9834db-35e9-44ef-a7e4-3c7713865f12"],"profileItemsById":{"3b0f3ad0-4fb1-42a3-a316-26dbe78ec2d8":{"durationMinutes":"00","durationSeconds":"30","id":"3b0f3ad0-4fb1-42a3-a316-26dbe78ec2d8","temperature":"98","title":"1","type":"profileStep"},"adf4d471-11b0-4426-9231-ff9bc7c62883":{"id":"adf4d471-11b0-4426-9231-ff9bc7c62883","title":"","steps":[{"durationMinutes":"00","durationSeconds":"10","id":"effb2efa-ebf9-4b46-b556-84bfcb20226c","temperature":"98","title":"2.1","type":"profileStep"},{"durationMinutes":"00","durationSeconds":"30","id":"c6c39636-48bf-40f9-b060-7dad520189c6","temperature":"60","title":"2.2","type":"profileStep"},{"durationMinutes":"00","durationSeconds":"30","id":"4b28c3b0-003f-4180-9804-6eabfd367c2f","temperature":"72","title":"2.3","type":"profileStep"}],"type":"profileCycle","repetitions":"12"},"fa9834db-35e9-44ef-a7e4-3c7713865f12":{"durationMinutes":"01","durationSeconds":"00","id":"fa9834db-35e9-44ef-a7e4-3c7713865f12","temperature":"72","title":"3","type":"profileStep"}},"profileTargetLidTemp":"105","profileVolume":"50","thermocyclerFormType":"thermocyclerProfile","id":"77324879-de62-49a9-bf51-5c031ec6cbbe","stepType":"thermocycler","stepName":"Step 10 Incubation","stepDetails":""},"c15b1b06-10d4-41c8-b138-4033b339234d":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"c15b1b06-10d4-41c8-b138-4033b339234d","stepType":"pause","stepName":"pause","stepDetails":""},"f64b3d56-ad04-49c6-b488-cb39c5686669":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"f64b3d56-ad04-49c6-b488-cb39c5686669","stepType":"pause","stepName":"pause","stepDetails":""},"9a7d40ba-ef83-4227-a085-5637e43c861d":{"blockIsActive":true,"blockTargetTemp":"4","lidIsActive":false,"lidOpen":true,"lidTargetTemp":"","moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":[],"profileItemsById":{},"profileTargetLidTemp":null,"profileVolume":null,"thermocyclerFormType":"thermocyclerState","id":"9a7d40ba-ef83-4227-a085-5637e43c861d","stepType":"thermocycler","stepName":"Step 10 Incubation","stepDetails":""},"04f26b45-6bf4-4d2c-905b-6f105a9858ff":{"labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"C2","useGripper":true,"id":"04f26b45-6bf4-4d2c-905b-6f105a9858ff","stepType":"moveLabware","stepName":"P2 to Deck C2","stepDetails":"","stepNumber":0},"ffca5fd7-7dd6-4057-a2d2-be77dbae061c":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":true,"aspirate_mix_times":"3","aspirate_mix_volume":"45","aspirate_mmFromBottom":1.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"1","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"50","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A10"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"50","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":true,"dispense_delay_seconds":"1","dispense_flowRate":"75","dispense_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":true,"dispense_mix_times":"5","dispense_mix_volume":"75","dispense_mmFromBottom":3,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"50","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A8"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"50","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"50","id":"ffca5fd7-7dd6-4057-a2d2-be77dbae061c","stepType":"moveLiquid","stepName":"SB + Sample 4","stepDetails":"","stepNumber":0},"931f1e2b-e2ec-4619-91ee-5f9ede272e5b":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"500","aspirate_labware":"6db7eb96-52b3-489e-805e-010e35d88119:opentrons/opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"300","blowout_location":"dest_well","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"12","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"300","dispense_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":5,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A2"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"ethanol_80","nozzles":null,"path":"single","pipette":"155ded0a-0639-45fb-b83f-df0574691c2f","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"","tipRack":"opentrons/opentrons_flex_96_filtertiprack_1000ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"4000","id":"931f1e2b-e2ec-4619-91ee-5f9ede272e5b","stepType":"moveLiquid","stepName":"EtOH to Res 4","stepDetails":"","stepNumber":0},"140d912a-8c6b-40ce-970c-8daacfe1cbd9":{"moduleId":"033331ec-47f1-4f9a-9c01-ca09a87b9ac1:temperatureModuleType","setTemperature":null,"targetTemperature":null,"id":"140d912a-8c6b-40ce-970c-8daacfe1cbd9","stepType":"temperature","stepName":"Temp C1 Deactivate","stepDetails":"","stepNumber":0},"cf61b16c-c425-4ba9-bc9c-03843139e6fe":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:05:00","id":"cf61b16c-c425-4ba9-bc9c-03843139e6fe","stepType":"pause","stepName":"Bead Incubation 4","stepDetails":"","stepNumber":0},"6fb6acc2-0251-4a07-87c0-62b583970515":{"labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"561cc9e8-ae90-49c1-bccf-75a85989930b:magneticBlockType","useGripper":true,"id":"6fb6acc2-0251-4a07-87c0-62b583970515","stepType":"moveLabware","stepName":"P2 to Mag","stepDetails":"","stepNumber":0},"432c9412-6291-4d0a-9841-db091445a75a":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:02:00","id":"432c9412-6291-4d0a-9841-db091445a75a","stepType":"pause","stepName":"Pause 2 min","stepDetails":"","stepNumber":0},"f9a6de00-061e-47ce-bc32-7260cbd23d1b":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"25","aspirate_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A8"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"100","dispense_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":"","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","id":"f9a6de00-061e-47ce-bc32-7260cbd23d1b","stepType":"moveLiquid","stepName":"Rem Sup 4","stepDetails":"","stepNumber":0},"fec8abe4-9a20-49c7-bd68-987f9d60cb16":{"aspirate_airGap_checkbox":true,"aspirate_airGap_volume":"10","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"150","aspirate_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"100","blowout_location":"dest_well","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"10","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"50","dispense_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":10,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A8"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"ethanol_80","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"150","id":"fec8abe4-9a20-49c7-bd68-987f9d60cb16","stepType":"moveLiquid","stepName":"Add EtOH 4.1","stepDetails":"","stepNumber":0},"bb4d034d-c710-4a75-a92e-cc9aba2dce6a":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"25","aspirate_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A8"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"100","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"10","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"150","dispense_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":4,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"ethanol_80","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","id":"bb4d034d-c710-4a75-a92e-cc9aba2dce6a","stepType":"moveLiquid","stepName":"Rem EtOH 4.1","stepDetails":"","stepNumber":0},"a850b308-03c6-4d2b-bdbd-9089c6d6fac9":{"aspirate_airGap_checkbox":true,"aspirate_airGap_volume":"10","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"150","aspirate_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"100","blowout_location":"dest_well","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"10","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"50","dispense_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":10,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A8"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"ethanol_80","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"150","id":"a850b308-03c6-4d2b-bdbd-9089c6d6fac9","stepType":"moveLiquid","stepName":"Add EtOH 4.2","stepDetails":"","stepNumber":0},"ee25b295-e13a-4f0b-8205-76883c68b65c":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"25","aspirate_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":0.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A8"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"100","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"10","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"150","dispense_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":6,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"ethanol_80","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","id":"ee25b295-e13a-4f0b-8205-76883c68b65c","stepType":"moveLiquid","stepName":"Rem EtOH 4.2","stepDetails":"","stepNumber":0},"4c82ee8a-4db8-4675-b0e4-68da5a04079d":{"labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"C2","useGripper":true,"id":"4c82ee8a-4db8-4675-b0e4-68da5a04079d","stepType":"moveLabware","stepName":"P2 to Deck C2","stepDetails":"","stepNumber":0},"aaa84f96-bd4f-452e-a798-b287e23fe3c3":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"20","aspirate_labware":"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"50","dispense_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":true,"dispense_mix_times":"5","dispense_mix_volume":"13","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A8"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"17","id":"aaa84f96-bd4f-452e-a798-b287e23fe3c3","stepType":"moveLiquid","stepName":"Elute 4","stepDetails":"","stepNumber":0},"9ac5ff0d-1e55-4ccf-a7b2-5bc8f8da460e":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:02:00","id":"9ac5ff0d-1e55-4ccf-a7b2-5bc8f8da460e","stepType":"pause","stepName":"Pause 2 min","stepDetails":"","stepNumber":0},"5d7d149f-5098-44cc-a92a-dc03408c985c":{"labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"561cc9e8-ae90-49c1-bccf-75a85989930b:magneticBlockType","useGripper":true,"id":"5d7d149f-5098-44cc-a92a-dc03408c985c","stepType":"moveLabware","stepName":"P2 to Mag","stepDetails":"","stepNumber":0},"baa6fbaf-2691-47cc-80e6-f5b8e0968158":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:02:00","id":"baa6fbaf-2691-47cc-80e6-f5b8e0968158","stepType":"pause","stepName":"Pause 2 min","stepDetails":"","stepNumber":0},"efbea6ed-7921-465b-87c0-e312054190be":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"20","aspirate_labware":"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":"","aspirate_mmFromBottom":0.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"500","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"500","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A8"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"716","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"20","dispense_labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":"","dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"500","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"500","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"c880e7c7-8497-484f-894a-6970bbd16e6c:wasteChute","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"2141dc88-dedc-41c1-8ebc-1a8868fa9069","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"20","tipRack":"opentrons/opentrons_flex_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"16","id":"efbea6ed-7921-465b-87c0-e312054190be","stepType":"moveLiquid","stepName":"Final Lib Elute","stepDetails":"","stepNumber":0},"e012458b-8027-4dde-a0d2-65b2025e7c97":{"labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","useGripper":true,"id":"e012458b-8027-4dde-a0d2-65b2025e7c97","stepType":"moveLabware","stepName":"P1 to Cycler","stepDetails":"","stepNumber":0},"baf4a902-0a6c-480f-94f2-65b7ca2dd710":{"blockIsActive":true,"blockTargetTemp":4,"lidIsActive":false,"lidOpen":false,"lidTargetTemp":null,"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":[],"profileItemsById":{},"profileTargetLidTemp":null,"profileVolume":null,"thermocyclerFormType":"thermocyclerState","blockIsActiveHold":false,"blockTargetTempHold":null,"lidIsActiveHold":false,"lidOpenHold":null,"lidTargetTempHold":null,"id":"baf4a902-0a6c-480f-94f2-65b7ca2dd710","stepType":"thermocycler","stepName":"Close Cycler","stepDetails":"","stepNumber":0},"fe7a35f3-3edb-407b-bd64-16888fe1c6a3":{"moduleId":null,"pauseAction":"untilResume","pauseMessage":"Library ready","pauseTemperature":null,"pauseTime":null,"id":"fe7a35f3-3edb-407b-bd64-16888fe1c6a3","stepType":"pause","stepName":"pause","stepDetails":"","stepNumber":0},"3236f89f-b731-4ec4-9190-0f7ef736b834":{"moduleId":"033331ec-47f1-4f9a-9c01-ca09a87b9ac1:temperatureModuleType","setTemperature":"true","targetTemperature":"4","id":"3236f89f-b731-4ec4-9190-0f7ef736b834","stepType":"temperature","stepName":"Temp C1 to 4C","stepDetails":"","stepNumber":0},"b9802f9f-e86d-4dde-a702-da50d1d07274":{"blockIsActive":false,"blockTargetTemp":"","lidIsActive":false,"lidOpen":true,"lidTargetTemp":null,"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":[],"profileItemsById":{},"profileTargetLidTemp":null,"profileVolume":null,"thermocyclerFormType":"thermocyclerState","blockIsActiveHold":false,"blockTargetTempHold":null,"lidIsActiveHold":false,"lidOpenHold":null,"lidTargetTempHold":null,"id":"b9802f9f-e86d-4dde-a702-da50d1d07274","stepType":"thermocycler","stepName":"Open Cycler","stepDetails":"","stepNumber":0},"644608f1-50ef-4b1b-8629-f861305d3095":{"labware":"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5","newLocation":"594810cf-69c3-4e9c-8f82-a8f9b38ad79d:opentrons/opentrons_96_well_aluminum_block/1","useGripper":true,"id":"644608f1-50ef-4b1b-8629-f861305d3095","stepType":"moveLabware","stepName":"P1 to Temp C1","stepDetails":"","stepNumber":0},"6c7ebf0d-153f-4e40-b1fd-db91ee3d0767":{"moduleId":null,"pauseAction":"untilResume","pauseMessage":"Take samples and place on ice. ","pauseTemperature":null,"pauseTime":null,"id":"6c7ebf0d-153f-4e40-b1fd-db91ee3d0767","stepType":"pause","stepName":"Take Libraries off","stepDetails":"","stepNumber":0},"321f5033-b31a-4493-9725-44f58ba2911a":{"moduleId":"033331ec-47f1-4f9a-9c01-ca09a87b9ac1:temperatureModuleType","setTemperature":null,"targetTemperature":null,"id":"321f5033-b31a-4493-9725-44f58ba2911a","stepType":"temperature","stepName":"Temp C1 Deactivate","stepDetails":"","stepNumber":0},"49e4fb93-c485-44fb-acc2-ec5ea60cd33b":{"blockIsActive":false,"blockTargetTemp":null,"lidIsActive":false,"lidOpen":false,"lidTargetTemp":null,"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":[],"profileItemsById":{},"profileTargetLidTemp":null,"profileVolume":null,"thermocyclerFormType":"thermocyclerState","blockIsActiveHold":false,"blockTargetTempHold":null,"lidIsActiveHold":false,"lidOpenHold":null,"lidTargetTempHold":null,"id":"49e4fb93-c485-44fb-acc2-ec5ea60cd33b","stepType":"thermocycler","stepName":"Deactivate Cycler","stepDetails":"","stepNumber":0},"26ef6f02-1418-4ec2-b9bd-109adb106918":{"blockIsActive":false,"blockTargetTemp":null,"lidIsActive":false,"lidOpen":false,"lidTargetTemp":null,"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":["62a1988b-c884-4693-8cdc-667c0401680a","c9310a97-ac23-457e-88f8-f2508cb6a3cc"],"profileItemsById":{"62a1988b-c884-4693-8cdc-667c0401680a":{"durationMinutes":"12","durationSeconds":"00","id":"62a1988b-c884-4693-8cdc-667c0401680a","temperature":"37","title":"1","type":"profileStep"},"c9310a97-ac23-457e-88f8-f2508cb6a3cc":{"durationMinutes":"15","durationSeconds":"00","id":"c9310a97-ac23-457e-88f8-f2508cb6a3cc","temperature":"65","title":"2","type":"profileStep"}},"profileTargetLidTemp":"75","profileVolume":"15","thermocyclerFormType":"thermocyclerProfile","id":"26ef6f02-1418-4ec2-b9bd-109adb106918","stepType":"thermocycler","stepName":"Step 2 Start","stepDetails":"","stepNumber":0},"842c4521-a376-4fe5-8739-451624403cf8":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"842c4521-a376-4fe5-8739-451624403cf8","stepType":"pause","stepName":"pause","stepDetails":""},"844bb3eb-7905-4b1a-8bac-0131d4ebdb5e":{"blockIsActive":true,"blockTargetTemp":"12","lidIsActive":true,"lidOpen":true,"lidTargetTemp":"85","moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":[],"profileItemsById":{},"profileTargetLidTemp":null,"profileVolume":null,"thermocyclerFormType":"thermocyclerState","id":"844bb3eb-7905-4b1a-8bac-0131d4ebdb5e","stepType":"thermocycler","stepName":"Step 2 End","stepDetails":"","stepNumber":0},"ff341267-ef63-4292-816a-fa787f31cd25":{"labware":"2bd3ba52-6320-4739-b104-ef168e2e144a:opentrons/opentrons_flex_96_filtertiprack_200ul/1","newLocation":"D4","useGripper":true,"id":"ff341267-ef63-4292-816a-fa787f31cd25","stepType":"moveLabware","stepName":"Box 4 B3 to D4","stepDetails":"","stepNumber":0},"634edd7d-9448-4353-b946-9804a77ef39d":{"labware":"4a3bea46-728a-498c-9c2e-a5caf006f10b:opentrons/opentrons_flex_96_filtertiprack_200ul/1","newLocation":"B3","useGripper":true,"id":"634edd7d-9448-4353-b946-9804a77ef39d","stepType":"moveLabware","stepName":"Box1 A4 to B3","stepDetails":"","stepNumber":0},"5c8ba096-577a-4172-9c56-c8b4eacd326b":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"5c8ba096-577a-4172-9c56-c8b4eacd326b","stepType":"pause","stepName":"pause","stepDetails":""},"6769123b-851a-42c1-9844-856920607e14":{"blockIsActive":true,"blockTargetTemp":"12","lidIsActive":true,"lidOpen":true,"lidTargetTemp":"75","moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":[],"profileItemsById":{},"profileTargetLidTemp":null,"profileVolume":null,"thermocyclerFormType":"thermocyclerState","id":"6769123b-851a-42c1-9844-856920607e14","stepType":"thermocycler","stepName":"Step 5 End","stepDetails":""},"623a4203-0603-43cf-a2aa-cfacdb39315c":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:02:00","id":"623a4203-0603-43cf-a2aa-cfacdb39315c","stepType":"pause","stepName":"Bead Bind 1","stepDetails":"","stepNumber":0},"ec801a04-3604-4071-977b-04b2089c27c3":{"moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","pauseAction":"untilThermocyclerProfileComplete","pauseMessage":"","pauseTemperature":null,"pauseTime":null,"id":"ec801a04-3604-4071-977b-04b2089c27c3","stepType":"pause","stepName":"pause","stepDetails":""},"38e6c41a-d1ae-4971-ba65-90fcc4989d3b":{"blockIsActive":true,"blockTargetTemp":"24","lidIsActive":true,"lidOpen":true,"lidTargetTemp":"56","moduleId":"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType","orderedProfileItems":[],"profileItemsById":{},"profileTargetLidTemp":null,"profileVolume":null,"thermocyclerFormType":"thermocyclerState","id":"38e6c41a-d1ae-4971-ba65-90fcc4989d3b","stepType":"thermocycler","stepName":"Step 7 Incubation","stepDetails":""},"978dd488-bdfe-4d41-a6a0-03c59e01e798":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:00:30","id":"978dd488-bdfe-4d41-a6a0-03c59e01e798","stepType":"pause","stepName":"Bind Beads","stepDetails":"","stepNumber":0},"d5fa704f-4dec-4e24-ac1e-adc84521bf6c":{"moduleId":"033331ec-47f1-4f9a-9c01-ca09a87b9ac1:temperatureModuleType","setTemperature":"true","targetTemperature":"24","id":"d5fa704f-4dec-4e24-ac1e-adc84521bf6c","stepType":"temperature","stepName":"Temp C1 24 C","stepDetails":"","stepNumber":0},"fb47df59-e217-48f5-913f-b4154de32eeb":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:05:00","id":"fb47df59-e217-48f5-913f-b4154de32eeb","stepType":"pause","stepName":"Bind Beads","stepDetails":"","stepNumber":0}},"orderedStepIds":["f7f8d8a4-ec78-4516-b402-e42da5136a85","3189d4da-e030-49de-9f7e-b0730c3c4d73","eb470c8d-e040-4d88-a53a-b77c01db6d5b","5ecf8966-038a-44e2-8ae3-69aa45dc2fe3","1e1f2b3d-2658-4c64-8190-432863878537","93745cb0-644f-439d-aa1a-4e038f1097b3","ec46e4a0-c689-4a20-9838-320b3b83165a","886936bf-210f-4e9f-bfc6-41e8e8e36aa4","7b2834b6-8bba-43c0-9020-3863f6988cca","b3ba6306-9ce0-4252-b76c-b751400875b0","b2d27fd1-e137-418c-a983-4f2afb0787fe","8ab7c733-f380-498c-b756-e6b7d67140c3","869f366b-90af-4459-9839-a08f9df5042c","9db89d6f-3c0a-40a2-b975-11e5b3c7b218","a08d8754-fb66-484b-bc0a-7e01c4d26985","d7a992d4-ad3b-4c2b-a85d-bbbf061b0090","92fd55db-ddb2-4820-b2bb-8303db043f83","c8f7ddf9-f232-44d9-a686-cd861d693341","26ef6f02-1418-4ec2-b9bd-109adb106918","803f90b2-4f50-4838-af63-292ba8ea44dc","441bfc07-aa25-4198-9ee5-47e960e3d619","7dd38451-c1fc-4845-a128-0a43408b57ea","f5abc40d-72f1-498e-ab60-efe9bc8e4680","c090a7a1-1c8e-4963-af89-99ed5ab2f89d","e1aa0d6f-4de9-44b5-ae3b-40ca0d0b5912","842c4521-a376-4fe5-8739-451624403cf8","844bb3eb-7905-4b1a-8bac-0131d4ebdb5e","9eba86f9-bb30-412d-ba62-9adf3128b015","d0e6a43e-f30b-4994-b7b0-8e1c7ebe778d","6b34a55f-e41e-4e34-867b-bd6a1ab638ec","470f8d7a-5548-4dac-9cb2-374e8b57859a","26115080-470c-4811-85a4-bd748d5fdc4f","d20a9cdc-2ecb-450c-80e1-d7fa8fcbda69","156fc5c3-6141-4012-8c4e-3d3308d3c386","041f07a1-5ab0-4a68-a2dc-3a138804b088","9fcfdacd-6205-4cf2-803b-cc1ccc4c44a7","d5fa704f-4dec-4e24-ac1e-adc84521bf6c","31aa158c-d167-4bd1-bb01-9586065b6edc","ee130f51-993f-44d2-8c7b-fd02475414d4","d3e00fc1-d353-4a63-ac05-eea9fd0fb43b","35cbdeeb-0475-4364-9602-afa936d7462b","4efa6455-d70c-4cf4-bfe4-30f4b724d4d5","c030b267-9047-46dc-9e20-12b6d8f7561c","f2efca7d-696e-4cf2-a436-f9c5c69d2033","5c8ba096-577a-4172-9c56-c8b4eacd326b","1553aead-bcfd-4b0f-be34-e401001333ef","92998ae9-bf8a-47f7-8bf9-4058c09e9262","623a4203-0603-43cf-a2aa-cfacdb39315c","0000e7c0-bf27-4bf7-8ff6-cd609ff06142","34b1c83a-e57c-4af9-92fb-7b33586a647f","6856b413-c500-4e1e-bbaa-3975badf4a2e","54774486-843d-45bd-a8fd-c5a5c67d9d61","1fd56567-fc34-40d5-8cd7-e6fb007f9cbd","d7c8fd93-eaac-428a-a75d-c97b245d60fc","2653b82b-3e88-40d4-847f-3d87dc044ffd","be1d53b9-199f-486b-83c3-b6bbc192f9e3","d9564769-82e4-4a83-9adc-75f07feb6f9c","2823cf89-b0c8-4e41-a3ee-932f3136215f","a8b6ac49-7601-4e24-b300-5d76f656235b","6d4000a6-cd41-4640-a975-260addd3cebe","2e04f225-f5c2-4fcc-b1ce-a5d269644616","41fe1efc-b5ea-4850-be65-74feeffd9d14","9d01c0b3-213d-4bf3-9411-c3eb38c5ae36","22952fc3-db6a-43fa-a4f9-31cf85207a05","e49bde28-4791-4955-ac5b-18cc0658a1b3","e264b32b-68ed-49e0-88aa-820560e95c3b","6c7584f1-72c8-4082-aa12-2029f8210e50","5563f1be-4fc8-454d-b136-d98570ccce12","e9e20c47-0064-4a55-b958-418cd6aa56af","4165fdc2-49b6-43d8-890d-467e1fb8c69c","9ff89971-903e-4a7d-b0a0-5da2074d777f","7074ea38-a3ae-4601-ad2d-387d3a797b26","7f3bc144-d1a5-4291-8b5b-1f8919245267","6769123b-851a-42c1-9844-856920607e14","f4803e9b-9f0d-4a4a-b771-85d9375f0e23","71837b00-b6e5-4228-a346-0c36f08d08e7","12d666f2-8d58-40fe-afc6-4d54babe13d9","3ebccc2a-97f4-44c0-af78-e88bdbb5bb85","70bfc436-5af2-4608-a2f1-b66fa327f9cc","0c12ea3f-5291-4a52-b951-cf35df48ed48","96469258-d0e8-4f14-9831-3fdc161a860f","8ec21f63-f7e0-4d65-9883-37a8b9ce2591","ef05de48-d9f7-4b0d-bf37-d50ceb7e1771","626ba193-3c88-4e91-a041-49e096f60331","ec801a04-3604-4071-977b-04b2089c27c3","cb785a74-ef4a-4f92-9964-52a9f8e30754","aefe376d-b858-4368-ad89-3efc7c95da05","a1fe84f0-edd8-4d72-afcf-283f326e52ea","702f6690-e012-4280-b959-d88ffa7819d5","edac41ea-88da-4f2e-a7e9-02991725dfb7","ffc9c3b1-0afd-47d4-bda9-fc2846110406","677857b1-2c23-40e4-99e0-61540d64026f","46ae79c9-590d-486d-84a3-7384f11a7eea","ed25af81-d3dd-467a-881c-48136fb724f0","7cf4faab-326c-4fe1-a98d-e3e2e2337552","7b2b54a5-8852-49c6-9ea5-5d71ccf1032b","0554afaa-ab39-4e01-83e9-3ce9b201b6a4","cca199c0-778d-416a-ac3f-8dbfbd6ed970","7d0ec1ae-06cf-42e5-9c8e-f44273a9990f","03fe6045-dab5-4f9b-8df2-aed4c306b5aa","1e790a52-0d5c-48ca-8beb-955894ca4a5f","0c65b540-99ba-4cc3-be12-f66cb3f7026c","e1c17946-b9d4-4aba-a088-b33d0a495a36","02bf3807-760d-44a5-a4b8-017cf8176df5","1c410b4a-4454-48fe-b78a-96f9cd127fb0","297ddfc3-b603-4ad2-bbf0-e049af302915","d89f8be9-2314-4b66-b2b5-53110fa1b73b","4efecefd-69e2-48a3-b51c-6b63d9aa786d","98aa17e5-bf28-4525-8587-914fe28f2efa","edaa1587-ad6a-48c3-8a6d-d24acbbf954d","e18e56f1-dcf0-4524-b709-2b0f39799716","38e6c41a-d1ae-4971-ba65-90fcc4989d3b","73fa53c8-6f93-483d-944e-266e5eda5201","8d9a4467-8ff3-449c-98c3-e01e5abfd80d","dc7bece4-3fff-4182-9566-5edce83cc425","84083ef9-f900-4b5d-ab8f-1c48530888eb","fb47df59-e217-48f5-913f-b4154de32eeb","fa1e579a-b348-4af7-afc9-30dfee5e8c9f","e3c5c90b-2104-4ad5-9b6e-74ee3a274a17","8f0b4880-2ad3-402c-a5d9-036ef7d3c20f","ceea5d2d-d3be-43e2-9ded-7d6d412fb848","c5574468-5135-4148-8968-fddd1c1b6877","50ea8e7d-a8b8-496a-bf19-ddd6f97818d7","fee907be-071b-4a48-8d86-51c4a95687d4","e45933c8-b509-4f6d-899d-0212c54ba6dc","dd2b4be2-0338-4dd7-ad15-522853de4ec7","c88aaf0d-3089-4ab6-ab11-b5c0aa156187","525a75df-bdeb-4442-a273-0aafaffc703f","67766d8d-402f-406e-8e04-bde10210ae42","8f8b3918-1079-4116-ac3c-40b562bbc214","7bd0b730-7dfb-46c3-bef8-b3722aedf519","d1545ccd-bb13-4f57-8e56-462b6dc1f69d","34c0364d-a594-415f-8557-b46d7b266d94","433fff8c-8d4f-4b4d-816c-66aefe4e7171","74dd0828-3c87-4905-9e04-c79c87cf88e7","7ad92f96-27c1-4510-a434-b095be7983b7","3dd3172b-cc1d-4ad9-83d3-2f527279bfcd","1f2823fd-4038-43d2-b281-6f0864178e47","4f6e9a4e-9884-41b3-b79b-6b7b156cbdb9","7e2051d4-509e-4cf6-a8fc-e64426ecc8db","5e6b81e7-55ea-4ebc-99af-00b943707c17","e2259737-faba-416d-b1cc-fd4bb8461d01","965c3b34-6ca7-4942-804e-7efcddfba656","d8a209bc-5e3b-48c3-bf0a-cd04d7cef980","98f991cb-b1b2-422a-95d6-2c607fda90bd","0991ee7d-2cf7-4ce7-9479-7bbed23a38c1","317b3b80-9bda-409c-8b90-fa34df75eb7c","69692c76-504c-4dc8-ab39-60c180422590","862cd5d9-67c1-44af-b5f3-0ab3c7361501","8d291db6-a2eb-4b93-8153-0273187621f3","bfa6f714-93e8-4f7b-8a76-6f8c5f5d173f","b5722d10-0871-4709-8b87-9f15b9b8eab9","5216b76f-3e59-4c1e-b1bd-2a650787bace","7e7ea0c5-ed4d-4f3e-917e-b7970e506f21","6be88374-e7e8-49fc-bef1-82fa7422a6c6","8d11d5ad-b9ab-4795-9100-4ba024ea66e0","cd2738d9-e67d-4d57-bc2a-571746846ff6","978dd488-bdfe-4d41-a6a0-03c59e01e798","777bb889-245c-44fa-82f3-20014c5301ed","0c6693f6-d4cf-44b1-911f-8d48a164ea9c","54656a37-8bf4-44b7-9005-eff753fb0a4a","6e2471bc-b27f-46f7-9aee-4acc4698dc5f","3a97c77e-ca29-43eb-b35d-849fe928bb2b","5a564527-44f3-4811-a0fa-2f5e70dabf02","29c2555d-1688-4863-9c43-37aeb388aaff","a1edded1-056e-47a5-8045-353904199f79","c35012c6-9596-4708-8f9f-3cbd0e0a60db","b0f7e2b8-6076-4da0-9eca-a8b4d322947c","95e77349-e268-4183-a389-87e2ea1f6d8b","94e477b9-879f-41a0-8e7d-0bfcdb6615c2","f9556003-fc64-49b6-8630-3bb1025e1337","7163c588-9e28-4108-acc5-095ec820c5ae","f25ebae4-5b7f-4c59-a66b-b90fdddb6ac5","b35f945f-dc93-4c88-8a85-fe00b4352208","401d0c97-8efa-4eb9-86d6-4f28e27af441","42bfc236-a318-4749-b03e-bb39175af7d1","f51935e7-2729-43d9-b434-75a7cd24eb9c","4956a732-c1da-497d-b0d3-fb58e6978ce1","5d7e914e-e00a-49f5-88f9-46b64b1a1012","111a5d9d-47c2-4e88-8df4-ad8e1c61ef35","85c028ad-e72d-4934-ad6f-db7b43319181","c333f046-1efe-4e14-b4db-c456bba6a3fa","0800bb1c-744a-4209-9cf6-cb25ad79e754","1f3abe18-9a03-4866-8156-693d1165ce19","69dcf1b5-7dd8-447a-8ef4-d0fb02ab86bb","918ad838-c887-41d2-8039-179f267ab37e","969ef19b-27e1-4cfe-9b47-c1d50698513a","e064752b-b811-460f-b00d-6039e820768b","76b3a9f2-d032-48f8-a43b-d1d40ecaa800","9adbca06-96e9-4655-bed5-50facdd713bc","55ac0a98-c66a-4a43-8359-19e8d40d0b57","cd582b08-577f-4b56-86b5-86d00ed56762","ac86ba5d-38ae-4b91-8656-bd743859e273","d7b5494b-4324-43a3-8716-85a1b3334e46","7c3023af-c4c3-4757-9c23-a92e522806c2","36b9e12a-eece-43e5-a70b-d82bb173bfe8","6f8f8767-fa71-41d8-8100-b428a8072707","036f94b6-27d4-46f7-8743-3b8b32e9ef98","dfa403fe-09bd-42ba-96a2-196151485275","c5ef0835-ac0e-49d1-8b58-da0a85c3694c","9a00210e-5114-49f0-9b6e-6c636931cd44","01897ea5-7cdd-4210-a608-ef4172381385","5b22c515-c378-4649-b385-af550cb6d080","2df9bac7-93b8-4a47-a132-52c3838ca551","971a608d-3a7d-4f27-bc4c-b7b6d4fdf4a5","36fa013f-d7e0-4f41-832d-4302126812ab","d098280c-6076-4bff-b2e5-71d0f6a72eeb","49460001-4c24-42dc-87cf-df2340af1411","8bbb5161-70cb-4176-9fae-cfffdce25161","ff341267-ef63-4292-816a-fa787f31cd25","634edd7d-9448-4353-b946-9804a77ef39d","51ab1e21-2b5f-46ad-a8a0-fbd7fad13c95","92f181b9-69cf-46ed-a03e-1f8df266dbc3","f779ddd5-65b3-4d6d-b4fd-8b24074411a2","49a5d69f-8c67-4c41-9703-5a9e95611993","0f02e4fe-4301-4619-b3f8-63e4496ac852","60e6a51f-0f26-4294-937b-2dff74bd1bcf","26fe086f-a731-41f6-b631-60627ab61232","2b1d3ba2-659c-420f-a6a3-c9147d37e89b","77324879-de62-49a9-bf51-5c031ec6cbbe","658f472d-0d5c-4c51-ab44-c53d0216ecfb","931f1e2b-e2ec-4619-91ee-5f9ede272e5b","c15b1b06-10d4-41c8-b138-4033b339234d","9a7d40ba-ef83-4227-a085-5637e43c861d","04f26b45-6bf4-4d2c-905b-6f105a9858ff","ffca5fd7-7dd6-4057-a2d2-be77dbae061c","cf61b16c-c425-4ba9-bc9c-03843139e6fe","6fb6acc2-0251-4a07-87c0-62b583970515","432c9412-6291-4d0a-9841-db091445a75a","f9a6de00-061e-47ce-bc32-7260cbd23d1b","fec8abe4-9a20-49c7-bd68-987f9d60cb16","bb4d034d-c710-4a75-a92e-cc9aba2dce6a","a850b308-03c6-4d2b-bdbd-9089c6d6fac9","ee25b295-e13a-4f0b-8205-76883c68b65c","4c82ee8a-4db8-4675-b0e4-68da5a04079d","aaa84f96-bd4f-452e-a798-b287e23fe3c3","9ac5ff0d-1e55-4ccf-a7b2-5bc8f8da460e","5d7d149f-5098-44cc-a92a-dc03408c985c","baa6fbaf-2691-47cc-80e6-f5b8e0968158","efbea6ed-7921-465b-87c0-e312054190be","140d912a-8c6b-40ce-970c-8daacfe1cbd9","e012458b-8027-4dde-a0d2-65b2025e7c97","baf4a902-0a6c-480f-94f2-65b7ca2dd710","fe7a35f3-3edb-407b-bd64-16888fe1c6a3","3236f89f-b731-4ec4-9190-0f7ef736b834","b9802f9f-e86d-4dde-a702-da50d1d07274","644608f1-50ef-4b1b-8629-f861305d3095","6c7ebf0d-153f-4e40-b1fd-db91ee3d0767","321f5033-b31a-4493-9725-44f58ba2911a","49e4fb93-c485-44fb-acc2-ec5ea60cd33b"],"pipettes":{"155ded0a-0639-45fb-b83f-df0574691c2f":{"pipetteName":"p1000_single_flex"},"2141dc88-dedc-41c1-8ebc-1a8868fa9069":{"pipetteName":"p1000_multi_flex"}},"modules":{"f20be06b-0a26-4ae5-a761-40da7ae2f72e:thermocyclerModuleType":{"model":"thermocyclerModuleV2"},"033331ec-47f1-4f9a-9c01-ca09a87b9ac1:temperatureModuleType":{"model":"temperatureModuleV2"},"65263cf9-315d-4e77-a59d-5e60ac83f781:temperatureModuleType":{"model":"temperatureModuleV2"},"561cc9e8-ae90-49c1-bccf-75a85989930b:magneticBlockType":{"model":"magneticBlockV1"}},"labware":{"b474f89a-f894-48b8-ae4e-dee6cbae8d7c:opentrons/opentrons_flex_96_filtertiprack_1000ul/1":{"displayName":"Opentrons Flex 96 Filter Tip Rack 1000 µL","labwareDefURI":"opentrons/opentrons_flex_96_filtertiprack_1000ul/1"},"271a7505-3035-4be2-8204-80a7546b6512:opentrons/opentrons_flex_96_filtertiprack_200ul/1":{"displayName":"Opentrons Flex 96 Filter Tip Rack 200 µL","labwareDefURI":"opentrons/opentrons_flex_96_filtertiprack_200ul/1"},"4a3bea46-728a-498c-9c2e-a5caf006f10b:opentrons/opentrons_flex_96_filtertiprack_200ul/1":{"displayName":"Opentrons Flex 96 Filter Tip Rack 200 µL (1)","labwareDefURI":"opentrons/opentrons_flex_96_filtertiprack_200ul/1"},"f1d18a33-99d2-4f9d-bdd6-3d4fe1f15b4a:opentrons/opentrons_flex_96_filtertiprack_200ul/1":{"displayName":"Opentrons Flex 96 Filter Tip Rack 200 µL (2)","labwareDefURI":"opentrons/opentrons_flex_96_filtertiprack_200ul/1"},"2d19a470-70c5-4006-9b83-85dd5572f12a:opentrons/opentrons_flex_96_filtertiprack_200ul/1":{"displayName":"Opentrons Flex 96 Filter Tip Rack 200 µL (3)","labwareDefURI":"opentrons/opentrons_flex_96_filtertiprack_200ul/1"},"2bd3ba52-6320-4739-b104-ef168e2e144a:opentrons/opentrons_flex_96_filtertiprack_200ul/1":{"displayName":"Opentrons Flex 96 Filter Tip Rack 200 µL (4)","labwareDefURI":"opentrons/opentrons_flex_96_filtertiprack_200ul/1"},"7be17658-efe0-4c22-a4a4-9c50c70e566a:opentrons/opentrons_flex_96_filtertiprack_200ul/1":{"displayName":"Opentrons Flex 96 Filter Tip Rack 200 µL (5)","labwareDefURI":"opentrons/opentrons_flex_96_filtertiprack_200ul/1"},"594810cf-69c3-4e9c-8f82-a8f9b38ad79d:opentrons/opentrons_96_well_aluminum_block/1":{"displayName":"Opentrons 96 Well Aluminum Block","labwareDefURI":"opentrons/opentrons_96_well_aluminum_block/1"},"3a7a5872-4975-4000-80c8-a713ce66c2cb:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5":{"displayName":"Plate 1","labwareDefURI":"opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5"},"6db7eb96-52b3-489e-805e-010e35d88119:opentrons/opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical/3":{"displayName":"Conical Tube Rack","labwareDefURI":"opentrons/opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical/3"},"b0549cbd-98d8-46e7-a243-a3ee7ac4675e:opentrons/nest_12_reservoir_15ml/3":{"displayName":"12 Well Reservoir","labwareDefURI":"opentrons/nest_12_reservoir_15ml/3"},"6d2fe684-a0bb-458a-89c8-25b3c868a6db:opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5":{"displayName":"Plate 2","labwareDefURI":"opentrons/nest_96_wellplate_100ul_pcr_full_skirt/5"},"09f00c19-3585-4f75-b625-35875b7edbc7:opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3":{"displayName":"Opentrons 24 Well Aluminum Block with Generic 2 mL Screwcap","labwareDefURI":"opentrons/opentrons_24_aluminumblock_generic_2ml_screwcap/3"}}}},"metadata":{"protocolName":"DuoSeq_FFPE_v.1","author":"","description":"","source":"Protocol Designer","created":1769803974419,"lastModified":1776718202673}}"""
