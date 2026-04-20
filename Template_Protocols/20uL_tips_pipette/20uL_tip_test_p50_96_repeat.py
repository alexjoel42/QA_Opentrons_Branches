'''
Robot os: Flex API 2.28
Deck tuned for 96ch right mount + SINGLE start="H12" (partial) without out-of-bounds:
- nest_12_reservoir_15ml B1 (water)
- appliedbiosystemsmicroamp_384_wellplate_40ul C3
- opentrons_96_wellplate_200ul_pcr_full_skirt D1
- opentrons_flex_96_tiprack_adapter + 20 µL rack D2 | bare 20 µL rack B2
- trash A3

Step 4: ALL on adapter D2 → aspirate/dispense 384 C3 → return_tip
Step 5: SINGLE H12 on bare B2 → one tip per cycle (well order matches H12 auto-tracking:
  A1–H1, then A2–H2, …) → same reservoir/liquid → dispense 96 D1 → drop_tip (partial cannot return_tip)
Step 6: Repeat 10×
'''

from opentrons import protocol_api

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.28"
}

metadata = {
    "protocolName": "20uL tip test P200 96 repeat",
    "description": "Alternating adapter vs bare 20uL racks; 10 cycles; H12 SINGLE deck",
}


def run(ctx: protocol_api.ProtocolContext):
    waste = ctx.load_waste_chute()
    adapter_d2 = ctx.load_adapter("opentrons_flex_96_tiprack_adapter", "D2")
    tips_adapter = adapter_d2.load_labware("opentrons_flex_96_tiprack_20ul")
    tips_bare = ctx.load_labware("opentrons_flex_96_tiprack_20ul", "B2")

    pipette = ctx.load_instrument(
        "flex_96channel_200",
        "right",
        tip_racks=[tips_adapter, tips_bare],
    )

    # Column-major A1–H1, A2–H2, … matches Opentrons 96ch SINGLE start=H12 default tracking order.
    bare_tip_order = [w for col in tips_bare.columns() for w in col]

    cycles = 10
    for n in range(cycles):
        ctx.comment(f"Static tip test cycle {n + 1} of {cycles}")

        pipette.configure_nozzle_layout(
            style=protocol_api.ALL,
            tip_racks=[tips_adapter, tips_bare],
        )
        pipette.pick_up_tip(tips_adapter.wells_by_name()["A1"])
        ctx.home()
        pipette.return_tip()

        # H12 primary: only the H12 nozzle is used for liquid; deck here keeps moves in-bounds.
        pipette.configure_nozzle_layout(
            style=protocol_api.SINGLE,
            start="H12",
            tip_racks=[tips_bare],
        )
        pipette.pick_up_tip(bare_tip_order[n])
        ctx.home()
        pipette.drop_tip()
