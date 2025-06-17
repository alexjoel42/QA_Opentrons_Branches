import json
from contextlib import nullcontext as pd_step
from opentrons import protocol_api, types

metadata = {
    "protocolName": "Double Me Offsets",
    "author": "Opentrons",
    "description": "Will the offsets double",
}

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.23",
}

def run(protocol: protocol_api.ProtocolContext) -> None:
     # Load Modules:
    thermocycler_module_1 = protocol.load_module("thermocyclerModuleV2", "B1")
    magnetic_block_1 = protocol.load_module("magneticBlockV1", "C2")
    # Load Adapters:
    adapter_1 = protocol.load_adapter(
        "opentrons_flex_96_tiprack_adapter",
        location="D1"
    )
    # Load Labware:
    tip_rack_1 = adapter_1.load_labware(
        "opentrons_flex_96_filtertiprack_50ul")
    well_plate_1 = magnetic_block_1.load_labware(
        "opentrons_96_wellplate_200ul_pcr_full_skirt"
    )
    well_plate_2 = protocol.load_labware('nest_96_wellplate_2000ul', location="B2")

    # Load Pipettes:
    pipette = protocol.load_instrument("flex_96channel_1000", tip_racks=[tip_rack_1])

    # Load Waste Chute:
    waste_chute = protocol.load_waste_chute()

    # Define Liquids:
    liquid_1 = protocol.define_liquid(
        "H20",
        display_color="#b925ff",
    )

    # Load Liquids:
    well_plate_1["A1"].load_liquid(liquid_1, 100)
    well_plate_1["B1"].load_liquid(liquid_1, 100)
    well_plate_1["C1"].load_liquid(liquid_1, 100)
    well_plate_1["D1"].load_liquid(liquid_1, 100)
    well_plate_1["E1"].load_liquid(liquid_1, 100)
    well_plate_1["F1"].load_liquid(liquid_1, 100)
    well_plate_1["G1"].load_liquid(liquid_1, 100)
    well_plate_1["H1"].load_liquid(liquid_1, 100)
    well_plate_1["A2"].load_liquid(liquid_1, 100)
    well_plate_1["B2"].load_liquid(liquid_1, 100)
    well_plate_1["C2"].load_liquid(liquid_1, 100)
    well_plate_1["D2"].load_liquid(liquid_1, 100)
    well_plate_1["E2"].load_liquid(liquid_1, 100)
    well_plate_1["F2"].load_liquid(liquid_1, 100)
    well_plate_1["G2"].load_liquid(liquid_1, 100)
    well_plate_1["H2"].load_liquid(liquid_1, 100)
    well_plate_1["A3"].load_liquid(liquid_1, 100)
    well_plate_1["B3"].load_liquid(liquid_1, 100)
    well_plate_1["C3"].load_liquid(liquid_1, 100)
    well_plate_1["D3"].load_liquid(liquid_1, 100)
    well_plate_1["E3"].load_liquid(liquid_1, 100)
    well_plate_1["F3"].load_liquid(liquid_1, 100)
    well_plate_1["G3"].load_liquid(liquid_1, 100)
    well_plate_1["H3"].load_liquid(liquid_1, 100)
    well_plate_1["A4"].load_liquid(liquid_1, 100)
    well_plate_1["B4"].load_liquid(liquid_1, 100)
    well_plate_1["C4"].load_liquid(liquid_1, 100)
    well_plate_1["D4"].load_liquid(liquid_1, 100)
    well_plate_1["E4"].load_liquid(liquid_1, 100)
    well_plate_1["F4"].load_liquid(liquid_1, 100)
    well_plate_1["G4"].load_liquid(liquid_1, 100)
    well_plate_1["H4"].load_liquid(liquid_1, 100)
    well_plate_1["A5"].load_liquid(liquid_1, 100)
    well_plate_1["B5"].load_liquid(liquid_1, 100)
    well_plate_1["C5"].load_liquid(liquid_1, 100)
    well_plate_1["D5"].load_liquid(liquid_1, 100)
    well_plate_1["E5"].load_liquid(liquid_1, 100)
    well_plate_1["F5"].load_liquid(liquid_1, 100)
    well_plate_1["G5"].load_liquid(liquid_1, 100)
    well_plate_1["H5"].load_liquid(liquid_1, 100)
    well_plate_1["A6"].load_liquid(liquid_1, 100)
    well_plate_1["B6"].load_liquid(liquid_1, 100)
    well_plate_1["C6"].load_liquid(liquid_1, 100)
    well_plate_1["D6"].load_liquid(liquid_1, 100)
    well_plate_1["E6"].load_liquid(liquid_1, 100)
    well_plate_1["F6"].load_liquid(liquid_1, 100)
    well_plate_1["G6"].load_liquid(liquid_1, 100)
    well_plate_1["H6"].load_liquid(liquid_1, 100)
    well_plate_1["A7"].load_liquid(liquid_1, 100)
    well_plate_1["B7"].load_liquid(liquid_1, 100)
    well_plate_1["C7"].load_liquid(liquid_1, 100)
    well_plate_1["D7"].load_liquid(liquid_1, 100)
    well_plate_1["E7"].load_liquid(liquid_1, 100)
    well_plate_1["F7"].load_liquid(liquid_1, 100)
    well_plate_1["G7"].load_liquid(liquid_1, 100)
    well_plate_1["H7"].load_liquid(liquid_1, 100)
    well_plate_1["A8"].load_liquid(liquid_1, 100)
    well_plate_1["B8"].load_liquid(liquid_1, 100)
    well_plate_1["C8"].load_liquid(liquid_1, 100)
    well_plate_1["D8"].load_liquid(liquid_1, 100)
    well_plate_1["E8"].load_liquid(liquid_1, 100)
    well_plate_1["F8"].load_liquid(liquid_1, 100)
    well_plate_1["G8"].load_liquid(liquid_1, 100)
    well_plate_1["H8"].load_liquid(liquid_1, 100)
    well_plate_1["A9"].load_liquid(liquid_1, 100)
    well_plate_1["B9"].load_liquid(liquid_1, 100)
    well_plate_1["C9"].load_liquid(liquid_1, 100)
    well_plate_1["D9"].load_liquid(liquid_1, 100)
    well_plate_1["E9"].load_liquid(liquid_1, 100)
    well_plate_1["F9"].load_liquid(liquid_1, 100)
    well_plate_1["G9"].load_liquid(liquid_1, 100)
    well_plate_1["H9"].load_liquid(liquid_1, 100)
    well_plate_1["A10"].load_liquid(liquid_1, 100)
    well_plate_1["B10"].load_liquid(liquid_1, 100)
    well_plate_1["C10"].load_liquid(liquid_1, 100)
    well_plate_1["D10"].load_liquid(liquid_1, 100)
    well_plate_1["E10"].load_liquid(liquid_1, 100)
    well_plate_1["F10"].load_liquid(liquid_1, 100)
    well_plate_1["G10"].load_liquid(liquid_1, 100)
    well_plate_1["H10"].load_liquid(liquid_1, 100)
    well_plate_1["A11"].load_liquid(liquid_1, 100)
    well_plate_1["B11"].load_liquid(liquid_1, 100)
    well_plate_1["C11"].load_liquid(liquid_1, 100)
    well_plate_1["D11"].load_liquid(liquid_1, 100)
    well_plate_1["E11"].load_liquid(liquid_1, 100)
    well_plate_1["F11"].load_liquid(liquid_1, 100)
    well_plate_1["G11"].load_liquid(liquid_1, 100)
    well_plate_1["H11"].load_liquid(liquid_1, 100)
    well_plate_1["A12"].load_liquid(liquid_1, 100)
    well_plate_1["B12"].load_liquid(liquid_1, 100)
    well_plate_1["C12"].load_liquid(liquid_1, 100)
    well_plate_1["D12"].load_liquid(liquid_1, 100)
    well_plate_1["E12"].load_liquid(liquid_1, 100)
    well_plate_1["F12"].load_liquid(liquid_1, 100)
    well_plate_1["G12"].load_liquid(liquid_1, 100)
    well_plate_1["H12"].load_liquid(liquid_1, 100)

    # PROTOCOL STEPS

    # Step 1:
    pipette.pick_up_tip()
    pipette.aspirate(10, well_plate_1['A1'])
    pipette.dispense(10, well_plate_2)
    

    # Step 2:
    thermocycler_module_1.open_lid()

    # Step 3:
    protocol.move_labware(well_plate_1, thermocycler_module_1, use_gripper=True)

    # step 4
    pipette.mix(well_plate_1, 10, 1)
    