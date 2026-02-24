from opentrons.protocol_api import COLUMN

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.28"
}


metadata = {
    "protocolName":'96 Channel Partial Tip Return',
    'author':'Jeremy'
}

def run(protocol_context):
    tiprack_1 = protocol_context.load_labware("opentrons_flex_96_tiprack_50ul", "D1")
    tiprack_2 = protocol_context.load_labware("opentrons_flex_96_tiprack_50ul", "D3")
    trash = protocol_context.load_trash_bin('A3')
    pipette = protocol_context.load_instrument("flex_96channel_200")

    # Configure for column on the right side
    pipette.configure_nozzle_layout(COLUMN, start="A12", tip_racks=[tiprack_1])

    # Pick up and return tip
    pipette.pick_up_tip()
    pipette.return_tip()

    tiprack_2.set_empty()
    for source_well, target_well in zip(tiprack_1.rows()[0], tiprack_2.rows()[0]):
        # Even though the first column is used we can still explicitly pick it up in the first iteration of this for loop
        pipette.pick_up_tip(source_well)
        pipette.drop_tip(target_well)