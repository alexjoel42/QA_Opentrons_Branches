"""
Concurrent Module Operations Smoke Test - API v2.29
Opentrons Flex

Tests concurrent operation of:
1. Heater-Shaker (HS) and Thermocycler (TC)
2. HS and Temperature Module GEN2 (TD)
3. TC, TD, and HS concurrently
4. TC, TD, HS, and Plate Reader concurrently
5. TC, TD, Plate Reader, and Gripper concurrently (no HS)
6. TC, TD, TD, HS concurrently (disabled — requires second TD on C3)
"""

from typing import cast

from opentrons import protocol_api
from opentrons.protocol_api.module_contexts import AbsorbanceReaderContext

metadata = {
    "protocolName": "Concurrent Module Operations Smoke Test - v2.29",
    "author": "QA Team",
}

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.29",
}

#################
### CONSTANTS ###
#################

HEATER_SHAKER_ADAPTER_NAME = "opentrons_96_pcr_adapter"
HEATER_SHAKER_V1_NAME = "heaterShakerModuleV1"
TEMPERATURE_MODULE_ADAPTER_NAME = "opentrons_96_well_aluminum_block"
TEMPERATURE_MODULE_GEN2_NAME = "temperature module gen2"
THERMOCYCLER_GEN2_NAME = "thermocycler module gen2"
PLATE_READER_NAME = "absorbanceReaderV1"
PLATE_READER_PLATE_NAME = "nest_96_wellplate_200ul_flat"
PCR_PLATE_NAME = "opentrons_96_wellplate_200ul_pcr_full_skirt"


def add_parameters(parameters: protocol_api.Parameters):
    """Add runtime parameters for test configuration"""
    
    parameters.add_str(
        variable_name="test_scenario",
        display_name="Test Scenario",
        description="Which concurrent module scenario to test",
        default="all",
        choices=[
            {"display_name": "All Tests", "value": "all"},
            {"display_name": "HS + TC Only", "value": "hs_tc"},
            {"display_name": "HS + TD Only", "value": "hs_td"},
            {"display_name": "TC + TD + HS Only", "value": "tc_td_hs"},
            {"display_name": "TC + TD + HS + PR Only", "value": "tc_td_hs_pr"},
            {
                "display_name": "TC + TD + PR + Gripper Only",
                "value": "tc_td_pr_gripper",
            },
            # {"display_name": "TC + TD + TD + HS Only", "value": "tc_td_td_hs"},  # Requires TD #2 on C3
        ],
    )


