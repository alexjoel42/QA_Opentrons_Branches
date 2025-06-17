import json
from contextlib import nullcontext as pd_step
from opentrons import protocol_api, types

metadata = {
    "protocolName": "Zymo_Magbead_DNA_Cells-Flex_96_channel  Truly fixed",
    "author": "Opentrons ",
    "description": "https://library.opentrons.com/p/Zymo_Magbead_DNA_Flex_96-Cells \n\n",
    "created": "2024-12-05T16:30:17.918Z",
    "lastModified": "2025-06-09T21:21:19.499Z",
    "protocolDesigner": "8.4.4",
    "source": "Protocol Designer",
}

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.24",
}

def run(protocol: protocol_api.ProtocolContext) -> None:
    # Load Modules:
    temperature_module_1 = protocol.load_module("temperatureModuleV2", "A3")
    magnetic_block_1 = protocol.load_module("magneticBlockV1", "C1")
    heater_shaker_module_1 = protocol.load_module("heaterShakerModuleV1", "D1")

    # Load Adapters:
    aluminum_block_1 = temperature_module_1.load_adapter(
        "opentrons_96_well_aluminum_block",
        namespace="opentrons",
        version=1,
    )
    adapter_1 = protocol.load_adapter(
        "opentrons_flex_96_tiprack_adapter",
        location="A1",
        namespace="opentrons",
        version=1,
    )
    adapter_2 = protocol.load_adapter(
        "opentrons_flex_96_tiprack_adapter",
        location="A2",
        namespace="opentrons",
        version=1,
    )
    adapter_3 = heater_shaker_module_1.load_adapter(
        "opentrons_96_deep_well_adapter",
        namespace="opentrons",
        version=1,
    )

    # Load Labware:
    well_plate_1 = aluminum_block_1.load_labware(
        "opentrons_96_wellplate_200ul_pcr_full_skirt",
        label="Elution plate",
        namespace="opentrons",
        version=2,
    )
    well_plate_2 = protocol.load_labware(
        "nest_96_wellplate_2ml_deep",
        location="B3",
        label="Wash 3",
        namespace="opentrons",
        version=2,
    )
    well_plate_3 = protocol.load_labware(
        "nest_96_wellplate_2ml_deep",
        location="C3",
        label="Binding 2",
        namespace="opentrons",
        version=2,
    )
    well_plate_4 = protocol.load_labware(
        "nest_96_wellplate_2ml_deep",
        location="B1",
        label="NEST 96 Deep Well Plate 2mL (3)",
        namespace="opentrons",
        version=2,
    )
    well_plate_5 = protocol.load_labware(
        "nest_96_wellplate_2ml_deep",
        location="B2",
        label="Wash 2",
        namespace="opentrons",
        version=2,
    )
    tip_rack_1 = adapter_1.load_labware(
        "opentrons_flex_96_tiprack_1000ul",
        label="Opentrons Flex 96 Tip Rack 1000 µL (1)",
        namespace="opentrons",
        version=1,
    )
    tip_rack_2 = adapter_2.load_labware(
        "opentrons_flex_96_tiprack_1000ul",
        label="Opentrons Flex 96 Tip Rack 1000 µL (2)",
        namespace="opentrons",
        version=1,
    )
    well_plate_6 = protocol.load_labware(
        "nest_96_wellplate_2ml_deep",
        location="D2",
        label="Lysis",
        namespace="opentrons",
        version=2,
    )
    well_plate_7 = protocol.load_labware(
        "nest_96_wellplate_2ml_deep",
        location="C2",
        label="Binding and Beading",
        namespace="opentrons",
        version=2,
    )
    tip_rack_3 = protocol.load_labware(
        "opentrons_flex_96_tiprack_1000ul",
        location=protocol_api.OFF_DECK,
        label="Opentrons Flex 96 Tip Rack 1000 µL (3)",
        namespace="opentrons",
        version=1,
    )
    tip_rack_4 = protocol.load_labware(
        "opentrons_flex_96_tiprack_1000ul",
        location=protocol_api.OFF_DECK,
        label="Opentrons Flex 96 Tip Rack 1000 µL (4)",
        namespace="opentrons",
        version=1,
    )
    tip_rack_5 = protocol.load_labware(
        "opentrons_flex_96_tiprack_1000ul",
        location=protocol_api.OFF_DECK,
        label="Opentrons Flex 96 Tip Rack 1000 µL (5)",
        namespace="opentrons",
        version=1,
    )
    tip_rack_6 = protocol.load_labware(
        "opentrons_flex_96_tiprack_1000ul",
        location=protocol_api.OFF_DECK,
        label="Opentrons Flex 96 Tip Rack 1000 µL (6)",
        namespace="opentrons",
        version=1,
    )
    tip_rack_7 = protocol.load_labware(
        "opentrons_flex_96_tiprack_1000ul",
        location=protocol_api.OFF_DECK,
        label="Opentrons Flex 96 Tip Rack 1000 µL (7)",
        namespace="opentrons",
        version=1,
    )
    tip_rack_8 = protocol.load_labware(
        "opentrons_flex_96_tiprack_1000ul",
        location=protocol_api.OFF_DECK,
        label="Opentrons Flex 96 Tip Rack 1000 µL (8)",
        namespace="opentrons",
        version=1,
    )
    tip_rack_9 = protocol.load_labware(
        "opentrons_flex_96_tiprack_1000ul",
        location=protocol_api.OFF_DECK,
        label="Opentrons Flex 96 Tip Rack 1000 µL (9)",
        namespace="opentrons",
        version=1,
    )
    tip_rack_10 = protocol.load_labware(
        "opentrons_flex_96_tiprack_1000ul",
        location=protocol_api.OFF_DECK,
        label="Opentrons Flex 96 Tip Rack 1000 µL (10)",
        namespace="opentrons",
        version=1,
    )
    tip_rack_11 = protocol.load_labware(
        "opentrons_flex_96_tiprack_1000ul",
        location=protocol_api.OFF_DECK,
        label="Opentrons Flex 96 Tip Rack 1000 µL (11)",
        namespace="opentrons",
        version=1,
    )
    tip_rack_12 = protocol.load_labware(
        "opentrons_flex_96_tiprack_1000ul",
        location=protocol_api.OFF_DECK,
        label="Opentrons Flex 96 Tip Rack 1000 µL (12)",
        namespace="opentrons",
        version=1,
    )
    tip_rack_13 = protocol.load_labware(
        "opentrons_flex_96_tiprack_1000ul",
        location=protocol_api.OFF_DECK,
        label="Opentrons Flex 96 Tip Rack 1000 µL (13)",
        namespace="opentrons",
        version=1,
    )
    tip_rack_14 = protocol.load_labware(
        "opentrons_flex_96_tiprack_1000ul",
        location=protocol_api.OFF_DECK,
        label="Opentrons Flex 96 Tip Rack 1000 µL (14)",
        namespace="opentrons",
        version=1,
    )
    tip_rack_15 = protocol.load_labware(
        "opentrons_flex_96_tiprack_1000ul",
        location=protocol_api.OFF_DECK,
        label="Opentrons Flex 96 Tip Rack 1000 µL (15)",
        namespace="opentrons",
        version=1,
    )
    tip_rack_16 = protocol.load_labware(
        "opentrons_flex_96_tiprack_1000ul",
        location=protocol_api.OFF_DECK,
        label="Opentrons Flex 96 Tip Rack 1000 µL (16)",
        namespace="opentrons",
        version=1,
    )
    well_plate_8 = adapter_3.load_labware(
        "nest_96_wellplate_2ml_deep",
        namespace="opentrons",
        version=2,
    )

    # Load Pipettes:
    pipette = protocol.load_instrument("flex_96channel_1000", tip_racks=[tip_rack_1, tip_rack_2, tip_rack_3, tip_rack_4, tip_rack_5, tip_rack_6, tip_rack_7, tip_rack_8, tip_rack_9, tip_rack_10, tip_rack_11, tip_rack_12, tip_rack_13, tip_rack_14, tip_rack_15, tip_rack_16])

    # Load Waste Chute:
    waste_chute = protocol.load_waste_chute()

    # Define Liquids:
    liquid_1 = protocol.define_liquid(
        "Elution Buffer",
        display_color="#ff4f4fff",
    )
    liquid_2 = protocol.define_liquid(
        "Wash 1",
        display_color="#0025ffff",
    )
    liquid_3 = protocol.define_liquid(
        "Wash 2",
        display_color="#850cbeff",
    )
    liquid_4 = protocol.define_liquid(
        "Wash 3",
        display_color="#9dfff0ff",
    )
    liquid_5 = protocol.define_liquid(
        "Binding 2",
        display_color="#50d5ffc2",
    )
    liquid_6 = protocol.define_liquid(
        "Lysis",
        display_color="#5aad31ff",
    )
    liquid_7 = protocol.define_liquid(
        "Binding and beading ",
        display_color="#a50d0dff",
    )
    liquid_8 = protocol.define_liquid(
        "Good Stuff",
        display_color="#ff4f4f",
    )

    # Load Liquids:
    well_plate_1["A1"].load_liquid(liquid_1, 80)
    well_plate_1["B1"].load_liquid(liquid_1, 80)
    well_plate_1["C1"].load_liquid(liquid_1, 80)
    well_plate_1["D1"].load_liquid(liquid_1, 80)
    well_plate_1["E1"].load_liquid(liquid_1, 80)
    well_plate_1["F1"].load_liquid(liquid_1, 80)
    well_plate_1["G1"].load_liquid(liquid_1, 80)
    well_plate_1["H1"].load_liquid(liquid_1, 80)
    well_plate_1["A2"].load_liquid(liquid_1, 80)
    well_plate_1["B2"].load_liquid(liquid_1, 80)
    well_plate_1["C2"].load_liquid(liquid_1, 80)
    well_plate_1["D2"].load_liquid(liquid_1, 80)
    well_plate_1["E2"].load_liquid(liquid_1, 80)
    well_plate_1["F2"].load_liquid(liquid_1, 80)
    well_plate_1["G2"].load_liquid(liquid_1, 80)
    well_plate_1["H2"].load_liquid(liquid_1, 80)
    well_plate_1["A3"].load_liquid(liquid_1, 80)
    well_plate_1["B3"].load_liquid(liquid_1, 80)
    well_plate_1["C3"].load_liquid(liquid_1, 80)
    well_plate_1["D3"].load_liquid(liquid_1, 80)
    well_plate_1["E3"].load_liquid(liquid_1, 80)
    well_plate_1["F3"].load_liquid(liquid_1, 80)
    well_plate_1["G3"].load_liquid(liquid_1, 80)
    well_plate_1["H3"].load_liquid(liquid_1, 80)
    well_plate_1["A4"].load_liquid(liquid_1, 80)
    well_plate_1["B4"].load_liquid(liquid_1, 80)
    well_plate_1["C4"].load_liquid(liquid_1, 80)
    well_plate_1["D4"].load_liquid(liquid_1, 80)
    well_plate_1["E4"].load_liquid(liquid_1, 80)
    well_plate_1["F4"].load_liquid(liquid_1, 80)
    well_plate_1["G4"].load_liquid(liquid_1, 80)
    well_plate_1["H4"].load_liquid(liquid_1, 80)
    well_plate_1["A5"].load_liquid(liquid_1, 80)
    well_plate_1["B5"].load_liquid(liquid_1, 80)
    well_plate_1["C5"].load_liquid(liquid_1, 80)
    well_plate_1["D5"].load_liquid(liquid_1, 80)
    well_plate_1["E5"].load_liquid(liquid_1, 80)
    well_plate_1["F5"].load_liquid(liquid_1, 80)
    well_plate_1["G5"].load_liquid(liquid_1, 80)
    well_plate_1["H5"].load_liquid(liquid_1, 80)
    well_plate_1["A6"].load_liquid(liquid_1, 80)
    well_plate_1["B6"].load_liquid(liquid_1, 80)
    well_plate_1["C6"].load_liquid(liquid_1, 80)
    well_plate_1["D6"].load_liquid(liquid_1, 80)
    well_plate_1["E6"].load_liquid(liquid_1, 80)
    well_plate_1["F6"].load_liquid(liquid_1, 80)
    well_plate_1["G6"].load_liquid(liquid_1, 80)
    well_plate_1["H6"].load_liquid(liquid_1, 80)
    well_plate_1["A7"].load_liquid(liquid_1, 80)
    well_plate_1["B7"].load_liquid(liquid_1, 80)
    well_plate_1["C7"].load_liquid(liquid_1, 80)
    well_plate_1["D7"].load_liquid(liquid_1, 80)
    well_plate_1["E7"].load_liquid(liquid_1, 80)
    well_plate_1["F7"].load_liquid(liquid_1, 80)
    well_plate_1["G7"].load_liquid(liquid_1, 80)
    well_plate_1["H7"].load_liquid(liquid_1, 80)
    well_plate_1["A8"].load_liquid(liquid_1, 80)
    well_plate_1["B8"].load_liquid(liquid_1, 80)
    well_plate_1["C8"].load_liquid(liquid_1, 80)
    well_plate_1["D8"].load_liquid(liquid_1, 80)
    well_plate_1["E8"].load_liquid(liquid_1, 80)
    well_plate_1["F8"].load_liquid(liquid_1, 80)
    well_plate_1["G8"].load_liquid(liquid_1, 80)
    well_plate_1["H8"].load_liquid(liquid_1, 80)
    well_plate_1["A9"].load_liquid(liquid_1, 80)
    well_plate_1["B9"].load_liquid(liquid_1, 80)
    well_plate_1["C9"].load_liquid(liquid_1, 80)
    well_plate_1["D9"].load_liquid(liquid_1, 80)
    well_plate_1["E9"].load_liquid(liquid_1, 80)
    well_plate_1["F9"].load_liquid(liquid_1, 80)
    well_plate_1["G9"].load_liquid(liquid_1, 80)
    well_plate_1["H9"].load_liquid(liquid_1, 80)
    well_plate_1["A10"].load_liquid(liquid_1, 80)
    well_plate_1["B10"].load_liquid(liquid_1, 80)
    well_plate_1["C10"].load_liquid(liquid_1, 80)
    well_plate_1["D10"].load_liquid(liquid_1, 80)
    well_plate_1["E10"].load_liquid(liquid_1, 80)
    well_plate_1["F10"].load_liquid(liquid_1, 80)
    well_plate_1["G10"].load_liquid(liquid_1, 80)
    well_plate_1["H10"].load_liquid(liquid_1, 80)
    well_plate_1["A11"].load_liquid(liquid_1, 80)
    well_plate_1["B11"].load_liquid(liquid_1, 80)
    well_plate_1["C11"].load_liquid(liquid_1, 80)
    well_plate_1["D11"].load_liquid(liquid_1, 80)
    well_plate_1["E11"].load_liquid(liquid_1, 80)
    well_plate_1["F11"].load_liquid(liquid_1, 80)
    well_plate_1["G11"].load_liquid(liquid_1, 80)
    well_plate_1["H11"].load_liquid(liquid_1, 80)
    well_plate_1["A12"].load_liquid(liquid_1, 80)
    well_plate_1["B12"].load_liquid(liquid_1, 80)
    well_plate_1["C12"].load_liquid(liquid_1, 80)
    well_plate_1["D12"].load_liquid(liquid_1, 80)
    well_plate_1["E12"].load_liquid(liquid_1, 80)
    well_plate_1["F12"].load_liquid(liquid_1, 80)
    well_plate_1["G12"].load_liquid(liquid_1, 80)
    well_plate_1["H12"].load_liquid(liquid_1, 80)
    well_plate_3["A1"].load_liquid(liquid_5, 600)
    well_plate_3["B1"].load_liquid(liquid_5, 600)
    well_plate_3["C1"].load_liquid(liquid_5, 600)
    well_plate_3["D1"].load_liquid(liquid_5, 600)
    well_plate_3["E1"].load_liquid(liquid_5, 600)
    well_plate_3["F1"].load_liquid(liquid_5, 600)
    well_plate_3["G1"].load_liquid(liquid_5, 600)
    well_plate_3["H1"].load_liquid(liquid_5, 600)
    well_plate_3["A2"].load_liquid(liquid_5, 600)
    well_plate_3["B2"].load_liquid(liquid_5, 600)
    well_plate_3["C2"].load_liquid(liquid_5, 600)
    well_plate_3["D2"].load_liquid(liquid_5, 600)
    well_plate_3["E2"].load_liquid(liquid_5, 600)
    well_plate_3["F2"].load_liquid(liquid_5, 600)
    well_plate_3["G2"].load_liquid(liquid_5, 600)
    well_plate_3["H2"].load_liquid(liquid_5, 600)
    well_plate_3["A3"].load_liquid(liquid_5, 600)
    well_plate_3["B3"].load_liquid(liquid_5, 600)
    well_plate_3["C3"].load_liquid(liquid_5, 600)
    well_plate_3["D3"].load_liquid(liquid_5, 600)
    well_plate_3["E3"].load_liquid(liquid_5, 600)
    well_plate_3["F3"].load_liquid(liquid_5, 600)
    well_plate_3["G3"].load_liquid(liquid_5, 600)
    well_plate_3["H3"].load_liquid(liquid_5, 600)
    well_plate_3["A4"].load_liquid(liquid_5, 600)
    well_plate_3["B4"].load_liquid(liquid_5, 600)
    well_plate_3["C4"].load_liquid(liquid_5, 600)
    well_plate_3["D4"].load_liquid(liquid_5, 600)
    well_plate_3["E4"].load_liquid(liquid_5, 600)
    well_plate_3["F4"].load_liquid(liquid_5, 600)
    well_plate_3["G4"].load_liquid(liquid_5, 600)
    well_plate_3["H4"].load_liquid(liquid_5, 600)
    well_plate_3["A5"].load_liquid(liquid_5, 600)
    well_plate_3["B5"].load_liquid(liquid_5, 600)
    well_plate_3["C5"].load_liquid(liquid_5, 600)
    well_plate_3["D5"].load_liquid(liquid_5, 600)
    well_plate_3["E5"].load_liquid(liquid_5, 600)
    well_plate_3["F5"].load_liquid(liquid_5, 600)
    well_plate_3["G5"].load_liquid(liquid_5, 600)
    well_plate_3["H5"].load_liquid(liquid_5, 600)
    well_plate_3["A6"].load_liquid(liquid_5, 600)
    well_plate_3["B6"].load_liquid(liquid_5, 600)
    well_plate_3["C6"].load_liquid(liquid_5, 600)
    well_plate_3["D6"].load_liquid(liquid_5, 600)
    well_plate_3["E6"].load_liquid(liquid_5, 600)
    well_plate_3["F6"].load_liquid(liquid_5, 600)
    well_plate_3["G6"].load_liquid(liquid_5, 600)
    well_plate_3["H6"].load_liquid(liquid_5, 600)
    well_plate_3["A7"].load_liquid(liquid_5, 600)
    well_plate_3["B7"].load_liquid(liquid_5, 600)
    well_plate_3["C7"].load_liquid(liquid_5, 600)
    well_plate_3["D7"].load_liquid(liquid_5, 600)
    well_plate_3["E7"].load_liquid(liquid_5, 600)
    well_plate_3["F7"].load_liquid(liquid_5, 600)
    well_plate_3["G7"].load_liquid(liquid_5, 600)
    well_plate_3["H7"].load_liquid(liquid_5, 600)
    well_plate_3["A8"].load_liquid(liquid_5, 600)
    well_plate_3["B8"].load_liquid(liquid_5, 600)
    well_plate_3["C8"].load_liquid(liquid_5, 600)
    well_plate_3["D8"].load_liquid(liquid_5, 600)
    well_plate_3["E8"].load_liquid(liquid_5, 600)
    well_plate_3["F8"].load_liquid(liquid_5, 600)
    well_plate_3["G8"].load_liquid(liquid_5, 600)
    well_plate_3["H8"].load_liquid(liquid_5, 600)
    well_plate_3["A9"].load_liquid(liquid_5, 600)
    well_plate_3["B9"].load_liquid(liquid_5, 600)
    well_plate_3["C9"].load_liquid(liquid_5, 600)
    well_plate_3["D9"].load_liquid(liquid_5, 600)
    well_plate_3["E9"].load_liquid(liquid_5, 600)
    well_plate_3["F9"].load_liquid(liquid_5, 600)
    well_plate_3["G9"].load_liquid(liquid_5, 600)
    well_plate_3["H9"].load_liquid(liquid_5, 600)
    well_plate_3["A10"].load_liquid(liquid_5, 600)
    well_plate_3["B10"].load_liquid(liquid_5, 600)
    well_plate_3["C10"].load_liquid(liquid_5, 600)
    well_plate_3["D10"].load_liquid(liquid_5, 600)
    well_plate_3["E10"].load_liquid(liquid_5, 600)
    well_plate_3["F10"].load_liquid(liquid_5, 600)
    well_plate_3["G10"].load_liquid(liquid_5, 600)
    well_plate_3["H10"].load_liquid(liquid_5, 600)
    well_plate_3["A11"].load_liquid(liquid_5, 600)
    well_plate_3["B11"].load_liquid(liquid_5, 600)
    well_plate_3["C11"].load_liquid(liquid_5, 600)
    well_plate_3["D11"].load_liquid(liquid_5, 600)
    well_plate_3["E11"].load_liquid(liquid_5, 600)
    well_plate_3["F11"].load_liquid(liquid_5, 600)
    well_plate_3["G11"].load_liquid(liquid_5, 600)
    well_plate_3["H11"].load_liquid(liquid_5, 600)
    well_plate_3["A12"].load_liquid(liquid_5, 600)
    well_plate_3["B12"].load_liquid(liquid_5, 600)
    well_plate_3["C12"].load_liquid(liquid_5, 600)
    well_plate_3["D12"].load_liquid(liquid_5, 600)
    well_plate_3["E12"].load_liquid(liquid_5, 600)
    well_plate_3["F12"].load_liquid(liquid_5, 600)
    well_plate_3["G12"].load_liquid(liquid_5, 600)
    well_plate_3["H12"].load_liquid(liquid_5, 600)
    well_plate_4["A1"].load_liquid(liquid_2, 600)
    well_plate_4["B1"].load_liquid(liquid_2, 600)
    well_plate_4["C1"].load_liquid(liquid_2, 600)
    well_plate_4["D1"].load_liquid(liquid_2, 600)
    well_plate_4["E1"].load_liquid(liquid_2, 600)
    well_plate_4["F1"].load_liquid(liquid_2, 600)
    well_plate_4["G1"].load_liquid(liquid_2, 600)
    well_plate_4["H1"].load_liquid(liquid_2, 600)
    well_plate_4["A2"].load_liquid(liquid_2, 600)
    well_plate_4["B2"].load_liquid(liquid_2, 600)
    well_plate_4["C2"].load_liquid(liquid_2, 600)
    well_plate_4["D2"].load_liquid(liquid_2, 600)
    well_plate_4["E2"].load_liquid(liquid_2, 600)
    well_plate_4["F2"].load_liquid(liquid_2, 600)
    well_plate_4["G2"].load_liquid(liquid_2, 600)
    well_plate_4["H2"].load_liquid(liquid_2, 600)
    well_plate_4["A3"].load_liquid(liquid_2, 600)
    well_plate_4["B3"].load_liquid(liquid_2, 600)
    well_plate_4["C3"].load_liquid(liquid_2, 600)
    well_plate_4["D3"].load_liquid(liquid_2, 600)
    well_plate_4["E3"].load_liquid(liquid_2, 600)
    well_plate_4["F3"].load_liquid(liquid_2, 600)
    well_plate_4["G3"].load_liquid(liquid_2, 600)
    well_plate_4["H3"].load_liquid(liquid_2, 600)
    well_plate_4["A4"].load_liquid(liquid_2, 600)
    well_plate_4["B4"].load_liquid(liquid_2, 600)
    well_plate_4["C4"].load_liquid(liquid_2, 600)
    well_plate_4["D4"].load_liquid(liquid_2, 600)
    well_plate_4["E4"].load_liquid(liquid_2, 600)
    well_plate_4["F4"].load_liquid(liquid_2, 600)
    well_plate_4["G4"].load_liquid(liquid_2, 600)
    well_plate_4["H4"].load_liquid(liquid_2, 600)
    well_plate_4["A5"].load_liquid(liquid_2, 600)
    well_plate_4["B5"].load_liquid(liquid_2, 600)
    well_plate_4["C5"].load_liquid(liquid_2, 600)
    well_plate_4["D5"].load_liquid(liquid_2, 600)
    well_plate_4["E5"].load_liquid(liquid_2, 600)
    well_plate_4["F5"].load_liquid(liquid_2, 600)
    well_plate_4["G5"].load_liquid(liquid_2, 600)
    well_plate_4["H5"].load_liquid(liquid_2, 600)
    well_plate_4["A6"].load_liquid(liquid_2, 600)
    well_plate_4["B6"].load_liquid(liquid_2, 600)
    well_plate_4["C6"].load_liquid(liquid_2, 600)
    well_plate_4["D6"].load_liquid(liquid_2, 600)
    well_plate_4["E6"].load_liquid(liquid_2, 600)
    well_plate_4["F6"].load_liquid(liquid_2, 600)
    well_plate_4["G6"].load_liquid(liquid_2, 600)
    well_plate_4["H6"].load_liquid(liquid_2, 600)
    well_plate_4["A7"].load_liquid(liquid_2, 600)
    well_plate_4["B7"].load_liquid(liquid_2, 600)
    well_plate_4["C7"].load_liquid(liquid_2, 600)
    well_plate_4["D7"].load_liquid(liquid_2, 600)
    well_plate_4["E7"].load_liquid(liquid_2, 600)
    well_plate_4["F7"].load_liquid(liquid_2, 600)
    well_plate_4["G7"].load_liquid(liquid_2, 600)
    well_plate_4["H7"].load_liquid(liquid_2, 600)
    well_plate_4["A8"].load_liquid(liquid_2, 600)
    well_plate_4["B8"].load_liquid(liquid_2, 600)
    well_plate_4["C8"].load_liquid(liquid_2, 600)
    well_plate_4["D8"].load_liquid(liquid_2, 600)
    well_plate_4["E8"].load_liquid(liquid_2, 600)
    well_plate_4["F8"].load_liquid(liquid_2, 600)
    well_plate_4["G8"].load_liquid(liquid_2, 600)
    well_plate_4["H8"].load_liquid(liquid_2, 600)
    well_plate_4["A9"].load_liquid(liquid_2, 600)
    well_plate_4["B9"].load_liquid(liquid_2, 600)
    well_plate_4["C9"].load_liquid(liquid_2, 600)
    well_plate_4["D9"].load_liquid(liquid_2, 600)
    well_plate_4["E9"].load_liquid(liquid_2, 600)
    well_plate_4["F9"].load_liquid(liquid_2, 600)
    well_plate_4["G9"].load_liquid(liquid_2, 600)
    well_plate_4["H9"].load_liquid(liquid_2, 600)
    well_plate_4["A10"].load_liquid(liquid_2, 600)
    well_plate_4["B10"].load_liquid(liquid_2, 600)
    well_plate_4["C10"].load_liquid(liquid_2, 600)
    well_plate_4["D10"].load_liquid(liquid_2, 600)
    well_plate_4["E10"].load_liquid(liquid_2, 600)
    well_plate_4["F10"].load_liquid(liquid_2, 600)
    well_plate_4["G10"].load_liquid(liquid_2, 600)
    well_plate_4["H10"].load_liquid(liquid_2, 600)
    well_plate_4["A11"].load_liquid(liquid_2, 600)
    well_plate_4["B11"].load_liquid(liquid_2, 600)
    well_plate_4["C11"].load_liquid(liquid_2, 600)
    well_plate_4["D11"].load_liquid(liquid_2, 600)
    well_plate_4["E11"].load_liquid(liquid_2, 600)
    well_plate_4["F11"].load_liquid(liquid_2, 600)
    well_plate_4["G11"].load_liquid(liquid_2, 600)
    well_plate_4["H11"].load_liquid(liquid_2, 600)
    well_plate_4["A12"].load_liquid(liquid_2, 600)
    well_plate_4["B12"].load_liquid(liquid_2, 600)
    well_plate_4["C12"].load_liquid(liquid_2, 600)
    well_plate_4["D12"].load_liquid(liquid_2, 600)
    well_plate_4["E12"].load_liquid(liquid_2, 600)
    well_plate_4["F12"].load_liquid(liquid_2, 600)
    well_plate_4["G12"].load_liquid(liquid_2, 600)
    well_plate_4["H12"].load_liquid(liquid_2, 600)
    well_plate_5["A1"].load_liquid(liquid_3, 1900)
    well_plate_5["B1"].load_liquid(liquid_3, 1900)
    well_plate_5["C1"].load_liquid(liquid_3, 1900)
    well_plate_5["D1"].load_liquid(liquid_3, 1900)
    well_plate_5["E1"].load_liquid(liquid_3, 1900)
    well_plate_5["F1"].load_liquid(liquid_3, 1900)
    well_plate_5["G1"].load_liquid(liquid_3, 1900)
    well_plate_5["H1"].load_liquid(liquid_3, 1900)
    well_plate_5["A2"].load_liquid(liquid_3, 1900)
    well_plate_5["B2"].load_liquid(liquid_3, 1900)
    well_plate_5["C2"].load_liquid(liquid_3, 1900)
    well_plate_5["D2"].load_liquid(liquid_3, 1900)
    well_plate_5["E2"].load_liquid(liquid_3, 1900)
    well_plate_5["F2"].load_liquid(liquid_3, 1900)
    well_plate_5["G2"].load_liquid(liquid_3, 1900)
    well_plate_5["H2"].load_liquid(liquid_3, 1900)
    well_plate_5["A3"].load_liquid(liquid_3, 1900)
    well_plate_5["B3"].load_liquid(liquid_3, 1900)
    well_plate_5["C3"].load_liquid(liquid_3, 1900)
    well_plate_5["D3"].load_liquid(liquid_3, 1900)
    well_plate_5["E3"].load_liquid(liquid_3, 1900)
    well_plate_5["F3"].load_liquid(liquid_3, 1900)
    well_plate_5["G3"].load_liquid(liquid_3, 1900)
    well_plate_5["H3"].load_liquid(liquid_3, 1900)
    well_plate_5["A4"].load_liquid(liquid_3, 1900)
    well_plate_5["B4"].load_liquid(liquid_3, 1900)
    well_plate_5["C4"].load_liquid(liquid_3, 1900)
    well_plate_5["D4"].load_liquid(liquid_3, 1900)
    well_plate_5["E4"].load_liquid(liquid_3, 1900)
    well_plate_5["F4"].load_liquid(liquid_3, 1900)
    well_plate_5["G4"].load_liquid(liquid_3, 1900)
    well_plate_5["H4"].load_liquid(liquid_3, 1900)
    well_plate_5["A5"].load_liquid(liquid_3, 1900)
    well_plate_5["B5"].load_liquid(liquid_3, 1900)
    well_plate_5["C5"].load_liquid(liquid_3, 1900)
    well_plate_5["D5"].load_liquid(liquid_3, 1900)
    well_plate_5["E5"].load_liquid(liquid_3, 1900)
    well_plate_5["F5"].load_liquid(liquid_3, 1900)
    well_plate_5["G5"].load_liquid(liquid_3, 1900)
    well_plate_5["H5"].load_liquid(liquid_3, 1900)
    well_plate_5["A6"].load_liquid(liquid_3, 1900)
    well_plate_5["B6"].load_liquid(liquid_3, 1900)
    well_plate_5["C6"].load_liquid(liquid_3, 1900)
    well_plate_5["D6"].load_liquid(liquid_3, 1900)
    well_plate_5["E6"].load_liquid(liquid_3, 1900)
    well_plate_5["F6"].load_liquid(liquid_3, 1900)
    well_plate_5["G6"].load_liquid(liquid_3, 1900)
    well_plate_5["H6"].load_liquid(liquid_3, 1900)
    well_plate_5["A7"].load_liquid(liquid_3, 1900)
    well_plate_5["B7"].load_liquid(liquid_3, 1900)
    well_plate_5["C7"].load_liquid(liquid_3, 1900)
    well_plate_5["D7"].load_liquid(liquid_3, 1900)
    well_plate_5["E7"].load_liquid(liquid_3, 1900)
    well_plate_5["F7"].load_liquid(liquid_3, 1900)
    well_plate_5["G7"].load_liquid(liquid_3, 1900)
    well_plate_5["H7"].load_liquid(liquid_3, 1900)
    well_plate_5["A8"].load_liquid(liquid_3, 1900)
    well_plate_5["B8"].load_liquid(liquid_3, 1900)
    well_plate_5["C8"].load_liquid(liquid_3, 1900)
    well_plate_5["D8"].load_liquid(liquid_3, 1900)
    well_plate_5["E8"].load_liquid(liquid_3, 1900)
    well_plate_5["F8"].load_liquid(liquid_3, 1900)
    well_plate_5["G8"].load_liquid(liquid_3, 1900)
    well_plate_5["H8"].load_liquid(liquid_3, 1900)
    well_plate_5["A9"].load_liquid(liquid_3, 1900)
    well_plate_5["B9"].load_liquid(liquid_3, 1900)
    well_plate_5["C9"].load_liquid(liquid_3, 1900)
    well_plate_5["D9"].load_liquid(liquid_3, 1900)
    well_plate_5["E9"].load_liquid(liquid_3, 1900)
    well_plate_5["F9"].load_liquid(liquid_3, 1900)
    well_plate_5["G9"].load_liquid(liquid_3, 1900)
    well_plate_5["H9"].load_liquid(liquid_3, 1900)
    well_plate_5["A10"].load_liquid(liquid_3, 1900)
    well_plate_5["B10"].load_liquid(liquid_3, 1900)
    well_plate_5["C10"].load_liquid(liquid_3, 1900)
    well_plate_5["D10"].load_liquid(liquid_3, 1900)
    well_plate_5["E10"].load_liquid(liquid_3, 1900)
    well_plate_5["F10"].load_liquid(liquid_3, 1900)
    well_plate_5["G10"].load_liquid(liquid_3, 1900)
    well_plate_5["H10"].load_liquid(liquid_3, 1900)
    well_plate_5["A11"].load_liquid(liquid_3, 1900)
    well_plate_5["B11"].load_liquid(liquid_3, 1900)
    well_plate_5["C11"].load_liquid(liquid_3, 1900)
    well_plate_5["D11"].load_liquid(liquid_3, 1900)
    well_plate_5["E11"].load_liquid(liquid_3, 1900)
    well_plate_5["F11"].load_liquid(liquid_3, 1900)
    well_plate_5["G11"].load_liquid(liquid_3, 1900)
    well_plate_5["H11"].load_liquid(liquid_3, 1900)
    well_plate_5["A12"].load_liquid(liquid_3, 1900)
    well_plate_5["B12"].load_liquid(liquid_3, 1900)
    well_plate_5["C12"].load_liquid(liquid_3, 1900)
    well_plate_5["D12"].load_liquid(liquid_3, 1900)
    well_plate_5["E12"].load_liquid(liquid_3, 1900)
    well_plate_5["F12"].load_liquid(liquid_3, 1900)
    well_plate_5["G12"].load_liquid(liquid_3, 1900)
    well_plate_5["H12"].load_liquid(liquid_3, 1900)
    well_plate_2["A1"].load_liquid(liquid_4, 1000)
    well_plate_2["B1"].load_liquid(liquid_4, 1000)
    well_plate_2["C1"].load_liquid(liquid_4, 1000)
    well_plate_2["D1"].load_liquid(liquid_4, 1000)
    well_plate_2["E1"].load_liquid(liquid_4, 1000)
    well_plate_2["F1"].load_liquid(liquid_4, 1000)
    well_plate_2["G1"].load_liquid(liquid_4, 1000)
    well_plate_2["H1"].load_liquid(liquid_4, 1000)
    well_plate_2["A2"].load_liquid(liquid_4, 1000)
    well_plate_2["B2"].load_liquid(liquid_4, 1000)
    well_plate_2["C2"].load_liquid(liquid_4, 1000)
    well_plate_2["D2"].load_liquid(liquid_4, 1000)
    well_plate_2["E2"].load_liquid(liquid_4, 1000)
    well_plate_2["F2"].load_liquid(liquid_4, 1000)
    well_plate_2["G2"].load_liquid(liquid_4, 1000)
    well_plate_2["H2"].load_liquid(liquid_4, 1000)
    well_plate_2["A3"].load_liquid(liquid_4, 1000)
    well_plate_2["B3"].load_liquid(liquid_4, 1000)
    well_plate_2["C3"].load_liquid(liquid_4, 1000)
    well_plate_2["D3"].load_liquid(liquid_4, 1000)
    well_plate_2["E3"].load_liquid(liquid_4, 1000)
    well_plate_2["F3"].load_liquid(liquid_4, 1000)
    well_plate_2["G3"].load_liquid(liquid_4, 1000)
    well_plate_2["H3"].load_liquid(liquid_4, 1000)
    well_plate_2["A4"].load_liquid(liquid_4, 1000)
    well_plate_2["B4"].load_liquid(liquid_4, 1000)
    well_plate_2["C4"].load_liquid(liquid_4, 1000)
    well_plate_2["D4"].load_liquid(liquid_4, 1000)
    well_plate_2["E4"].load_liquid(liquid_4, 1000)
    well_plate_2["F4"].load_liquid(liquid_4, 1000)
    well_plate_2["G4"].load_liquid(liquid_4, 1000)
    well_plate_2["H4"].load_liquid(liquid_4, 1000)
    well_plate_2["A5"].load_liquid(liquid_4, 1000)
    well_plate_2["B5"].load_liquid(liquid_4, 1000)
    well_plate_2["C5"].load_liquid(liquid_4, 1000)
    well_plate_2["D5"].load_liquid(liquid_4, 1000)
    well_plate_2["E5"].load_liquid(liquid_4, 1000)
    well_plate_2["F5"].load_liquid(liquid_4, 1000)
    well_plate_2["G5"].load_liquid(liquid_4, 1000)
    well_plate_2["H5"].load_liquid(liquid_4, 1000)
    well_plate_2["A6"].load_liquid(liquid_4, 1000)
    well_plate_2["B6"].load_liquid(liquid_4, 1000)
    well_plate_2["C6"].load_liquid(liquid_4, 1000)
    well_plate_2["D6"].load_liquid(liquid_4, 1000)
    well_plate_2["E6"].load_liquid(liquid_4, 1000)
    well_plate_2["F6"].load_liquid(liquid_4, 1000)
    well_plate_2["G6"].load_liquid(liquid_4, 1000)
    well_plate_2["H6"].load_liquid(liquid_4, 1000)
    well_plate_2["A7"].load_liquid(liquid_4, 1000)
    well_plate_2["B7"].load_liquid(liquid_4, 1000)
    well_plate_2["C7"].load_liquid(liquid_4, 1000)
    well_plate_2["D7"].load_liquid(liquid_4, 1000)
    well_plate_2["E7"].load_liquid(liquid_4, 1000)
    well_plate_2["F7"].load_liquid(liquid_4, 1000)
    well_plate_2["G7"].load_liquid(liquid_4, 1000)
    well_plate_2["H7"].load_liquid(liquid_4, 1000)
    well_plate_2["A8"].load_liquid(liquid_4, 1000)
    well_plate_2["B8"].load_liquid(liquid_4, 1000)
    well_plate_2["C8"].load_liquid(liquid_4, 1000)
    well_plate_2["D8"].load_liquid(liquid_4, 1000)
    well_plate_2["E8"].load_liquid(liquid_4, 1000)
    well_plate_2["F8"].load_liquid(liquid_4, 1000)
    well_plate_2["G8"].load_liquid(liquid_4, 1000)
    well_plate_2["H8"].load_liquid(liquid_4, 1000)
    well_plate_2["A9"].load_liquid(liquid_4, 1000)
    well_plate_2["B9"].load_liquid(liquid_4, 1000)
    well_plate_2["C9"].load_liquid(liquid_4, 1000)
    well_plate_2["D9"].load_liquid(liquid_4, 1000)
    well_plate_2["E9"].load_liquid(liquid_4, 1000)
    well_plate_2["F9"].load_liquid(liquid_4, 1000)
    well_plate_2["G9"].load_liquid(liquid_4, 1000)
    well_plate_2["H9"].load_liquid(liquid_4, 1000)
    well_plate_2["A10"].load_liquid(liquid_4, 1000)
    well_plate_2["B10"].load_liquid(liquid_4, 1000)
    well_plate_2["C10"].load_liquid(liquid_4, 1000)
    well_plate_2["D10"].load_liquid(liquid_4, 1000)
    well_plate_2["E10"].load_liquid(liquid_4, 1000)
    well_plate_2["F10"].load_liquid(liquid_4, 1000)
    well_plate_2["G10"].load_liquid(liquid_4, 1000)
    well_plate_2["H10"].load_liquid(liquid_4, 1000)
    well_plate_2["A11"].load_liquid(liquid_4, 1000)
    well_plate_2["B11"].load_liquid(liquid_4, 1000)
    well_plate_2["C11"].load_liquid(liquid_4, 1000)
    well_plate_2["D11"].load_liquid(liquid_4, 1000)
    well_plate_2["E11"].load_liquid(liquid_4, 1000)
    well_plate_2["F11"].load_liquid(liquid_4, 1000)
    well_plate_2["G11"].load_liquid(liquid_4, 1000)
    well_plate_2["H11"].load_liquid(liquid_4, 1000)
    well_plate_2["A12"].load_liquid(liquid_4, 1000)
    well_plate_2["B12"].load_liquid(liquid_4, 1000)
    well_plate_2["C12"].load_liquid(liquid_4, 1000)
    well_plate_2["D12"].load_liquid(liquid_4, 1000)
    well_plate_2["E12"].load_liquid(liquid_4, 1000)
    well_plate_2["F12"].load_liquid(liquid_4, 1000)
    well_plate_2["G12"].load_liquid(liquid_4, 1000)
    well_plate_2["H12"].load_liquid(liquid_4, 1000)
    well_plate_6["A1"].load_liquid(liquid_6, 291)
    well_plate_6["B1"].load_liquid(liquid_6, 291)
    well_plate_6["C1"].load_liquid(liquid_6, 291)
    well_plate_6["D1"].load_liquid(liquid_6, 291)
    well_plate_6["E1"].load_liquid(liquid_6, 291)
    well_plate_6["F1"].load_liquid(liquid_6, 291)
    well_plate_6["G1"].load_liquid(liquid_6, 291)
    well_plate_6["H1"].load_liquid(liquid_6, 291)
    well_plate_6["A2"].load_liquid(liquid_6, 291)
    well_plate_6["B2"].load_liquid(liquid_6, 291)
    well_plate_6["C2"].load_liquid(liquid_6, 291)
    well_plate_6["D2"].load_liquid(liquid_6, 291)
    well_plate_6["E2"].load_liquid(liquid_6, 291)
    well_plate_6["F2"].load_liquid(liquid_6, 291)
    well_plate_6["G2"].load_liquid(liquid_6, 291)
    well_plate_6["H2"].load_liquid(liquid_6, 291)
    well_plate_6["A3"].load_liquid(liquid_6, 291)
    well_plate_6["B3"].load_liquid(liquid_6, 291)
    well_plate_6["C3"].load_liquid(liquid_6, 291)
    well_plate_6["D3"].load_liquid(liquid_6, 291)
    well_plate_6["E3"].load_liquid(liquid_6, 291)
    well_plate_6["F3"].load_liquid(liquid_6, 291)
    well_plate_6["G3"].load_liquid(liquid_6, 291)
    well_plate_6["H3"].load_liquid(liquid_6, 291)
    well_plate_6["A4"].load_liquid(liquid_6, 291)
    well_plate_6["B4"].load_liquid(liquid_6, 291)
    well_plate_6["C4"].load_liquid(liquid_6, 291)
    well_plate_6["D4"].load_liquid(liquid_6, 291)
    well_plate_6["E4"].load_liquid(liquid_6, 291)
    well_plate_6["F4"].load_liquid(liquid_6, 291)
    well_plate_6["G4"].load_liquid(liquid_6, 291)
    well_plate_6["H4"].load_liquid(liquid_6, 291)
    well_plate_6["A5"].load_liquid(liquid_6, 291)
    well_plate_6["B5"].load_liquid(liquid_6, 291)
    well_plate_6["C5"].load_liquid(liquid_6, 291)
    well_plate_6["D5"].load_liquid(liquid_6, 291)
    well_plate_6["E5"].load_liquid(liquid_6, 291)
    well_plate_6["F5"].load_liquid(liquid_6, 291)
    well_plate_6["G5"].load_liquid(liquid_6, 291)
    well_plate_6["H5"].load_liquid(liquid_6, 291)
    well_plate_6["A6"].load_liquid(liquid_6, 291)
    well_plate_6["B6"].load_liquid(liquid_6, 291)
    well_plate_6["C6"].load_liquid(liquid_6, 291)
    well_plate_6["D6"].load_liquid(liquid_6, 291)
    well_plate_6["E6"].load_liquid(liquid_6, 291)
    well_plate_6["F6"].load_liquid(liquid_6, 291)
    well_plate_6["G6"].load_liquid(liquid_6, 291)
    well_plate_6["H6"].load_liquid(liquid_6, 291)
    well_plate_6["A7"].load_liquid(liquid_6, 291)
    well_plate_6["B7"].load_liquid(liquid_6, 291)
    well_plate_6["C7"].load_liquid(liquid_6, 291)
    well_plate_6["D7"].load_liquid(liquid_6, 291)
    well_plate_6["E7"].load_liquid(liquid_6, 291)
    well_plate_6["F7"].load_liquid(liquid_6, 291)
    well_plate_6["G7"].load_liquid(liquid_6, 291)
    well_plate_6["H7"].load_liquid(liquid_6, 291)
    well_plate_6["A8"].load_liquid(liquid_6, 291)
    well_plate_6["B8"].load_liquid(liquid_6, 291)
    well_plate_6["C8"].load_liquid(liquid_6, 291)
    well_plate_6["D8"].load_liquid(liquid_6, 291)
    well_plate_6["E8"].load_liquid(liquid_6, 291)
    well_plate_6["F8"].load_liquid(liquid_6, 291)
    well_plate_6["G8"].load_liquid(liquid_6, 291)
    well_plate_6["H8"].load_liquid(liquid_6, 291)
    well_plate_6["A9"].load_liquid(liquid_6, 291)
    well_plate_6["B9"].load_liquid(liquid_6, 291)
    well_plate_6["C9"].load_liquid(liquid_6, 291)
    well_plate_6["D9"].load_liquid(liquid_6, 291)
    well_plate_6["E9"].load_liquid(liquid_6, 291)
    well_plate_6["F9"].load_liquid(liquid_6, 291)
    well_plate_6["G9"].load_liquid(liquid_6, 291)
    well_plate_6["H9"].load_liquid(liquid_6, 291)
    well_plate_6["A10"].load_liquid(liquid_6, 291)
    well_plate_6["B10"].load_liquid(liquid_6, 291)
    well_plate_6["C10"].load_liquid(liquid_6, 291)
    well_plate_6["D10"].load_liquid(liquid_6, 291)
    well_plate_6["E10"].load_liquid(liquid_6, 291)
    well_plate_6["F10"].load_liquid(liquid_6, 291)
    well_plate_6["G10"].load_liquid(liquid_6, 291)
    well_plate_6["H10"].load_liquid(liquid_6, 291)
    well_plate_6["A11"].load_liquid(liquid_6, 291)
    well_plate_6["B11"].load_liquid(liquid_6, 291)
    well_plate_6["C11"].load_liquid(liquid_6, 291)
    well_plate_6["D11"].load_liquid(liquid_6, 291)
    well_plate_6["E11"].load_liquid(liquid_6, 291)
    well_plate_6["F11"].load_liquid(liquid_6, 291)
    well_plate_6["G11"].load_liquid(liquid_6, 291)
    well_plate_6["H11"].load_liquid(liquid_6, 291)
    well_plate_6["A12"].load_liquid(liquid_6, 291)
    well_plate_6["B12"].load_liquid(liquid_6, 291)
    well_plate_6["C12"].load_liquid(liquid_6, 291)
    well_plate_6["D12"].load_liquid(liquid_6, 291)
    well_plate_6["E12"].load_liquid(liquid_6, 291)
    well_plate_6["F12"].load_liquid(liquid_6, 291)
    well_plate_6["G12"].load_liquid(liquid_6, 291)
    well_plate_6["H12"].load_liquid(liquid_6, 291)
    well_plate_7["A1"].load_liquid(liquid_7, 696)
    well_plate_7["B1"].load_liquid(liquid_7, 696)
    well_plate_7["C1"].load_liquid(liquid_7, 696)
    well_plate_7["D1"].load_liquid(liquid_7, 696)
    well_plate_7["E1"].load_liquid(liquid_7, 696)
    well_plate_7["F1"].load_liquid(liquid_7, 696)
    well_plate_7["G1"].load_liquid(liquid_7, 696)
    well_plate_7["H1"].load_liquid(liquid_7, 696)
    well_plate_7["A2"].load_liquid(liquid_7, 696)
    well_plate_7["B2"].load_liquid(liquid_7, 696)
    well_plate_7["C2"].load_liquid(liquid_7, 696)
    well_plate_7["D2"].load_liquid(liquid_7, 696)
    well_plate_7["E2"].load_liquid(liquid_7, 696)
    well_plate_7["F2"].load_liquid(liquid_7, 696)
    well_plate_7["G2"].load_liquid(liquid_7, 696)
    well_plate_7["H2"].load_liquid(liquid_7, 696)
    well_plate_7["A3"].load_liquid(liquid_7, 696)
    well_plate_7["B3"].load_liquid(liquid_7, 696)
    well_plate_7["C3"].load_liquid(liquid_7, 696)
    well_plate_7["D3"].load_liquid(liquid_7, 696)
    well_plate_7["E3"].load_liquid(liquid_7, 696)
    well_plate_7["F3"].load_liquid(liquid_7, 696)
    well_plate_7["G3"].load_liquid(liquid_7, 696)
    well_plate_7["H3"].load_liquid(liquid_7, 696)
    well_plate_7["A4"].load_liquid(liquid_7, 696)
    well_plate_7["B4"].load_liquid(liquid_7, 696)
    well_plate_7["C4"].load_liquid(liquid_7, 696)
    well_plate_7["D4"].load_liquid(liquid_7, 696)
    well_plate_7["E4"].load_liquid(liquid_7, 696)
    well_plate_7["F4"].load_liquid(liquid_7, 696)
    well_plate_7["G4"].load_liquid(liquid_7, 696)
    well_plate_7["H4"].load_liquid(liquid_7, 696)
    well_plate_7["A5"].load_liquid(liquid_7, 696)
    well_plate_7["B5"].load_liquid(liquid_7, 696)
    well_plate_7["C5"].load_liquid(liquid_7, 696)
    well_plate_7["D5"].load_liquid(liquid_7, 696)
    well_plate_7["E5"].load_liquid(liquid_7, 696)
    well_plate_7["F5"].load_liquid(liquid_7, 696)
    well_plate_7["G5"].load_liquid(liquid_7, 696)
    well_plate_7["H5"].load_liquid(liquid_7, 696)
    well_plate_7["A6"].load_liquid(liquid_7, 696)
    well_plate_7["B6"].load_liquid(liquid_7, 696)
    well_plate_7["C6"].load_liquid(liquid_7, 696)
    well_plate_7["D6"].load_liquid(liquid_7, 696)
    well_plate_7["E6"].load_liquid(liquid_7, 696)
    well_plate_7["F6"].load_liquid(liquid_7, 696)
    well_plate_7["G6"].load_liquid(liquid_7, 696)
    well_plate_7["H6"].load_liquid(liquid_7, 696)
    well_plate_7["A7"].load_liquid(liquid_7, 696)
    well_plate_7["B7"].load_liquid(liquid_7, 696)
    well_plate_7["C7"].load_liquid(liquid_7, 696)
    well_plate_7["D7"].load_liquid(liquid_7, 696)
    well_plate_7["E7"].load_liquid(liquid_7, 696)
    well_plate_7["F7"].load_liquid(liquid_7, 696)
    well_plate_7["G7"].load_liquid(liquid_7, 696)
    well_plate_7["H7"].load_liquid(liquid_7, 696)
    well_plate_7["A8"].load_liquid(liquid_7, 696)
    well_plate_7["B8"].load_liquid(liquid_7, 696)
    well_plate_7["C8"].load_liquid(liquid_7, 696)
    well_plate_7["D8"].load_liquid(liquid_7, 696)
    well_plate_7["E8"].load_liquid(liquid_7, 696)
    well_plate_7["F8"].load_liquid(liquid_7, 696)
    well_plate_7["G8"].load_liquid(liquid_7, 696)
    well_plate_7["H8"].load_liquid(liquid_7, 696)
    well_plate_7["A9"].load_liquid(liquid_7, 696)
    well_plate_7["B9"].load_liquid(liquid_7, 696)
    well_plate_7["C9"].load_liquid(liquid_7, 696)
    well_plate_7["D9"].load_liquid(liquid_7, 696)
    well_plate_7["E9"].load_liquid(liquid_7, 696)
    well_plate_7["F9"].load_liquid(liquid_7, 696)
    well_plate_7["G9"].load_liquid(liquid_7, 696)
    well_plate_7["H9"].load_liquid(liquid_7, 696)
    well_plate_7["A10"].load_liquid(liquid_7, 696)
    well_plate_7["B10"].load_liquid(liquid_7, 696)
    well_plate_7["C10"].load_liquid(liquid_7, 696)
    well_plate_7["D10"].load_liquid(liquid_7, 696)
    well_plate_7["E10"].load_liquid(liquid_7, 696)
    well_plate_7["F10"].load_liquid(liquid_7, 696)
    well_plate_7["G10"].load_liquid(liquid_7, 696)
    well_plate_7["H10"].load_liquid(liquid_7, 696)
    well_plate_7["A11"].load_liquid(liquid_7, 696)
    well_plate_7["B11"].load_liquid(liquid_7, 696)
    well_plate_7["C11"].load_liquid(liquid_7, 696)
    well_plate_7["D11"].load_liquid(liquid_7, 696)
    well_plate_7["E11"].load_liquid(liquid_7, 696)
    well_plate_7["F11"].load_liquid(liquid_7, 696)
    well_plate_7["G11"].load_liquid(liquid_7, 696)
    well_plate_7["H11"].load_liquid(liquid_7, 696)
    well_plate_7["A12"].load_liquid(liquid_7, 696)
    well_plate_7["B12"].load_liquid(liquid_7, 696)
    well_plate_7["C12"].load_liquid(liquid_7, 696)
    well_plate_7["D12"].load_liquid(liquid_7, 696)
    well_plate_7["E12"].load_liquid(liquid_7, 696)
    well_plate_7["F12"].load_liquid(liquid_7, 696)
    well_plate_7["G12"].load_liquid(liquid_7, 696)
    well_plate_7["H12"].load_liquid(liquid_7, 696)
    well_plate_8["A1"].load_liquid(liquid_8, 1500)
    well_plate_8["B1"].load_liquid(liquid_8, 1500)
    well_plate_8["C1"].load_liquid(liquid_8, 1500)
    well_plate_8["D1"].load_liquid(liquid_8, 1500)
    well_plate_8["E1"].load_liquid(liquid_8, 1500)
    well_plate_8["F1"].load_liquid(liquid_8, 1500)
    well_plate_8["G1"].load_liquid(liquid_8, 1500)
    well_plate_8["H1"].load_liquid(liquid_8, 1500)
    well_plate_8["A2"].load_liquid(liquid_8, 1500)
    well_plate_8["B2"].load_liquid(liquid_8, 1500)
    well_plate_8["C2"].load_liquid(liquid_8, 1500)
    well_plate_8["D2"].load_liquid(liquid_8, 1500)
    well_plate_8["E2"].load_liquid(liquid_8, 1500)
    well_plate_8["F2"].load_liquid(liquid_8, 1500)
    well_plate_8["G2"].load_liquid(liquid_8, 1500)
    well_plate_8["H2"].load_liquid(liquid_8, 1500)
    well_plate_8["A3"].load_liquid(liquid_8, 1500)
    well_plate_8["B3"].load_liquid(liquid_8, 1500)
    well_plate_8["C3"].load_liquid(liquid_8, 1500)
    well_plate_8["D3"].load_liquid(liquid_8, 1500)
    well_plate_8["E3"].load_liquid(liquid_8, 1500)
    well_plate_8["F3"].load_liquid(liquid_8, 1500)
    well_plate_8["G3"].load_liquid(liquid_8, 1500)
    well_plate_8["H3"].load_liquid(liquid_8, 1500)
    well_plate_8["A4"].load_liquid(liquid_8, 1500)
    well_plate_8["B4"].load_liquid(liquid_8, 1500)
    well_plate_8["C4"].load_liquid(liquid_8, 1500)
    well_plate_8["D4"].load_liquid(liquid_8, 1500)
    well_plate_8["E4"].load_liquid(liquid_8, 1500)
    well_plate_8["F4"].load_liquid(liquid_8, 1500)
    well_plate_8["G4"].load_liquid(liquid_8, 1500)
    well_plate_8["H4"].load_liquid(liquid_8, 1500)
    well_plate_8["A5"].load_liquid(liquid_8, 1500)
    well_plate_8["B5"].load_liquid(liquid_8, 1500)
    well_plate_8["C5"].load_liquid(liquid_8, 1500)
    well_plate_8["D5"].load_liquid(liquid_8, 1500)
    well_plate_8["E5"].load_liquid(liquid_8, 1500)
    well_plate_8["F5"].load_liquid(liquid_8, 1500)
    well_plate_8["G5"].load_liquid(liquid_8, 1500)
    well_plate_8["H5"].load_liquid(liquid_8, 1500)
    well_plate_8["A6"].load_liquid(liquid_8, 1500)
    well_plate_8["B6"].load_liquid(liquid_8, 1500)
    well_plate_8["C6"].load_liquid(liquid_8, 1500)
    well_plate_8["D6"].load_liquid(liquid_8, 1500)
    well_plate_8["E6"].load_liquid(liquid_8, 1500)
    well_plate_8["F6"].load_liquid(liquid_8, 1500)
    well_plate_8["G6"].load_liquid(liquid_8, 1500)
    well_plate_8["H6"].load_liquid(liquid_8, 1500)
    well_plate_8["A7"].load_liquid(liquid_8, 1500)
    well_plate_8["B7"].load_liquid(liquid_8, 1500)
    well_plate_8["C7"].load_liquid(liquid_8, 1500)
    well_plate_8["D7"].load_liquid(liquid_8, 1500)
    well_plate_8["E7"].load_liquid(liquid_8, 1500)
    well_plate_8["F7"].load_liquid(liquid_8, 1500)
    well_plate_8["G7"].load_liquid(liquid_8, 1500)
    well_plate_8["H7"].load_liquid(liquid_8, 1500)
    well_plate_8["A8"].load_liquid(liquid_8, 1500)
    well_plate_8["B8"].load_liquid(liquid_8, 1500)
    well_plate_8["C8"].load_liquid(liquid_8, 1500)
    well_plate_8["D8"].load_liquid(liquid_8, 1500)
    well_plate_8["E8"].load_liquid(liquid_8, 1500)
    well_plate_8["F8"].load_liquid(liquid_8, 1500)
    well_plate_8["G8"].load_liquid(liquid_8, 1500)
    well_plate_8["H8"].load_liquid(liquid_8, 1500)
    well_plate_8["A9"].load_liquid(liquid_8, 1500)
    well_plate_8["B9"].load_liquid(liquid_8, 1500)
    well_plate_8["C9"].load_liquid(liquid_8, 1500)
    well_plate_8["D9"].load_liquid(liquid_8, 1500)
    well_plate_8["E9"].load_liquid(liquid_8, 1500)
    well_plate_8["F9"].load_liquid(liquid_8, 1500)
    well_plate_8["G9"].load_liquid(liquid_8, 1500)
    well_plate_8["H9"].load_liquid(liquid_8, 1500)
    well_plate_8["A10"].load_liquid(liquid_8, 1500)
    well_plate_8["B10"].load_liquid(liquid_8, 1500)
    well_plate_8["C10"].load_liquid(liquid_8, 1500)
    well_plate_8["D10"].load_liquid(liquid_8, 1500)
    well_plate_8["E10"].load_liquid(liquid_8, 1500)
    well_plate_8["F10"].load_liquid(liquid_8, 1500)
    well_plate_8["G10"].load_liquid(liquid_8, 1500)
    well_plate_8["H10"].load_liquid(liquid_8, 1500)
    well_plate_8["A11"].load_liquid(liquid_8, 1500)
    well_plate_8["B11"].load_liquid(liquid_8, 1500)
    well_plate_8["C11"].load_liquid(liquid_8, 1500)
    well_plate_8["D11"].load_liquid(liquid_8, 1500)
    well_plate_8["E11"].load_liquid(liquid_8, 1500)
    well_plate_8["F11"].load_liquid(liquid_8, 1500)
    well_plate_8["G11"].load_liquid(liquid_8, 1500)
    well_plate_8["H11"].load_liquid(liquid_8, 1500)
    well_plate_8["A12"].load_liquid(liquid_8, 1500)
    well_plate_8["B12"].load_liquid(liquid_8, 1500)
    well_plate_8["C12"].load_liquid(liquid_8, 1500)
    well_plate_8["D12"].load_liquid(liquid_8, 1500)
    well_plate_8["E12"].load_liquid(liquid_8, 1500)
    well_plate_8["F12"].load_liquid(liquid_8, 1500)
    well_plate_8["G12"].load_liquid(liquid_8, 1500)
    well_plate_8["H12"].load_liquid(liquid_8, 1500)

    # PROTOCOL STEPS

    # Step 1:
    heater_shaker_module_1.close_labware_latch()
    heater_shaker_module_1.deactivate_heater()

    # Step 2:
    pipette.configure_nozzle_layout(protocol_api.ALL)
    pipette.pick_up_tip(location=tip_rack_1)
    pipette.move_to(well_plate_6["A1"].top(z=2))
    pipette.prepare_to_aspirate()
    pipette.move_to(well_plate_6["A1"].top(z=2))
    pipette.move_to(well_plate_6["A1"].bottom(), speed=35)
    pipette.aspirate(volume=220, flow_rate=160)
    pipette.move_to(well_plate_6["A1"].top(z=2), speed=35)
    pipette.air_gap(volume=20, in_place=True, flow_rate=160)
    pipette.move_to(well_plate_8["A1"].top(z=2))
    pipette.dispense(volume=20, flow_rate=160, push_out=0)
    pipette.move_to(well_plate_8["A1"].bottom(), speed=35)
    pipette.dispense(volume=220, flow_rate=160, push_out=20)
    pipette.move_to(well_plate_8["A1"].top(z=2), speed=35)

    # Step 3:
    pipette.mix(
        repetitions=8,
        volume=198,
        location=well_plate_8["A1"].bottom(z=1),
        aspirate_flow_rate=150,
        dispense_flow_rate=150,
        final_push_out=20,
    )
    pipette.drop_tip(waste_chute)

    # Step 4:
    heater_shaker_module_1.close_labware_latch()
    heater_shaker_module_1.deactivate_heater()
    heater_shaker_module_1.set_and_wait_for_shake_speed(2000)
    protocol.delay(seconds=1800)
    heater_shaker_module_1.deactivate_shaker()
    heater_shaker_module_1.deactivate_heater()

