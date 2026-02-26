from opentrons.protocol_api import ProtocolContext
import sys 


metadata = {
    "protocolName": "Flex Stacker Camera Test",
    "author": "Opentrons <protocols@opentrons.com>",
}
requirements = {
    "robotType": "Flex",
    "apiLevel": "2.27",
}

def run(protocol: ProtocolContext) -> None:
    """Protocol."""
    trash = protocol.load_trash_bin('A3')
    tiprack_1 = protocol.load_labware("opentrons_flex_96_tiprack_50ul", "C2")
    tiprack_2 = protocol.load_labware("opentrons_flex_96_tiprack_50ul", "C3")
    trash = protocol.load_waste_chute()
    protocol.capture_image(home_before=True, filename="Example_1")
    pipette_50 = protocol.load_instrument("flex_8channel_50", "left", tip_racks=[tiprack_1, tiprack_2])
    pipette_50.pick_up_tip()
    pipette_50.drop_tip()

    protocol.delay(seconds=1)
    load_labware = protocol.load_labware
    protocol.capture_image(home_before=True, filename="Example2")
    protocol.home()
