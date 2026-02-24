from opentrons.protocol_api import ProtocolContext

metadata = {
    "protocolName": "OT-2 Camera Test",
    "author": "Opentrons <protocols@opentrons.com>",
}
requirements = {
    "robotType": "OT-2",
    "apiLevel": "2.27",
}

def run(protocol: ProtocolContext) -> None:
    """Protocol."""
    #CONTRAST PICS
    protocol.capture_image(home_before=True, filename="This is the longest Filename Ever and it will cause suffering")
