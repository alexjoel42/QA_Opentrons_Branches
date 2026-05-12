from opentrons import protocol_api

metadata = {"protocolName": "Exception then new group", "author": "QA"}
requirements = {"robotType": "Flex", "apiLevel": "2.29"}

def run(protocol: protocol_api.ProtocolContext) -> None:
    protocol.load_trash_bin("A3")
    try:
        with protocol.group_steps("dies"):
            protocol.comment("before boom")
            raise RuntimeError("intentional")
    except RuntimeError:
        pass
    with protocol.group_steps("after"):  # should work if finally cleared annotation_ids
        protocol.comment("recovered")