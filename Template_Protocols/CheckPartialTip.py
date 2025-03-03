from opentrons import protocol_api
from opentrons.protocol_api import SINGLE, ALL

requirements = {"robotType": "Flex", "apiLevel": "2.22"}

def run(protocol: protocol_api.ProtocolContext):
    partial_rack = protocol.load_labware(
        load_name="opentrons_flex_96_tiprack_1000ul",
        location="B2"
    )
    trash = protocol.load_trash_bin("A3")
    pipette = protocol.load_instrument("flex_8channel_1000", mount="left")
    pipette.configure_nozzle_layout(
        style=SINGLE,
        start="H1",
        tip_racks=[partial_rack]
    )
    pipette.pick_up_tip()
    pipette.drop_tip()