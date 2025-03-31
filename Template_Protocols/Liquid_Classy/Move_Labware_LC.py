
from typing import List
from opentrons import protocol_api, types
from opentrons.protocol_api import Labware
from opentrons.protocol_api.module_contexts import (
    FlexStackerContext,
)


metadata = {
    "protocolName": "Switching tip rack",
    "author": "QA team",
}

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.23",
}


#################
### CONSTANTS ###
#################

##############################
# Runtime Parameters Support #
##############################

# -------------------------- #
# Added in API version: 2.18 #
# -------------------------- #


def add_parameters(parameters: protocol_api.Parameters):
    """This is the standard use of parameters"""

    # We are using the defaults for every case.
    # Other tests cover regression testing for
    # other types of parameters and UI appearance
    # there are many tests in Analyses Battery that cover errors and edge cases
    parameters.add_str(
        variable_name="pipette_name_left",
        display_name="Pipette name to use",
        description="Configuration of QA test to perform",
        choices=[{"display_name": "flex_96channel_1000", "value": "flex_96channel_1000"},
                 {"display_name": "flex_8_channel_1000", "value": "flex_8_channel_1000"},
                 {"display_name": "flex_8_channe_50ul", "value": "flex_8_channe_50ul"}],
        default="flex_96channel_1000",

        )

   
import itertools
def run(ctx: protocol_api.ProtocolContext) -> None:
    waste_chute = ctx.load_waste_chute()
    
    
    
    if ctx.params.pipette_name_left == 'flex_96channel_1000' or ctx.params.pipette_name_right == 'flex_96channel_1000':
        my_adapter_50 = ctx.load_adapter("opentrons_flex_96_tiprack_adapter", 'A2')
        tip_rack_50 = my_adapter_50.load_labware("opentrons_flex_96_tiprack_50ul")
        my_adapter_50_second = ctx.load_adapter("opentrons_flex_96_tiprack_adapter", 'B2')
        tip_rack_200 = my_adapter_50_second.load_labware("opentrons_flex_96_tiprack_200ul")
        tip_racks =[tip_rack_50,tip_rack_200 ]
        pipette_left = ctx.load_instrument('flex_96channel_1000', mount = 'left', tip_racks = tip_racks)
        pipette_left.trash_container = waste_chute
    else:
        pipette_left = ctx.load_instrument(ctx.params.pipette_name_left, mount = 'left', tip_racks =tip_racks)
        chute = ctx.load_waste_chute()
    water_class = ctx.define_liquid_class("water")
    glycerol_50 = ctx.define_liquid_class("glycerol_50")
    ethanol_80 = ctx.define_liquid_class("ethanol_80")
    classy = [water_class,glycerol_50, ethanol_80 ]
    plate_1 = ctx.load_labware('opentrons_96_wellplate_200ul_pcr_full_skirt','B3' )
    plate_2 = ctx.load_labware('opentrons_96_wellplate_200ul_pcr_full_skirt', 'C3')
    for i in range(8):
        pipette_left.transfer_liquid(volume = 50, source = plate_1['A1'], dest=plate_2['A1'], liquid_class =classy[2], new_tip = 'once')
    ''' 
    pipette_left.transfer_liquid(volume = 200, source = plate_1['A1'], dest=plate_2['A1'], liquid_class =classy[3], new_tip = 'once')
    pipette_left.transfer_liquid(volume = 200, source = plate_1['A1'], dest=plate_2['A1'], liquid_class =classy[3], new_tip = 'always')
    


    '''


   



