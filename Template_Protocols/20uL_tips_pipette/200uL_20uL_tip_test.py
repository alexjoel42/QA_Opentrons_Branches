''' 
200uL, p50, P50 8-Channel Tip Test Protocol
Minimum 0.5uL volume test for 20uL 
tip overlap with LPC/meniscus level detection 
- 1.0mm off 
- 
'''

from opentrons import protocol_api

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.28"
}

def run(ctx: protocol_api.ProtocolContext):
    # --- 1. HARDWARE & LABWARE SETUP ---
    stacker = ctx.load_module('flexStackerModuleV1', 'C4')
    waste = ctx.load_waste_chute()
    
    # Define the labware pool
    stacker.set_stored_labware(
        load_name="opentrons_flex_96_tiprack_20ul",
        count=5,
        lid="opentrons_flex_tiprack_lid"
    )
    
    # Retrieve the labware object
    tip_rack = stacker.retrieve()
    
    # Deck locations
    working_slot = 'A2'
    reservoir = ctx.load_labware('nest_12_reservoir_15ml', 'C2')
    plate = ctx.load_labware('corning_96_wellplate_360ul_flat', 'D2')
    
    # MODIFIED: Load P50 Single-Channel Pipette
    pipette = ctx.load_instrument('flex_1channel_50', 'right')
    
    # --- 2. LOAD LIQUID CLASSES ---
    glycerol_lc = ctx.get_liquid_class(name='glycerol_50')
    ethanol_lc = ctx.get_liquid_class(name='ethanol_80')
    water_lc = ctx.get_liquid_class(name='water')

    # --- 3. STACKER & GRIPPER MANIPULATION ---
    ctx.comment("Moving retrieved Tip Rack to deck...")
    ctx.move_labware(
        labware=tip_rack,
        new_location=working_slot,
        use_gripper=True
    )

    ctx.comment("Removing lid to waste...")
    ctx.move_lid(tip_rack, waste, use_gripper=True)

    # --- 4. LIQUID CLASS STRESS TEST ---
    # Single channel picks up a single tip at A1
    pipette.pick_up_tip(tip_rack.wells_by_name()['A1'])

    classy = [water_lc, glycerol_lc, ethanol_lc]
    
    for i, LC in enumerate(classy):
        ctx.comment(f"Testing Liquid Class: {LC.name}")
        # Note: Transferring to single wells since it's a single-channel
        pipette.transfer_with_liquid_class(
            volume=45,
            source=reservoir.wells()[i],
            dest=plate.wells()[i],
            liquid_class=LC,
            new_tip='never'
        )

    pipette.drop_tip()

    # --- 5. SINGLE NOZZLE TEST (Simplified) ---
    # MODIFIED: Removed configure_nozzle_layout as it is for multi-channel only
    ctx.comment("Starting Single Nozzle Stress Test")
    
    pipette.pick_up_tip(tip_rack.wells_by_name()['A2'])
    
    pipette.transfer_with_liquid_class(
        volume=25,
        source=reservoir.wells()[5],
        dest=plate.wells_by_name()['H12'],
        liquid_class=water_lc,
        new_tip='never'
    )
    
    pipette.return_tip()

    # General aspiration test
    pipette.pick_up_tip(tip_rack['A3'])
    pipette.aspirate(10, reservoir.wells()[0])
    pipette.dispense(3, plate.wells()[0])
    pipette.dispense(6, plate.wells()[1])
    pipette.dispense(0.7, plate.wells()[2])
    pipette.blow_out()
    pipette.return_tip()

    # --- 6. LIQUID PROBING ---
    ctx.comment("Probing for liquid level in reservoir...")
    
    pipette.pick_up_tip(tip_rack.wells_by_name()['A4'])
    
    # Detect liquid level in the first reservoir well
    found_height = pipette.detect_liquid_presence(reservoir.wells()[0])
    
    ctx.comment(f"Liquid detected at {found_height} mm from bottom.")
    
    # Aspirate using the detected height
    pipette.aspirate(20, reservoir.wells()[0].bottom(found_height - 2))
    pipette.dispense(20, plate.wells_by_name()['A5'])
    
    pipette.drop_tip()