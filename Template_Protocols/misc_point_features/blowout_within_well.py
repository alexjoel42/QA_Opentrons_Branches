import opentrons.protocol_api as protocol_api
requirements = {
"robotType": "Flex",
"apiLevel": "2.28"
}

metadata = {
"protocolName":'Test different blowout locations & positions',
'author':'sanniti'
}


BLOWOUT_OPTIONS = {
	"trash": {"position_reference": "well-top", "offset": {"x": 1, "y": 2, "z": 3}},
	"source": {"position_reference": "well-center", "offset": {"x": 1, "y": 2, "z": 3}},
	"destination": {"position_reference": "well-bottom", "offset": {"x": 1, "y": 2, "z": 3}},
}

def add_parameters(params):
	params.add_str(
	    variable_name="blowout_option",
	    display_name="Blowout Option",
	    choices=[
	        {"display_name": "Trash (well-top + offset )", "value": "trash"},
	        {"display_name": "Source (well-center + offset)", "value": "source"},
	        {"display_name": "Dest (well-bottom + offset)", "value": "destination"}
	    ],
	    default="destination",
	)
	params.add_str(
		variable_name="trash_option",
		display_name="Trash Option",
		choices=[
			{"display_name": "Trash Labware in A2", "value": "trash_labware"},
			{"display_name": "Flex Trash Bin in A3", "value": "trash_bin"},
		],
		default="trash_bin"
	)

def run(protocol_context: protocol_api.ProtocolContext):
	trash_selection = protocol_context.params.trash_option
	blowout_selection = protocol_context.params.blowout_option
	
	tiprack = protocol_context.load_labware(
		"opentrons_flex_96_tiprack_50ul", "B2"
		)
	pipette_50 = protocol_context.load_instrument(
		"flex_8channel_50", mount="right", tip_racks=[tiprack],
		)
	if trash_selection == "trash_bin":
		trash = protocol_context.load_trash_bin("A3")
	else:
		trash = protocol_context.load_labware("nest_1_reservoir_290ml", "A2")
	pipette_50.trash_container = trash

	nest_plate = protocol_context.load_labware(
		"nest_96_wellplate_200ul_flat", "D2"
		)
	arma_plate = protocol_context.load_labware(
		"armadillo_96_wellplate_200ul_pcr_full_skirt", "C2"
		)

	water = protocol_context.get_liquid_class("ethanol_80")
	water_blowout_props = water.get_for(pipette_50, tiprack).dispense.retract.blowout
	water_blowout_props.enabled = True
	water_blowout_props.location = blowout_selection
	
	water_blowout_props.blowout_position = BLOWOUT_OPTIONS[blowout_selection]

	pipette_50.transfer_with_liquid_class(
		liquid_class=water,
		volume=40,
		source=nest_plate['A1'],
		dest=arma_plate['A1'],
		new_tip="always",
		trash_location=trash,
		group_wells=False
		)