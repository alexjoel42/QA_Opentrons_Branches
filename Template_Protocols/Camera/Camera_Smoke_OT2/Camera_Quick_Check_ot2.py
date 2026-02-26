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
    protocol.capture_image(home_before=True, filename="Example_photo_1")
    protocol.delay(seconds=1)
    protocol.capture_image(home_before=True, filename="Example_photo_2")
    protocol.home()
    protocol.capture_image(home_before=True, filename="Example_photo_3")
    protocol.delay(seconds=1)
    protocol.capture_image(home_before=False, filename="Example_photo_4")
    protocol.delay(seconds=1)
    protocol.capture_image(home_before=True, filename="Example_photo_5")
