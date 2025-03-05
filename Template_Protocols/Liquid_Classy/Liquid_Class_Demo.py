requirements = {
	"robotType": "Flex",
	"apiLevel": "2.23"
}

metadata = {
    "protocolName":'Test cases',
    'author':'Alex'
}

def run(protocol_context):
	# Define labware, trash and pipette
	tiprack = protocol_context.load_labware("opentrons_flex_96_tiprack_200ul", "C2")
	trash = protocol_context.load_trash_bin('A3')
	pipette_1k = protocol_context.load_instrument("flex_1channel_1000", "left", tip_racks=[tiprack])
	nest_plate = protocol_context.load_labware("nest_96_wellplate_2ml_deep", "D1")
	arma_plate = protocol_context.load_labware("armadillo_96_wellplate_200ul_pcr_full_skirt", "D3")

	# Define water liquid class
	water_class = protocol_context.define_liquid_class("water")

	# Transfer 100ul of water from two wells of source to two wells of destination
	# Use one tip and use the trash as the trash location
	
	pipette_1k.transfer_liquid(
		liquid_class=water_class,
		volume=100,
		source=nest_plate.columns()[0][:2],
		dest=arma_plate.columns()[0][:2].top(),
		new_tip="once",
		trash_location=trash,
	)
	
	''' 
	# Get the liquid class properties for the pipette and tiprack combination we're using
	water_p1k_props = water_class.get_for(pipette_1k, tiprack)
	
    

	# Inline enable mix, touch tip and pre-wet for aspirate, touch tip and blow out for dispense
	water_p1k_props.aspirate.mix.enabled = True
	water_p1k_props.aspirate.pre_wet = True
	water_p1k_props.aspirate.retract.touch_tip.enabled = True
	water_p1k_props.dispense.retract.touch_tip.enabled = True
	water_p1k_props.dispense.retract.blowout.location = "source"
	water_p1k_props.dispense.retract.blowout.flow_rate = pipette_1k.flow_rate.blow_out
	water_p1k_props.dispense.retract.blowout.enabled = True

	# Continue transfer of the next two wells with the new settings applied
	pipette_1k.transfer_liquid(
		liquid_class=water_class,
		volume=100,
		source=nest_plate.columns()[0][2:4],
		dest=arma_plate.columns()[0][2:4],
		new_tip="once",
		trash_location=trash,
	)
	'''