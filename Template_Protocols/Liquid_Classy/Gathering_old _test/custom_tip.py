from opentrons import protocol_api

requirements = {"robotType": "Flex", "apiLevel":"2.21"}

def run(protocol: protocol_api.ProtocolContext):
    plate = protocol.load_labware(
        load_name="corning_96_wellplate_360ul_flat",
        location="D1")
    tiprack_1 = protocol.load_labware(
        load_name="liquidclass_96_tiprack_210ul",
        location="D2")
    trash = protocol.load_trash_bin("A3")
    pipette = protocol.load_instrument(
        instrument_name="flex_1channel_1000",
        mount="left",
    tip_racks=[tiprack_1])

    pipette.pick_up_tip()
    pipette.aspirate(100, plate["A1"])
    pipette.dispense(100, plate["B1"])
    pipette.drop_tip()