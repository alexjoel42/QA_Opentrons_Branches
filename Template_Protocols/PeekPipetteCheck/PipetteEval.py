from opentrons import protocol_api
from opentrons.protocol_api import PARTIAL_COLUMN, ALL, SINGLE
requirements = {"robotType": "Flex", "apiLevel": "2.22"}
metadata = {"protocolName": "Peek pipette eval"}


def run(protocol: protocol_api.ProtocolContext):
    plate = protocol.load_labware(
        load_name="corning_96_wellplate_360ul_flat",
        location="D1")
    tiprack_1 = protocol.load_labware(
        load_name="opentrons_flex_96_tiprack_50ul",
        location="D2")
    trash = protocol.load_trash_bin("A3")
    pipette = protocol.load_instrument(
        instrument_name="flex_8channel_1000_em",
        mount="right",
        tip_racks=[tiprack_1])

    pipette.flow_rate.aspirate = 400
    pipette.flow_rate.dispense = 5
    pipette.flow_rate.blow_out = 1
    pipette.pick_up_tip()
    pipette.aspirate(5, plate["A1"])
    pipette.dispense(5, plate["A1"])
    pipette.blow_out()
    pipette.return_tip()
    pipette.pick_up_tip()
    pipette.configure_for_volume(12)
    pipette.aspirate(10, plate["A1"])
    protocol.delay(seconds=30)
    pipette.dispense(10, plate["A1"].bottom(z=0))
    pipette.drop_tip()



