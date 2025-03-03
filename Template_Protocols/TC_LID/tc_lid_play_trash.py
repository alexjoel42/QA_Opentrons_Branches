from typing import List
from opentrons.protocol_api import ProtocolContext, Labware

metadata = {"protocolName": "Opentrons Flex TC Lid Trash Test"}
requirements = {"robotType": "Flex", "apiLevel": "2.20"}


LID_COUNT = 5
LID_DEFINITION = "opentrons_tough_pcr_auto_sealing_lid"
LID_BOTTOM_DEFINITION = "opentrons_tough_pcr_auto_sealing_lid"

def run(protocol: ProtocolContext):
    # Tiprack to occupy space above test trashbin for collision checking
    tiprack = protocol.load_labware("opentrons_flex_96_tiprack_200ul", 'C3')
    thermocycler = protocol.load_module("thermocyclerModuleV2")
    thermocycler.open_lid()
    plate_in_cycler = thermocycler.load_labware(
        "opentrons_96_wellplate_200ul_pcr_full_skirt"
    )
    trash = protocol.load_trash_bin('A3')
    deck_riser_adapter = protocol.load_adapter("opentrons_flex_deck_riser", 'D1')
    lids: List[Labware] = [deck_riser_adapter.load_labware(LID_BOTTOM_DEFINITION, 'D1')]
    for i in range(LID_COUNT - 1):
        lids.append(lids[-1].load_labware(LID_DEFINITION))
    lids.reverse()  # NOTE: reversing to more easily loop through lids from top-to-bottom

    for lid in lids:
        protocol.move_labware(
            lid,
            plate_in_cycler,
            use_gripper=True,
        )
        thermocycler.close_lid()
        thermocycler.open_lid()
        protocol.move_labware(
            lid,
            trash,
            use_gripper=True,
        )




