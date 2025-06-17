import json
from contextlib import nullcontext as pd_step
from opentrons import protocol_api, types

metadata = {
    "protocolName": "COVID Testing",
    "author": "Opentrons",
    "description": "Combine components of a PCR reaction, including patient swab samples, and run PCR to test for COVID-19. ",
    "created": "2025-04-21T19:19:09.837Z",
    "lastModified": "2025-05-15T19:41:27.286Z",
    "protocolDesigner": "8.4.4",
    "source": "Protocol Designer",
}

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.23",
}

def run(protocol: protocol_api.ProtocolContext) -> None:
    # Load Modules:
    thermocycler_module_1 = protocol.load_module("thermocyclerModuleV2", "B1")
    heater_shaker_module_1 = protocol.load_module("heaterShakerModuleV1", "D1")

    # Load Adapters:
    adapter_1 = heater_shaker_module_1.load_adapter(
        "opentrons_96_pcr_adapter",
        namespace="opentrons",
        version=1,
    )

    # Load Labware:
    tip_rack_1 = protocol.load_labware(
        "opentrons_flex_96_tiprack_1000ul",
        location="B2",
        namespace="opentrons",
        version=1,
    )
    tip_rack_2 = protocol.load_labware(
        "opentrons_flex_96_filtertiprack_50ul",
        location="A2",
        namespace="opentrons",
        version=1,
    )
    well_plate_1 = protocol.load_labware(
        "opentrons_96_wellplate_200ul_pcr_full_skirt",
        location="D2",
        label="Opentrons Tough 96 Well Plate 200 µL PCR Full Skirt (1)",
        namespace="opentrons",
        version=2,
    )
    well_plate_2 = protocol.load_labware(
        "opentrons_96_wellplate_200ul_pcr_full_skirt",
        location="C3",
        label="Opentrons Tough 96 Well Plate 200 µL PCR Full Skirt (2)",
        namespace="opentrons",
        version=2,
    )
    reservoir_1 = protocol.load_labware(
        "nest_12_reservoir_15ml",
        location="C2",
        namespace="opentrons",
        version=1,
    )

    # Load Pipettes:
    pipette_left = protocol.load_instrument("flex_8channel_1000", "left", tip_racks=[tip_rack_1, tip_rack_2])

    # Load Trash Bins:
    trash_bin_1 = protocol.load_trash_bin("A3")

    # Define Liquids:
    liquid_1 = protocol.define_liquid(
        "water",
        display_color="#50d5ffff",
    )
    liquid_2 = protocol.define_liquid(
        "master mix",
        description="PCR master mix containing forward and reverse primers, dNTPs, buffer, and DNA polymerase.",
        display_color="#b925ffff",
    )
    liquid_3 = protocol.define_liquid(
        "patient A DNA sample",
        display_color="#7eff42ff",
    )

    # Load Liquids:
    reservoir_1["A1"].load_liquid(liquid_1, 10000)
    well_plate_2["A1"].load_liquid(liquid_2, 12)
    well_plate_2["B1"].load_liquid(liquid_2, 12)
    well_plate_2["C1"].load_liquid(liquid_2, 12)
    well_plate_2["D1"].load_liquid(liquid_2, 12)
    well_plate_2["E1"].load_liquid(liquid_2, 12)
    well_plate_2["F1"].load_liquid(liquid_2, 12)
    well_plate_2["G1"].load_liquid(liquid_2, 12)
    well_plate_2["H1"].load_liquid(liquid_2, 12)
    well_plate_2["A3"].load_liquid(liquid_3, 5)
    well_plate_2["B3"].load_liquid(liquid_3, 5)
    well_plate_2["C3"].load_liquid(liquid_3, 5)
    well_plate_2["D3"].load_liquid(liquid_3, 5)
    well_plate_2["E3"].load_liquid(liquid_3, 5)
    well_plate_2["F3"].load_liquid(liquid_3, 5)
    well_plate_2["G3"].load_liquid(liquid_3, 5)
    well_plate_2["H3"].load_liquid(liquid_3, 5)

    # PROTOCOL STEPS

    # Step 1:
    pipette_left.pick_up_tip(location=tip_rack_2)
    pipette_left.move_to(well_plate_2["A1"].top(z=2))
    pipette_left.prepare_to_aspirate()
    pipette_left.move_to(well_plate_2["A1"].top())
    pipette_left.move_to(well_plate_2["A1"].bottom(), speed=100)
    pipette_left.flow_rate.aspirate = 478
    pipette_left.flow_rate.dispense = 478
    pipette_left.mix(
        repetitions=2,
        volume=6,
    )
    pipette_left.aspirate(
        volume=10,
        rate=478 / pipette_left.flow_rate.aspirate,
    )
    pipette_left.move_to(well_plate_2["A1"].top(), speed=100)
    pipette_left.move_to(well_plate_1["A1"].top())
    pipette_left.move_to(well_plate_1["A1"].bottom(), speed=100)
    pipette_left.dispense(
        volume=10,
        rate=478 / pipette_left.flow_rate.dispense,
        push_out=7,
    )
    pipette_left.move_to(well_plate_1["A1"].bottom(), speed=100)
    pipette_left.drop_tip()

    # Step 2:
    pipette_left.pick_up_tip(location=tip_rack_2)
    pipette_left.move_to(well_plate_2["A3"].top(z=2))
    pipette_left.prepare_to_aspirate()
    pipette_left.move_to(well_plate_2["A3"].top())
    pipette_left.move_to(well_plate_2["A3"].bottom(), speed=100)
    pipette_left.flow_rate.aspirate = 478
    pipette_left.flow_rate.dispense = 478
    pipette_left.mix(
        repetitions=1,
        volume=2.5,
    )
    pipette_left.aspirate(
        volume=5,
        rate=478 / pipette_left.flow_rate.aspirate,
    )
    pipette_left.move_to(well_plate_2["A3"].top(), speed=100)
    pipette_left.move_to(well_plate_1["A1"].top())
    pipette_left.move_to(well_plate_1["A1"].bottom(), speed=100)
    pipette_left.dispense(
        volume=5,
        rate=478 / pipette_left.flow_rate.dispense,
        push_out=7,
    )
    pipette_left.move_to(well_plate_1["A1"].bottom(), speed=100)
    pipette_left.drop_tip()

    # Step 3:
    pipette_left.pick_up_tip(location=tip_rack_2)
    pipette_left.move_to(reservoir_1["A1"].top(z=2))
    pipette_left.prepare_to_aspirate()
    pipette_left.move_to(reservoir_1["A1"].top())
    pipette_left.move_to(reservoir_1["A1"].bottom(), speed=100)
    pipette_left.aspirate(
        volume=5,
        rate=478 / pipette_left.flow_rate.aspirate,
    )
    pipette_left.move_to(reservoir_1["A1"].top(), speed=100)
    pipette_left.move_to(well_plate_1["A1"].top())
    pipette_left.move_to(well_plate_1["A1"].bottom(), speed=100)
    pipette_left.dispense(
        volume=5,
        rate=478 / pipette_left.flow_rate.dispense,
        push_out=7,
    )
    pipette_left.move_to(well_plate_1["A1"].bottom(), speed=100)
    pipette_left.drop_tip()

    # Step 4:
    heater_shaker_module_1.deactivate_heater()
    heater_shaker_module_1.open_labware_latch()

    # Step 5:
    protocol.move_labware(well_plate_1, adapter_1, use_gripper=True)

    # Step 6:
    heater_shaker_module_1.close_labware_latch()
    heater_shaker_module_1.deactivate_heater()

    # Step 7:
    heater_shaker_module_1.close_labware_latch()
    heater_shaker_module_1.deactivate_heater()
    heater_shaker_module_1.set_and_wait_for_shake_speed(200)
    protocol.delay(seconds=30)
    heater_shaker_module_1.deactivate_shaker()
    heater_shaker_module_1.deactivate_heater()

    # Step 8:
    heater_shaker_module_1.deactivate_heater()
    heater_shaker_module_1.open_labware_latch()

    # Step 9:
    thermocycler_module_1.open_lid()

    # Step 10:
    protocol.move_labware(well_plate_1, thermocycler_module_1, use_gripper=True)

    # Step 11:
    thermocycler_module_1.close_lid()

    # Step 12:
    thermocycler_module_1.set_lid_temperature(45)
    thermocycler_module_1.execute_profile(
        [
            {"temperature": 96, "hold_time_seconds": 30},
            {"temperature": 96, "hold_time_seconds": 10},
            {"temperature": 60, "hold_time_seconds": 20},
            {"temperature": 72, "hold_time_seconds": 40},
        ],
        1,
        block_max_volume=20,
    )
    thermocycler_module_1.set_block_temperature(4)
    thermocycler_module_1.deactivate_lid()

    # Step 13:
    thermocycler_module_1.open_lid()

