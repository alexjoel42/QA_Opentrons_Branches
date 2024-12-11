from typing import List
from opentrons.protocol_api import ProtocolContext, Labware

metadata = {"protocolName": "off deck labware break REGULAR LABWARE"}
requirements = {"robotType": "Flex", "apiLevel": "2.20"}

LID_COUNT = 5
LID_DEFINITION = "opentrons_tough_pcr_auto_sealing_lid"
LID_BOTTOM_DEFINITION = "opentrons_tough_pcr_auto_sealing_lid"


def run(protocol: ProtocolContext):
    # Tiprack to occupy space above test trashbin for collision checking
    # tiprack = protocol.load_labware("opentrons_flex_96_tiprack_200ul", 'C3')

    tiprack_1000 = protocol.load_labware(load_name='opentrons_flex_96_tiprack_50ul', location="B2")
    pipette = protocol.load_instrument("flex_8channel_50", "right", tip_racks=[tiprack_1000])
    pipette.pick_up_tip()


    thermocycler = protocol.load_module("thermocyclerModuleV2")
    thermocycler.open_lid()
    plate_in_cycler = thermocycler.load_labware(
        "opentrons_96_wellplate_200ul_pcr_full_skirt"
    )
    trash = protocol.load_trash_bin('A3')
    #pipette.aspirate(10, plate_in_cycler['A1'])

    lid = protocol.load_labware('opentrons_96_wellplate_200ul_pcr_full_skirt', "C4")
    '''
    deck_riser_adapter = protocol.load_adapter("opentrons_flex_deck_riser", 'C4')
    lid = deck_riser_adapter.load_labware(LID_BOTTOM_DEFINITION)
    '''
    protocol.move_labware(
        lid,
        "D2",
        use_gripper=True,
    )

