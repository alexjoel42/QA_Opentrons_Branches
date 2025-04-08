
from opentrons import protocol_api

metadata = {
    "protocolName": "Module pipetting",
    "author": "QA team",
}

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.23",
}


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
    tip_racks = []
    slots = ['A2','C1','C2']
    for slot in slots:
        tip_rack = ctx.load_labware("opentrons_flex_96_tiprack_50ul", slot)
        tip_racks.append(tip_rack)
    pipette_96_channel = ctx.load_instrument('flex_8channel_50', mount="right", tip_racks=tip_racks, liquid_presence_detection=False)
    pipette_96_channel.trash_container = waste_chute
    water_class = ctx.define_liquid_class("water")
    glycerol_50 = ctx.define_liquid_class("glycerol_50")
    ethanol_80 = ctx.define_liquid_class("ethanol_80")
    #pipette_96_channel.consolidate_liquid(volume= 20, source =  [Dest_1.columns()[0], Dest_2.columns()[0]], dest = Source_plate.columns()[0], liquid_class = ethanol_80, new_tip = 'Once')
    pipette_96_channel.transfer_liquid(volume= 20, source = Source_plate.columns()[0], dest = Dest_1.columns()[0], liquid_class = ethanol_80, new_tip = 'Once' )
    pipette_96_channel.distribute_liquid(volume= 20, source = Source_plate.columns()[0], dest = [Dest_1.columns()[0], Dest_2.columns()], liquid_class = ethanol_80, new_tip = 'Once' )