DESIGNER_APPLICATION = """{"robot":{"model":"OT-3 Standard"},"designerApplication":{"name":"opentrons/protocol-designer","version":"8.5.0","data":{"pipetteTiprackAssignments":{"986da183-276c-49a7-bb4e-6c929635a151":["opentrons/opentrons_flex_96_tiprack_1000ul/1","opentrons/opentrons_flex_96_filtertiprack_50ul/1"]},"dismissedWarnings":{"form":[],"timeline":[]},"ingredients":{"0":{"displayName":"water","description":null,"displayColor":"#50d5ffff","liquidGroupId":"0","liquidClass":null},"1":{"displayName":"master mix","description":"PCR master mix containing forward and reverse primers, dNTPs, buffer, and DNA polymerase.","displayColor":"#b925ffff","liquidGroupId":"1","liquidClass":null},"2":{"displayName":"patient A DNA sample","description":null,"displayColor":"#7eff42ff","liquidGroupId":"2","liquidClass":null}},"ingredLocations":{"e6ff13e4-bac4-4635-8fed-a2d206521346:opentrons/nest_12_reservoir_15ml/1":{"A1":{"0":{"volume":10000}}},"60a7e129-8d4b-494c-8acd-17a9836f142e:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2":{"A1":{"1":{"volume":12}},"B1":{"1":{"volume":12}},"C1":{"1":{"volume":12}},"D1":{"1":{"volume":12}},"E1":{"1":{"volume":12}},"F1":{"1":{"volume":12}},"G1":{"1":{"volume":12}},"H1":{"1":{"volume":12}},"A3":{"2":{"volume":5}},"B3":{"2":{"volume":5}},"C3":{"2":{"volume":5}},"D3":{"2":{"volume":5}},"E3":{"2":{"volume":5}},"F3":{"2":{"volume":5}},"G3":{"2":{"volume":5}},"H3":{"2":{"volume":5}}}},"savedStepForms":{"__INITIAL_DECK_SETUP_STEP__":{"labwareLocationUpdate":{"84f76d25-6753-476b-a8d3-e7ff16022258:opentrons/opentrons_flex_96_tiprack_1000ul/1":"B2","4185a3ec-548f-4b52-950d-73dee4d20b4a:opentrons/opentrons_flex_96_filtertiprack_50ul/1":"A2","77d2fa6a-a9e6-4c68-92b2-afc163f96282:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2":"D2","60a7e129-8d4b-494c-8acd-17a9836f142e:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2":"C3","e6ff13e4-bac4-4635-8fed-a2d206521346:opentrons/nest_12_reservoir_15ml/1":"C2","33d1937f-81e0-4bec-96ff-00deceff3e23:opentrons/opentrons_96_pcr_adapter/1":"4d97ec01-fccc-4d7e-a43b-e78ea482776a:heaterShakerModuleType"},"moduleLocationUpdate":{"0859b448-cbdf-4849-98f3-d9047fa22c8e:thermocyclerModuleType":"B1","4d97ec01-fccc-4d7e-a43b-e78ea482776a:heaterShakerModuleType":"D1"},"pipetteLocationUpdate":{"986da183-276c-49a7-bb4e-6c929635a151":"left"},"trashBinLocationUpdate":{"6f2a1910-d975-432d-b3d8-106f4b2e07ff:trashBin":"cutoutA3"},"wasteChuteLocationUpdate":{},"stagingAreaLocationUpdate":{},"gripperLocationUpdate":{"701d2122-fada-4c89-9ba0-c04f4e513243:gripper":"mounted"},"stepType":"manualIntervention","id":"__INITIAL_DECK_SETUP_STEP__"},"3835e4ab-c649-4bd7-9d84-1135026c1385":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_mmFromBottom":null,"aspirate_delay_seconds":"1","aspirate_flowRate":"478","aspirate_labware":"60a7e129-8d4b-494c-8acd-17a9836f142e:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2","aspirate_mix_checkbox":true,"aspirate_mix_times":"2","aspirate_mix_volume":"6","aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":null,"aspirate_retract_mmFromBottom":0,"aspirate_retract_speed":100,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":null,"aspirate_submerge_speed":100,"aspirate_submerge_mmFromBottom":0,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":300,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":null,"blowout_location":null,"blowout_z_offset":0,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_mmFromBottom":null,"dispense_delay_seconds":"1","dispense_flowRate":null,"dispense_labware":"77d2fa6a-a9e6-4c68-92b2-afc163f96282:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":null,"dispense_retract_mmFromBottom":0,"dispense_retract_speed":100,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":null,"dispense_submerge_speed":100,"dispense_submerge_mmFromBottom":0,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":300,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"6f2a1910-d975-432d-b3d8-106f4b2e07ff:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"986da183-276c-49a7-bb4e-6c929635a151","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":7,"tipRack":"opentrons/opentrons_flex_96_filtertiprack_50ul/1","volume":"10","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","id":"3835e4ab-c649-4bd7-9d84-1135026c1385","dispense_touchTip_mmfromTop":null},"e0b64d0c-ddac-4fd6-a849-5b3876501be4":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_mmFromBottom":null,"aspirate_delay_seconds":"1","aspirate_flowRate":"478","aspirate_labware":"60a7e129-8d4b-494c-8acd-17a9836f142e:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2","aspirate_mix_checkbox":true,"aspirate_mix_times":"1","aspirate_mix_volume":"2.5","aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":null,"aspirate_retract_mmFromBottom":0,"aspirate_retract_speed":100,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":null,"aspirate_submerge_speed":100,"aspirate_submerge_mmFromBottom":0,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":300,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":null,"blowout_location":null,"blowout_z_offset":0,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_mmFromBottom":null,"dispense_delay_seconds":"1","dispense_flowRate":null,"dispense_labware":"77d2fa6a-a9e6-4c68-92b2-afc163f96282:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":null,"dispense_retract_mmFromBottom":0,"dispense_retract_speed":100,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":null,"dispense_submerge_speed":100,"dispense_submerge_mmFromBottom":0,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":300,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"6f2a1910-d975-432d-b3d8-106f4b2e07ff:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"986da183-276c-49a7-bb4e-6c929635a151","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":7,"tipRack":"opentrons/opentrons_flex_96_filtertiprack_50ul/1","volume":"5","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","id":"e0b64d0c-ddac-4fd6-a849-5b3876501be4","dispense_touchTip_mmfromTop":null},"496d3cdb-8697-4644-adc8-bac4671c2175":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_mmFromBottom":null,"aspirate_delay_seconds":"1","aspirate_flowRate":"478","aspirate_labware":"e6ff13e4-bac4-4635-8fed-a2d206521346:opentrons/nest_12_reservoir_15ml/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":null,"aspirate_retract_mmFromBottom":0,"aspirate_retract_speed":100,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":null,"aspirate_submerge_speed":100,"aspirate_submerge_mmFromBottom":0,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":300,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":null,"blowout_location":null,"blowout_z_offset":0,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_mmFromBottom":null,"dispense_delay_seconds":"1","dispense_flowRate":null,"dispense_labware":"77d2fa6a-a9e6-4c68-92b2-afc163f96282:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":null,"dispense_retract_mmFromBottom":0,"dispense_retract_speed":100,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":null,"dispense_submerge_speed":100,"dispense_submerge_mmFromBottom":0,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":300,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"6f2a1910-d975-432d-b3d8-106f4b2e07ff:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"986da183-276c-49a7-bb4e-6c929635a151","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":7,"tipRack":"opentrons/opentrons_flex_96_filtertiprack_50ul/1","volume":"5","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","id":"496d3cdb-8697-4644-adc8-bac4671c2175","dispense_touchTip_mmfromTop":null},"08f5b8c3-5415-4f62-a27e-b2ee2be36aca":{"labware":"77d2fa6a-a9e6-4c68-92b2-afc163f96282:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2","newLocation":"33d1937f-81e0-4bec-96ff-00deceff3e23:opentrons/opentrons_96_pcr_adapter/1","useGripper":true,"id":"08f5b8c3-5415-4f62-a27e-b2ee2be36aca","stepType":"moveLabware","stepName":"move","stepDetails":""},"92520259-6f6f-4847-8440-67952b75bee7":{"heaterShakerSetTimer":null,"heaterShakerTimer":null,"latchOpen":true,"moduleId":"4d97ec01-fccc-4d7e-a43b-e78ea482776a:heaterShakerModuleType","setHeaterShakerTemperature":null,"setShake":null,"targetHeaterShakerTemperature":null,"targetSpeed":null,"id":"92520259-6f6f-4847-8440-67952b75bee7","stepType":"heaterShaker","stepName":"heater-shaker","stepDetails":""},"9481ae5d-fb11-4d32-9a41-143869f96ce5":{"heaterShakerSetTimer":null,"heaterShakerTimer":null,"latchOpen":false,"moduleId":"4d97ec01-fccc-4d7e-a43b-e78ea482776a:heaterShakerModuleType","setHeaterShakerTemperature":null,"setShake":null,"targetHeaterShakerTemperature":null,"targetSpeed":null,"id":"9481ae5d-fb11-4d32-9a41-143869f96ce5","stepType":"heaterShaker","stepName":"heater-shaker","stepDetails":""},"d0fd8ada-3163-498f-b5fc-09a4d5ceae54":{"heaterShakerSetTimer":true,"heaterShakerTimer":"00:30","latchOpen":false,"moduleId":"4d97ec01-fccc-4d7e-a43b-e78ea482776a:heaterShakerModuleType","setHeaterShakerTemperature":null,"setShake":true,"targetHeaterShakerTemperature":null,"targetSpeed":"200","id":"d0fd8ada-3163-498f-b5fc-09a4d5ceae54","stepType":"heaterShaker","stepName":"heater-shaker","stepDetails":""},"11ceb3e7-9440-4e49-b8e4-c34368204165":{"heaterShakerSetTimer":null,"heaterShakerTimer":null,"latchOpen":true,"moduleId":"4d97ec01-fccc-4d7e-a43b-e78ea482776a:heaterShakerModuleType","setHeaterShakerTemperature":null,"setShake":null,"targetHeaterShakerTemperature":null,"targetSpeed":null,"id":"11ceb3e7-9440-4e49-b8e4-c34368204165","stepType":"heaterShaker","stepName":"heater-shaker","stepDetails":""},"52c4a4b2-8336-4465-b265-54c50d07821d":{"labware":"77d2fa6a-a9e6-4c68-92b2-afc163f96282:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2","newLocation":"0859b448-cbdf-4849-98f3-d9047fa22c8e:thermocyclerModuleType","useGripper":true,"id":"52c4a4b2-8336-4465-b265-54c50d07821d","stepType":"moveLabware","stepName":"move","stepDetails":""},"476e8c0f-dd0b-43b2-a53c-ac759cc175f2":{"blockIsActive":false,"blockIsActiveHold":false,"blockTargetTemp":null,"blockTargetTempHold":null,"lidIsActive":false,"lidIsActiveHold":false,"lidOpen":true,"lidOpenHold":null,"lidTargetTemp":null,"lidTargetTempHold":null,"moduleId":"0859b448-cbdf-4849-98f3-d9047fa22c8e:thermocyclerModuleType","orderedProfileItems":[],"profileItemsById":{},"profileTargetLidTemp":null,"profileVolume":null,"thermocyclerFormType":"thermocyclerState","id":"476e8c0f-dd0b-43b2-a53c-ac759cc175f2","stepType":"thermocycler","stepName":"thermocycler","stepDetails":""},"8bb12ce0-70df-4425-a16f-e841322fb2f2":{"blockIsActive":false,"blockIsActiveHold":false,"blockTargetTemp":null,"blockTargetTempHold":null,"lidIsActive":false,"lidIsActiveHold":false,"lidOpen":false,"lidOpenHold":null,"lidTargetTemp":null,"lidTargetTempHold":null,"moduleId":"0859b448-cbdf-4849-98f3-d9047fa22c8e:thermocyclerModuleType","orderedProfileItems":[],"profileItemsById":{},"profileTargetLidTemp":null,"profileVolume":null,"thermocyclerFormType":"thermocyclerState","id":"8bb12ce0-70df-4425-a16f-e841322fb2f2","stepType":"thermocycler","stepName":"thermocycler","stepDetails":""},"c9be8870-6542-4a3c-b4b9-d1996b078f64":{"blockIsActive":false,"blockIsActiveHold":true,"blockTargetTemp":null,"blockTargetTempHold":"4","lidIsActive":false,"lidIsActiveHold":false,"lidOpen":false,"lidOpenHold":null,"lidTargetTemp":null,"lidTargetTempHold":null,"moduleId":"0859b448-cbdf-4849-98f3-d9047fa22c8e:thermocyclerModuleType","orderedProfileItems":["43beff23-ae8e-4244-afb7-2250ab8a6fa0","4928d07b-d619-4bcf-82d7-630bd7ffec4c"],"profileItemsById":{"43beff23-ae8e-4244-afb7-2250ab8a6fa0":{"durationMinutes":"0","durationSeconds":"30","id":"43beff23-ae8e-4244-afb7-2250ab8a6fa0","temperature":"96","title":"Initial denaturation","type":"profileStep"},"4928d07b-d619-4bcf-82d7-630bd7ffec4c":{"id":"4928d07b-d619-4bcf-82d7-630bd7ffec4c","title":"","steps":[{"durationMinutes":"0","durationSeconds":"10","id":"406f9ade-aeb3-4806-85ad-7a6d615264d2","temperature":"96","title":"Denaturation","type":"profileStep"},{"durationMinutes":"0","durationSeconds":"20","id":"2c2983cd-c04c-4f93-a5a5-74752e3a1050","temperature":"60","title":"Annealing","type":"profileStep"},{"durationMinutes":"0","durationSeconds":"40","id":"66cde258-f7d4-4953-8191-1e0f34b88507","temperature":"72","title":"Extension","type":"profileStep"}],"type":"profileCycle","repetitions":"1"}},"profileTargetLidTemp":"45","profileVolume":"20","thermocyclerFormType":"thermocyclerProfile","id":"c9be8870-6542-4a3c-b4b9-d1996b078f64","stepType":"thermocycler","stepName":"thermocycler","stepDetails":""},"dec9ad1a-4592-4ca5-b216-b5d22a796313":{"blockIsActive":true,"blockIsActiveHold":false,"blockTargetTemp":4,"blockTargetTempHold":null,"lidIsActive":false,"lidIsActiveHold":false,"lidOpen":true,"lidOpenHold":null,"lidTargetTemp":null,"lidTargetTempHold":null,"moduleId":"0859b448-cbdf-4849-98f3-d9047fa22c8e:thermocyclerModuleType","orderedProfileItems":[],"profileItemsById":{},"profileTargetLidTemp":null,"profileVolume":null,"thermocyclerFormType":"thermocyclerState","id":"dec9ad1a-4592-4ca5-b216-b5d22a796313","stepType":"thermocycler","stepName":"thermocycler","stepDetails":""}},"orderedStepIds":["3835e4ab-c649-4bd7-9d84-1135026c1385","e0b64d0c-ddac-4fd6-a849-5b3876501be4","496d3cdb-8697-4644-adc8-bac4671c2175","92520259-6f6f-4847-8440-67952b75bee7","08f5b8c3-5415-4f62-a27e-b2ee2be36aca","9481ae5d-fb11-4d32-9a41-143869f96ce5","d0fd8ada-3163-498f-b5fc-09a4d5ceae54","11ceb3e7-9440-4e49-b8e4-c34368204165","476e8c0f-dd0b-43b2-a53c-ac759cc175f2","52c4a4b2-8336-4465-b265-54c50d07821d","8bb12ce0-70df-4425-a16f-e841322fb2f2","c9be8870-6542-4a3c-b4b9-d1996b078f64","dec9ad1a-4592-4ca5-b216-b5d22a796313"],"pipettes":{"986da183-276c-49a7-bb4e-6c929635a151":{"pipetteName":"p1000_multi_flex"}},"modules":{"0859b448-cbdf-4849-98f3-d9047fa22c8e:thermocyclerModuleType":{"model":"thermocyclerModuleV2"},"4d97ec01-fccc-4d7e-a43b-e78ea482776a:heaterShakerModuleType":{"model":"heaterShakerModuleV1"}},"labware":{"33d1937f-81e0-4bec-96ff-00deceff3e23:opentrons/opentrons_96_pcr_adapter/1":{"displayName":"Opentrons 96 PCR Heater-Shaker Adapter","labwareDefURI":"opentrons/opentrons_96_pcr_adapter/1"},"84f76d25-6753-476b-a8d3-e7ff16022258:opentrons/opentrons_flex_96_tiprack_1000ul/1":{"displayName":"Opentrons Flex 96 Tip Rack 1000 µL","labwareDefURI":"opentrons/opentrons_flex_96_tiprack_1000ul/1"},"4185a3ec-548f-4b52-950d-73dee4d20b4a:opentrons/opentrons_flex_96_filtertiprack_50ul/1":{"displayName":"Opentrons Flex 96 Filter Tip Rack 50 µL","labwareDefURI":"opentrons/opentrons_flex_96_filtertiprack_50ul/1"},"77d2fa6a-a9e6-4c68-92b2-afc163f96282:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2":{"displayName":"Opentrons Tough 96 Well Plate 200 µL PCR Full Skirt (1)","labwareDefURI":"opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2"},"60a7e129-8d4b-494c-8acd-17a9836f142e:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2":{"displayName":"Opentrons Tough 96 Well Plate 200 µL PCR Full Skirt (2)","labwareDefURI":"opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2"},"e6ff13e4-bac4-4635-8fed-a2d206521346:opentrons/nest_12_reservoir_15ml/1":{"displayName":"NEST 12 Well Reservoir 15 mL","labwareDefURI":"opentrons/nest_12_reservoir_15ml/1"}}}},"metadata":{"protocolName":"COVID Testing","author":"Opentrons","description":"Combine components of a PCR reaction, including patient swab samples, and run PCR to test for COVID-19. ","created":1745263149837,"lastModified":1747338087286,"category":null,"subcategory":null,"tags":[],"source":"Protocol Designer"}}"""