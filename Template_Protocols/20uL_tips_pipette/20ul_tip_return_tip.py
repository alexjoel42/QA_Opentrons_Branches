
'''

api level: 2.28
robot type: Flex

This protocol is used to test the return tip feature of the 20uL tip.

It will pick up a tip from a tiprack and return it to the tiprack.

It will then repeat the process 2 times.

I want one tip rack on an adapter on D2 and when partial tip on B2 


'''


from opentrons import protocol_api

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.28"
}

metadata = {
    "protocolName": "20uL tip return tip"
}


def run(protocol: protocol_api.ProtocolContext):
    waste = protocol.load_waste_chute()
    adapter = protocol.load_adapter("opentrons_flex_96_tiprack_adapter", "D2")
    tips = adapter.load_labware("opentrons_flex_96_tiprack_20ul")
    pipette = protocol.load_instrument("flex_96channel_200", "left", tip_racks=[tips])
    pipette.configure_nozzle_layout(style=protocol_api.ALL, tip_racks=[tips])
    for _ in range(2):
        pipette.pick_up_tip(tips.wells_by_name()["A1"])
        protocol.home()
        pipette.return_tip()