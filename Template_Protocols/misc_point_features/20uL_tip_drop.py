'''

'''

from opentrons import protocol_api

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.28",
}

metadata = {
    "protocolName": "p50 right mount meniscus no probe",
}


def run(protocol: protocol_api.ProtocolContext):
    waste = protocol.load_waste_chute()
    tiprack = protocol.load_labware("opentrons_flex_96_tiprack_50ul", "B2")
    pipette = protocol.load_instrument(
        "flex_8channel_50", mount="right", tip_racks=[tiprack]
    )
    plate = protocol.load_labware("opentrons_96_wellplate_200ul_pcr_full_skirt", "C2")
    pipette.pick_up_tip()
    water= protocol.define_liquid(name = "water", description="sample", display_color="#0000FF")
    plate['A1'].load_liquid(liquid = water, volume = 1)

    pipette.aspirate(20, location=plate["A1"].meniscus(z=-1), end_location=plate["A1"].meniscus(z=-1))
    pipette.drop_tip()
   

