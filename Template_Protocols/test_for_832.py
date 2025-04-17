from opentrons import protocol_api
from opentrons import types
from opentrons.protocol_api import SINGLE, ALL
import math
import numpy as np

metadata = {
    "protocolName": "Moving Shortly",
    "author": "QA",
    "description": "Moving very short distances",
}

requirements = {"robotType": "Flex", "apiLevel": "2.22"}


TIPRACK_96_ADAPTER_NAME = "opentrons_flex_96_tiprack_adapter"
TIPRACK_96_NAME = "opentrons_flex_96_tiprack_1000ul"
PIPETTE_96_CHANNEL_NAME = "flex_96channel_1000"
def run(protocol: protocol_api.ProtocolContext):
    tip_rack_1 = protocol.load_labware(TIPRACK_96_NAME, "A2", adapter=TIPRACK_96_ADAPTER_NAME)
    
    tip_racks = [tip_rack_1]

    ##########################
    ### PIPETTE DEFINITION ###
    ##########################

    pipette = protocol.load_instrument(PIPETTE_96_CHANNEL_NAME, mount="left", tip_racks=tip_racks, liquid_presence_detection=True)
    pipette.trash_container = protocol.load_waste_chute()
    Test_Labware = protocol.load_labware('nest_1_reservoir_290ml', 'D2')
    Test_Labware_2 = protocol.load_labware('nest_96_wellplate_2ml_deep', 'B2')
    pipette.pick_up_tip()
    x = 0
    for boop in range(10):
        for beep in range(0,100):
            for i in range(0,10):
                pipette.move_to(Test_Labware['A1'].top(z=-i/10))
                print('taco')
        for i in range(100):
            for i in range(10):
                pipette.touch_tip(Test_Labware_2['A2'], radius=0.1, speed= 80.0)
                print('taco')
            
            

