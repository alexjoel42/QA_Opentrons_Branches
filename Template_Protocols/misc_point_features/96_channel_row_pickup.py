from opentrons import protocol_api
from opentrons.protocol_api import ROW

metadata = {
    "protocolName": "row pickup",
    "author": "QA team",
}

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.29",
}

def run(ctx: protocol_api.ProtocolContext) -> None:
    ctx.load_waste_chute()
    source_reservoir = ctx.load_labware("nest_1_reservoir_290ml", "D2")
    
    # Load adapter, then load the tip rack directly onto the adapter
    tip_rack_3 = ctx.load_labware("opentrons_flex_96_tiprack_1000ul", 'C3')

    water = ctx.define_liquid(
        name="water",
        description="High Quality H2O",
        display_color="#42AB2D",
    )
    source_reservoir["A1"].load_liquid(liquid=water, volume=15000)

    pipette_96_channel = ctx.load_instrument(
        "flex_96channel_1000",
        mount="left",
        tip_racks=[tip_rack_3],
        liquid_presence_detection=False, 
    )
    
    # 96 channel row pickup
    pipette_96_channel.configure_nozzle_layout(style=ROW, start="H1")
    pipette_96_channel.pick_up_tip(tip_rack_3)
    
    ctx.comment("Dynamically mixing in the reservoir using LLD")
    pipette_96_channel.dynamic_mix(
        volume=900,
        # Added target="dynamic" to ensure LLD sensors are active for the mix
        aspirate_start_location=source_reservoir["A1"].meniscus(target="dynamic", z=-2),
        dispense_start_location=source_reservoir["A1"].meniscus(target="dynamic", z=-1),
        repetitions=3,
        final_push_out=3,
    )
    
    pipette_96_channel.return_tip()