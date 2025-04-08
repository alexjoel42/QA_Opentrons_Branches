
from opentrons import protocol_api

metadata = {
    "protocolName": "Module pipetting",
    "author": "QA team",
}

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.23",
}

def run(ctx: protocol_api.ProtocolContext) -> None:

    ################
    ### FIXTURES ###
    ################

    waste_chute = ctx.load_waste_chute()
     ################
    ### Labware ###
    ################
    Source_plate = ctx.load_labware('agilent_1_reservoir_290ml', 'A3')
    Dest_1 = ctx.load_labware('nest_96_wellplate_2ml_deep', 'A1')
    tip_racks = []
    slots = ['A2']
    for slot in slots:
        tip_rack = ctx.load_labware("opentrons_flex_96_tiprack_1000ul", slot)
        tip_racks.append(tip_rack)
    pipette_96_channel = ctx.load_instrument('flex_8channel_1000', mount="left", tip_racks=tip_racks, liquid_presence_detection=False)
    pipette_96_channel.trash_container = waste_chute

    ###############
    ### LC Config ###
    ###############
    ethanol_80 = ctx.define_liquid_class("ethanol_80")
    ethanol_80_config = ethanol_80.get_for(pipette_96_channel, tip_racks[0])
    ethanol_80_config.dispense.mix.enabled = True 
    ethanol_80_config.dispense.mix.repetitions = 20
    ethanol_80_config.dispense.mix.volume = 15

    #####
    # Protocol Steps
    #####
    pipette_96_channel.transfer_liquid(volume= 1000, source = Source_plate.columns()[0], dest = Dest_1.columns()[0], liquid_class = ethanol_80, new_tip = 'Once' )





