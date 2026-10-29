from opentrons import protocol_api
metadata = {
    "protocolName": "Module disconnects",
    "author": "QA team",
}

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.29",
}


def run(protocol: protocol_api.ProtocolContext) -> None:
    waste = protocol.load_waste_chute()
    for i in range(600):
        protocol.comment("This is round 1 600 comments")
