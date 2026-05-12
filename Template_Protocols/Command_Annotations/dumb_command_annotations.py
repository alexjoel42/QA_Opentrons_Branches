from opentrons import protocol_api

metadata = {"protocolName": "Break leaked GroupedSteps", "author": "QA"}
requirements = {"robotType": "Flex", "apiLevel": "2.29"}

def run(protocol: protocol_api.ProtocolContext) -> None:
    protocol.load_trash_bin("A3")
    protocol.create_and_start_step_group("first", "no end_group() called")
    protocol.comment("still inside first group")
    with protocol.group_steps("second"):  # same ValueError as nested
        protocol.comment("unreachable")