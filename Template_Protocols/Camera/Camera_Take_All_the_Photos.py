from opentrons.protocol_api import ProtocolContext
Envir_Robot = 'OT-2'
Envir_Robot = 'Flex'

metadata = {
    "protocolName": "Camera Test",
    "author": "Opentrons <protocols@opentrons.com>",
}
requirements = {
    "robotType": "{Enivr_Robot}".format(Enivr_Robot=Envir_Robot),
    "apiLevel": "2.28",
}

def run(protocol: ProtocolContext) -> None:
    if Envir_Robot == 'OT-2':
        for i in range(500):
            protocol.capture_image(home_before=False, filename="500", zoom=2.0, contrast=10)
        protocol.comment('500')
        for i in range(1000):
            protocol.comment('1500')  
            protocol.capture_image(home_before=False, filename="1500", zoom=2.0, contrast=10)
        for i in range(5000):
            protocol.comment('6500')
            protocol.capture_image(home_before=False, filename="6500", zoom=2.0, contrast=10)



        else:
            for i in range(5000):
                protocol.capture_image(home_before=False, filename="5000-flex", zoom=2.0, contrast=10)
                protocol.comment('5000')
            for i in range(10000):
                protocol.comment('15000')  
                protocol.capture_image(home_before=False, filename="15000-flex", zoom=2.0, contrast=10)
            for i in range(15000):
                protocol.comment('30000')
                protocol.capture_image(home_before=False, filename="30000-flex", zoom=2.0, contrast=10)
            