DESIGNER_APPLICATION = """{"robot":{"model":"OT-3 Standard"},"designerApplication":{"name":"opentrons/protocol-designer","version":"8.5.0","data":{"pipetteTiprackAssignments":{"88bd044e-beef-455e-9a9d-2ef2c0dac83e":["opentrons/opentrons_flex_96_tiprack_1000ul/1"]},"dismissedWarnings":{"form":[],"timeline":["LABWARE_IN_WASTE_CHUTE_HAS_LIQUID"]},"ingredients":{"0":{"displayName":"Elution Buffer","description":"","liquidGroupId":"0","displayColor":"#ff4f4fff","liquidClass":null},"1":{"displayName":"Wash 1","description":"","liquidGroupId":"1","displayColor":"#0025ffff","liquidClass":null},"2":{"displayName":"Wash 2","description":"","liquidGroupId":"2","displayColor":"#850cbeff","liquidClass":null},"3":{"displayName":"Wash 3","description":"","liquidGroupId":"3","displayColor":"#9dfff0ff","liquidClass":null},"4":{"displayName":"Binding 2","description":"","liquidGroupId":"4","displayColor":"#50d5ffc2","liquidClass":null},"5":{"displayName":"Lysis","description":"","liquidGroupId":"5","displayColor":"#5aad31ff","liquidClass":null},"6":{"displayName":"Binding and beading ","description":"","liquidGroupId":"6","displayColor":"#a50d0dff","liquidClass":null},"7":{"displayName":"Good Stuff","description":null,"liquidGroupId":"7","displayColor":"#ff4f4f","liquidClass":null}},"ingredLocations":{"40f50c87-c1e1-4944-8b79-cd47b1dbfa59:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2":{"A1":{"0":{"volume":80}},"B1":{"0":{"volume":80}},"C1":{"0":{"volume":80}},"D1":{"0":{"volume":80}},"E1":{"0":{"volume":80}},"F1":{"0":{"volume":80}},"G1":{"0":{"volume":80}},"H1":{"0":{"volume":80}},"A2":{"0":{"volume":80}},"B2":{"0":{"volume":80}},"C2":{"0":{"volume":80}},"D2":{"0":{"volume":80}},"E2":{"0":{"volume":80}},"F2":{"0":{"volume":80}},"G2":{"0":{"volume":80}},"H2":{"0":{"volume":80}},"A3":{"0":{"volume":80}},"B3":{"0":{"volume":80}},"C3":{"0":{"volume":80}},"D3":{"0":{"volume":80}},"E3":{"0":{"volume":80}},"F3":{"0":{"volume":80}},"G3":{"0":{"volume":80}},"H3":{"0":{"volume":80}},"A4":{"0":{"volume":80}},"B4":{"0":{"volume":80}},"C4":{"0":{"volume":80}},"D4":{"0":{"volume":80}},"E4":{"0":{"volume":80}},"F4":{"0":{"volume":80}},"G4":{"0":{"volume":80}},"H4":{"0":{"volume":80}},"A5":{"0":{"volume":80}},"B5":{"0":{"volume":80}},"C5":{"0":{"volume":80}},"D5":{"0":{"volume":80}},"E5":{"0":{"volume":80}},"F5":{"0":{"volume":80}},"G5":{"0":{"volume":80}},"H5":{"0":{"volume":80}},"A6":{"0":{"volume":80}},"B6":{"0":{"volume":80}},"C6":{"0":{"volume":80}},"D6":{"0":{"volume":80}},"E6":{"0":{"volume":80}},"F6":{"0":{"volume":80}},"G6":{"0":{"volume":80}},"H6":{"0":{"volume":80}},"A7":{"0":{"volume":80}},"B7":{"0":{"volume":80}},"C7":{"0":{"volume":80}},"D7":{"0":{"volume":80}},"E7":{"0":{"volume":80}},"F7":{"0":{"volume":80}},"G7":{"0":{"volume":80}},"H7":{"0":{"volume":80}},"A8":{"0":{"volume":80}},"B8":{"0":{"volume":80}},"C8":{"0":{"volume":80}},"D8":{"0":{"volume":80}},"E8":{"0":{"volume":80}},"F8":{"0":{"volume":80}},"G8":{"0":{"volume":80}},"H8":{"0":{"volume":80}},"A9":{"0":{"volume":80}},"B9":{"0":{"volume":80}},"C9":{"0":{"volume":80}},"D9":{"0":{"volume":80}},"E9":{"0":{"volume":80}},"F9":{"0":{"volume":80}},"G9":{"0":{"volume":80}},"H9":{"0":{"volume":80}},"A10":{"0":{"volume":80}},"B10":{"0":{"volume":80}},"C10":{"0":{"volume":80}},"D10":{"0":{"volume":80}},"E10":{"0":{"volume":80}},"F10":{"0":{"volume":80}},"G10":{"0":{"volume":80}},"H10":{"0":{"volume":80}},"A11":{"0":{"volume":80}},"B11":{"0":{"volume":80}},"C11":{"0":{"volume":80}},"D11":{"0":{"volume":80}},"E11":{"0":{"volume":80}},"F11":{"0":{"volume":80}},"G11":{"0":{"volume":80}},"H11":{"0":{"volume":80}},"A12":{"0":{"volume":80}},"B12":{"0":{"volume":80}},"C12":{"0":{"volume":80}},"D12":{"0":{"volume":80}},"E12":{"0":{"volume":80}},"F12":{"0":{"volume":80}},"G12":{"0":{"volume":80}},"H12":{"0":{"volume":80}}},"812212f1-6284-4b62-bc76-f66c6d8c2ff9:opentrons/nest_96_wellplate_2ml_deep/2":{"A1":{"4":{"volume":600}},"B1":{"4":{"volume":600}},"C1":{"4":{"volume":600}},"D1":{"4":{"volume":600}},"E1":{"4":{"volume":600}},"F1":{"4":{"volume":600}},"G1":{"4":{"volume":600}},"H1":{"4":{"volume":600}},"A2":{"4":{"volume":600}},"B2":{"4":{"volume":600}},"C2":{"4":{"volume":600}},"D2":{"4":{"volume":600}},"E2":{"4":{"volume":600}},"F2":{"4":{"volume":600}},"G2":{"4":{"volume":600}},"H2":{"4":{"volume":600}},"A3":{"4":{"volume":600}},"B3":{"4":{"volume":600}},"C3":{"4":{"volume":600}},"D3":{"4":{"volume":600}},"E3":{"4":{"volume":600}},"F3":{"4":{"volume":600}},"G3":{"4":{"volume":600}},"H3":{"4":{"volume":600}},"A4":{"4":{"volume":600}},"B4":{"4":{"volume":600}},"C4":{"4":{"volume":600}},"D4":{"4":{"volume":600}},"E4":{"4":{"volume":600}},"F4":{"4":{"volume":600}},"G4":{"4":{"volume":600}},"H4":{"4":{"volume":600}},"A5":{"4":{"volume":600}},"B5":{"4":{"volume":600}},"C5":{"4":{"volume":600}},"D5":{"4":{"volume":600}},"E5":{"4":{"volume":600}},"F5":{"4":{"volume":600}},"G5":{"4":{"volume":600}},"H5":{"4":{"volume":600}},"A6":{"4":{"volume":600}},"B6":{"4":{"volume":600}},"C6":{"4":{"volume":600}},"D6":{"4":{"volume":600}},"E6":{"4":{"volume":600}},"F6":{"4":{"volume":600}},"G6":{"4":{"volume":600}},"H6":{"4":{"volume":600}},"A7":{"4":{"volume":600}},"B7":{"4":{"volume":600}},"C7":{"4":{"volume":600}},"D7":{"4":{"volume":600}},"E7":{"4":{"volume":600}},"F7":{"4":{"volume":600}},"G7":{"4":{"volume":600}},"H7":{"4":{"volume":600}},"A8":{"4":{"volume":600}},"B8":{"4":{"volume":600}},"C8":{"4":{"volume":600}},"D8":{"4":{"volume":600}},"E8":{"4":{"volume":600}},"F8":{"4":{"volume":600}},"G8":{"4":{"volume":600}},"H8":{"4":{"volume":600}},"A9":{"4":{"volume":600}},"B9":{"4":{"volume":600}},"C9":{"4":{"volume":600}},"D9":{"4":{"volume":600}},"E9":{"4":{"volume":600}},"F9":{"4":{"volume":600}},"G9":{"4":{"volume":600}},"H9":{"4":{"volume":600}},"A10":{"4":{"volume":600}},"B10":{"4":{"volume":600}},"C10":{"4":{"volume":600}},"D10":{"4":{"volume":600}},"E10":{"4":{"volume":600}},"F10":{"4":{"volume":600}},"G10":{"4":{"volume":600}},"H10":{"4":{"volume":600}},"A11":{"4":{"volume":600}},"B11":{"4":{"volume":600}},"C11":{"4":{"volume":600}},"D11":{"4":{"volume":600}},"E11":{"4":{"volume":600}},"F11":{"4":{"volume":600}},"G11":{"4":{"volume":600}},"H11":{"4":{"volume":600}},"A12":{"4":{"volume":600}},"B12":{"4":{"volume":600}},"C12":{"4":{"volume":600}},"D12":{"4":{"volume":600}},"E12":{"4":{"volume":600}},"F12":{"4":{"volume":600}},"G12":{"4":{"volume":600}},"H12":{"4":{"volume":600}}},"a18a9f6c-551e-4a06-bd74-070c1209c7ae:opentrons/nest_96_wellplate_2ml_deep/2":{"A1":{"1":{"volume":600}},"B1":{"1":{"volume":600}},"C1":{"1":{"volume":600}},"D1":{"1":{"volume":600}},"E1":{"1":{"volume":600}},"F1":{"1":{"volume":600}},"G1":{"1":{"volume":600}},"H1":{"1":{"volume":600}},"A2":{"1":{"volume":600}},"B2":{"1":{"volume":600}},"C2":{"1":{"volume":600}},"D2":{"1":{"volume":600}},"E2":{"1":{"volume":600}},"F2":{"1":{"volume":600}},"G2":{"1":{"volume":600}},"H2":{"1":{"volume":600}},"A3":{"1":{"volume":600}},"B3":{"1":{"volume":600}},"C3":{"1":{"volume":600}},"D3":{"1":{"volume":600}},"E3":{"1":{"volume":600}},"F3":{"1":{"volume":600}},"G3":{"1":{"volume":600}},"H3":{"1":{"volume":600}},"A4":{"1":{"volume":600}},"B4":{"1":{"volume":600}},"C4":{"1":{"volume":600}},"D4":{"1":{"volume":600}},"E4":{"1":{"volume":600}},"F4":{"1":{"volume":600}},"G4":{"1":{"volume":600}},"H4":{"1":{"volume":600}},"A5":{"1":{"volume":600}},"B5":{"1":{"volume":600}},"C5":{"1":{"volume":600}},"D5":{"1":{"volume":600}},"E5":{"1":{"volume":600}},"F5":{"1":{"volume":600}},"G5":{"1":{"volume":600}},"H5":{"1":{"volume":600}},"A6":{"1":{"volume":600}},"B6":{"1":{"volume":600}},"C6":{"1":{"volume":600}},"D6":{"1":{"volume":600}},"E6":{"1":{"volume":600}},"F6":{"1":{"volume":600}},"G6":{"1":{"volume":600}},"H6":{"1":{"volume":600}},"A7":{"1":{"volume":600}},"B7":{"1":{"volume":600}},"C7":{"1":{"volume":600}},"D7":{"1":{"volume":600}},"E7":{"1":{"volume":600}},"F7":{"1":{"volume":600}},"G7":{"1":{"volume":600}},"H7":{"1":{"volume":600}},"A8":{"1":{"volume":600}},"B8":{"1":{"volume":600}},"C8":{"1":{"volume":600}},"D8":{"1":{"volume":600}},"E8":{"1":{"volume":600}},"F8":{"1":{"volume":600}},"G8":{"1":{"volume":600}},"H8":{"1":{"volume":600}},"A9":{"1":{"volume":600}},"B9":{"1":{"volume":600}},"C9":{"1":{"volume":600}},"D9":{"1":{"volume":600}},"E9":{"1":{"volume":600}},"F9":{"1":{"volume":600}},"G9":{"1":{"volume":600}},"H9":{"1":{"volume":600}},"A10":{"1":{"volume":600}},"B10":{"1":{"volume":600}},"C10":{"1":{"volume":600}},"D10":{"1":{"volume":600}},"E10":{"1":{"volume":600}},"F10":{"1":{"volume":600}},"G10":{"1":{"volume":600}},"H10":{"1":{"volume":600}},"A11":{"1":{"volume":600}},"B11":{"1":{"volume":600}},"C11":{"1":{"volume":600}},"D11":{"1":{"volume":600}},"E11":{"1":{"volume":600}},"F11":{"1":{"volume":600}},"G11":{"1":{"volume":600}},"H11":{"1":{"volume":600}},"A12":{"1":{"volume":600}},"B12":{"1":{"volume":600}},"C12":{"1":{"volume":600}},"D12":{"1":{"volume":600}},"E12":{"1":{"volume":600}},"F12":{"1":{"volume":600}},"G12":{"1":{"volume":600}},"H12":{"1":{"volume":600}}},"591b398c-7c32-4f1e-b6aa-2b242d8a1c4e:opentrons/nest_96_wellplate_2ml_deep/2":{"A1":{"2":{"volume":1900}},"B1":{"2":{"volume":1900}},"C1":{"2":{"volume":1900}},"D1":{"2":{"volume":1900}},"E1":{"2":{"volume":1900}},"F1":{"2":{"volume":1900}},"G1":{"2":{"volume":1900}},"H1":{"2":{"volume":1900}},"A2":{"2":{"volume":1900}},"B2":{"2":{"volume":1900}},"C2":{"2":{"volume":1900}},"D2":{"2":{"volume":1900}},"E2":{"2":{"volume":1900}},"F2":{"2":{"volume":1900}},"G2":{"2":{"volume":1900}},"H2":{"2":{"volume":1900}},"A3":{"2":{"volume":1900}},"B3":{"2":{"volume":1900}},"C3":{"2":{"volume":1900}},"D3":{"2":{"volume":1900}},"E3":{"2":{"volume":1900}},"F3":{"2":{"volume":1900}},"G3":{"2":{"volume":1900}},"H3":{"2":{"volume":1900}},"A4":{"2":{"volume":1900}},"B4":{"2":{"volume":1900}},"C4":{"2":{"volume":1900}},"D4":{"2":{"volume":1900}},"E4":{"2":{"volume":1900}},"F4":{"2":{"volume":1900}},"G4":{"2":{"volume":1900}},"H4":{"2":{"volume":1900}},"A5":{"2":{"volume":1900}},"B5":{"2":{"volume":1900}},"C5":{"2":{"volume":1900}},"D5":{"2":{"volume":1900}},"E5":{"2":{"volume":1900}},"F5":{"2":{"volume":1900}},"G5":{"2":{"volume":1900}},"H5":{"2":{"volume":1900}},"A6":{"2":{"volume":1900}},"B6":{"2":{"volume":1900}},"C6":{"2":{"volume":1900}},"D6":{"2":{"volume":1900}},"E6":{"2":{"volume":1900}},"F6":{"2":{"volume":1900}},"G6":{"2":{"volume":1900}},"H6":{"2":{"volume":1900}},"A7":{"2":{"volume":1900}},"B7":{"2":{"volume":1900}},"C7":{"2":{"volume":1900}},"D7":{"2":{"volume":1900}},"E7":{"2":{"volume":1900}},"F7":{"2":{"volume":1900}},"G7":{"2":{"volume":1900}},"H7":{"2":{"volume":1900}},"A8":{"2":{"volume":1900}},"B8":{"2":{"volume":1900}},"C8":{"2":{"volume":1900}},"D8":{"2":{"volume":1900}},"E8":{"2":{"volume":1900}},"F8":{"2":{"volume":1900}},"G8":{"2":{"volume":1900}},"H8":{"2":{"volume":1900}},"A9":{"2":{"volume":1900}},"B9":{"2":{"volume":1900}},"C9":{"2":{"volume":1900}},"D9":{"2":{"volume":1900}},"E9":{"2":{"volume":1900}},"F9":{"2":{"volume":1900}},"G9":{"2":{"volume":1900}},"H9":{"2":{"volume":1900}},"A10":{"2":{"volume":1900}},"B10":{"2":{"volume":1900}},"C10":{"2":{"volume":1900}},"D10":{"2":{"volume":1900}},"E10":{"2":{"volume":1900}},"F10":{"2":{"volume":1900}},"G10":{"2":{"volume":1900}},"H10":{"2":{"volume":1900}},"A11":{"2":{"volume":1900}},"B11":{"2":{"volume":1900}},"C11":{"2":{"volume":1900}},"D11":{"2":{"volume":1900}},"E11":{"2":{"volume":1900}},"F11":{"2":{"volume":1900}},"G11":{"2":{"volume":1900}},"H11":{"2":{"volume":1900}},"A12":{"2":{"volume":1900}},"B12":{"2":{"volume":1900}},"C12":{"2":{"volume":1900}},"D12":{"2":{"volume":1900}},"E12":{"2":{"volume":1900}},"F12":{"2":{"volume":1900}},"G12":{"2":{"volume":1900}},"H12":{"2":{"volume":1900}}},"d4110d80-d905-434b-8b55-b15c6e2d4cfe:opentrons/nest_96_wellplate_2ml_deep/2":{"A1":{"3":{"volume":1000}},"B1":{"3":{"volume":1000}},"C1":{"3":{"volume":1000}},"D1":{"3":{"volume":1000}},"E1":{"3":{"volume":1000}},"F1":{"3":{"volume":1000}},"G1":{"3":{"volume":1000}},"H1":{"3":{"volume":1000}},"A2":{"3":{"volume":1000}},"B2":{"3":{"volume":1000}},"C2":{"3":{"volume":1000}},"D2":{"3":{"volume":1000}},"E2":{"3":{"volume":1000}},"F2":{"3":{"volume":1000}},"G2":{"3":{"volume":1000}},"H2":{"3":{"volume":1000}},"A3":{"3":{"volume":1000}},"B3":{"3":{"volume":1000}},"C3":{"3":{"volume":1000}},"D3":{"3":{"volume":1000}},"E3":{"3":{"volume":1000}},"F3":{"3":{"volume":1000}},"G3":{"3":{"volume":1000}},"H3":{"3":{"volume":1000}},"A4":{"3":{"volume":1000}},"B4":{"3":{"volume":1000}},"C4":{"3":{"volume":1000}},"D4":{"3":{"volume":1000}},"E4":{"3":{"volume":1000}},"F4":{"3":{"volume":1000}},"G4":{"3":{"volume":1000}},"H4":{"3":{"volume":1000}},"A5":{"3":{"volume":1000}},"B5":{"3":{"volume":1000}},"C5":{"3":{"volume":1000}},"D5":{"3":{"volume":1000}},"E5":{"3":{"volume":1000}},"F5":{"3":{"volume":1000}},"G5":{"3":{"volume":1000}},"H5":{"3":{"volume":1000}},"A6":{"3":{"volume":1000}},"B6":{"3":{"volume":1000}},"C6":{"3":{"volume":1000}},"D6":{"3":{"volume":1000}},"E6":{"3":{"volume":1000}},"F6":{"3":{"volume":1000}},"G6":{"3":{"volume":1000}},"H6":{"3":{"volume":1000}},"A7":{"3":{"volume":1000}},"B7":{"3":{"volume":1000}},"C7":{"3":{"volume":1000}},"D7":{"3":{"volume":1000}},"E7":{"3":{"volume":1000}},"F7":{"3":{"volume":1000}},"G7":{"3":{"volume":1000}},"H7":{"3":{"volume":1000}},"A8":{"3":{"volume":1000}},"B8":{"3":{"volume":1000}},"C8":{"3":{"volume":1000}},"D8":{"3":{"volume":1000}},"E8":{"3":{"volume":1000}},"F8":{"3":{"volume":1000}},"G8":{"3":{"volume":1000}},"H8":{"3":{"volume":1000}},"A9":{"3":{"volume":1000}},"B9":{"3":{"volume":1000}},"C9":{"3":{"volume":1000}},"D9":{"3":{"volume":1000}},"E9":{"3":{"volume":1000}},"F9":{"3":{"volume":1000}},"G9":{"3":{"volume":1000}},"H9":{"3":{"volume":1000}},"A10":{"3":{"volume":1000}},"B10":{"3":{"volume":1000}},"C10":{"3":{"volume":1000}},"D10":{"3":{"volume":1000}},"E10":{"3":{"volume":1000}},"F10":{"3":{"volume":1000}},"G10":{"3":{"volume":1000}},"H10":{"3":{"volume":1000}},"A11":{"3":{"volume":1000}},"B11":{"3":{"volume":1000}},"C11":{"3":{"volume":1000}},"D11":{"3":{"volume":1000}},"E11":{"3":{"volume":1000}},"F11":{"3":{"volume":1000}},"G11":{"3":{"volume":1000}},"H11":{"3":{"volume":1000}},"A12":{"3":{"volume":1000}},"B12":{"3":{"volume":1000}},"C12":{"3":{"volume":1000}},"D12":{"3":{"volume":1000}},"E12":{"3":{"volume":1000}},"F12":{"3":{"volume":1000}},"G12":{"3":{"volume":1000}},"H12":{"3":{"volume":1000}}},"34d93400-0e5b-4698-bd38-85b39add8cb2:opentrons/nest_96_wellplate_2ml_deep/2":{"A1":{"5":{"volume":291}},"B1":{"5":{"volume":291}},"C1":{"5":{"volume":291}},"D1":{"5":{"volume":291}},"E1":{"5":{"volume":291}},"F1":{"5":{"volume":291}},"G1":{"5":{"volume":291}},"H1":{"5":{"volume":291}},"A2":{"5":{"volume":291}},"B2":{"5":{"volume":291}},"C2":{"5":{"volume":291}},"D2":{"5":{"volume":291}},"E2":{"5":{"volume":291}},"F2":{"5":{"volume":291}},"G2":{"5":{"volume":291}},"H2":{"5":{"volume":291}},"A3":{"5":{"volume":291}},"B3":{"5":{"volume":291}},"C3":{"5":{"volume":291}},"D3":{"5":{"volume":291}},"E3":{"5":{"volume":291}},"F3":{"5":{"volume":291}},"G3":{"5":{"volume":291}},"H3":{"5":{"volume":291}},"A4":{"5":{"volume":291}},"B4":{"5":{"volume":291}},"C4":{"5":{"volume":291}},"D4":{"5":{"volume":291}},"E4":{"5":{"volume":291}},"F4":{"5":{"volume":291}},"G4":{"5":{"volume":291}},"H4":{"5":{"volume":291}},"A5":{"5":{"volume":291}},"B5":{"5":{"volume":291}},"C5":{"5":{"volume":291}},"D5":{"5":{"volume":291}},"E5":{"5":{"volume":291}},"F5":{"5":{"volume":291}},"G5":{"5":{"volume":291}},"H5":{"5":{"volume":291}},"A6":{"5":{"volume":291}},"B6":{"5":{"volume":291}},"C6":{"5":{"volume":291}},"D6":{"5":{"volume":291}},"E6":{"5":{"volume":291}},"F6":{"5":{"volume":291}},"G6":{"5":{"volume":291}},"H6":{"5":{"volume":291}},"A7":{"5":{"volume":291}},"B7":{"5":{"volume":291}},"C7":{"5":{"volume":291}},"D7":{"5":{"volume":291}},"E7":{"5":{"volume":291}},"F7":{"5":{"volume":291}},"G7":{"5":{"volume":291}},"H7":{"5":{"volume":291}},"A8":{"5":{"volume":291}},"B8":{"5":{"volume":291}},"C8":{"5":{"volume":291}},"D8":{"5":{"volume":291}},"E8":{"5":{"volume":291}},"F8":{"5":{"volume":291}},"G8":{"5":{"volume":291}},"H8":{"5":{"volume":291}},"A9":{"5":{"volume":291}},"B9":{"5":{"volume":291}},"C9":{"5":{"volume":291}},"D9":{"5":{"volume":291}},"E9":{"5":{"volume":291}},"F9":{"5":{"volume":291}},"G9":{"5":{"volume":291}},"H9":{"5":{"volume":291}},"A10":{"5":{"volume":291}},"B10":{"5":{"volume":291}},"C10":{"5":{"volume":291}},"D10":{"5":{"volume":291}},"E10":{"5":{"volume":291}},"F10":{"5":{"volume":291}},"G10":{"5":{"volume":291}},"H10":{"5":{"volume":291}},"A11":{"5":{"volume":291}},"B11":{"5":{"volume":291}},"C11":{"5":{"volume":291}},"D11":{"5":{"volume":291}},"E11":{"5":{"volume":291}},"F11":{"5":{"volume":291}},"G11":{"5":{"volume":291}},"H11":{"5":{"volume":291}},"A12":{"5":{"volume":291}},"B12":{"5":{"volume":291}},"C12":{"5":{"volume":291}},"D12":{"5":{"volume":291}},"E12":{"5":{"volume":291}},"F12":{"5":{"volume":291}},"G12":{"5":{"volume":291}},"H12":{"5":{"volume":291}}},"b5696d32-aa10-4188-b9f0-bd40fbf1ab0b:opentrons/nest_96_wellplate_2ml_deep/2":{"A1":{"6":{"volume":696}},"B1":{"6":{"volume":696}},"C1":{"6":{"volume":696}},"D1":{"6":{"volume":696}},"E1":{"6":{"volume":696}},"F1":{"6":{"volume":696}},"G1":{"6":{"volume":696}},"H1":{"6":{"volume":696}},"A2":{"6":{"volume":696}},"B2":{"6":{"volume":696}},"C2":{"6":{"volume":696}},"D2":{"6":{"volume":696}},"E2":{"6":{"volume":696}},"F2":{"6":{"volume":696}},"G2":{"6":{"volume":696}},"H2":{"6":{"volume":696}},"A3":{"6":{"volume":696}},"B3":{"6":{"volume":696}},"C3":{"6":{"volume":696}},"D3":{"6":{"volume":696}},"E3":{"6":{"volume":696}},"F3":{"6":{"volume":696}},"G3":{"6":{"volume":696}},"H3":{"6":{"volume":696}},"A4":{"6":{"volume":696}},"B4":{"6":{"volume":696}},"C4":{"6":{"volume":696}},"D4":{"6":{"volume":696}},"E4":{"6":{"volume":696}},"F4":{"6":{"volume":696}},"G4":{"6":{"volume":696}},"H4":{"6":{"volume":696}},"A5":{"6":{"volume":696}},"B5":{"6":{"volume":696}},"C5":{"6":{"volume":696}},"D5":{"6":{"volume":696}},"E5":{"6":{"volume":696}},"F5":{"6":{"volume":696}},"G5":{"6":{"volume":696}},"H5":{"6":{"volume":696}},"A6":{"6":{"volume":696}},"B6":{"6":{"volume":696}},"C6":{"6":{"volume":696}},"D6":{"6":{"volume":696}},"E6":{"6":{"volume":696}},"F6":{"6":{"volume":696}},"G6":{"6":{"volume":696}},"H6":{"6":{"volume":696}},"A7":{"6":{"volume":696}},"B7":{"6":{"volume":696}},"C7":{"6":{"volume":696}},"D7":{"6":{"volume":696}},"E7":{"6":{"volume":696}},"F7":{"6":{"volume":696}},"G7":{"6":{"volume":696}},"H7":{"6":{"volume":696}},"A8":{"6":{"volume":696}},"B8":{"6":{"volume":696}},"C8":{"6":{"volume":696}},"D8":{"6":{"volume":696}},"E8":{"6":{"volume":696}},"F8":{"6":{"volume":696}},"G8":{"6":{"volume":696}},"H8":{"6":{"volume":696}},"A9":{"6":{"volume":696}},"B9":{"6":{"volume":696}},"C9":{"6":{"volume":696}},"D9":{"6":{"volume":696}},"E9":{"6":{"volume":696}},"F9":{"6":{"volume":696}},"G9":{"6":{"volume":696}},"H9":{"6":{"volume":696}},"A10":{"6":{"volume":696}},"B10":{"6":{"volume":696}},"C10":{"6":{"volume":696}},"D10":{"6":{"volume":696}},"E10":{"6":{"volume":696}},"F10":{"6":{"volume":696}},"G10":{"6":{"volume":696}},"H10":{"6":{"volume":696}},"A11":{"6":{"volume":696}},"B11":{"6":{"volume":696}},"C11":{"6":{"volume":696}},"D11":{"6":{"volume":696}},"E11":{"6":{"volume":696}},"F11":{"6":{"volume":696}},"G11":{"6":{"volume":696}},"H11":{"6":{"volume":696}},"A12":{"6":{"volume":696}},"B12":{"6":{"volume":696}},"C12":{"6":{"volume":696}},"D12":{"6":{"volume":696}},"E12":{"6":{"volume":696}},"F12":{"6":{"volume":696}},"G12":{"6":{"volume":696}},"H12":{"6":{"volume":696}}},"fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2":{"A1":{"7":{"volume":1500}},"B1":{"7":{"volume":1500}},"C1":{"7":{"volume":1500}},"D1":{"7":{"volume":1500}},"E1":{"7":{"volume":1500}},"F1":{"7":{"volume":1500}},"G1":{"7":{"volume":1500}},"H1":{"7":{"volume":1500}},"A2":{"7":{"volume":1500}},"B2":{"7":{"volume":1500}},"C2":{"7":{"volume":1500}},"D2":{"7":{"volume":1500}},"E2":{"7":{"volume":1500}},"F2":{"7":{"volume":1500}},"G2":{"7":{"volume":1500}},"H2":{"7":{"volume":1500}},"A3":{"7":{"volume":1500}},"B3":{"7":{"volume":1500}},"C3":{"7":{"volume":1500}},"D3":{"7":{"volume":1500}},"E3":{"7":{"volume":1500}},"F3":{"7":{"volume":1500}},"G3":{"7":{"volume":1500}},"H3":{"7":{"volume":1500}},"A4":{"7":{"volume":1500}},"B4":{"7":{"volume":1500}},"C4":{"7":{"volume":1500}},"D4":{"7":{"volume":1500}},"E4":{"7":{"volume":1500}},"F4":{"7":{"volume":1500}},"G4":{"7":{"volume":1500}},"H4":{"7":{"volume":1500}},"A5":{"7":{"volume":1500}},"B5":{"7":{"volume":1500}},"C5":{"7":{"volume":1500}},"D5":{"7":{"volume":1500}},"E5":{"7":{"volume":1500}},"F5":{"7":{"volume":1500}},"G5":{"7":{"volume":1500}},"H5":{"7":{"volume":1500}},"A6":{"7":{"volume":1500}},"B6":{"7":{"volume":1500}},"C6":{"7":{"volume":1500}},"D6":{"7":{"volume":1500}},"E6":{"7":{"volume":1500}},"F6":{"7":{"volume":1500}},"G6":{"7":{"volume":1500}},"H6":{"7":{"volume":1500}},"A7":{"7":{"volume":1500}},"B7":{"7":{"volume":1500}},"C7":{"7":{"volume":1500}},"D7":{"7":{"volume":1500}},"E7":{"7":{"volume":1500}},"F7":{"7":{"volume":1500}},"G7":{"7":{"volume":1500}},"H7":{"7":{"volume":1500}},"A8":{"7":{"volume":1500}},"B8":{"7":{"volume":1500}},"C8":{"7":{"volume":1500}},"D8":{"7":{"volume":1500}},"E8":{"7":{"volume":1500}},"F8":{"7":{"volume":1500}},"G8":{"7":{"volume":1500}},"H8":{"7":{"volume":1500}},"A9":{"7":{"volume":1500}},"B9":{"7":{"volume":1500}},"C9":{"7":{"volume":1500}},"D9":{"7":{"volume":1500}},"E9":{"7":{"volume":1500}},"F9":{"7":{"volume":1500}},"G9":{"7":{"volume":1500}},"H9":{"7":{"volume":1500}},"A10":{"7":{"volume":1500}},"B10":{"7":{"volume":1500}},"C10":{"7":{"volume":1500}},"D10":{"7":{"volume":1500}},"E10":{"7":{"volume":1500}},"F10":{"7":{"volume":1500}},"G10":{"7":{"volume":1500}},"H10":{"7":{"volume":1500}},"A11":{"7":{"volume":1500}},"B11":{"7":{"volume":1500}},"C11":{"7":{"volume":1500}},"D11":{"7":{"volume":1500}},"E11":{"7":{"volume":1500}},"F11":{"7":{"volume":1500}},"G11":{"7":{"volume":1500}},"H11":{"7":{"volume":1500}},"A12":{"7":{"volume":1500}},"B12":{"7":{"volume":1500}},"C12":{"7":{"volume":1500}},"D12":{"7":{"volume":1500}},"E12":{"7":{"volume":1500}},"F12":{"7":{"volume":1500}},"G12":{"7":{"volume":1500}},"H12":{"7":{"volume":1500}}}},"savedStepForms":{"__INITIAL_DECK_SETUP_STEP__":{"labwareLocationUpdate":{"83cb3c5a-0a43-45a4-8ff1-d0cdc1c4385c:opentrons/opentrons_96_well_aluminum_block/1":"9583a841-45d6-48b4-9ed7-b9b47956ebce:temperatureModuleType","40f50c87-c1e1-4944-8b79-cd47b1dbfa59:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2":"83cb3c5a-0a43-45a4-8ff1-d0cdc1c4385c:opentrons/opentrons_96_well_aluminum_block/1","d4110d80-d905-434b-8b55-b15c6e2d4cfe:opentrons/nest_96_wellplate_2ml_deep/2":"B3","812212f1-6284-4b62-bc76-f66c6d8c2ff9:opentrons/nest_96_wellplate_2ml_deep/2":"C3","a18a9f6c-551e-4a06-bd74-070c1209c7ae:opentrons/nest_96_wellplate_2ml_deep/2":"B1","591b398c-7c32-4f1e-b6aa-2b242d8a1c4e:opentrons/nest_96_wellplate_2ml_deep/2":"B2","150eef86-25a6-43a7-bd42-5822d2fb0fe9:opentrons/opentrons_flex_96_tiprack_adapter/1":"A1","1ba09e74-b9ef-4546-9796-ad00c3b8676b:opentrons/opentrons_flex_96_tiprack_1000ul/1":"150eef86-25a6-43a7-bd42-5822d2fb0fe9:opentrons/opentrons_flex_96_tiprack_adapter/1","d051808a-d010-45f8-99ae-58c0933997ed:opentrons/opentrons_flex_96_tiprack_adapter/1":"A2","8ade46ff-3078-4bd1-b000-24b15aa395e6:opentrons/opentrons_flex_96_tiprack_1000ul/1":"d051808a-d010-45f8-99ae-58c0933997ed:opentrons/opentrons_flex_96_tiprack_adapter/1","34d93400-0e5b-4698-bd38-85b39add8cb2:opentrons/nest_96_wellplate_2ml_deep/2":"D2","b5696d32-aa10-4188-b9f0-bd40fbf1ab0b:opentrons/nest_96_wellplate_2ml_deep/2":"C2","e16fe8c1-f551-4333-a358-a0f8454fb238:opentrons/opentrons_flex_96_tiprack_1000ul/1":"offDeck","8da8aff4-2db6-46ab-a0e5-661b44fb8002:opentrons/opentrons_flex_96_tiprack_1000ul/1":"offDeck","cf6f1150-d9ad-444d-8de6-837075f6d22d:opentrons/opentrons_flex_96_tiprack_1000ul/1":"offDeck","561372cc-a2b3-4411-b1eb-f5e6d6aafeaa:opentrons/opentrons_flex_96_tiprack_1000ul/1":"offDeck","35b00671-1950-45f7-9e28-681e1027449e:opentrons/opentrons_flex_96_tiprack_1000ul/1":"offDeck","8015b314-63c4-419e-b454-504c51c7b13e:opentrons/opentrons_flex_96_tiprack_1000ul/1":"offDeck","98f7b3bc-f465-4876-9dc6-949d796d2d0c:opentrons/opentrons_flex_96_tiprack_1000ul/1":"offDeck","6e8b0426-4915-4a4d-85b6-d740bca07f35:opentrons/opentrons_flex_96_tiprack_1000ul/1":"offDeck","3aabe684-5254-439e-98cd-1096515284fe:opentrons/opentrons_flex_96_tiprack_1000ul/1":"offDeck","eb25a5e3-8be6-4ba0-9dc9-35a95305f175:opentrons/opentrons_flex_96_tiprack_1000ul/1":"offDeck","d395af7f-9c85-4d9c-9d30-569a05de86c0:opentrons/opentrons_flex_96_tiprack_1000ul/1":"offDeck","e633da9d-d2ce-4f1d-a8a3-35ec6f89d910:opentrons/opentrons_flex_96_tiprack_1000ul/1":"offDeck","f3adca02-de60-41d7-84d5-be0829327053:opentrons/opentrons_flex_96_tiprack_1000ul/1":"offDeck","159dad22-035c-4cc5-acc8-6d2c66f81b31:opentrons/opentrons_flex_96_tiprack_1000ul/1":"offDeck","6c9b8a8e-f53d-49a3-b65a-8bc27da85931:opentrons/opentrons_96_deep_well_adapter/1":"d2594396-9fe0-4822-b882-08d3950c16b0:heaterShakerModuleType","fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2":"6c9b8a8e-f53d-49a3-b65a-8bc27da85931:opentrons/opentrons_96_deep_well_adapter/1"},"moduleLocationUpdate":{"9583a841-45d6-48b4-9ed7-b9b47956ebce:temperatureModuleType":"A3","fb8de043-8d7f-4a81-978f-a765966324fc:magneticBlockType":"C1","d2594396-9fe0-4822-b882-08d3950c16b0:heaterShakerModuleType":"D1"},"pipetteLocationUpdate":{"88bd044e-beef-455e-9a9d-2ef2c0dac83e":"left"},"trashBinLocationUpdate":{},"wasteChuteLocationUpdate":{"e92a2d8a-3c9a-4080-9f07-1d44b4cdeca9:wasteChute":"cutoutD3"},"stagingAreaLocationUpdate":{},"gripperLocationUpdate":{"3159da5f-c9a2-4550-9ef3-f39f8ad819cb:gripper":"mounted"},"stepType":"manualIntervention","id":"__INITIAL_DECK_SETUP_STEP__"},"1d7cc1f0-7fcc-4f95-9b40-f90171c08eac":{"aspirate_airGap_checkbox":true,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_mmFromBottom":null,"aspirate_delay_seconds":"1","aspirate_flowRate":"160","aspirate_labware":"34d93400-0e5b-4698-bd38-85b39add8cb2:opentrons/nest_96_wellplate_2ml_deep/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":null,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":35,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":null,"aspirate_submerge_speed":35,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":300,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":80,"blowout_location":null,"blowout_z_offset":0,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_mmFromBottom":null,"dispense_delay_seconds":"1","dispense_flowRate":"160","dispense_labware":"fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":null,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":35,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":null,"dispense_submerge_speed":35,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":300,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"e92a2d8a-3c9a-4080-9f07-1d44b4cdeca9:wasteChute","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"88bd044e-beef-455e-9a9d-2ef2c0dac83e","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":20,"tipRack":"opentrons/opentrons_flex_96_tiprack_1000ul/1","volume":"220","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","id":"1d7cc1f0-7fcc-4f95-9b40-f90171c08eac","dispense_touchTip_mmfromTop":null},"292c185a-672a-41ff-9cc6-e88a0d41cea9":{"heaterShakerSetTimer":null,"heaterShakerTimer":null,"latchOpen":false,"moduleId":"d2594396-9fe0-4822-b882-08d3950c16b0:heaterShakerModuleType","setHeaterShakerTemperature":null,"setShake":null,"targetHeaterShakerTemperature":null,"targetSpeed":null,"id":"292c185a-672a-41ff-9cc6-e88a0d41cea9","stepType":"heaterShaker","stepName":"heater-shaker","stepDetails":""},"9b65c911-d8c6-47a5-984b-d8d4712539f5":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"150","blowout_checkbox":false,"blowout_flowRate":null,"blowout_location":null,"blowout_z_offset":0,"changeTip":"never","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"150","dropTip_location":"e92a2d8a-3c9a-4080-9f07-1d44b4cdeca9:wasteChute","labware":"fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"88bd044e-beef-455e-9a9d-2ef2c0dac83e","pushOut_checkbox":true,"pushOut_volume":20,"times":"8","tipRack":"opentrons/opentrons_flex_96_tiprack_1000ul/1","volume":"198","wells":["A1"],"stepType":"mix","stepName":"mix","stepDetails":"","id":"9b65c911-d8c6-47a5-984b-d8d4712539f5"},"69fc16aa-8ac4-4684-a9d5-554d5ac8f371":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"150","blowout_checkbox":false,"blowout_flowRate":null,"blowout_location":null,"blowout_z_offset":0,"changeTip":"once","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"187","dropTip_location":"e92a2d8a-3c9a-4080-9f07-1d44b4cdeca9:wasteChute","labware":"b5696d32-aa10-4188-b9f0-bd40fbf1ab0b:opentrons/nest_96_wellplate_2ml_deep/2","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"88bd044e-beef-455e-9a9d-2ef2c0dac83e","pushOut_checkbox":true,"pushOut_volume":20,"times":"23","tipRack":"opentrons/opentrons_flex_96_tiprack_1000ul/1","volume":"562.5","wells":["A1"],"stepType":"mix","stepName":"mix","stepDetails":"","id":"69fc16aa-8ac4-4684-a9d5-554d5ac8f371"},"a2a94aa3-f432-476a-8092-5733670da115":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_mmFromBottom":null,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"b5696d32-aa10-4188-b9f0-bd40fbf1ab0b:opentrons/nest_96_wellplate_2ml_deep/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":null,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":35,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":null,"aspirate_submerge_speed":35,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":300,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":80,"blowout_location":null,"blowout_z_offset":0,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_mmFromBottom":null,"dispense_delay_seconds":"1","dispense_flowRate":"160","dispense_labware":"fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":null,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":35,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":null,"dispense_submerge_speed":35,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":300,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"e92a2d8a-3c9a-4080-9f07-1d44b4cdeca9:wasteChute","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"88bd044e-beef-455e-9a9d-2ef2c0dac83e","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":20,"tipRack":"opentrons/opentrons_flex_96_tiprack_1000ul/1","volume":"625","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","id":"a2a94aa3-f432-476a-8092-5733670da115","dispense_touchTip_mmfromTop":null},"3e0990ca-eda8-4280-ad13-c5eb7b20bfc1":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"150","blowout_checkbox":false,"blowout_flowRate":null,"blowout_location":null,"blowout_z_offset":0,"changeTip":"never","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"187.2","dropTip_location":"e92a2d8a-3c9a-4080-9f07-1d44b4cdeca9:wasteChute","labware":"fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"88bd044e-beef-455e-9a9d-2ef2c0dac83e","pushOut_checkbox":true,"pushOut_volume":20,"times":"30","tipRack":"opentrons/opentrons_flex_96_tiprack_1000ul/1","volume":"751.5","wells":["A1"],"stepType":"mix","stepName":"mix","stepDetails":"","id":"3e0990ca-eda8-4280-ad13-c5eb7b20bfc1"},"1fc3f43a-e460-4aac-a02d-5542d48e3d4c":{"labware":"fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2","newLocation":"fb8de043-8d7f-4a81-978f-a765966324fc:magneticBlockType","useGripper":true,"id":"1fc3f43a-e460-4aac-a02d-5542d48e3d4c","stepType":"moveLabware","stepName":"move","stepDetails":""},"85cfba4d-c218-4c3e-89e1-53673e76d315":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"Delaying for 2 minutes while beads pellet ","pauseTemperature":null,"pauseTime":"00:02:00","id":"85cfba4d-c218-4c3e-89e1-53673e76d315","stepType":"pause","stepName":"pause","stepDetails":""},"a10afdd6-4800-469e-bb36-47b8f39eb785":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_mmFromBottom":null,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":null,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":35,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":null,"aspirate_submerge_speed":35,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":300,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":80,"blowout_location":null,"blowout_z_offset":0,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_mmFromBottom":null,"dispense_delay_seconds":"1","dispense_flowRate":"150","dispense_labware":"b5696d32-aa10-4188-b9f0-bd40fbf1ab0b:opentrons/nest_96_wellplate_2ml_deep/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":null,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":35,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":null,"dispense_submerge_speed":35,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":300,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"e92a2d8a-3c9a-4080-9f07-1d44b4cdeca9:wasteChute","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"88bd044e-beef-455e-9a9d-2ef2c0dac83e","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":20,"tipRack":"opentrons/opentrons_flex_96_tiprack_1000ul/1","volume":"835","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","id":"a10afdd6-4800-469e-bb36-47b8f39eb785","dispense_touchTip_mmfromTop":null},"dabe7d31-09e5-49e6-aa70-5567691be9df":{"labware":"1ba09e74-b9ef-4546-9796-ad00c3b8676b:opentrons/opentrons_flex_96_tiprack_1000ul/1","newLocation":"cutoutD3","useGripper":true,"id":"dabe7d31-09e5-49e6-aa70-5567691be9df","stepType":"moveLabware","stepName":"move","stepDetails":""},"53037414-3d35-40b8-a361-a2de6a729cc1":{"labware":"8ade46ff-3078-4bd1-b000-24b15aa395e6:opentrons/opentrons_flex_96_tiprack_1000ul/1","newLocation":"cutoutD3","useGripper":true,"id":"53037414-3d35-40b8-a361-a2de6a729cc1","stepType":"moveLabware","stepName":"move","stepDetails":""},"18ad61fe-13e4-4485-8db3-9d2448680697":{"heaterShakerSetTimer":null,"heaterShakerTimer":null,"latchOpen":true,"moduleId":"d2594396-9fe0-4822-b882-08d3950c16b0:heaterShakerModuleType","setHeaterShakerTemperature":null,"setShake":null,"targetHeaterShakerTemperature":null,"targetSpeed":null,"id":"18ad61fe-13e4-4485-8db3-9d2448680697","stepType":"heaterShaker","stepName":"heater-shaker","stepDetails":""},"fce04b51-8e40-4563-8f12-c6e0acc15d84":{"labware":"fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2","newLocation":"6c9b8a8e-f53d-49a3-b65a-8bc27da85931:opentrons/opentrons_96_deep_well_adapter/1","useGripper":true,"id":"fce04b51-8e40-4563-8f12-c6e0acc15d84","stepType":"moveLabware","stepName":"move","stepDetails":""},"2423bef9-414a-4000-ae2c-a82dca326120":{"heaterShakerSetTimer":null,"heaterShakerTimer":null,"latchOpen":false,"moduleId":"d2594396-9fe0-4822-b882-08d3950c16b0:heaterShakerModuleType","setHeaterShakerTemperature":null,"setShake":null,"targetHeaterShakerTemperature":null,"targetSpeed":null,"id":"2423bef9-414a-4000-ae2c-a82dca326120","stepType":"heaterShaker","stepName":"heater-shaker","stepDetails":""},"3f6314e5-650c-4e52-b7f3-65e7bdc76faa":{"aspirate_airGap_checkbox":true,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_mmFromBottom":null,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"812212f1-6284-4b62-bc76-f66c6d8c2ff9:opentrons/nest_96_wellplate_2ml_deep/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":null,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":35,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":null,"aspirate_submerge_speed":35,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":300,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":80,"blowout_location":null,"blowout_z_offset":0,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_mmFromBottom":null,"dispense_delay_seconds":"1","dispense_flowRate":"150","dispense_labware":"fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":null,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":35,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":null,"dispense_submerge_speed":35,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":300,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"e92a2d8a-3c9a-4080-9f07-1d44b4cdeca9:wasteChute","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"88bd044e-beef-455e-9a9d-2ef2c0dac83e","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":20,"tipRack":"opentrons/opentrons_flex_96_tiprack_1000ul/1","volume":"500","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","id":"3f6314e5-650c-4e52-b7f3-65e7bdc76faa","dispense_touchTip_mmfromTop":null},"229b55a9-103e-466a-bd78-2978685c8b54":{"labware":"8015b314-63c4-419e-b454-504c51c7b13e:opentrons/opentrons_flex_96_tiprack_1000ul/1","newLocation":"cutoutD3","useGripper":true,"id":"229b55a9-103e-466a-bd78-2978685c8b54","stepType":"moveLabware","stepName":"move","stepDetails":""},"f8e55fca-018a-4df6-884c-f2f54e1fb8db":{"labware":"8da8aff4-2db6-46ab-a0e5-661b44fb8002:opentrons/opentrons_flex_96_tiprack_1000ul/1","newLocation":"d051808a-d010-45f8-99ae-58c0933997ed:opentrons/opentrons_flex_96_tiprack_adapter/1","useGripper":false,"id":"f8e55fca-018a-4df6-884c-f2f54e1fb8db","stepType":"moveLabware","stepName":"move","stepDetails":""},"1619c960-fb02-4d0f-8455-8f57651d39b3":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"160","blowout_checkbox":true,"blowout_flowRate":80,"blowout_location":"dest_well","blowout_z_offset":-3,"changeTip":"once","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"160","dropTip_location":"e92a2d8a-3c9a-4080-9f07-1d44b4cdeca9:wasteChute","labware":"b5696d32-aa10-4188-b9f0-bd40fbf1ab0b:opentrons/nest_96_wellplate_2ml_deep/2","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"88bd044e-beef-455e-9a9d-2ef2c0dac83e","pushOut_checkbox":true,"pushOut_volume":20,"times":"33","tipRack":"opentrons/opentrons_flex_96_tiprack_1000ul/1","volume":"450","wells":["A1"],"stepType":"mix","stepName":"mix","stepDetails":"","id":"1619c960-fb02-4d0f-8455-8f57651d39b3"},"3bf90df6-c951-4015-ba3d-925b5378ff4c":{"labware":"8da8aff4-2db6-46ab-a0e5-661b44fb8002:opentrons/opentrons_flex_96_tiprack_1000ul/1","newLocation":"cutoutD3","useGripper":true,"id":"3bf90df6-c951-4015-ba3d-925b5378ff4c","stepType":"moveLabware","stepName":"move","stepDetails":""},"ace65c4c-c3bc-49f1-b240-2f6d7e6e259a":{"labware":"cf6f1150-d9ad-444d-8de6-837075f6d22d:opentrons/opentrons_flex_96_tiprack_1000ul/1","newLocation":"d051808a-d010-45f8-99ae-58c0933997ed:opentrons/opentrons_flex_96_tiprack_adapter/1","useGripper":false,"id":"ace65c4c-c3bc-49f1-b240-2f6d7e6e259a","stepType":"moveLabware","stepName":"move","stepDetails":""},"1cbd8c9c-5097-4311-8045-5781a69f6ab8":{"heaterShakerSetTimer":true,"heaterShakerTimer":"10:00","latchOpen":false,"moduleId":"d2594396-9fe0-4822-b882-08d3950c16b0:heaterShakerModuleType","setHeaterShakerTemperature":null,"setShake":true,"targetHeaterShakerTemperature":null,"targetSpeed":"1800","id":"1cbd8c9c-5097-4311-8045-5781a69f6ab8","stepType":"heaterShaker","stepName":"heater-shaker","stepDetails":""},"14d7eba2-b537-474d-83ac-ecaaad8ef5f9":{"heaterShakerSetTimer":null,"heaterShakerTimer":null,"latchOpen":true,"moduleId":"d2594396-9fe0-4822-b882-08d3950c16b0:heaterShakerModuleType","setHeaterShakerTemperature":null,"setShake":null,"targetHeaterShakerTemperature":null,"targetSpeed":null,"id":"14d7eba2-b537-474d-83ac-ecaaad8ef5f9","stepType":"heaterShaker","stepName":"heater-shaker","stepDetails":""},"ea9b6717-43be-449a-9f2a-8d9fd7d7f616":{"labware":"fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2","newLocation":"fb8de043-8d7f-4a81-978f-a765966324fc:magneticBlockType","useGripper":true,"id":"ea9b6717-43be-449a-9f2a-8d9fd7d7f616","stepType":"moveLabware","stepName":"move","stepDetails":""},"54fa1587-c3f4-4a12-a7e2-a97211fd6902":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:02:00","id":"54fa1587-c3f4-4a12-a7e2-a97211fd6902","stepType":"pause","stepName":"pause","stepDetails":""},"7e29eafe-ecaf-4104-b734-d3dc7fa5df6e":{"labware":"cf6f1150-d9ad-444d-8de6-837075f6d22d:opentrons/opentrons_flex_96_tiprack_1000ul/1","newLocation":"cutoutD3","useGripper":true,"id":"7e29eafe-ecaf-4104-b734-d3dc7fa5df6e","stepType":"moveLabware","stepName":"move","stepDetails":""},"2252ab68-b501-4c59-92d3-91cb4cca5ed9":{"labware":"35b00671-1950-45f7-9e28-681e1027449e:opentrons/opentrons_flex_96_tiprack_1000ul/1","newLocation":"150eef86-25a6-43a7-bd42-5822d2fb0fe9:opentrons/opentrons_flex_96_tiprack_adapter/1","useGripper":false,"id":"2252ab68-b501-4c59-92d3-91cb4cca5ed9","stepType":"moveLabware","stepName":"move","stepDetails":""},"920f2d91-61b6-490c-aa71-e53f6ed6eb50":{"labware":"fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2","newLocation":"6c9b8a8e-f53d-49a3-b65a-8bc27da85931:opentrons/opentrons_96_deep_well_adapter/1","useGripper":true,"id":"920f2d91-61b6-490c-aa71-e53f6ed6eb50","stepType":"moveLabware","stepName":"move","stepDetails":""},"039fc07d-7086-4e56-a203-1363a5e2a84b":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_mmFromBottom":null,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":null,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":35,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":null,"aspirate_submerge_speed":35,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":300,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":80,"blowout_location":null,"blowout_z_offset":0,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":true,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_mmFromBottom":null,"dispense_delay_seconds":"1","dispense_flowRate":"150","dispense_labware":"b5696d32-aa10-4188-b9f0-bd40fbf1ab0b:opentrons/nest_96_wellplate_2ml_deep/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":null,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":35,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":null,"dispense_submerge_speed":35,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":300,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"e92a2d8a-3c9a-4080-9f07-1d44b4cdeca9:wasteChute","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"88bd044e-beef-455e-9a9d-2ef2c0dac83e","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":20,"tipRack":"opentrons/opentrons_flex_96_tiprack_1000ul/1","volume":"500","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","id":"039fc07d-7086-4e56-a203-1363a5e2a84b","dispense_touchTip_mmfromTop":null},"6519cdb4-6c2b-4ca1-904b-3b401936b855":{"heaterShakerSetTimer":null,"heaterShakerTimer":null,"latchOpen":false,"moduleId":"d2594396-9fe0-4822-b882-08d3950c16b0:heaterShakerModuleType","setHeaterShakerTemperature":null,"setShake":null,"targetHeaterShakerTemperature":null,"targetSpeed":null,"id":"6519cdb4-6c2b-4ca1-904b-3b401936b855","stepType":"heaterShaker","stepName":"heater-shaker","stepDetails":""},"7eb7d367-f867-420f-8176-7cbcb14e5800":{"labware":"fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2","newLocation":"fb8de043-8d7f-4a81-978f-a765966324fc:magneticBlockType","useGripper":true,"id":"7eb7d367-f867-420f-8176-7cbcb14e5800","stepType":"moveLabware","stepName":"move","stepDetails":""},"28803063-290b-4b85-8379-16b22f6e7bbb":{"heaterShakerSetTimer":null,"heaterShakerTimer":null,"latchOpen":true,"moduleId":"d2594396-9fe0-4822-b882-08d3950c16b0:heaterShakerModuleType","setHeaterShakerTemperature":null,"setShake":null,"targetHeaterShakerTemperature":null,"targetSpeed":null,"id":"28803063-290b-4b85-8379-16b22f6e7bbb","stepType":"heaterShaker","stepName":"heater-shaker","stepDetails":""},"b0ac1cf7-5e4a-4f18-b248-4930711f1869":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_mmFromBottom":null,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"a18a9f6c-551e-4a06-bd74-070c1209c7ae:opentrons/nest_96_wellplate_2ml_deep/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":null,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":35,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":null,"aspirate_submerge_speed":35,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":300,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":80,"blowout_location":null,"blowout_z_offset":0,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_mmFromBottom":null,"dispense_delay_seconds":"1","dispense_flowRate":"150","dispense_labware":"fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":null,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":35,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":null,"dispense_submerge_speed":35,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":300,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"e92a2d8a-3c9a-4080-9f07-1d44b4cdeca9:wasteChute","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"88bd044e-beef-455e-9a9d-2ef2c0dac83e","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":20,"tipRack":"opentrons/opentrons_flex_96_tiprack_1000ul/1","volume":"500","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","id":"b0ac1cf7-5e4a-4f18-b248-4930711f1869","dispense_touchTip_mmfromTop":null},"f81e1e43-eb0b-4a18-8e63-1db33644d46c":{"labware":"35b00671-1950-45f7-9e28-681e1027449e:opentrons/opentrons_flex_96_tiprack_1000ul/1","newLocation":"cutoutD3","useGripper":true,"id":"f81e1e43-eb0b-4a18-8e63-1db33644d46c","stepType":"moveLabware","stepName":"move","stepDetails":""},"0e6d9634-a886-4a5d-ac73-1316114c3152":{"labware":"98f7b3bc-f465-4876-9dc6-949d796d2d0c:opentrons/opentrons_flex_96_tiprack_1000ul/1","newLocation":"d051808a-d010-45f8-99ae-58c0933997ed:opentrons/opentrons_flex_96_tiprack_adapter/1","useGripper":false,"id":"0e6d9634-a886-4a5d-ac73-1316114c3152","stepType":"moveLabware","stepName":"move","stepDetails":""},"a76dea7e-ab5b-4f1c-95a4-126b62aedc29":{"labware":"98f7b3bc-f465-4876-9dc6-949d796d2d0c:opentrons/opentrons_flex_96_tiprack_1000ul/1","newLocation":"cutoutD3","useGripper":true,"id":"a76dea7e-ab5b-4f1c-95a4-126b62aedc29","stepType":"moveLabware","stepName":"move","stepDetails":""},"46c5bce7-a41c-40d6-a7f7-0d545ef06661":{"labware":"6e8b0426-4915-4a4d-85b6-d740bca07f35:opentrons/opentrons_flex_96_tiprack_1000ul/1","newLocation":"150eef86-25a6-43a7-bd42-5822d2fb0fe9:opentrons/opentrons_flex_96_tiprack_adapter/1","useGripper":false,"id":"46c5bce7-a41c-40d6-a7f7-0d545ef06661","stepType":"moveLabware","stepName":"move","stepDetails":""},"2012d968-f0b6-4f3f-ad97-772654c7816b":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"Pausing for 120 seconds. Please wait 2 minute(s) for beads to pellet in wash #1.\n\n------Removing Supernatant-----\n\n","pauseTemperature":null,"pauseTime":"00:02:00","id":"2012d968-f0b6-4f3f-ad97-772654c7816b","stepType":"pause","stepName":"pause","stepDetails":""},"d918172d-d8fd-4f38-974d-a6610552c402":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_mmFromBottom":null,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":null,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":35,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":null,"aspirate_submerge_speed":35,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":300,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":80,"blowout_location":null,"blowout_z_offset":0,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_mmFromBottom":null,"dispense_delay_seconds":"1","dispense_flowRate":"150","dispense_labware":"b5696d32-aa10-4188-b9f0-bd40fbf1ab0b:opentrons/nest_96_wellplate_2ml_deep/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":null,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":35,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":null,"dispense_submerge_speed":35,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":300,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"e92a2d8a-3c9a-4080-9f07-1d44b4cdeca9:wasteChute","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"88bd044e-beef-455e-9a9d-2ef2c0dac83e","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":20,"tipRack":"opentrons/opentrons_flex_96_tiprack_1000ul/1","volume":"500","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","id":"d918172d-d8fd-4f38-974d-a6610552c402","dispense_touchTip_mmfromTop":null},"d3268af3-e0c5-4e68-8716-5260dea25612":{"labware":"fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2","newLocation":"6c9b8a8e-f53d-49a3-b65a-8bc27da85931:opentrons/opentrons_96_deep_well_adapter/1","useGripper":true,"id":"d3268af3-e0c5-4e68-8716-5260dea25612","stepType":"moveLabware","stepName":"move","stepDetails":""},"b9d5e4b7-099f-46d2-a102-31dec007f2f1":{"heaterShakerSetTimer":null,"heaterShakerTimer":null,"latchOpen":true,"moduleId":"d2594396-9fe0-4822-b882-08d3950c16b0:heaterShakerModuleType","setHeaterShakerTemperature":null,"setShake":null,"targetHeaterShakerTemperature":null,"targetSpeed":null,"id":"b9d5e4b7-099f-46d2-a102-31dec007f2f1","stepType":"heaterShaker","stepName":"heater-shaker","stepDetails":""},"97ffdc1a-7122-4469-907a-c8c12d16d3cb":{"heaterShakerSetTimer":null,"heaterShakerTimer":null,"latchOpen":false,"moduleId":"d2594396-9fe0-4822-b882-08d3950c16b0:heaterShakerModuleType","setHeaterShakerTemperature":null,"setShake":null,"targetHeaterShakerTemperature":null,"targetSpeed":null,"id":"97ffdc1a-7122-4469-907a-c8c12d16d3cb","stepType":"heaterShaker","stepName":"heater-shaker","stepDetails":""},"f87c84d0-9338-4d97-995f-0ceb606253ee":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_mmFromBottom":null,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"591b398c-7c32-4f1e-b6aa-2b242d8a1c4e:opentrons/nest_96_wellplate_2ml_deep/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":null,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":35,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":null,"aspirate_submerge_speed":35,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":300,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":80,"blowout_location":null,"blowout_z_offset":0,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_mmFromBottom":null,"dispense_delay_seconds":"1","dispense_flowRate":"150","dispense_labware":"fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":null,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":35,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":null,"dispense_submerge_speed":35,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":300,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"e92a2d8a-3c9a-4080-9f07-1d44b4cdeca9:wasteChute","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"88bd044e-beef-455e-9a9d-2ef2c0dac83e","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":20,"tipRack":"opentrons/opentrons_flex_96_tiprack_1000ul/1","volume":"900","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","id":"f87c84d0-9338-4d97-995f-0ceb606253ee","dispense_touchTip_mmfromTop":null},"b79047e8-9bef-4704-a9fd-a47e51754641":{"labware":"6e8b0426-4915-4a4d-85b6-d740bca07f35:opentrons/opentrons_flex_96_tiprack_1000ul/1","newLocation":"cutoutD3","useGripper":true,"id":"b79047e8-9bef-4704-a9fd-a47e51754641","stepType":"moveLabware","stepName":"move","stepDetails":""},"51691984-8ab3-4090-b1ad-09e7850913a3":{"labware":"3aabe684-5254-439e-98cd-1096515284fe:opentrons/opentrons_flex_96_tiprack_1000ul/1","newLocation":"150eef86-25a6-43a7-bd42-5822d2fb0fe9:opentrons/opentrons_flex_96_tiprack_adapter/1","useGripper":false,"id":"51691984-8ab3-4090-b1ad-09e7850913a3","stepType":"moveLabware","stepName":"move","stepDetails":""},"51075926-c141-4ead-a6d6-d9f5f5f40068":{"heaterShakerSetTimer":null,"heaterShakerTimer":null,"latchOpen":true,"moduleId":"d2594396-9fe0-4822-b882-08d3950c16b0:heaterShakerModuleType","setHeaterShakerTemperature":null,"setShake":false,"targetHeaterShakerTemperature":null,"targetSpeed":"","id":"51075926-c141-4ead-a6d6-d9f5f5f40068","stepType":"heaterShaker","stepName":"heater-shaker","stepDetails":""},"91bcb449-523b-45fc-b41c-951126ca98bb":{"labware":"fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2","newLocation":"fb8de043-8d7f-4a81-978f-a765966324fc:magneticBlockType","useGripper":true,"id":"91bcb449-523b-45fc-b41c-951126ca98bb","stepType":"moveLabware","stepName":"move","stepDetails":""},"70f3a366-2106-456c-a378-32a916d66cd3":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"Pausing for 120 seconds. Please wait 2 minute(s) for beads to pellet in wash #3.\n\n","pauseTemperature":null,"pauseTime":"00:02:00","id":"70f3a366-2106-456c-a378-32a916d66cd3","stepType":"pause","stepName":"pause","stepDetails":""},"6e1bd191-b6bd-41de-ac2b-4558a57d9c05":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_mmFromBottom":null,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":null,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":35,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":null,"aspirate_submerge_speed":35,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":300,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":80,"blowout_location":null,"blowout_z_offset":0,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_mmFromBottom":null,"dispense_delay_seconds":"1","dispense_flowRate":"150","dispense_labware":"812212f1-6284-4b62-bc76-f66c6d8c2ff9:opentrons/nest_96_wellplate_2ml_deep/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":null,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":35,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":null,"dispense_submerge_speed":35,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":300,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"e92a2d8a-3c9a-4080-9f07-1d44b4cdeca9:wasteChute","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"88bd044e-beef-455e-9a9d-2ef2c0dac83e","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":20,"tipRack":"opentrons/opentrons_flex_96_tiprack_1000ul/1","volume":"900","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","id":"6e1bd191-b6bd-41de-ac2b-4558a57d9c05","dispense_touchTip_mmfromTop":null},"8621767f-b44c-419b-b074-829742317e09":{"labware":"3aabe684-5254-439e-98cd-1096515284fe:opentrons/opentrons_flex_96_tiprack_1000ul/1","newLocation":"cutoutD3","useGripper":true,"id":"8621767f-b44c-419b-b074-829742317e09","stepType":"moveLabware","stepName":"move","stepDetails":""},"83680de6-58af-43db-92c0-da40757b3ce1":{"labware":"eb25a5e3-8be6-4ba0-9dc9-35a95305f175:opentrons/opentrons_flex_96_tiprack_1000ul/1","newLocation":"150eef86-25a6-43a7-bd42-5822d2fb0fe9:opentrons/opentrons_flex_96_tiprack_adapter/1","useGripper":false,"id":"83680de6-58af-43db-92c0-da40757b3ce1","stepType":"moveLabware","stepName":"move","stepDetails":""},"ecd1bb79-5faa-447a-94db-d6d3209d7217":{"labware":"fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2","newLocation":"6c9b8a8e-f53d-49a3-b65a-8bc27da85931:opentrons/opentrons_96_deep_well_adapter/1","useGripper":true,"id":"ecd1bb79-5faa-447a-94db-d6d3209d7217","stepType":"moveLabware","stepName":"move","stepDetails":""},"348e9b2e-74d2-4daf-9c54-819e2ce713ca":{"heaterShakerSetTimer":null,"heaterShakerTimer":null,"latchOpen":true,"moduleId":"d2594396-9fe0-4822-b882-08d3950c16b0:heaterShakerModuleType","setHeaterShakerTemperature":null,"setShake":null,"targetHeaterShakerTemperature":null,"targetSpeed":null,"id":"348e9b2e-74d2-4daf-9c54-819e2ce713ca","stepType":"heaterShaker","stepName":"heater-shaker","stepDetails":""},"7a513ab1-1e4d-4ccf-bcba-b02dcc21fdb8":{"heaterShakerSetTimer":null,"heaterShakerTimer":null,"latchOpen":false,"moduleId":"d2594396-9fe0-4822-b882-08d3950c16b0:heaterShakerModuleType","setHeaterShakerTemperature":null,"setShake":null,"targetHeaterShakerTemperature":null,"targetSpeed":null,"id":"7a513ab1-1e4d-4ccf-bcba-b02dcc21fdb8","stepType":"heaterShaker","stepName":"heater-shaker","stepDetails":""},"d423bfe8-28ef-4f61-b796-ee0b2584da95":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_mmFromBottom":null,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"d4110d80-d905-434b-8b55-b15c6e2d4cfe:opentrons/nest_96_wellplate_2ml_deep/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":null,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":35,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":null,"aspirate_submerge_speed":35,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":300,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":80,"blowout_location":null,"blowout_z_offset":0,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_mmFromBottom":null,"dispense_delay_seconds":"1","dispense_flowRate":"150","dispense_labware":"fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":null,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":35,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":null,"dispense_submerge_speed":35,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":300,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"e92a2d8a-3c9a-4080-9f07-1d44b4cdeca9:wasteChute","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"88bd044e-beef-455e-9a9d-2ef2c0dac83e","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":20,"tipRack":"opentrons/opentrons_flex_96_tiprack_1000ul/1","volume":"900","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","id":"d423bfe8-28ef-4f61-b796-ee0b2584da95","dispense_touchTip_mmfromTop":null},"140cc79f-705e-405b-aaea-fda47d35508c":{"labware":"eb25a5e3-8be6-4ba0-9dc9-35a95305f175:opentrons/opentrons_flex_96_tiprack_1000ul/1","newLocation":"cutoutD3","useGripper":true,"id":"140cc79f-705e-405b-aaea-fda47d35508c","stepType":"moveLabware","stepName":"move","stepDetails":""},"cfe5dee9-6c12-457d-83b8-b7780edd86f7":{"labware":"d395af7f-9c85-4d9c-9d30-569a05de86c0:opentrons/opentrons_flex_96_tiprack_1000ul/1","newLocation":"d051808a-d010-45f8-99ae-58c0933997ed:opentrons/opentrons_flex_96_tiprack_adapter/1","useGripper":false,"id":"cfe5dee9-6c12-457d-83b8-b7780edd86f7","stepType":"moveLabware","stepName":"move","stepDetails":""},"2e8fbdd8-bc12-46a8-aee5-7a6a114d763a":{"heaterShakerSetTimer":null,"heaterShakerTimer":null,"latchOpen":true,"moduleId":"d2594396-9fe0-4822-b882-08d3950c16b0:heaterShakerModuleType","setHeaterShakerTemperature":null,"setShake":null,"targetHeaterShakerTemperature":null,"targetSpeed":null,"id":"2e8fbdd8-bc12-46a8-aee5-7a6a114d763a","stepType":"heaterShaker","stepName":"heater-shaker","stepDetails":""},"4d17795a-ff77-4c9a-9f21-e48841e3e1c0":{"labware":"fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2","newLocation":"fb8de043-8d7f-4a81-978f-a765966324fc:magneticBlockType","useGripper":true,"id":"4d17795a-ff77-4c9a-9f21-e48841e3e1c0","stepType":"moveLabware","stepName":"move","stepDetails":""},"c3cff2bc-13ac-4261-9b3b-5054ed550348":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_mmFromBottom":null,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":null,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":35,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":null,"aspirate_submerge_speed":35,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":300,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":80,"blowout_location":null,"blowout_z_offset":0,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_mmFromBottom":null,"dispense_delay_seconds":"1","dispense_flowRate":"150","dispense_labware":"591b398c-7c32-4f1e-b6aa-2b242d8a1c4e:opentrons/nest_96_wellplate_2ml_deep/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":null,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":35,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":null,"dispense_submerge_speed":35,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":300,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"e92a2d8a-3c9a-4080-9f07-1d44b4cdeca9:wasteChute","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"88bd044e-beef-455e-9a9d-2ef2c0dac83e","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":20,"tipRack":"opentrons/opentrons_flex_96_tiprack_1000ul/1","volume":"900","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","id":"c3cff2bc-13ac-4261-9b3b-5054ed550348","dispense_touchTip_mmfromTop":null},"d810ad49-c800-46ef-a5fc-3c8e9e3412ef":{"labware":"d395af7f-9c85-4d9c-9d30-569a05de86c0:opentrons/opentrons_flex_96_tiprack_1000ul/1","newLocation":"cutoutD3","useGripper":true,"id":"d810ad49-c800-46ef-a5fc-3c8e9e3412ef","stepType":"moveLabware","stepName":"move","stepDetails":""},"d14e6dfd-04df-4a0b-8ec8-fc69a7d96672":{"labware":"e633da9d-d2ce-4f1d-a8a3-35ec6f89d910:opentrons/opentrons_flex_96_tiprack_1000ul/1","newLocation":"150eef86-25a6-43a7-bd42-5822d2fb0fe9:opentrons/opentrons_flex_96_tiprack_adapter/1","useGripper":false,"id":"d14e6dfd-04df-4a0b-8ec8-fc69a7d96672","stepType":"moveLabware","stepName":"move","stepDetails":""},"d7d68a8f-4c8f-47b8-bd35-7aa6d2e9d6b2":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"Pausing for 120 seconds. Please wait 2 minute(s) for beads to pellet in wash #4.\n\n------Removing Supernatant-----\n\n\n\n","pauseTemperature":null,"pauseTime":"00:02:00","id":"d7d68a8f-4c8f-47b8-bd35-7aa6d2e9d6b2","stepType":"pause","stepName":"pause","stepDetails":""},"d84e404a-6ac3-4b6a-bf1e-b1b062ca9764":{"labware":"fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2","newLocation":"6c9b8a8e-f53d-49a3-b65a-8bc27da85931:opentrons/opentrons_96_deep_well_adapter/1","useGripper":true,"id":"d84e404a-6ac3-4b6a-bf1e-b1b062ca9764","stepType":"moveLabware","stepName":"move","stepDetails":""},"90a7deef-0ab7-49f6-8402-df691d74c881":{"moduleId":"d2594396-9fe0-4822-b882-08d3950c16b0:heaterShakerModuleType","pauseAction":"untilTemperature","pauseMessage":"","pauseTemperature":"55","pauseTime":null,"id":"90a7deef-0ab7-49f6-8402-df691d74c881","stepType":"pause","stepName":"pause","stepDetails":""},"4ab1d0b7-e4bf-4a3d-bc3a-241d89604ab2":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_mmFromBottom":null,"aspirate_delay_seconds":"1","aspirate_flowRate":"25","aspirate_labware":"40f50c87-c1e1-4944-8b79-cd47b1dbfa59:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":null,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":35,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":null,"aspirate_submerge_speed":35,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":300,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":80,"blowout_location":null,"blowout_z_offset":0,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_mmFromBottom":null,"dispense_delay_seconds":"1","dispense_flowRate":"150","dispense_labware":"fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":null,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":35,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":null,"dispense_submerge_speed":35,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":300,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"e92a2d8a-3c9a-4080-9f07-1d44b4cdeca9:wasteChute","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"88bd044e-beef-455e-9a9d-2ef2c0dac83e","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":20,"tipRack":"opentrons/opentrons_flex_96_tiprack_1000ul/1","volume":"75","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","id":"4ab1d0b7-e4bf-4a3d-bc3a-241d89604ab2","dispense_touchTip_mmfromTop":null},"3cdd212b-751d-4d59-8244-1a9f9a51ca96":{"labware":"e633da9d-d2ce-4f1d-a8a3-35ec6f89d910:opentrons/opentrons_flex_96_tiprack_1000ul/1","newLocation":"cutoutD3","useGripper":true,"id":"3cdd212b-751d-4d59-8244-1a9f9a51ca96","stepType":"moveLabware","stepName":"move","stepDetails":""},"6d07b2ba-de77-426a-a5a4-18567c897e44":{"labware":"f3adca02-de60-41d7-84d5-be0829327053:opentrons/opentrons_flex_96_tiprack_1000ul/1","newLocation":"d051808a-d010-45f8-99ae-58c0933997ed:opentrons/opentrons_flex_96_tiprack_adapter/1","useGripper":false,"id":"6d07b2ba-de77-426a-a5a4-18567c897e44","stepType":"moveLabware","stepName":"move","stepDetails":""},"38d2d49b-5c8f-42f5-8c31-1704fa5af1d1":{"heaterShakerSetTimer":null,"heaterShakerTimer":null,"latchOpen":true,"moduleId":"d2594396-9fe0-4822-b882-08d3950c16b0:heaterShakerModuleType","setHeaterShakerTemperature":null,"setShake":null,"targetHeaterShakerTemperature":null,"targetSpeed":null,"id":"38d2d49b-5c8f-42f5-8c31-1704fa5af1d1","stepType":"heaterShaker","stepName":"heater-shaker","stepDetails":""},"a7f3be53-ddd4-4042-b9dc-401fcc9d8b52":{"labware":"fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2","newLocation":"fb8de043-8d7f-4a81-978f-a765966324fc:magneticBlockType","useGripper":true,"id":"a7f3be53-ddd4-4042-b9dc-401fcc9d8b52","stepType":"moveLabware","stepName":"move","stepDetails":""},"6ea72a11-e66c-4122-b6f0-6900c6359522":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"Pausing for 120 seconds. Please wait 2 minute(s) for beads to pellet.\n\n------Transfer DNA to Final Elution Plate-----\n\n","pauseTemperature":null,"pauseTime":"00:02:00","id":"6ea72a11-e66c-4122-b6f0-6900c6359522","stepType":"pause","stepName":"pause","stepDetails":""},"fa4b5920-6dc5-472f-a98c-937e7825bc15":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_mmFromBottom":null,"aspirate_delay_seconds":"1","aspirate_flowRate":"25","aspirate_labware":"fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":null,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":35,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":null,"aspirate_submerge_speed":35,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":300,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":80,"blowout_location":null,"blowout_z_offset":0,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_mmFromBottom":null,"dispense_delay_seconds":"1","dispense_flowRate":"150","dispense_labware":"40f50c87-c1e1-4944-8b79-cd47b1dbfa59:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":null,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":35,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":null,"dispense_submerge_speed":35,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":300,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"e92a2d8a-3c9a-4080-9f07-1d44b4cdeca9:wasteChute","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"88bd044e-beef-455e-9a9d-2ef2c0dac83e","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":20,"tipRack":"opentrons/opentrons_flex_96_tiprack_1000ul/1","volume":"75","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","id":"fa4b5920-6dc5-472f-a98c-937e7825bc15","dispense_touchTip_mmfromTop":null},"0518b9b3-3229-4646-a458-8a27db465f77":{"labware":"f3adca02-de60-41d7-84d5-be0829327053:opentrons/opentrons_flex_96_tiprack_1000ul/1","newLocation":"cutoutD3","useGripper":true,"id":"0518b9b3-3229-4646-a458-8a27db465f77","stepType":"moveLabware","stepName":"move","stepDetails":""},"a8419f15-d38e-468e-8f7a-4ff09e79228d":{"labware":"561372cc-a2b3-4411-b1eb-f5e6d6aafeaa:opentrons/opentrons_flex_96_tiprack_1000ul/1","newLocation":"150eef86-25a6-43a7-bd42-5822d2fb0fe9:opentrons/opentrons_flex_96_tiprack_adapter/1","useGripper":false,"id":"a8419f15-d38e-468e-8f7a-4ff09e79228d","stepType":"moveLabware","stepName":"move","stepDetails":""},"f5ee006c-578c-4d89-9a15-b654ea4545cd":{"heaterShakerSetTimer":true,"heaterShakerTimer":"30:00","latchOpen":false,"moduleId":"d2594396-9fe0-4822-b882-08d3950c16b0:heaterShakerModuleType","setHeaterShakerTemperature":null,"setShake":true,"targetHeaterShakerTemperature":null,"targetSpeed":"2000","id":"f5ee006c-578c-4d89-9a15-b654ea4545cd","stepType":"heaterShaker","stepName":"heater-shaker","stepDetails":""},"1f2642b5-f324-4875-8a40-e02485378f7d":{"heaterShakerSetTimer":true,"heaterShakerTimer":"10:00","latchOpen":false,"moduleId":"d2594396-9fe0-4822-b882-08d3950c16b0:heaterShakerModuleType","setHeaterShakerTemperature":null,"setShake":true,"targetHeaterShakerTemperature":null,"targetSpeed":"1800","id":"1f2642b5-f324-4875-8a40-e02485378f7d","stepType":"heaterShaker","stepName":"heater-shaker","stepDetails":""},"e5051d89-5d07-47b4-8672-2c2e8ade0f4a":{"heaterShakerSetTimer":true,"heaterShakerTimer":"05:00","latchOpen":false,"moduleId":"d2594396-9fe0-4822-b882-08d3950c16b0:heaterShakerModuleType","setHeaterShakerTemperature":null,"setShake":true,"targetHeaterShakerTemperature":null,"targetSpeed":"1800","id":"e5051d89-5d07-47b4-8672-2c2e8ade0f4a","stepType":"heaterShaker","stepName":"heater-shaker","stepDetails":""},"7a4cbdad-f930-4baa-acea-5248fd0309f4":{"heaterShakerSetTimer":true,"heaterShakerTimer":"05:00","latchOpen":false,"moduleId":"d2594396-9fe0-4822-b882-08d3950c16b0:heaterShakerModuleType","setHeaterShakerTemperature":null,"setShake":true,"targetHeaterShakerTemperature":null,"targetSpeed":"1800","id":"7a4cbdad-f930-4baa-acea-5248fd0309f4","stepType":"heaterShaker","stepName":"heater-shaker","stepDetails":""},"43653037-3174-4d1d-92be-3e65b0f22b94":{"heaterShakerSetTimer":true,"heaterShakerTimer":"05:00","latchOpen":false,"moduleId":"d2594396-9fe0-4822-b882-08d3950c16b0:heaterShakerModuleType","setHeaterShakerTemperature":null,"setShake":true,"targetHeaterShakerTemperature":null,"targetSpeed":"1800","id":"43653037-3174-4d1d-92be-3e65b0f22b94","stepType":"heaterShaker","stepName":"heater-shaker","stepDetails":""},"dec1df8c-c653-4440-8dfc-2abda98abccf":{"heaterShakerSetTimer":null,"heaterShakerTimer":null,"latchOpen":false,"moduleId":"d2594396-9fe0-4822-b882-08d3950c16b0:heaterShakerModuleType","setHeaterShakerTemperature":true,"setShake":null,"targetHeaterShakerTemperature":"55","targetSpeed":null,"id":"dec1df8c-c653-4440-8dfc-2abda98abccf","stepType":"heaterShaker","stepName":"heater-shaker","stepDetails":""},"72f403ee-e035-4bd7-b87b-0482ab9e0d74":{"moduleId":"d2594396-9fe0-4822-b882-08d3950c16b0:heaterShakerModuleType","pauseAction":"untilTemperature","pauseMessage":"","pauseTemperature":"55","pauseTime":null,"id":"72f403ee-e035-4bd7-b87b-0482ab9e0d74","stepType":"pause","stepName":"pause","stepDetails":""},"601da490-7b31-4a0f-95c4-95276f4d41ef":{"heaterShakerSetTimer":true,"heaterShakerTimer":"05:00","latchOpen":false,"moduleId":"d2594396-9fe0-4822-b882-08d3950c16b0:heaterShakerModuleType","setHeaterShakerTemperature":null,"setShake":true,"targetHeaterShakerTemperature":null,"targetSpeed":"2000","id":"601da490-7b31-4a0f-95c4-95276f4d41ef","stepType":"heaterShaker","stepName":"heater-shaker","stepDetails":""},"70ff283a-99b6-431d-bd8e-f42a14d8cae4":{"labware":"8015b314-63c4-419e-b454-504c51c7b13e:opentrons/opentrons_flex_96_tiprack_1000ul/1","newLocation":"150eef86-25a6-43a7-bd42-5822d2fb0fe9:opentrons/opentrons_flex_96_tiprack_adapter/1","useGripper":false,"id":"70ff283a-99b6-431d-bd8e-f42a14d8cae4","stepType":"moveLabware","stepName":"move","stepDetails":""}},"orderedStepIds":["292c185a-672a-41ff-9cc6-e88a0d41cea9","1d7cc1f0-7fcc-4f95-9b40-f90171c08eac","9b65c911-d8c6-47a5-984b-d8d4712539f5","f5ee006c-578c-4d89-9a15-b654ea4545cd","69fc16aa-8ac4-4684-a9d5-554d5ac8f371","a2a94aa3-f432-476a-8092-5733670da115","3e0990ca-eda8-4280-ad13-c5eb7b20bfc1","1f2642b5-f324-4875-8a40-e02485378f7d","348e9b2e-74d2-4daf-9c54-819e2ce713ca","1fc3f43a-e460-4aac-a02d-5542d48e3d4c","85cfba4d-c218-4c3e-89e1-53673e76d315","53037414-3d35-40b8-a361-a2de6a729cc1","dabe7d31-09e5-49e6-aa70-5567691be9df","70ff283a-99b6-431d-bd8e-f42a14d8cae4","a10afdd6-4800-469e-bb36-47b8f39eb785","18ad61fe-13e4-4485-8db3-9d2448680697","fce04b51-8e40-4563-8f12-c6e0acc15d84","2423bef9-414a-4000-ae2c-a82dca326120","229b55a9-103e-466a-bd78-2978685c8b54","f8e55fca-018a-4df6-884c-f2f54e1fb8db","3f6314e5-650c-4e52-b7f3-65e7bdc76faa","3bf90df6-c951-4015-ba3d-925b5378ff4c","ace65c4c-c3bc-49f1-b240-2f6d7e6e259a","1619c960-fb02-4d0f-8455-8f57651d39b3","1cbd8c9c-5097-4311-8045-5781a69f6ab8","14d7eba2-b537-474d-83ac-ecaaad8ef5f9","ea9b6717-43be-449a-9f2a-8d9fd7d7f616","54fa1587-c3f4-4a12-a7e2-a97211fd6902","7e29eafe-ecaf-4104-b734-d3dc7fa5df6e","2252ab68-b501-4c59-92d3-91cb4cca5ed9","920f2d91-61b6-490c-aa71-e53f6ed6eb50","6519cdb4-6c2b-4ca1-904b-3b401936b855","039fc07d-7086-4e56-a203-1363a5e2a84b","28803063-290b-4b85-8379-16b22f6e7bbb","7eb7d367-f867-420f-8176-7cbcb14e5800","f81e1e43-eb0b-4a18-8e63-1db33644d46c","0e6d9634-a886-4a5d-ac73-1316114c3152","b0ac1cf7-5e4a-4f18-b248-4930711f1869","e5051d89-5d07-47b4-8672-2c2e8ade0f4a","a76dea7e-ab5b-4f1c-95a4-126b62aedc29","46c5bce7-a41c-40d6-a7f7-0d545ef06661","2012d968-f0b6-4f3f-ad97-772654c7816b","d918172d-d8fd-4f38-974d-a6610552c402","b9d5e4b7-099f-46d2-a102-31dec007f2f1","d3268af3-e0c5-4e68-8716-5260dea25612","97ffdc1a-7122-4469-907a-c8c12d16d3cb","b79047e8-9bef-4704-a9fd-a47e51754641","51691984-8ab3-4090-b1ad-09e7850913a3","f87c84d0-9338-4d97-995f-0ceb606253ee","7a4cbdad-f930-4baa-acea-5248fd0309f4","51075926-c141-4ead-a6d6-d9f5f5f40068","91bcb449-523b-45fc-b41c-951126ca98bb","8621767f-b44c-419b-b074-829742317e09","83680de6-58af-43db-92c0-da40757b3ce1","70f3a366-2106-456c-a378-32a916d66cd3","6e1bd191-b6bd-41de-ac2b-4558a57d9c05","ecd1bb79-5faa-447a-94db-d6d3209d7217","7a513ab1-1e4d-4ccf-bcba-b02dcc21fdb8","cfe5dee9-6c12-457d-83b8-b7780edd86f7","140cc79f-705e-405b-aaea-fda47d35508c","d423bfe8-28ef-4f61-b796-ee0b2584da95","43653037-3174-4d1d-92be-3e65b0f22b94","2e8fbdd8-bc12-46a8-aee5-7a6a114d763a","d810ad49-c800-46ef-a5fc-3c8e9e3412ef","d14e6dfd-04df-4a0b-8ec8-fc69a7d96672","4d17795a-ff77-4c9a-9f21-e48841e3e1c0","d7d68a8f-4c8f-47b8-bd35-7aa6d2e9d6b2","c3cff2bc-13ac-4261-9b3b-5054ed550348","d84e404a-6ac3-4b6a-bf1e-b1b062ca9764","dec1df8c-c653-4440-8dfc-2abda98abccf","72f403ee-e035-4bd7-b87b-0482ab9e0d74","6d07b2ba-de77-426a-a5a4-18567c897e44","3cdd212b-751d-4d59-8244-1a9f9a51ca96","90a7deef-0ab7-49f6-8402-df691d74c881","4ab1d0b7-e4bf-4a3d-bc3a-241d89604ab2","601da490-7b31-4a0f-95c4-95276f4d41ef","38d2d49b-5c8f-42f5-8c31-1704fa5af1d1","0518b9b3-3229-4646-a458-8a27db465f77","a8419f15-d38e-468e-8f7a-4ff09e79228d","a7f3be53-ddd4-4042-b9dc-401fcc9d8b52","6ea72a11-e66c-4122-b6f0-6900c6359522","fa4b5920-6dc5-472f-a98c-937e7825bc15"],"pipettes":{"88bd044e-beef-455e-9a9d-2ef2c0dac83e":{"pipetteName":"p1000_96"}},"modules":{"9583a841-45d6-48b4-9ed7-b9b47956ebce:temperatureModuleType":{"model":"temperatureModuleV2"},"fb8de043-8d7f-4a81-978f-a765966324fc:magneticBlockType":{"model":"magneticBlockV1"},"d2594396-9fe0-4822-b882-08d3950c16b0:heaterShakerModuleType":{"model":"heaterShakerModuleV1"}},"labware":{"83cb3c5a-0a43-45a4-8ff1-d0cdc1c4385c:opentrons/opentrons_96_well_aluminum_block/1":{"displayName":"Opentrons 96 Well Aluminum Block","labwareDefURI":"opentrons/opentrons_96_well_aluminum_block/1"},"150eef86-25a6-43a7-bd42-5822d2fb0fe9:opentrons/opentrons_flex_96_tiprack_adapter/1":{"displayName":"Opentrons Flex 96 Tip Rack Adapter","labwareDefURI":"opentrons/opentrons_flex_96_tiprack_adapter/1"},"d051808a-d010-45f8-99ae-58c0933997ed:opentrons/opentrons_flex_96_tiprack_adapter/1":{"displayName":"Opentrons Flex 96 Tip Rack Adapter","labwareDefURI":"opentrons/opentrons_flex_96_tiprack_adapter/1"},"6c9b8a8e-f53d-49a3-b65a-8bc27da85931:opentrons/opentrons_96_deep_well_adapter/1":{"displayName":"Opentrons 96 Deep Well Heater-Shaker Adapter","labwareDefURI":"opentrons/opentrons_96_deep_well_adapter/1"},"40f50c87-c1e1-4944-8b79-cd47b1dbfa59:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2":{"displayName":"Elution plate","labwareDefURI":"opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2"},"d4110d80-d905-434b-8b55-b15c6e2d4cfe:opentrons/nest_96_wellplate_2ml_deep/2":{"displayName":"Wash 3","labwareDefURI":"opentrons/nest_96_wellplate_2ml_deep/2"},"812212f1-6284-4b62-bc76-f66c6d8c2ff9:opentrons/nest_96_wellplate_2ml_deep/2":{"displayName":"Binding 2","labwareDefURI":"opentrons/nest_96_wellplate_2ml_deep/2"},"a18a9f6c-551e-4a06-bd74-070c1209c7ae:opentrons/nest_96_wellplate_2ml_deep/2":{"displayName":"NEST 96 Deep Well Plate 2mL (3)","labwareDefURI":"opentrons/nest_96_wellplate_2ml_deep/2"},"591b398c-7c32-4f1e-b6aa-2b242d8a1c4e:opentrons/nest_96_wellplate_2ml_deep/2":{"displayName":"Wash 2","labwareDefURI":"opentrons/nest_96_wellplate_2ml_deep/2"},"1ba09e74-b9ef-4546-9796-ad00c3b8676b:opentrons/opentrons_flex_96_tiprack_1000ul/1":{"displayName":"Opentrons Flex 96 Tip Rack 1000 µL (1)","labwareDefURI":"opentrons/opentrons_flex_96_tiprack_1000ul/1"},"8ade46ff-3078-4bd1-b000-24b15aa395e6:opentrons/opentrons_flex_96_tiprack_1000ul/1":{"displayName":"Opentrons Flex 96 Tip Rack 1000 µL (2)","labwareDefURI":"opentrons/opentrons_flex_96_tiprack_1000ul/1"},"34d93400-0e5b-4698-bd38-85b39add8cb2:opentrons/nest_96_wellplate_2ml_deep/2":{"displayName":"Lysis","labwareDefURI":"opentrons/nest_96_wellplate_2ml_deep/2"},"b5696d32-aa10-4188-b9f0-bd40fbf1ab0b:opentrons/nest_96_wellplate_2ml_deep/2":{"displayName":"Binding and Beading","labwareDefURI":"opentrons/nest_96_wellplate_2ml_deep/2"},"e16fe8c1-f551-4333-a358-a0f8454fb238:opentrons/opentrons_flex_96_tiprack_1000ul/1":{"displayName":"Opentrons Flex 96 Tip Rack 1000 µL (3)","labwareDefURI":"opentrons/opentrons_flex_96_tiprack_1000ul/1"},"8da8aff4-2db6-46ab-a0e5-661b44fb8002:opentrons/opentrons_flex_96_tiprack_1000ul/1":{"displayName":"Opentrons Flex 96 Tip Rack 1000 µL (4)","labwareDefURI":"opentrons/opentrons_flex_96_tiprack_1000ul/1"},"cf6f1150-d9ad-444d-8de6-837075f6d22d:opentrons/opentrons_flex_96_tiprack_1000ul/1":{"displayName":"Opentrons Flex 96 Tip Rack 1000 µL (5)","labwareDefURI":"opentrons/opentrons_flex_96_tiprack_1000ul/1"},"561372cc-a2b3-4411-b1eb-f5e6d6aafeaa:opentrons/opentrons_flex_96_tiprack_1000ul/1":{"displayName":"Opentrons Flex 96 Tip Rack 1000 µL (6)","labwareDefURI":"opentrons/opentrons_flex_96_tiprack_1000ul/1"},"35b00671-1950-45f7-9e28-681e1027449e:opentrons/opentrons_flex_96_tiprack_1000ul/1":{"displayName":"Opentrons Flex 96 Tip Rack 1000 µL (7)","labwareDefURI":"opentrons/opentrons_flex_96_tiprack_1000ul/1"},"8015b314-63c4-419e-b454-504c51c7b13e:opentrons/opentrons_flex_96_tiprack_1000ul/1":{"displayName":"Opentrons Flex 96 Tip Rack 1000 µL (8)","labwareDefURI":"opentrons/opentrons_flex_96_tiprack_1000ul/1"},"98f7b3bc-f465-4876-9dc6-949d796d2d0c:opentrons/opentrons_flex_96_tiprack_1000ul/1":{"displayName":"Opentrons Flex 96 Tip Rack 1000 µL (9)","labwareDefURI":"opentrons/opentrons_flex_96_tiprack_1000ul/1"},"6e8b0426-4915-4a4d-85b6-d740bca07f35:opentrons/opentrons_flex_96_tiprack_1000ul/1":{"displayName":"Opentrons Flex 96 Tip Rack 1000 µL (10)","labwareDefURI":"opentrons/opentrons_flex_96_tiprack_1000ul/1"},"3aabe684-5254-439e-98cd-1096515284fe:opentrons/opentrons_flex_96_tiprack_1000ul/1":{"displayName":"Opentrons Flex 96 Tip Rack 1000 µL (11)","labwareDefURI":"opentrons/opentrons_flex_96_tiprack_1000ul/1"},"eb25a5e3-8be6-4ba0-9dc9-35a95305f175:opentrons/opentrons_flex_96_tiprack_1000ul/1":{"displayName":"Opentrons Flex 96 Tip Rack 1000 µL (12)","labwareDefURI":"opentrons/opentrons_flex_96_tiprack_1000ul/1"},"d395af7f-9c85-4d9c-9d30-569a05de86c0:opentrons/opentrons_flex_96_tiprack_1000ul/1":{"displayName":"Opentrons Flex 96 Tip Rack 1000 µL (13)","labwareDefURI":"opentrons/opentrons_flex_96_tiprack_1000ul/1"},"e633da9d-d2ce-4f1d-a8a3-35ec6f89d910:opentrons/opentrons_flex_96_tiprack_1000ul/1":{"displayName":"Opentrons Flex 96 Tip Rack 1000 µL (14)","labwareDefURI":"opentrons/opentrons_flex_96_tiprack_1000ul/1"},"f3adca02-de60-41d7-84d5-be0829327053:opentrons/opentrons_flex_96_tiprack_1000ul/1":{"displayName":"Opentrons Flex 96 Tip Rack 1000 µL (15)","labwareDefURI":"opentrons/opentrons_flex_96_tiprack_1000ul/1"},"159dad22-035c-4cc5-acc8-6d2c66f81b31:opentrons/opentrons_flex_96_tiprack_1000ul/1":{"displayName":"Opentrons Flex 96 Tip Rack 1000 µL (16)","labwareDefURI":"opentrons/opentrons_flex_96_tiprack_1000ul/1"},"fc093d83-32f7-4f1b-8964-2b3c37896655:opentrons/nest_96_wellplate_2ml_deep/2":{"displayName":"NEST 96 Deep Well Plate 2mL","labwareDefURI":"opentrons/nest_96_wellplate_2ml_deep/2"}}}},"metadata":{"protocolName":"Zymo_Magbead_DNA_Cells-Flex_96_channel  Truly fixed","author":"Opentrons ","description":"https://library.opentrons.com/p/Zymo_Magbead_DNA_Flex_96-Cells \n\n","created":1733416217918,"lastModified":1749504079499,"category":null,"subcategory":null,"tags":[],"source":"Protocol Designer"}}"""
