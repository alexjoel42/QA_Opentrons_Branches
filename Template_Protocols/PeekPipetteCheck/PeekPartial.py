from opentrons import protocol_api
from opentrons.protocol_api import SINGLE, ALL

requirements = {"robotType": "Flex", "apiLevel": "2.22"}

def run(protocol: protocol_api.ProtocolContext):
    partial_rack = protocol.load_labware(
        load_name="opentrons_flex_96_tiprack_1000ul",
        location="C3"
    )
    trash = protocol.load_trash_bin("A3")
    pipette = protocol.load_instrument(
        instrument_name="flex_8channel_1000_em",
        mount="right"
    )
    pipette.configure_nozzle_layout(
        style=SINGLE,
        start="A1",
        tip_racks=[partial_rack]
    )
    plate = protocol.load_labware(
        load_name="corning_96_wellplate_360ul_flat",
        location="C2")
    pipette.pick_up_tip()

    pipette.aspirate(10, plate["A1"])
    protocol.delay(seconds=30)
    pipette.dispense(10, plate["A1"].bottom(z=0))
    pipette.blow_out()
    pipette.drop_tip()