from typing import List, Dict, Any, Optional
from opentrons.protocol_api import ProtocolContext, Labware

metadata = {"protocolName": "Opentrons Flex Deck Riser with TC Lids Test"}
requirements = {"robotType": "Flex", "apiLevel": "2.23"}

LID_DEFINITION = "opentrons_tough_pcr_auto_sealing_lid"
DECK_RISER_NAME = "opentrons_flex_deck_riser"
USING_THERMOCYCLER = True

def run(protocol: ProtocolContext):
    # SETUP
    deck_riser_adapter = protocol.load_adapter(DECK_RISER_NAME, "A2")
    trash = protocol.load_trash_bin("A3")

    stack = protocol.load_lid_stack(LID_DEFINITION, "B2", 5)
    
    thermocycler = protocol.load_module("thermocyclerModuleV2")
    thermocycler.open_lid()
    plate_in_cycler = thermocycler.load_labware("armadillo_96_wellplate_200ul_pcr_full_skirt")


    protocol.move_lid(stack, plate_in_cycler, True)

    # Move the lid to the empty riser, creating a new lid stack
    used_stack = protocol.move_lid(plate_in_cycler, deck_riser_adapter, True)
    protocol.move_lid(stack, plate_in_cycler, True)
    protocol.move_lid(plate_in_cycler, used_stack, True)
    protocol.move_lid(stack, plate_in_cycler, True)
    protocol.move_lid(plate_in_cycler, used_stack, True)
    protocol.move_lid(stack, plate_in_cycler, True)
    protocol.move_lid(plate_in_cycler, used_stack, True)
    protocol.move_lid(stack, plate_in_cycler, True)
    protocol.move_lid(plate_in_cycler, used_stack, True)

    # Trash all the lids
    protocol.move_lid(used_stack, trash, True)
    protocol.move_lid(used_stack, trash, True)
    protocol.move_lid(used_stack, trash, True)
    protocol.move_lid(used_stack, trash, True)
    protocol.move_lid(used_stack, trash, True)
