'''
Robot os: Flex API 2.28
Step 1: Load the labware: 384 well plate appliedbiosystemsmicroamp_384_wellplate_40ul and opentrons_96_wellplate_200ul_pcr_full_skirt in slot B3 and C3
Step 2: Load the pipette: flex_96channel_200 in right mount
Step 3: Load one 20uL in d2 with the adapter and one in b2 without the adapter
Step 4: Pick up a tip from the rack in d2 with the adapter and dispense 20uL into the 384 well plate in slot B3 then return the tip to the rack in d2 with the adapter
Step 5: Bare B2 rack uses SINGLE (ALL pickup requires the adapter; COLUMN start must be a corner nozzle only). PE does not allow return_tip with partial nozzles — drop to trash; one new tip per cycle via wells()[n].
step 6: Repeat steps 4 and 5 10 times to test the tips static
'''

from opentrons import protocol_api

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.28"
}

metadata = {
    "protocolName": "20uL tip test P50 96 repeat",
    "description": "Alternating adapter vs bare 20uL racks; 10 cycles static tip test",
}


def run(ctx: protocol_api.ProtocolContext):
    # Step 1 — deck layout from spec; A1 reservoir supplies liquid for aspirate/dispense cycles
    plate_384 = ctx.load_labware(
        "appliedbiosystemsmicroamp_384_wellplate_40ul",
        "B3"
    )
    plate_96_pcr = ctx.load_labware(
        "opentrons_96_wellplate_200ul_pcr_full_skirt",
        "C3",
    )
    reservoir = ctx.load_labware("nest_12_reservoir_15ml", "A1", "Water")
    trash = ctx.load_trash_bin("A3")

    # Step 3 — D2: 20 µL rack on adapter; B2: same tip type, deck only
    adapter_d2 = ctx.load_adapter("opentrons_flex_96_tiprack_adapter", "D2")
    tips_adapter = adapter_d2.load_labware("opentrons_flex_96_tiprack_20ul")
    tips_bare = ctx.load_labware("opentrons_flex_96_tiprack_20ul", "B2")

    # Step 2
    pipette = ctx.load_instrument(
        "flex_96channel_200",
        "right",
        tip_racks=[tips_adapter, tips_bare],
    )

    dest_384 = plate_384.wells_by_name()["A1"]
    # Step 5 text references "384" in C3; labware loaded in C3 is 96 PCR — dispense into that plate
    dest_96 = plate_96_pcr.wells_by_name()["A1"]
    source = reservoir.wells_by_name()["A1"]

    cycles = 10
    for n in range(cycles):
        ctx.comment(f"Static tip test cycle {n + 1} of {cycles}")

        # Steps 4–5: ALL + adapter; bare deck only allows partial pickup. After partial layout,
        # pick_up_tip(labware) can see an empty rack list — use explicit Wells for adapter picks.
        pipette.configure_nozzle_layout(
            style=protocol_api.ALL,
            tip_racks=[tips_adapter, tips_bare],
        )
        pipette.pick_up_tip(tips_adapter.wells_by_name()["A1"])
        pipette.aspirate(20, source)
        pipette.dispense(20, dest_384)
        pipette.return_tip()

        pipette.configure_nozzle_layout(
            style=protocol_api.SINGLE,
            start="A1",
            tip_racks=[tips_bare],
        )
        pipette.pick_up_tip(tips_bare.wells()[n])
        pipette.aspirate(20, source)
        pipette.dispense(20, dest_96)
        pipette.drop_tip(trash)
