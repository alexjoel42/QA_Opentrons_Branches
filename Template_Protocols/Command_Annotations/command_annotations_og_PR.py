requirements = {
	"robotType": "Flex",
	"apiLevel": "2.29"
}

metadata = {
    "protocolName":'Command Annotations PAPI Test',
    'author':'Jeremy'
}

def run(protocol_context):
	tiprack = protocol_context.load_labware("opentrons_flex_96_tiprack_200ul", "C2")
	trash = protocol_context.load_trash_bin('A3')
	pipette_1k = protocol_context.load_instrument("flex_1channel_1000", "right", tip_racks=[tiprack])
	nest_plate = protocol_context.load_labware("nest_96_wellplate_2ml_deep", "D1")
	arma_plate = protocol_context.load_labware("armadillo_96_wellplate_200ul_pcr_full_skirt", "D3")

	with protocol_context.group_steps("Aspirate and Dispense 1"):
		pipette_1k.pick_up_tip()
		pipette_1k.aspirate(50, nest_plate['A1'].bottom(z=1))
		pipette_1k.dispense(50, arma_plate['A1'].bottom(z=1))
		pipette_1k.drop_tip()

	pipette_1k.pick_up_tip()
	pipette_1k.aspirate(50, nest_plate['B1'].bottom(z=1))
	pipette_1k.dispense(50, arma_plate['B1'].bottom(z=1))
	pipette_1k.drop_tip()


	step_group = protocol_context.create_and_start_step_group("Aspirate and Dispense 2",  description="We touch tip here before dropping the tip.")

	pipette_1k.pick_up_tip()
	pipette_1k.aspirate(50, nest_plate['C1'].bottom(z=1))
	pipette_1k.dispense(50, arma_plate['C1'].bottom(z=1))
	pipette_1k.touch_tip()
	pipette_1k.drop_tip()
	# Doesn't work yet because we need to wire up

	pipette_1k.pick_up_tip()
	pipette_1k.drop_tip()