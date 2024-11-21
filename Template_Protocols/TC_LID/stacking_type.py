from typing import List, Dict, Any, Optional
from opentrons.protocol_api import ProtocolContext, Labware

metadata = {"Stacking a deep well plate on its adapter "}
requirements = {"robotType": "Flex", "apiLevel": "2.21"}


def run(protocol: ProtocolContext):
    temp_mod = protocol.load_module(
        module_name="temperature module gen2", location="D1"
    )
    adapter = temp_mod.load_adapter("opentrons_96_deep_well_temp_mod_adapter")
    stack = protocol.load_labware("nest_96_wellplate_2ml_deep",'A1' )

    protocol.move_labware(stack, adapter)



