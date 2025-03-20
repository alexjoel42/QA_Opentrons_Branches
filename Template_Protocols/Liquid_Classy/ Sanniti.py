metadata = {
	"name": "Testing transfer_liquid with LPD"
}

requirements = {
	"robotType": "Flex",
	"apiLevel": "2.23"
}


###### You need this in 8.3 ##########
from opentrons_shared_data.load import get_shared_data_root
import os
def get_latest_version(loadname: str) -> int:
	latest = sorted(os.listdir(f"{get_shared_data_root()}/labware/definitions/3/{loadname}/"))[-1]
	return int(latest[0])
#######################################

def run(protocol_context):
	tiprack1 = protocol_context.load_labware("opentrons_flex_96_tiprack_50ul", "B3")
	trash = protocol_context.load_trash_bin('A3')
	pipette_50 = protocol_context.load_instrument("flex_1channel_50", "left", tip_racks=[tiprack1], liquid_presence_detection=True)

	nest_plate = protocol_context.load_labware("nest_96_wellplate_2ml_deep", "D1")
	tuberack = protocol_context.load_labware("opentrons_10_tuberack_nest_4x50ml_6x15ml_conical", "D3", version=get_latest_version("opentrons_10_tuberack_nest_4x50ml_6x15ml_conical"))

	water_class = protocol_context.define_liquid_class("water")
	water_p50_props = water_class.get_for(pipette_50, tiprack1)
	
	# blue_water = protocol_context.define_liquid(
	# 	name="Blue water",
	# 	description="Blue colored water for demo",
	# 	display_color="#0000FF"
	# )
	# tuberack.wells_by_name()["B3"].load_liquid(liquid=blue_water, volume=10000)
	# water_p50_props.aspirate.mix.enabled = True
	# water_p50_props.aspirate.pre_wet = True
	water_p50_props.aspirate.retract.touch_tip.enabled = True
	water_p50_props.dispense.retract.touch_tip.enabled = True

	# Should transfer successfully
	pipette_50.transfer_liquid(
		liquid_class=water_class,
		volume=30,
		source=[tuberack.wells_by_name()["B3"], tuberack.wells_by_name()["B3"]],
		dest=nest_plate.rows()[0][:2],
		new_tip="once",
		trash_location=trash,
	)
