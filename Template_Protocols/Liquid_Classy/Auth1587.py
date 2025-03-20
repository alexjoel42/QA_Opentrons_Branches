metadata = {
	"name": "Testing transfer_liquid with LPD"
}

requirements = {
	"robotType": "Flex",
	"apiLevel": "2.23"
}


###### You need this in 8.3 ##########

from opentrons import protocol_api

def run(protocol_context):
	tiprack1 = protocol_context.load_labware("opentrons_flex_96_tiprack_50ul", "B3")
	trash = protocol_context.load_trash_bin('A3')
	pipette_50 = protocol_context.load_instrument("flex_1channel_50", "left", tip_racks=[tiprack1], liquid_presence_detection=True)

	plate = protocol_context.load_labware("nest_96_wellplate_2ml_deep", "D1")
	#tuberack = protocol_context.load_labware("opentrons_10_tuberack_nest_4x50ml_6x15ml_conical", "D3", version=get_latest_version("opentrons_10_tuberack_nest_4x50ml_6x15ml_conical"))

	water_class = protocol_context.define_liquid_class("water")
	ethanol_class = protocol_context.define_liquid_class('ethanol_80')
	# glycerin = protocol_context.define_liquid_class('glycerin_50')
	
	pipette_50.transfer(volume =  10 ,source = plate['A1'], dest = [plate.wells_by_name()[well_name] for well_name in ['B1', 'B2', 'B3']])
	pipette_50.transfer_liquid(liquid_class = water_class, volume = 10 ,source = plate['A1'], dest = plate['A1'])
	#pipette_50.distribute_liquid(liquid_class = ethanol_class, volume = 10, source = plate['A1'], dest  =[plate.wells_by_name()[well_name] for well_name in ['B1', 'B2', 'B3']])
