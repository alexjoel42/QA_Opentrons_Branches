from opentrons import protocol_api

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.28"
}

metadata = {
    "protocolName": "Thermocycler Ramp_Rate",
    "author": "QA"
}

def run(protocol: protocol_api.ProtocolContext):
    # 1. Load the Thermocycler Module (V2 for Flex)
    # The 'B1' slot is the standard location for the TC on the Flex
    tc_mod = protocol.load_module("thermocyclerModuleV2")

    # 2. Open the lid to start (optional, but good practice for setup)
    if tc_mod.lid_position != "open":
        tc_mod.open_lid()

    # 3. NON-BLOCKING: Start heating to 80°C
    # The protocol will immediately move to the next line while the TC heats up.
    # Good for pre-heating while the pipette is busy.
    protocol.comment("Pre-heating TC to 80°C...")
    tc_mod.start_set_block_temperature(
        temperature=80, 
        block_max_volume=100,
        ramp_rate=1
    )

    # --- SIMULATED WORK ---
    # The robot would usually be picking up tips or moving plates here.
    protocol.delay(seconds=10, msg="Simulating work while TC heats up")
    # ----------------------

    # 4. BLOCKING: Set temperature to 4°C
    # The robot will STOP here and wait until the block physically reaches 4°C.
    protocol.comment("Cooling TC to 4°C and waiting for completion...")
    tc_mod.set_block_temperature(
        temperature=95,
        ramp_rate=4.25
    )

    tc_mod.set_block_temperature(
        temperature=80,
        ramp_rate=0.5
    )
    
    # 5. Hold at 4°C and deactivate
    tc_mod.deactivate_block()
    tc_mod.open_lid()