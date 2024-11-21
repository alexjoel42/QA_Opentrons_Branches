from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': '96ch sanity check',
    'author': 'Name <opentrons@example.com>',
    'description': 'Simple protocol to get started using the OT-2',
}

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.16",
}

DRYRUN = 'YES'
USE_GRIPPER = 'TRUE'

# protocol run function
def run(protocol: protocol_api.ProtocolContext):
    adapter1 = protocol.load_adapter("opentrons_flex_96_tiprack_adapter", "C3")
    tiprack1 = adapter1.load_labware('opentrons_flex_96_tiprack_1000ul', 'C3')
    p1000 = protocol.load_instrument('flex_96channel_1000', mount = 'left', tip_racks=[tiprack1])
    sample_plate = protocol.load_labware('nest_12_reservoir_15ml','B2')
    for i in range(3):
        p1000.pick_up_tip()
        p1000.aspirate(50, sample_plate['A1'])
        p1000.dispense(50, sample_plate['A1'])
        p1000.aspirate(66, sample_plate["A1"])
        p1000.dispense(66, sample_plate['A1'])
        p1000.return_tip()
        p1000.reset_tipracks()

    p1000.pick_up_tip()
    p1000.return_tip()
