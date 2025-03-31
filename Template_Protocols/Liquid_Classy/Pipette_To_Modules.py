
from typing import List
from opentrons import protocol_api, types
from opentrons.protocol_api import Labware
from opentrons.protocol_api.module_contexts import (
    FlexStackerContext,
)


metadata = {
    "protocolName": "Module pipetting",
    "author": "QA-Alex",
}

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.23",
}


#################
### CONSTANTS ###
#################

DeckSlots = [
    "A1",
    "A2",
    "A3",
    "A4",
    "B1",
    "B2",
    "B3",
    "B4",
    "C1",
    "C2",
    "C3",
    "C4",
    "D1",
    "D2",
    "D3",
    "D4",
]

HEATER_SHAKER_ADAPTER_NAME = "opentrons_96_pcr_adapter"
HEATER_SHAKER_NAME = "heaterShakerModuleV1"
MAGNETIC_BLOCK_NAME = "magneticBlockV1"
TEMPERATURE_MODULE_ADAPTER_NAME = "opentrons_96_well_aluminum_block"
TEMPERATURE_MODULE_NAME = "temperature module gen2"
THERMOCYCLER_NAME = "thermocycler module gen2"
ABSORBANCE_READER = "absorbanceReaderV1"
DECK_RISER_NAME = "opentrons_flex_deck_riser"
TC_LID = "opentrons_tough_pcr_auto_sealing_lid"
LID_COUNT = 5
TIPRACK_96_ADAPTER_NAME = "opentrons_flex_96_tiprack_adapter"
TIPRACK_96_NAME = "opentrons_flex_96_tiprack_1000ul"
PIPETTE_96_CHANNEL_NAME = "flex_96channel_1000"
FLEX_STACKER = "flexStackerModuleV1"


def add_parameters(parameters: protocol_api.Parameters):
    """This is the standard use of parameters"""
    parameters.add_str(
        variable_name="test_configuration",
        display_name="Test Configuration",
        description="Configuration of QA test to perform",
        default="full",
        choices=[{"display_name": "Full Smoke Test", "value": "full"}],
    )

    parameters.add_str(
        variable_name="reservoir_name",
        display_name="Reservoir Name",
        description="Name of the reservoir",
        default="nest_1_reservoir_290ml",
        choices=[{"display_name": "Nest 1 Well 290 mL", "value": "nest_1_reservoir_290ml"}],
    )

    parameters.add_str(
        variable_name="well_plate_name",
        display_name="Well Plate Name",
        description="Name of the well plate",
        default="opentrons_96_wellplate_200ul_pcr_full_skirt",
        choices=[{"display_name": "Opentrons Tough 96 Well 200 µL", "value": "opentrons_96_wellplate_200ul_pcr_full_skirt"}],
    )
    

import itertools



