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

    protocol.capture_image(home_before=True, filename="Minimum_File_Length *****")


