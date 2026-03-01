
from opentrons import protocol_api
requirements = {
	"robotType": "Flex",
	"apiLevel": "2.28"
}

metadata = {
    "protocolName":'Command Annotations edge cases',
    'author':'Alex'
}

def run(protocol_context:protocol_api.ProtocolContext):
	tiprack = protocol_context.load_labware("opentrons_flex_96_tiprack_200ul", "C2")
	trash = protocol_context.load_trash_bin('A3')
	pipette_1k = protocol_context.load_instrument("flex_1channel_1000", "right", tip_racks=[tiprack])
	nest_plate = protocol_context.load_labware("nest_96_wellplate_2ml_deep", "D1")
	arma_plate = protocol_context.load_labware("armadillo_96_wellplate_200ul_pcr_full_skirt", "D3")
	'''
	with protocol_context.group_steps("Demonstrates a nested group"):
		protocol_context.comment("This step group has a normal aspirate and dispense")
		with protocol_context.group_steps("This should be nested"):
			protocol_context.comment("This is a nested step group inside the first step group")
			pipette_1k.pick_up_tip()
			pipette_1k.return_tip()
	''' 


	step_group = protocol_context.create_and_start_step_group("Incremental step grouping")

	pipette_1k.pick_up_tip()
	pipette_1k.aspirate(50, nest_plate['C1'].bottom(z=1))
	pipette_1k.dispense(50, arma_plate['C1'].bottom(z=1))
	pipette_1k.touch_tip()
	pipette_1k.drop_tip()
	# Doesn't work yet because we need to wire up
	step_group.close_group()

	pipette_1k.pick_up_tip()
	pipette_1k.return_tip()