def run(ctx: protocol_api.ProtocolContext) -> None:

    ################
    ### FIXTURES ###
    ################

    waste_chute = ctx.load_waste_chute()

    ###############
    ### MODULES ###
    ###############
    # deck_riser_adapter = ctx.load_adapter(DECK_RISER_NAME, "A4")
    thermocycler = ctx.load_module(THERMOCYCLER_NAME)  # A1 & B1
    magnetic_block = ctx.load_module(MAGNETIC_BLOCK_NAME, "A3")
    heater_shaker = ctx.load_module(HEATER_SHAKER_NAME, "C1")
    temperature_module = ctx.load_module(TEMPERATURE_MODULE_NAME, "D1")
    absorbance_module = ctx.load_module(ABSORBANCE_READER, "B3")
    lids = ctx.load_lid_stack(load_name = TC_LID, location =  "C4", quantity = 5, adapter = DECK_RISER_NAME)
    thermocycler.open_lid()
    heater_shaker.close_labware_latch()
    absorbance_module.close_lid()
    absorbance_module.initialize("single", [600], 450)
    absorbance_module.open_lid()

    stacker: FlexStackerContext = ctx.load_module(
        "flexStackerModuleV1", "A4"
    )  # type: ignore[assignment]
    stacker.set_stored_labware(
        load_name="opentrons_flex_96_tiprack_200ul",
        count=6,
        lid="opentrons_flex_tiprack_lid",
    )



    #######################
    ### MODULE ADAPTERS ###
    #######################

    temperature_module_adapter = temperature_module.load_adapter(TEMPERATURE_MODULE_ADAPTER_NAME)
    heater_shaker_adapter = heater_shaker.load_adapter(HEATER_SHAKER_ADAPTER_NAME)
    adapters = [temperature_module_adapter, heater_shaker_adapter]
    mag_plate = magnetic_block.load_labware('nest_96_wellplate_2ml_deep')
    Temp_Plate = adapters[0].load_labware('opentrons_96_wellplate_200ul_pcr_full_skirt')
    HS_Plate = adapters[1].load_labware('opentrons_96_wellplate_200ul_pcr_full_skirt')
    TC_Plate = thermocycler.load_labware('opentrons_96_wellplate_200ul_pcr_full_skirt')
    # tip_adapter = ctx.load_adapter(TIPRACK_96_ADAPTER_NAME, "A2")
    deck_slots_racks = ['A2', 'C2', 'B2']
    tip_racks =[]
    for slot in deck_slots_racks:
        if slot == 'A2':
            my_adapter_50_A2= ctx.load_adapter("opentrons_flex_96_tiprack_adapter", slot)
            tip_racks.append(my_adapter_50_A2.load_labware("opentrons_flex_96_tiprack_50ul"))
        else:
             my_adapter_50 = ctx.load_adapter("opentrons_flex_96_tiprack_adapter", slot)
             tip_racks.append(my_adapter_50.load_labware("opentrons_flex_96_tiprack_50ul"))
        
        
    pipette_96_channel = ctx.load_instrument(PIPETTE_96_CHANNEL_NAME, mount="left", tip_racks=tip_racks, liquid_presence_detection=True)
    pipette_96_channel.trash_container = waste_chute
    water_class = ctx.define_liquid_class("water")
    glycerol_50 = ctx.define_liquid_class("glycerol_50")
    ethanol_80 = ctx.define_liquid_class("ethanol_80")
    classy = [water_class,glycerol_50, ethanol_80 ]
    Module_Labware =  [mag_plate, Temp_Plate, HS_Plate, TC_Plate]
    #pipette_96_channel.pick_up_tip()
    generate_labware_transfers(pipette_96_channel, Module_Labware,classy)
    stacker_rack = stacker.retrieve()
    tip_racks.append(stacker_rack)
    ctx.move_labware(tip_racks[0], waste_chute)
    ctx.move_labware(stacker_rack, my_adapter_50_A2)
    #pipette_96_channel.pick_up_tip()
    for LC in classy:
        pipette_96_channel.consolidate_liquid(volume= 10, source = [Module_Labware[1]['A1'], Module_Labware[2]['A1'], Module_Labware[3]['A1']], dest = Module_Labware[0]['A1'], liquid_class = LC, new_tip = 'Once' )
    # pipette_96_channel.drop_tip()
    pipette_96_channel.transfer_liquid(volume = 200, source =Module_Labware[0]['A1'] , dest = Module_Labware[1]['A1'], liquid_class = water_class , new_tip ='Once')



   


    ''' 
    for i in range(0,2):

        pipette_96_channel.transfer_liquid(volume = 1, source = Source_Labware[0]['A1'], dest = Destination_Labware[0], liquid_class= classy[0])
        pipette_96_channel.transfer_liquid(volume = 1, source = Source_Labware[0]['A1'], dest = Destination_Labware[0], liquid_class= classy[0])

    '''

def generate_labware_transfers(pipette, Module_Labware, classy):
    """Generates all permutations of liquid transfers between two labware."""
    pipette.pick_up_tip()
    for source_labware, dest_labware in itertools.permutations(Module_Labware, 2):
        for LC in classy:
            pipette.transfer_liquid(volume = 1, source =source_labware['A1'] , dest = dest_labware['A1'], liquid_class =LC, new_tip ='never')
    pipette.return_tip()
