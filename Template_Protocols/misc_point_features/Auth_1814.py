from opentrons import protocol_api

metadata = {
    'protocolName': 'Simple Transfer Protocol',
    'author': 'OpentronsAI',
    'description': 'Transfer from Opentrons Tough 200µL plate to NEST 12-well reservoir using P1000 Single-Channel',
    'source': 'OpentronsAI'
}

requirements = {
    'robotType': 'OT-2',
    'apiLevel': '2.28'
}

def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    source_plate = protocol.load_labware('opentrons_96_wellplate_200ul_pcr_full_skirt', '1', 'Source Plate')
    destination_reservoir = protocol.load_labware('nest_12_reservoir_15ml', '2', 'Destination Reservoir')
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '3', 'Tip Rack')
    
    # Load pipette
    p1000 = protocol.load_instrument('p1000_single_gen2', 'right', tip_racks=[tiprack])
    
    # Protocol steps
    # Transfer 100 µL from well A1 of source plate to well A1 of reservoir
    p1000.transfer(100, source_plate['A1'], destination_reservoir['A1'], new_tip='always')