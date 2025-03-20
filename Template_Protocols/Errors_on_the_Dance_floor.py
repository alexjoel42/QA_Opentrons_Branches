from opentrons import protocol_api
from opentrons.protocol_api import SINGLE, ALL

requirements = {"robotType": "Flex", "apiLevel": "2.21"}
metadata = {"protocolName": "this is an error"}

def run(protocol: protocol_api.ProtocolContext):
    tip_rack_1 = protocol.load_labware(
        load_name="opentrons_flex_96_tiprack_50ul",
        location="D4"
    )

    trash = protocol.load_trash_bin("B3")
    pipette = protocol.load_instrument(
        instrument_name = "flex_1channel_50",
        mount = "right",
        tip_racks=[tip_rack_1])

    plate = protocol.load_labware("opentrons_96_wellplate_200ul_pcr_full_skirt", "C3")
    protocol.move_labware(labware=plate, new_location="C2")
    protocol.move_labware(
        labware=tip_rack_1,
        new_location="D2"
    )
    ''' 
    protocol.move_labware(
        labware=tip_rack_1,
        new_location="C2"
    )
    '''

    pipette.pick_up_tip()
    pipette.aspirate(10, plate['A1'])
    pipette.return_tip()
    protocol.comment('this is an error.')
    protocol.comment('this is an error.')
    protocol.pause('this is an error')
    protocol.delay(minutes = 2, msg = 'this is an error')




