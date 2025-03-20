from typing import List
from opentrons.protocol_api import ProtocolContext, Labware

metadata = {"protocolName": "Opentrons Flex TC Lid off deck Test, pipette break"}
requirements = {"robotType": "Flex", "apiLevel": "2.23"}


LID_COUNT = 5
LID_DEFINITION = "opentrons_tough_pcr_auto_sealing_lid"
LID_BOTTOM_DEFINITION = "opentrons_tough_pcr_auto_sealing_lid"
DECK_RISER_NAME = "opentrons_flex_deck_riser"


def run(protocol: ProtocolContext):
    # Tiprack to occupy space above test trashbin for collision checking
    #tiprack = protocol.load_labware("opentrons_flex_96_tiprack_200ul", 'C3')

    tiprack_1000 = protocol.load_labware(load_name='opentrons_flex_96_tiprack_50ul', location="B2")
    pipette = protocol.load_instrument("flex_8channel_50", "right", tip_racks=[tiprack_1000])
    thermocycler = protocol.load_module("thermocyclerModuleV2")
    thermocycler.open_lid()
    plate_in_cycler = thermocycler.load_labware(
        "biorad_96_wellplate_200ul_pcr"
    )
    trash = protocol.load_trash_bin('A3')
    #pipette.aspirate(10, plate_in_cycler['A1'])
    lid = protocol.load_lid_stack(LID_DEFINITION, "A2", 5, adapter =DECK_RISER_NAME )
    '''
    for i in range(LID_COUNT - 2):
        lids.append(lids[-1].load_labware(LID_DEFINITION))
    lids.reverse()  # NOTE: reversing to more easily loop through lids from top-to-bottom
    i = 0
''' 
    for i in range(4):
        protocol.move_lid(
            lid,
            plate_in_cycler,
            use_gripper=True,
        )
        thermocycler.close_lid()
        thermocycler.open_lid()
        protocol.move_lid(plate_in_cycler,"D3",use_gripper=True)

  
    




        






