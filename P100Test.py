from opentrons import protocol_api

metadata = {
    'protocolName': 'Flex P1000 Single-Channel Protocol',
    'author': 'Your Name <email@example.com>',
    'description': 'Protocol using Flex P1000 Single-Channel with multiple tip racks',
}
requirements = {"robotType": "Flex", "apiLevel": "2.21"}


def run(protocol: protocol_api.ProtocolContext):
    trash = protocol.load_trash_bin("A3")

    # Load labware
    tip_rack_50ul = protocol.load_labware('opentrons_flex_96_tiprack_50uL', 'D1')
    tip_rack_200ul = protocol.load_labware('opentrons_flex_96_tiprack_200ul', 'D2')
    tip_rack_1000ul = protocol.load_labware('opentrons_flex_96_tiprack_1000ul', 'D3')
    sample_plate = protocol.load_labware('nest_96_wellplate_2ml_deep', 'A2')
    destination_plate = protocol.load_labware('armadillo_96_wellplate_200ul_pcr_full_skirt', 'B2')

    # Load pipette
    pipette = protocol.load_instrument(
        'flex_1channel_1000',
        mount='left',
        tip_racks=[tip_rack_200ul, tip_rack_50ul , tip_rack_1000ul]
    )

    # Protocol steps
    #pipette.pick_up_tip(tip_rack_50ul['A1'])
    pipette.distribute(100, sample_plate['A1'], [destination_plate['A1'], destination_plate['A2'],destination_plate['A3']])
    # Return tip
    #pipette.return_tip()

    # Add more steps as needed...