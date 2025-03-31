
from opentrons import protocol_api

metadata = {
    "protocolName": "Module pipetting",
    "author": "QA team",
}

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.23",
}


TIPRACK_96_ADAPTER_NAME = "opentrons_flex_96_tiprack_adapter"
TIPRACK_96_NAME = "opentrons_flex_96_tiprack_1000ul"
PIPETTE_96_CHANNEL_NAME = "flex_96channel_1000"

def run(ctx: protocol_api.ProtocolContext) -> None:

    ################
    ### FIXTURES ###
    ################

    waste_chute = ctx.load_waste_chute()

    ###############
    ### MODULES ###
    ###############


    #######################
    ### MODULE ADAPTERS ###
    #######################
    Source_plate = ctx.load_labware('opentrons_96_wellplate_200ul_pcr_full_skirt', 'A3')
    Dest_1 =  ctx.load_labware('opentrons_96_wellplate_200ul_pcr_full_skirt', 'B1')
    Dest_2 =  ctx.load_labware('opentrons_96_wellplate_200ul_pcr_full_skirt', 'B2')
    my_adapter_50 = ctx.load_adapter("opentrons_flex_96_tiprack_adapter", 'A2')
    tip_rack = my_adapter_50.load_labware("opentrons_flex_96_tiprack_50ul")
    pipette_96_channel = ctx.load_instrument(PIPETTE_96_CHANNEL_NAME, mount="left", tip_racks=[tip_rack], liquid_presence_detection=True)
    pipette_96_channel.trash_container = waste_chute
    water_class = ctx.define_liquid_class("water")
    glycerol_50 = ctx.define_liquid_class("glycerol_50")
    ethanol_80 = ctx.define_liquid_class("ethanol_80")
    pipette_96_channel.pick_up_tip()
    pipette_96_channel.consolidate_liquid(volume= 20, source = Source_plate['A1'], dest = [Dest_1['A1'], Dest_2['A1']], liquid_class = ethanol_80, new_tip = 'Never' )
    pipette_96_channel.drop_tip()