def run(ctx: protocol_api.ProtocolContext) -> None:
    """Main protocol function for concurrent module operations"""

    test_scenario = ctx.params.test_scenario

    ###############
    ### MODULES ###
    ###############


    ctx.comment("========== LOADING MODULES ==========")
    
    # Load Thermocycler (slots A1 & B1)
    thermocycler = ctx.load_module(THERMOCYCLER_GEN2_NAME)
    ctx.comment(f"Thermocycler loaded at {thermocycler.parent}")
    
    # Load Heater-Shaker on D1
    heater_shaker_01 = ctx.load_module(HEATER_SHAKER_V1_NAME, "C1")
    ctx.comment(f"Heater-Shaker 01 loaded at {heater_shaker_01.parent}")
    
    # Load Temperature Module GEN2 on C1
    temperature_module_01 = ctx.load_module(TEMPERATURE_MODULE_GEN2_NAME, "D1")
    ctx.comment(f"Temperature Module 01 loaded at {temperature_module_01.parent}")

    # Load Absorbance Plate Reader on B3
    plate_reader = cast(
        AbsorbanceReaderContext,
        ctx.load_module(PLATE_READER_NAME, "B3"),
    )
    ctx.comment(f"Plate Reader loaded at {plate_reader.parent}")

    # Load second Heater-Shaker on B3 (disabled — replaced by Plate Reader)
    # heater_shaker_02 = ctx.load_module(HEATER_SHAKER_V1_NAME, "B3")
    # ctx.comment(f"Heater-Shaker 02 loaded at {heater_shaker_02.parent}")

    # Load second Temperature Module GEN2 on C3 (removed)
    # temperature_module_02 = ctx.load_module(TEMPERATURE_MODULE_GEN2_NAME, "C3")
    # ctx.comment(f"Temperature Module 02 loaded at {temperature_module_02.parent}")

    for i in range(3):
        ctx.comment(f'This is iteration {i}')
        # Initialize module states
        thermocycler.open_lid()
        heater_shaker_01.open_labware_latch()
        # heater_shaker_02.open_labware_latch()
        plate_reader.close_lid()

        #######################
        ### MODULE ADAPTERS ###
        #######################

        ctx.comment("========== LOADING MODULE ADAPTERS ==========")
        
        temperature_module_adapter_01 = temperature_module_01.load_adapter(TEMPERATURE_MODULE_ADAPTER_NAME)
        # temperature_module_adapter_02 = temperature_module_02.load_adapter(TEMPERATURE_MODULE_ADAPTER_NAME)
        heater_shaker_adapter_01 = heater_shaker_01.load_adapter(HEATER_SHAKER_ADAPTER_NAME)
        # heater_shaker_adapter_02 = heater_shaker_02.load_adapter(HEATER_SHAKER_ADAPTER_NAME)

        # Shared labware for plate-reader / gripper scenarios (loaded once for "all")
        needs_pr_labware = test_scenario in ["all", "tc_td_hs_pr", "tc_td_pr_gripper"]
        reader_plate = None
        pcr_plate = None
        if needs_pr_labware:
            ctx.load_trash_bin("A3")
            reader_plate = ctx.load_labware(PLATE_READER_PLATE_NAME, "C2")
        if test_scenario in ["all", "tc_td_pr_gripper"]:
            pcr_plate = ctx.load_labware(PCR_PLATE_NAME, "C3")

        ctx.comment("========== MODULE INITIALIZATION COMPLETE ==========")

        # ========== TEST 1: HS and TC Operating Concurrently ==========
        if test_scenario in ["all", "hs_tc"]:
            ctx.comment("")
            ctx.comment("╔════════════════════════════════════════════════════════════════╗")
            ctx.comment("║  TEST 1: HEATER-SHAKER (HS) and THERMOCYCLER (TC) CONCURRENT   ║")
            ctx.comment("╠════════════════════════════════════════════════════════════════╣")
            ctx.comment("║  Description:                                                  ║")
            ctx.comment("║    Two independent modules operating at the same time.         ║")
            ctx.comment("║    - HS on D1: Heating to 37°C (independent operation)         ║")
            ctx.comment("║    - TC on A1/B1: Executing 3-step PCR profile                 ║")
            ctx.comment("║                                                                ║")
            ctx.comment("║  Expected Behavior:                                            ║")
            ctx.comment("║    Both tasks start immediately and run concurrently.          ║")
            ctx.comment("║    Protocol continues without waiting for either to complete.  ║")
            ctx.comment("╚════════════════════════════════════════════════════════════════╝")
            ctx.comment("")
            
            # ASYNC: Start HS temperature change
            hs_task = heater_shaker_01.set_target_temperature(celsius=37.0)
            ctx.comment("→ HS 01 async task initiated: Setting target temperature to 37°C")

            # ASYNC: Start TC profile execution
            tc_steps = [
                {"temperature": 95, "hold_time_seconds": 10},
                {"temperature": 60, "hold_time_seconds": 10},
                {"temperature": 72, "hold_time_seconds": 10},
            ]
            tc_task = thermocycler.start_execute_profile(steps=tc_steps, repetitions=1)
            ctx.comment("→ TC async task initiated: Executing 3-step PCR profile (95→60→72°C)")

            ctx.comment("⏳ Both tasks running concurrently...")
            # Wait for both tasks to complete using ctx.wait_for_tasks()
            ctx.wait_for_tasks([hs_task, tc_task])
            ctx.comment("✓ TEST 1 COMPLETE: HS and TC finished")
            ctx.comment("")

        # ========== TEST 2: HS and TD Operating Concurrently ==========
        if test_scenario in ["all", "hs_td"]:
            ctx.comment("")
            ctx.comment("╔════════════════════════════════════════════════════════════════╗")
            ctx.comment("║  TEST 2: HEATER-SHAKER (HS) and TEMPERATURE MODULE (TD)        ║")
            ctx.comment("║          CONCURRENT                                            ║")
            ctx.comment("╠════════════════════════════════════════════════════════════════╣")
            ctx.comment("║  Description:                                                  ║")
            ctx.comment("║    Two temperature control modules with opposite objectives.   ║")
            ctx.comment("║    - HS on D1: Heating to 45°C (warm operation)                ║")
            ctx.comment("║    - TD on C1: Cooling to 4°C (cold operation)                 ║")
            ctx.comment("║                                                                ║")
            ctx.comment("║  Expected Behavior:                                            ║")
            ctx.comment("║    Both modules operate independently and simultaneously.       ║")
            ctx.comment("║    Demonstrates temperature control on different modules       ║")
            ctx.comment("║    at the same time.                                           ║")
            ctx.comment("╚════════════════════════════════════════════════════════════════╝")
            ctx.comment("")

            # ASYNC: Start HS temperature change
            hs_task = heater_shaker_01.set_target_temperature(celsius=45.0)
            ctx.comment("→ HS 01 async task initiated: Setting target temperature to 45°C")

            # ASYNC: Start TD temperature change
            td_task = temperature_module_01.start_set_temperature(celsius=4.0)
            ctx.comment("→ TD 01 async task initiated: Setting temperature to 4°C")

            ctx.comment("⏳ Both tasks running concurrently (heating ↑ and cooling ↓)...")
            # Wait for both tasks to complete using ctx.wait_for_tasks()
            ctx.wait_for_tasks([hs_task, td_task])
            ctx.comment("✓ TEST 2 COMPLETE: HS and TD finished")
            ctx.comment("")

        # ========== TEST 3: TC, TD, and HS Operating Concurrently ==========
        if test_scenario in ["all", "tc_td_hs"]:
            ctx.comment("")
            ctx.comment("╔════════════════════════════════════════════════════════════════╗")
            ctx.comment("║  TEST 3: THERMOCYCLER (TC), TEMPERATURE MODULE (TD), and       ║")
            ctx.comment("║          HEATER-SHAKER (HS) CONCURRENT                         ║")
            ctx.comment("╠════════════════════════════════════════════════════════════════╣")
            ctx.comment("║  Description:                                                  ║")
            ctx.comment("║    Three independent modules running simultaneously.            ║")
            ctx.comment("║    - TC on A1/B1: Running PCR amplification cycles             ║")
            ctx.comment("║    - TD on C1: Pre-conditioning samples to 25°C                ║")
            ctx.comment("║    - HS on D1: Warming reaction vessel to 50°C                 ║")
            ctx.comment("║                                                                ║")
            ctx.comment("║  Expected Behavior:                                            ║")
            ctx.comment("║    All three tasks start immediately without blocking.         ║")
            ctx.comment("║    Maximum hardware parallelization: 3 modules active.         ║")
            ctx.comment("║    Demonstrates typical multi-step protocol workflow.          ║")
            ctx.comment("╚════════════════════════════════════════════════════════════════╝")
            ctx.comment("")

            # ASYNC: Start TC profile execution
            tc_steps = [
                {"temperature": 94, "hold_time_seconds": 8},
                {"temperature": 58, "hold_time_seconds": 8},
                {"temperature": 72, "hold_time_seconds": 8},
            ]
            tc_task = thermocycler.start_execute_profile(steps=tc_steps, repetitions=2)
            ctx.comment("→ TC async task initiated: Executing 3-step PCR profile (94→58→72°C)")

            # ASYNC: Start TD temperature change
            td_task = temperature_module_01.start_set_temperature(celsius=25.0)
            ctx.comment("→ TD 01 async task initiated: Setting temperature to 25°C")

            # ASYNC: Start HS temperature change
            hs_task = heater_shaker_01.set_target_temperature(celsius=50.0)
            ctx.comment("→ HS 01 async task initiated: Setting target temperature to 50°C")

            ctx.comment("⏳ All three tasks running concurrently (TC + TD + HS)...")
            # Wait for all three tasks to complete using ctx.wait_for_tasks()
            ctx.wait_for_tasks([tc_task, td_task, hs_task])
            ctx.comment("✓ TEST 3 COMPLETE: TC, TD, and HS finished")
            ctx.comment("")

        # ========== TEST 4: TC, TD, HS, and Plate Reader Operating Concurrently ==========
        if test_scenario in ["all", "tc_td_hs_pr"]:
            ctx.comment("")
            ctx.comment("╔════════════════════════════════════════════════════════════════╗")
            ctx.comment("║  TEST 4: THERMOCYCLER (TC), TEMPERATURE MODULE (TD),           ║")
            ctx.comment("║          HEATER-SHAKER (HS), and PLATE READER (PR) CONCURRENT  ║")
            ctx.comment("╠════════════════════════════════════════════════════════════════╣")
            ctx.comment("║  Description:                                                  ║")
            ctx.comment("║    Four independent modules running simultaneously.             ║")
            ctx.comment("║    - TC on A1/B1: Executing PCR amplification                  ║")
            ctx.comment("║    - TD on C1: Pre-incubating samples to 37°C                  ║")
            ctx.comment("║    - HS on D1: Heating reaction vessel to 55°C                 ║")
            ctx.comment("║    - PR on B3: Initializing and reading absorbance at 562 nm   ║")
            ctx.comment("║                                                                ║")
            ctx.comment("║  Expected Behavior:                                            ║")
            ctx.comment("║    Temperature tasks start without blocking.                   ║")
            ctx.comment("║    Plate reader initialize/read runs while modules heat.         ║")
            ctx.comment("║    Demonstrates mixed module types operating in parallel.      ║")
            ctx.comment("╚════════════════════════════════════════════════════════════════╝")
            ctx.comment("")

            assert reader_plate is not None

            # ASYNC: Start TC profile execution
            tc_steps = [
                {"temperature": 95, "hold_time_seconds": 10},
                {"temperature": 62, "hold_time_seconds": 10},
                {"temperature": 72, "hold_time_seconds": 10},
            ]
            tc_task = thermocycler.start_execute_profile(steps=tc_steps, repetitions=1)
            ctx.comment("→ TC async task initiated: Executing 3-step PCR profile (95→62→72°C)")

            # ASYNC: Start TD temperature change
            td_task = temperature_module_01.start_set_temperature(celsius=37.0)
            ctx.comment("→ TD 01 async task initiated: Setting temperature to 37°C")

            # ASYNC: Start HS temperature change
            hs_task = heater_shaker_01.set_target_temperature(celsius=55.0)
            ctx.comment("→ HS 01 async task initiated: Setting target temperature to 55°C")

            ctx.comment("⏳ Temperature tasks running concurrently with plate reader setup...")
            plate_reader.initialize("single", [562])
            plate_reader.open_lid()
            ctx.move_labware(reader_plate, plate_reader, use_gripper=True)
            plate_reader.close_lid()
            read_result = plate_reader.read()
            ctx.comment(f"→ PR read complete: {read_result}")

            ctx.wait_for_tasks([tc_task, td_task, hs_task])
            plate_reader.open_lid()
            ctx.move_labware(reader_plate, "C2", use_gripper=True)
            plate_reader.close_lid()
            ctx.comment("✓ TEST 4 COMPLETE: TC, TD, HS, and Plate Reader finished")
            ctx.comment("")

        # ========== TEST 5: TC, TD, Plate Reader, and Gripper (no HS) ==========
        if test_scenario in ["all", "tc_td_pr_gripper"]:
            ctx.comment("")
            ctx.comment("╔════════════════════════════════════════════════════════════════╗")
            ctx.comment("║  TEST 5: THERMOCYCLER (TC), TEMPERATURE MODULE (TD),           ║")
            ctx.comment("║          PLATE READER (PR), and GRIPPER CONCURRENT             ║")
            ctx.comment("╠════════════════════════════════════════════════════════════════╣")
            ctx.comment("║  Description:                                                  ║")
            ctx.comment("║    TC + TD run async while gripper moves labware between       ║")
            ctx.comment("║    deck slots, TD, TC, and the plate reader.                   ║")
            ctx.comment("║    - TC on A1/B1: Executing PCR amplification                  ║")
            ctx.comment("║    - TD on D1: Holding samples at 37°C                         ║")
            ctx.comment("║    - PR on B3: Absorbance read at 562 nm                       ║")
            ctx.comment("║    - Gripper: Move plates TD ↔ deck ↔ PR; onto TC after profile ║")
            ctx.comment("║                                                                ║")
            ctx.comment("║  Expected Behavior:                                            ║")
            ctx.comment("║    Module tasks continue while gripper relocates labware.      ║")
            ctx.comment("║    No heater-shaker heating (isolates TC/TD/PR + gripper).     ║")
            ctx.comment("╚════════════════════════════════════════════════════════════════╝")
            ctx.comment("")

            assert reader_plate is not None
            assert pcr_plate is not None

            # Ensure modules are ready for gripper access
            thermocycler.open_lid()
            plate_reader.close_lid()

            # ASYNC: Start TC profile execution
            tc_steps = [
                {"temperature": 95, "hold_time_seconds": 10},
                {"temperature": 60, "hold_time_seconds": 10},
                {"temperature": 72, "hold_time_seconds": 10},
            ]
            tc_task = thermocycler.start_execute_profile(steps=tc_steps, repetitions=1)
            ctx.comment("→ TC async task initiated: Executing 3-step PCR profile (95→60→72°C)")

            # ASYNC: Start TD temperature change
            td_task = temperature_module_01.start_set_temperature(celsius=37.0)
            ctx.comment("→ TD 01 async task initiated: Setting temperature to 37°C")

            ctx.comment("⏳ TC + TD running concurrently with gripper labware moves...")

            # Gripper: move PCR plate onto TD adapter, then back to C3
            ctx.move_labware(pcr_plate, temperature_module_adapter_01, use_gripper=True)
            ctx.comment("→ Gripper moved PCR plate onto TD")
            ctx.move_labware(pcr_plate, "C3", use_gripper=True)
            ctx.comment("→ Gripper returned PCR plate to C3")

            # Plate reader initialize + gripper load + read (while TC/TD still running)
            plate_reader.initialize("single", [562])
            plate_reader.open_lid()
            ctx.move_labware(reader_plate, plate_reader, use_gripper=True)
            ctx.comment("→ Gripper moved reader plate onto PR")
            plate_reader.close_lid()
            read_result = plate_reader.read()
            ctx.comment(f"→ PR read complete: {read_result}")

            ctx.wait_for_tasks([tc_task, td_task])

            # Gripper: park PCR plate on TC after profile completes, then return to C3
            thermocycler.open_lid()
            ctx.move_labware(pcr_plate, thermocycler, use_gripper=True)
            ctx.comment("→ Gripper moved PCR plate onto TC")
            ctx.move_labware(pcr_plate, "C3", use_gripper=True)
            ctx.comment("→ Gripper returned PCR plate to C3")

            plate_reader.open_lid()
            ctx.move_labware(reader_plate, "C2", use_gripper=True)
            plate_reader.close_lid()
            ctx.comment("✓ TEST 5 COMPLETE: TC, TD, Plate Reader, and Gripper finished")
            ctx.comment("")

        # ========== TEST 6: TC, TD(1), TD(2), and HS Operating Concurrently ==========
        # Disabled — requires Temperature Module #2 on C3
        # if test_scenario in ["all", "tc_td_td_hs"]:
        #     ctx.comment("")
        #     ctx.comment("╔════════════════════════════════════════════════════════════════╗")
        #     ctx.comment("║  TEST 6: THERMOCYCLER (TC), TEMPERATURE MODULE (TD #1),        ║")
        #     ctx.comment("║          TEMPERATURE MODULE (TD #2), and HEATER-SHAKER (HS)    ║")
        #     ctx.comment("║          CONCURRENT                                            ║")
        #     ctx.comment("╠════════════════════════════════════════════════════════════════╣")
        #     ctx.comment("║  Description:                                                  ║")
        #     ctx.comment("║    Four independent modules running simultaneously.             ║")
        #     ctx.comment("║    - TC on A1/B1: Executing PCR amplification                  ║")
        #     ctx.comment("║    - TD #1 on C1: Warming samples to 20°C                      ║")
        #     ctx.comment("║    - TD #2 on C3: Deep freezing samples to 10°C                ║")
        #     ctx.comment("║    - HS on D1: Heating reaction chamber to 60°C                ║")
        #     ctx.comment("║                                                                ║")
        #     ctx.comment("║  Expected Behavior:                                            ║")
        #     ctx.comment("║    All four tasks start without blocking.                      ║")
        #     ctx.comment("║    Demonstrates multiple instances of Temperature Module       ║")
        #     ctx.comment("║    at different setpoints operating concurrently.              ║")
        #     ctx.comment("║    Shows advanced temperature profile management.              ║")
        #     ctx.comment("╚════════════════════════════════════════════════════════════════╝")
        #     ctx.comment("")
        #
        #     # ASYNC: Start TC profile execution
        #     tc_steps = [
        #         {"temperature": 98, "hold_time_seconds": 8},
        #         {"temperature": 55, "hold_time_seconds": 8},
        #         {"temperature": 72, "hold_time_seconds": 8},
        #     ]
        #     tc_task = thermocycler.start_execute_profile(steps=tc_steps, repetitions=1)
        #     ctx.comment("→ TC async task initiated: Executing 3-step PCR profile (98→55→72°C)")
        #
        #     # ASYNC: Start TD #1 temperature change
        #     td_task_01 = temperature_module_01.start_set_temperature(celsius=20.0)
        #     ctx.comment("→ TD 01 async task initiated: Setting temperature to 20°C")
        #
        #     # ASYNC: Start TD #2 temperature change
        #     td_task_02 = temperature_module_02.start_set_temperature(celsius=10.0)
        #     ctx.comment("→ TD 02 async task initiated: Setting temperature to 10°C")
        #
        #     # ASYNC: Start HS temperature change
        #     hs_task = heater_shaker_01.set_target_temperature(celsius=60.0)
        #     ctx.comment("→ HS 01 async task initiated: Setting target temperature to 60°C")
        #
        #     ctx.comment("⏳ All four tasks running concurrently (TC + TD₁ + TD₂ + HS)...")
        #     ctx.wait_for_tasks([tc_task, td_task_01, td_task_02, hs_task])
        #     ctx.comment("✓ TEST 6 COMPLETE: TC, TD #1, TD #2, and HS finished")
        #     ctx.comment("")

        # ========== Deactivate All Modules ==========
        ctx.comment("========== DEACTIVATING ALL MODULES ==========")
        heater_shaker_01.close_labware_latch()
        # heater_shaker_02.close_labware_latch()
        plate_reader.close_lid()

        heater_shaker_01.deactivate_heater()
        # heater_shaker_02.deactivate_heater()
        temperature_module_01.deactivate()
        # temperature_module_02.deactivate()
        thermocycler.deactivate_block()
        thermocycler.deactivate_lid()

        ctx.comment("========== ALL CONCURRENT MODULE TESTS COMPLETE ==========")
        ctx.comment("Smoke test successfully demonstrated concurrent module operations")