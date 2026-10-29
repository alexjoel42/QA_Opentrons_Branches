from opentrons import protocol_api

metadata = {
    'protocolName': 'Proof of long protocols crash robot good, 12k protocol',
}

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.29"
}

TIPRACK_96_ADAPTER_NAME = "opentrons_flex_96_tiprack_adapter"
TIPRACK_96_1000 = "opentrons_flex_96_tiprack_1000ul"
WELL_PLATE_NAME = "opentrons_96_wellplate_200ul_pcr_full_skirt"
PIPETTE_96_CHANNEL_NAME = "flex_96channel_1000"


def run(ctx: protocol_api.ProtocolContext):
    waste_chute = ctx.load_waste_chute()

    tip_rack_adapter = ctx.load_adapter(TIPRACK_96_ADAPTER_NAME, "C2")
    tip_rack = tip_rack_adapter.load_labware(TIPRACK_96_1000)

    well_plate = ctx.load_labware(WELL_PLATE_NAME, "D2")

    pipette = ctx.load_instrument(
        PIPETTE_96_CHANNEL_NAME,
        mount="left",
        tip_racks=[tip_rack],
    )

    pipette.pick_up_tip()
    target_well = well_plate["A1"]
    for i in range(3000):
        pipette.move_to(target_well.top(z=10))
        pipette.move_to(target_well.top(z=0))
        pipette.aspirate(100, target_well.bottom(z=5))
        pipette.dispense(100, target_well.top(z=0))
        
