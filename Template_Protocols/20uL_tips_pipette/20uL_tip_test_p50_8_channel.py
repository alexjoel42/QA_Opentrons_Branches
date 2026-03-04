from opentrons import protocol_api

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.28"
}

def run(ctx: protocol_api.ProtocolContext):
    # --- 1. HARDWARE & LABWARE SETUP ---
    # Load Flex Stacker in slot C4 as per your setup
    stacker = ctx.load_module('flexStackerModuleV1', 'C4')
    waste = ctx.load_waste_chute()
    
    # FIX: Define the labware pool before retrieval
    # This must match the physical labware and lid count in the hopper
    stacker.set_stored_labware(
    load_name="opentrons_flex_96_tiprack_20ul",
    count=5,
    lid="opentrons_flex_tiprack_lid"
)
    
    # Retrieve the labware object from the stacker pool
    tip_rack = stacker.retrieve()
    
    # Deck locations for testing
    working_slot = 'A2'
    reservoir = ctx.load_labware('nest_12_reservoir_15ml', 'C2')
    plate = ctx.load_labware('corning_96_wellplate_360ul_flat', 'D2')
    
    # Load P50 8-Channel Pipette
    pipette = ctx.load_instrument('flex_8channel_50', 'right')
    
    # --- 2. LOAD LIQUID CLASSES ---
    # Accessing Opentrons-verified liquid class definitions
 
    glycerol_lc = ctx.get_liquid_class(name='glycerol_50')
    ethanol_lc = ctx.get_liquid_class(name='ethanol_80')

    # --- 3. STACKER & GRIPPER MANIPULATION ---
    ctx.comment("Moving retrieved Tip Rack to deck...")
    
    # Move rack from stacker shuttle to working deck using the Gripper
    ctx.move_labware(
        labware=tip_rack,
        new_location=working_slot,
        use_gripper=True
    )

    # Remove lid and place it in slot B2 to access tips
    ctx.comment("Removing lid to access tips...")
    ctx.move_lid(tip_rack, waste, use_gripper=True)
    ctx.move_labware(labware=tip_rack, new_location='C1', use_gripper=True)

    # --- 4. LIQUID CLASS STRESS TEST ---
    pipette.pick_up_tip(tip_rack.wells_by_name()['A1'])

    # Stress testing across verified classes

    water_lc = ctx.get_liquid_class(name='water')
    classy = [water_lc]
    
    for i, LC in enumerate(classy):
        ctx.comment(f"Testing Liquid Class: {LC.name}")
        
        # Use transfer_with_liquid_class for automated physics handling
        pipette.transfer_with_liquid_class(
            volume=45,
            source=reservoir.wells()[i],
            dest=plate.wells()[i],
            liquid_class=LC,
            new_tip='never',
            group_wells=False
        )

    pipette.drop_tip()

    # --- 5. PARTIAL TIP PICKUP TEST ---
    ctx.comment("Starting Partial Tip Pickup (Single Nozzle) Test")
    
    # Configure pipette for SINGLE nozzle layout
    pipette.configure_nozzle_layout(
        style=protocol_api.SINGLE,
        start="H1"
    )

    # Pick up a single tip from a new column
    pipette.pick_up_tip(tip_rack.wells_by_name()['A2'])
    
    # Stress test single nozzle with viscous liquid class
    pipette.transfer_with_liquid_class(
        volume=25,
        source=reservoir.wells()[5],
        dest=plate.wells_by_name()['H12'],
        liquid_class=water_lc,
        new_tip='never'
    )
    
    pipette.return_tip()

    # Reset nozzle layout for clean exit
    pipette.configure_nozzle_layout(style=protocol_api.ALL)
    pipette.pick_up_tip(tip_rack['A3'])
    pipette.aspirate(10, reservoir.wells()[0])
    pipette.dispense(3, plate.wells()[0])
    pipette.dispense(6, plate.wells()[1])
    pipette.dispense(0.7, plate.wells()[2])
    pipette.blow_out()
    pipette.return_tip()

    # --- 6. LIQUID PROBING (After Line 108) ---
    ctx.comment("Probing for liquid level in reservoir...")
    
    # Pick up a tip to perform probing
    pipette.pick_up_tip(tip_rack.wells_by_name()['A4'])
    
    # Detect liquid level in the first reservoir well
    # The pipette will move down until it senses the surface
    found_height = pipette.detect_liquid_presence(reservoir.wells()[0])
    
    ctx.comment(f"Liquid detected at {found_height} mm from the bottom of the well.")
    
    # Example: Aspirate from the detected height (using the offset from probing)
    pipette.aspirate(20, reservoir.wells()[0].bottom(found_height - 2))
    pipette.dispense(20, plate.wells_by_name()['A5'])
    
    pipette.drop_tip()

