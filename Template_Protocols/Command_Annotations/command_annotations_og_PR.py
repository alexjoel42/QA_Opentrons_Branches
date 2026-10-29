from opentrons import protocol_api
from dataclasses import dataclass
from typing import List, Set, Union


requirements = {
	"apiLevel": "2.29",
	"robotType":'Flex'
}

metadata = {
    "protocolName":'Command Annotations PAPI Test',
    'author':'QA'
}

def run(protocol_context: protocol_api):
	tiprack = protocol_context.load_labware("opentrons_flex_96_tiprack_200ul", "C2")
	trash = protocol_context.load_trash_bin('A3')
	pipette_1k = protocol_context.load_instrument("flex_1channel_1000", "right", tip_racks=[tiprack])
	nest_plate = protocol_context.load_labware("nest_96_wellplate_2ml_deep", "D1")
	arma_plate = protocol_context.load_labware("armadillo_96_wellplate_200ul_pcr_full_skirt", "D3")
	
	with protocol_context.group_steps(f"Step group one!"):
		pipette_1k.pick_up_tip()
		pipette_1k.aspirate(50, nest_plate[f'A1'].bottom(z=1))
		pipette_1k.dispense(50, arma_plate[f'A1'].bottom(z=1))
		pipette_1k.drop_tip()
	

	pipette_1k.pick_up_tip()
	pipette_1k.aspirate(50, nest_plate['B1'].bottom(z=1))
	pipette_1k.dispense(50, arma_plate['B1'].bottom(z=1))
	pipette_1k.drop_tip()


	step_group = protocol_context.create_and_start_step_group("start and stop step group!",  description="We touch tip here before dropping the tip.")
	pipette_1k.pick_up_tip()
	pipette_1k.aspirate(50, nest_plate['C1'].bottom(z=1))
	pipette_1k.dispense(50, arma_plate['C1'].bottom(z=1))
	pipette_1k.touch_tip()
	pipette_1k.drop_tip()
	step_group.end_group()

	pipette_1k.pick_up_tip()
	pipette_1k.return_tip()