from opentrons import protocol_api
from opentrons.protocol_api import SINGLE

metadata = {
    "protocolName": "Flex LLD - Tough Labware Simple",
    "author": "QA team",
}

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.29",
}

def run(ctx: protocol_api.ProtocolContext) -> None:
    ctx.load_waste_chute()
    pcr_plate = ctx.load_labware("opentrons_96_wellplate_200ul_pcr_full_skirt", "C2")
    tip_rack = ctx.load_labware("opentrons_flex_96_tiprack_50ul", "A2")

    water = ctx.define_liquid(
        name="water",
        description="High Quality H2O",
        display_color="#42AB2D",
    )
    pcr_plate["A1"].load_liquid(liquid=water, volume=15000)

    pipette = ctx.load_instrument(
        "flex_8channel_50",
        mount="left",
        tip_racks=[tip_rack],
        liquid_presence_detection=True,
    )

    pipette.pick_up_tip()
    pipette.detect_liquid_presence(pcr_plate["A1"])

    ctx.comment("Aspirating from reservoir using Liquid Level Detection")
    pipette.aspirate(
        volume=15,
        location=pcr_plate["A1"].meniscus(target="dynamic", z=-1),
    )
    ctx.comment("Dispensing into PCR plate using Liquid Level Detection")
    pipette.dispense(
        volume=15,
        location=pcr_plate["A1"].meniscus(target="dynamic", z=-1),
    )
    pipette.return_tip()