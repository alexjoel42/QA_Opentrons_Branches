'''
Use a meniscus relative below labware to aspirate and dispense a liquid class

'''

from opentrons import protocol_api

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.28"
}
metadata = {
    "protocolName": "Meniscus relative below labware"
}

def run(protocol: protocol_api.ProtocolContext):
    trash = protocol.load_trash_bin('A3')
    tip_rack = protocol.load_labware('opentrons_flex_96_tiprack_20ul', 'A1')
    plate = protocol.load_labware('opentrons_96_wellplate_200ul_pcr_full_skirt', 'B1')
    pipette = protocol.load_instrument('flex_1channel_50', 'left', tip_racks=[tip_rack])
    liquid = protocol.define_liquid(name='water',  description='water', display_color = '#0000FF')
    plate.load_liquid_by_well({plate['A1']: 1}, liquid)
    pipette.pick_up_tip()
    pipette.measure_liquid_height(plate["A1"])
    pipette.drop_tip()
    protocol.comment('Use the meniscus to aspirate and dispense')
  
 
    pipette.pick_up_tip()
    pipette.aspirate(
    volume=5,
    location=plate["A1"].meniscus(z=-20, target="start"),
    end_location=plate["A1"].meniscus(z=-20, target="end"))
    pipette.dispense(5,
    location=plate["A1"].meniscus(z=-20, target="start"),
    end_location=plate["A1"].meniscus(z=-20, target="end"))
    pipette.drop_tip()
