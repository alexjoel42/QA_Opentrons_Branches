
from opentrons import protocol_api, types

requirements = {
    "robotType": "OT-2",
    "apiLevel": "2.22",
}

def run(protocol: protocol_api.ProtocolContext):
    # Load Labware:
    tip_rack_1 = protocol.load_labware(
        "opentrons_96_tiprack_300ul",
        location="2",
        namespace="opentrons",
        version=1,
    )
    reservoir_1 = protocol.load_labware(
        "agilent_1_reservoir_290ml",
        location="3",
        namespace="opentrons",
        version=2,
    )
    well_plate_1 = protocol.load_labware(
        "armadillo_96_wellplate_200ul_pcr_full_skirt",
        location="6",
        label="(Retired) Armadillo 96 Well Plate 200 µL PCR Full Skirt",
        namespace="opentrons",
        version=3,
    )

    # Load Pipettes:
    pipette_right = protocol.load_instrument("p300_multi_gen2", "left", tip_racks=[tip_rack_1])

    # Define Liquids:
    liquid_1 = protocol.define_liquid(
        "H20",
        display_color="#b925ff",
    )

    # Load Liquids:
    reservoir_1["A1"].load_liquid(liquid_1, 100000)
    # PROTOCOL STEPS

    # Step 1:
    pipette_right.pick_up_tip(location=tip_rack_1)
    pipette_right.aspirate(
        volume=100,
        location = reservoir_1["A1"],
        rate=94 / pipette_right.flow_rate.aspirate,
    )
    pipette_right.return_tip()
