import json
from contextlib import nullcontext as pd_step
from opentrons import protocol_api, types

metadata = {
    "created": "2025-06-04T19:07:40.125Z",
    "lastModified": "2025-06-04T20:21:24.468Z",
    "protocolDesigner": "8.4.4",
    "source": "Protocol Designer",
}

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.24",
}

def run(protocol: protocol_api.ProtocolContext) -> None:
    # Load Modules:
    thermocycler_module_1 = protocol.load_module("thermocyclerModuleV2", "B1")
    magnetic_block_1 = protocol.load_module("magneticBlockV1", "C2")
    heater_shaker_module_1 = protocol.load_module("heaterShakerModuleV1", "D1")
    absorbance_reader_1 = protocol.load_module("absorbanceReaderV1", "B3")
    temperature_module_1 = protocol.load_module("temperatureModuleV2", "C1")

    # Load Adapters:
    adapter_3 = protocol.load_adapter(
        "opentrons_flex_96_tiprack_adapter",
        location="D2",
        namespace="opentrons",
        version=1,
    )
    adapter_2 = protocol.load_adapter(
        "opentrons_flex_96_tiprack_adapter",
        location="C3",
        namespace="opentrons",
        version=1,
    )
    adapter_1 = protocol.load_adapter(
        "opentrons_flex_96_tiprack_adapter",
        location="B2",
        namespace="opentrons",
        version=1,
    )
    adapter_4 = heater_shaker_module_1.load_adapter(
        "opentrons_96_pcr_adapter",
        namespace="opentrons",
        version=1,
    )
    aluminum_block_1 = temperature_module_1.load_adapter(
        "opentrons_96_well_aluminum_block",
        namespace="opentrons",
        version=1,
    )

    # Load Labware:
    tip_rack_1 = adapter_3.load_labware(
        "opentrons_flex_96_filtertiprack_1000ul",
        namespace="opentrons",
        version=1,
    )
    tip_rack_2 = adapter_2.load_labware(
        "opentrons_flex_96_filtertiprack_200ul",
        namespace="opentrons",
        version=1,
    )
    tip_rack_3 = adapter_1.load_labware(
        "opentrons_flex_96_filtertiprack_50ul",
        namespace="opentrons",
        version=1,
    )
    well_plate_1 = adapter_4.load_labware(
        "opentrons_96_wellplate_200ul_pcr_full_skirt",
        namespace="opentrons",
        version=3,
    )
    well_plate_2 = aluminum_block_1.load_labware(
        "biorad_96_wellplate_200ul_pcr",
        namespace="opentrons",
        version=3,
    )

    # Load Pipettes:
    pipette = protocol.load_instrument("flex_96channel_1000", tip_racks=[tip_rack_1, tip_rack_2, tip_rack_3])

    # Load Waste Chute:
    waste_chute = protocol.load_waste_chute()

    # Define Liquids:
    liquid_1 = protocol.define_liquid(
        "H20",
        display_color="#b925ff",
    )

    # PROTOCOL STEPS

    # Step 1:
    heater_shaker_module_1.close_labware_latch()
    heater_shaker_module_1.set_target_temperature(95)
    heater_shaker_module_1.set_and_wait_for_shake_speed(300)
    heater_shaker_module_1.wait_for_temperature()
    protocol.delay(seconds=60)

    # Step 2:
    heater_shaker_module_1.deactivate_heater()
    heater_shaker_module_1.open_labware_latch()

    # Step 3:
    absorbance_reader_1.close_lid()
    absorbance_reader_1.initialize("single", [450], reference_wavelength=600)

    # Step 4:
    absorbance_reader_1.open_lid()

    # Step 5:
    protocol.move_labware(well_plate_1, absorbance_reader_1, use_gripper=True)

    # Step 6:
    absorbance_reader_1.close_lid()
    absorbance_reader_1.read(export_filename="Potato")

    # Step 7:
    absorbance_reader_1.open_lid()

    # Step 8:
    protocol.move_labware(well_plate_1, "A2", use_gripper=True)

    # Step 9:
    thermocycler_module_1.open_lid()

    # Step 10:
    protocol.move_labware(well_plate_1, thermocycler_module_1, use_gripper=True)

    # Step 11:
    thermocycler_module_1.close_lid()
    thermocycler_module_1.set_lid_temperature(110)
    thermocycler_module_1.execute_profile(
        [
            {"temperature": 4, "hold_time_seconds": 10},
            {"temperature": 4, "hold_time_seconds": 10},
            {"temperature": 90, "hold_time_seconds": 10},
            {"temperature": 20, "hold_time_seconds": 10},
            {"temperature": 4, "hold_time_seconds": 10},
            {"temperature": 90, "hold_time_seconds": 10},
            {"temperature": 20, "hold_time_seconds": 10},
            {"temperature": 4, "hold_time_seconds": 10},
            {"temperature": 90, "hold_time_seconds": 10},
            {"temperature": 20, "hold_time_seconds": 10},
            {"temperature": 4, "hold_time_seconds": 10},
            {"temperature": 90, "hold_time_seconds": 10},
            {"temperature": 20, "hold_time_seconds": 10},
        ],
        1,
        block_max_volume=100,
    )
    thermocycler_module_1.set_block_temperature(55)

    # Step 12:
    temperature_module_1.start_set_temperature(55)

    # Step 13:
    temperature_module_1.await_temperature(55)

    # Step 14:
    protocol.delay(seconds=10)

    # Step 15:
    temperature_module_1.deactivate()

DESIGNER_APPLICATION = """{"robot":{"model":"OT-3 Standard"},"designerApplication":{"name":"opentrons/protocol-designer","version":"8.5.0","data":{"pipetteTiprackAssignments":{"d23ff181-e41f-4aa7-ad11-fd398fb2bdae":["opentrons/opentrons_flex_96_filtertiprack_1000ul/1","opentrons/opentrons_flex_96_filtertiprack_200ul/1","opentrons/opentrons_flex_96_filtertiprack_50ul/1"]},"dismissedWarnings":{"form":[],"timeline":[]},"ingredients":{"0":{"displayName":"H20","displayColor":"#b925ff","liquidClass":"waterV1","description":null,"liquidGroupId":"0"}},"ingredLocations":{},"savedStepForms":{"__INITIAL_DECK_SETUP_STEP__":{"stepType":"manualIntervention","id":"__INITIAL_DECK_SETUP_STEP__","labwareLocationUpdate":{"86e483ea-a31f-4bb8-9549-ffee8e2f286d:opentrons/opentrons_flex_96_tiprack_adapter/1":"D2","f4b8d2ef-0534-44e2-85b3-29d531cd8d62:opentrons/opentrons_flex_96_filtertiprack_1000ul/1":"86e483ea-a31f-4bb8-9549-ffee8e2f286d:opentrons/opentrons_flex_96_tiprack_adapter/1","405bf2f0-7d4e-4400-b272-350db82e70f7:opentrons/opentrons_flex_96_tiprack_adapter/1":"C3","8b34412a-c7ab-4606-8277-3b2fe4713f41:opentrons/opentrons_flex_96_filtertiprack_200ul/1":"405bf2f0-7d4e-4400-b272-350db82e70f7:opentrons/opentrons_flex_96_tiprack_adapter/1","10e95bb7-9aa7-4ed3-b3af-d3d1ebd6516d:opentrons/opentrons_flex_96_tiprack_adapter/1":"B2","b7c404da-901b-483c-a4de-4e107097bd08:opentrons/opentrons_flex_96_filtertiprack_50ul/1":"10e95bb7-9aa7-4ed3-b3af-d3d1ebd6516d:opentrons/opentrons_flex_96_tiprack_adapter/1","e3a51bfe-d2f0-4c8f-a21c-55c032f33766:opentrons/opentrons_96_pcr_adapter/1":"dfc31782-93b0-4ff9-bc23-b12262d53e99:heaterShakerModuleType","ef0952db-de5a-4946-93fa-d95f7f795752:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/3":"e3a51bfe-d2f0-4c8f-a21c-55c032f33766:opentrons/opentrons_96_pcr_adapter/1","6e6eaf24-df26-4039-acc2-f649819a15f4:opentrons/opentrons_96_well_aluminum_block/1":"9813524d-ab98-43da-b9dc-856d063a279d:temperatureModuleType","c6c2d29c-d398-472c-bf30-bd200cc4750d:opentrons/biorad_96_wellplate_200ul_pcr/3":"6e6eaf24-df26-4039-acc2-f649819a15f4:opentrons/opentrons_96_well_aluminum_block/1"},"pipetteLocationUpdate":{"d23ff181-e41f-4aa7-ad11-fd398fb2bdae":"left"},"moduleLocationUpdate":{"2af0d2b0-17b5-4024-a6ee-2f2fdb9d2fe8:thermocyclerModuleType":"B1","67682551-f4e1-46e4-a355-019d032e3f61:magneticBlockType":"C2","dfc31782-93b0-4ff9-bc23-b12262d53e99:heaterShakerModuleType":"D1","05e56fe4-cf53-45f8-9fc1-36bf8f00a617:absorbanceReaderType":"B3","9813524d-ab98-43da-b9dc-856d063a279d:temperatureModuleType":"C1"},"trashBinLocationUpdate":{},"wasteChuteLocationUpdate":{},"stagingAreaLocationUpdate":{},"gripperLocationUpdate":{"4289e9f8-22e3-440c-b007-5acfa87ab06e:gripper":"mounted"},"__INITIAL_DECK_SETUP_STEP__":{"stepType":"manualIntervention","id":"__INITIAL_DECK_SETUP_STEP__","labwareLocationUpdate":{},"pipetteLocationUpdate":{"d23ff181-e41f-4aa7-ad11-fd398fb2bdae":"left"},"moduleLocationUpdate":{},"trashBinLocationUpdate":{},"wasteChuteLocationUpdate":{"54ed4f79-f6ed-43ff-af2a-bd25569c1d41:wasteChute":"cutoutD3"},"stagingAreaLocationUpdate":{},"gripperLocationUpdate":{}}},"173bb328-2cd2-4bf3-869f-507ff65f402a":{"id":"173bb328-2cd2-4bf3-869f-507ff65f402a","stepType":"absorbanceReader","stepName":"absorbance plate reader","stepDetails":"","absorbanceReaderFormType":"absorbanceReaderInitialize","fileName":null,"lidOpen":null,"mode":"single","moduleId":"05e56fe4-cf53-45f8-9fc1-36bf8f00a617:absorbanceReaderType","referenceWavelength":"600","referenceWavelengthActive":true,"wavelengths":["450"]},"18fb25cb-bdd6-49d8-9f22-3f6eda3c894f":{"id":"18fb25cb-bdd6-49d8-9f22-3f6eda3c894f","stepType":"absorbanceReader","stepName":"absorbance plate reader","stepDetails":"","absorbanceReaderFormType":"absorbanceReaderLid","fileName":null,"lidOpen":true,"mode":"single","moduleId":"05e56fe4-cf53-45f8-9fc1-36bf8f00a617:absorbanceReaderType","referenceWavelength":null,"referenceWavelengthActive":false,"wavelengths":["450"]},"c87b46c4-dc35-448a-a135-c8ee013ad96f":{"id":"c87b46c4-dc35-448a-a135-c8ee013ad96f","stepType":"moveLabware","stepName":"move","stepDetails":"","labware":"ef0952db-de5a-4946-93fa-d95f7f795752:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/3","newLocation":"05e56fe4-cf53-45f8-9fc1-36bf8f00a617:absorbanceReaderType","useGripper":true},"274b2e7f-f77b-40c3-984f-eab15946c818":{"id":"274b2e7f-f77b-40c3-984f-eab15946c818","stepType":"absorbanceReader","stepName":"absorbance plate reader","stepDetails":"","absorbanceReaderFormType":"absorbanceReaderRead","fileName":"Potato","lidOpen":null,"mode":"single","moduleId":"05e56fe4-cf53-45f8-9fc1-36bf8f00a617:absorbanceReaderType","referenceWavelength":null,"referenceWavelengthActive":false,"wavelengths":["450"]},"b71695a2-7179-4229-84a1-5a5220785166":{"id":"b71695a2-7179-4229-84a1-5a5220785166","stepType":"absorbanceReader","stepName":"absorbance plate reader","stepDetails":"","absorbanceReaderFormType":"absorbanceReaderLid","fileName":null,"lidOpen":true,"mode":"single","moduleId":"05e56fe4-cf53-45f8-9fc1-36bf8f00a617:absorbanceReaderType","referenceWavelength":null,"referenceWavelengthActive":false,"wavelengths":["450"]},"f17ac366-6886-4162-91cd-41c625eb0d46":{"id":"f17ac366-6886-4162-91cd-41c625eb0d46","stepType":"heaterShaker","stepName":"heater-Shaker state","stepDetails":"","heaterShakerSetTimer":null,"heaterShakerTimer":null,"latchOpen":true,"moduleId":"dfc31782-93b0-4ff9-bc23-b12262d53e99:heaterShakerModuleType","setHeaterShakerTemperature":null,"setShake":null,"targetHeaterShakerTemperature":null,"targetSpeed":null},"6f8af9d3-1174-4270-9dff-7ee2e20c73f8":{"id":"6f8af9d3-1174-4270-9dff-7ee2e20c73f8","stepType":"heaterShaker","stepName":"heater-Shaker state","stepDetails":"","heaterShakerSetTimer":true,"heaterShakerTimer":"1:00","latchOpen":false,"moduleId":"dfc31782-93b0-4ff9-bc23-b12262d53e99:heaterShakerModuleType","setHeaterShakerTemperature":true,"setShake":true,"targetHeaterShakerTemperature":"95","targetSpeed":"300"},"08ce4017-b7a8-4041-8919-0c9bbc95c3aa":{"id":"08ce4017-b7a8-4041-8919-0c9bbc95c3aa","stepType":"moveLabware","stepName":"move","stepDetails":"","labware":"ef0952db-de5a-4946-93fa-d95f7f795752:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/3","newLocation":"A2","useGripper":true},"2b507519-a48b-486b-b817-0b6123177730":{"id":"2b507519-a48b-486b-b817-0b6123177730","stepType":"thermocycler","stepName":"thermocycler","stepDetails":"","blockIsActive":false,"blockIsActiveHold":false,"blockTargetTemp":null,"blockTargetTempHold":null,"lidIsActive":false,"lidIsActiveHold":false,"lidOpen":true,"lidOpenHold":null,"lidTargetTemp":"","lidTargetTempHold":null,"moduleId":"2af0d2b0-17b5-4024-a6ee-2f2fdb9d2fe8:thermocyclerModuleType","orderedProfileItems":[],"profileItemsById":{},"profileTargetLidTemp":null,"profileVolume":null,"thermocyclerFormType":"thermocyclerState"},"91d692df-5785-45f9-a469-ced1118bf5c5":{"id":"91d692df-5785-45f9-a469-ced1118bf5c5","stepType":"moveLabware","stepName":"move","stepDetails":"","labware":"ef0952db-de5a-4946-93fa-d95f7f795752:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/3","newLocation":"2af0d2b0-17b5-4024-a6ee-2f2fdb9d2fe8:thermocyclerModuleType","useGripper":true},"a59162be-3ae3-45d9-9253-338738844a1f":{"id":"a59162be-3ae3-45d9-9253-338738844a1f","stepType":"thermocycler","stepName":"thermocycler","stepDetails":"","blockIsActive":false,"blockIsActiveHold":true,"blockTargetTemp":null,"blockTargetTempHold":"55","lidIsActive":false,"lidIsActiveHold":true,"lidOpen":false,"lidOpenHold":false,"lidTargetTemp":null,"lidTargetTempHold":"110","moduleId":"2af0d2b0-17b5-4024-a6ee-2f2fdb9d2fe8:thermocyclerModuleType","orderedProfileItems":["5bb933fe-1da3-4e7c-98a1-ebaec004ba90","04971119-631c-465f-a63e-429c43cf8c82"],"profileItemsById":{"5bb933fe-1da3-4e7c-98a1-ebaec004ba90":{"durationMinutes":"00","durationSeconds":"10","id":"5bb933fe-1da3-4e7c-98a1-ebaec004ba90","temperature":"4","title":"f","type":"profileStep"},"04971119-631c-465f-a63e-429c43cf8c82":{"id":"04971119-631c-465f-a63e-429c43cf8c82","title":"","steps":[{"durationMinutes":"00","durationSeconds":"10","id":"fe73d444-0925-4e51-8d80-70e885706d19","temperature":"4","title":"f","type":"profileStep"},{"durationMinutes":"00","durationSeconds":"10","id":"3d080a2b-90f4-4ee2-ac80-b30401d5430c","temperature":"90","title":"ff","type":"profileStep"},{"durationMinutes":"00","durationSeconds":"10","id":"34365131-9bfd-4d55-8f2a-35f3032277f0","temperature":"20","title":"ff","type":"profileStep"}],"type":"profileCycle","repetitions":"4"}},"profileTargetLidTemp":"110","profileVolume":"100","thermocyclerFormType":"thermocyclerProfile"},"2bd8c5db-7a71-4e34-a12c-653cbcadc368":{"id":"2bd8c5db-7a71-4e34-a12c-653cbcadc368","stepType":"temperature","stepName":"temperature module state","stepDetails":"","moduleId":"9813524d-ab98-43da-b9dc-856d063a279d:temperatureModuleType","setTemperature":"true","targetTemperature":"55"},"d096d142-3f82-4d12-91a3-412b2766aa0a":{"id":"d096d142-3f82-4d12-91a3-412b2766aa0a","stepType":"pause","stepName":"pause","stepDetails":"","moduleId":"9813524d-ab98-43da-b9dc-856d063a279d:temperatureModuleType","pauseAction":"untilTemperature","pauseMessage":"","pauseTemperature":"55","pauseTime":null},"dbac2c1e-3dd9-475b-a010-5587822193f5":{"id":"dbac2c1e-3dd9-475b-a010-5587822193f5","stepType":"temperature","stepName":"temperature module state","stepDetails":"","moduleId":"9813524d-ab98-43da-b9dc-856d063a279d:temperatureModuleType","setTemperature":null,"targetTemperature":null},"a1bc29ef-e9b9-4bd6-a6fb-9a9a54d42769":{"id":"a1bc29ef-e9b9-4bd6-a6fb-9a9a54d42769","stepType":"pause","stepName":"pause","stepDetails":"","moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:00:10"}},"orderedStepIds":["6f8af9d3-1174-4270-9dff-7ee2e20c73f8","f17ac366-6886-4162-91cd-41c625eb0d46","173bb328-2cd2-4bf3-869f-507ff65f402a","18fb25cb-bdd6-49d8-9f22-3f6eda3c894f","c87b46c4-dc35-448a-a135-c8ee013ad96f","274b2e7f-f77b-40c3-984f-eab15946c818","b71695a2-7179-4229-84a1-5a5220785166","08ce4017-b7a8-4041-8919-0c9bbc95c3aa","2b507519-a48b-486b-b817-0b6123177730","91d692df-5785-45f9-a469-ced1118bf5c5","a59162be-3ae3-45d9-9253-338738844a1f","2bd8c5db-7a71-4e34-a12c-653cbcadc368","d096d142-3f82-4d12-91a3-412b2766aa0a","a1bc29ef-e9b9-4bd6-a6fb-9a9a54d42769","dbac2c1e-3dd9-475b-a010-5587822193f5"],"pipettes":{"d23ff181-e41f-4aa7-ad11-fd398fb2bdae":{"pipetteName":"p1000_96"}},"modules":{"2af0d2b0-17b5-4024-a6ee-2f2fdb9d2fe8:thermocyclerModuleType":{"model":"thermocyclerModuleV2"},"67682551-f4e1-46e4-a355-019d032e3f61:magneticBlockType":{"model":"magneticBlockV1"},"dfc31782-93b0-4ff9-bc23-b12262d53e99:heaterShakerModuleType":{"model":"heaterShakerModuleV1"},"05e56fe4-cf53-45f8-9fc1-36bf8f00a617:absorbanceReaderType":{"model":"absorbanceReaderV1"},"9813524d-ab98-43da-b9dc-856d063a279d:temperatureModuleType":{"model":"temperatureModuleV2"}},"labware":{"86e483ea-a31f-4bb8-9549-ffee8e2f286d:opentrons/opentrons_flex_96_tiprack_adapter/1":{"displayName":"Opentrons Flex 96 Tip Rack Adapter","labwareDefURI":"opentrons/opentrons_flex_96_tiprack_adapter/1"},"f4b8d2ef-0534-44e2-85b3-29d531cd8d62:opentrons/opentrons_flex_96_filtertiprack_1000ul/1":{"displayName":"Opentrons Flex 96 Filter Tip Rack 1000 µL","labwareDefURI":"opentrons/opentrons_flex_96_filtertiprack_1000ul/1"},"405bf2f0-7d4e-4400-b272-350db82e70f7:opentrons/opentrons_flex_96_tiprack_adapter/1":{"displayName":"Opentrons Flex 96 Tip Rack Adapter","labwareDefURI":"opentrons/opentrons_flex_96_tiprack_adapter/1"},"8b34412a-c7ab-4606-8277-3b2fe4713f41:opentrons/opentrons_flex_96_filtertiprack_200ul/1":{"displayName":"Opentrons Flex 96 Filter Tip Rack 200 µL","labwareDefURI":"opentrons/opentrons_flex_96_filtertiprack_200ul/1"},"10e95bb7-9aa7-4ed3-b3af-d3d1ebd6516d:opentrons/opentrons_flex_96_tiprack_adapter/1":{"displayName":"Opentrons Flex 96 Tip Rack Adapter","labwareDefURI":"opentrons/opentrons_flex_96_tiprack_adapter/1"},"b7c404da-901b-483c-a4de-4e107097bd08:opentrons/opentrons_flex_96_filtertiprack_50ul/1":{"displayName":"Opentrons Flex 96 Filter Tip Rack 50 µL","labwareDefURI":"opentrons/opentrons_flex_96_filtertiprack_50ul/1"},"e3a51bfe-d2f0-4c8f-a21c-55c032f33766:opentrons/opentrons_96_pcr_adapter/1":{"displayName":"Opentrons 96 PCR Heater-Shaker Adapter","labwareDefURI":"opentrons/opentrons_96_pcr_adapter/1"},"ef0952db-de5a-4946-93fa-d95f7f795752:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/3":{"displayName":"Opentrons Tough 96 Well Plate 200 µL PCR Full Skirt","labwareDefURI":"opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/3"},"6e6eaf24-df26-4039-acc2-f649819a15f4:opentrons/opentrons_96_well_aluminum_block/1":{"displayName":"Opentrons 96 Well Aluminum Block","labwareDefURI":"opentrons/opentrons_96_well_aluminum_block/1"},"c6c2d29c-d398-472c-bf30-bd200cc4750d:opentrons/biorad_96_wellplate_200ul_pcr/3":{"displayName":"Bio-Rad 96 Well Plate 200 µL PCR","labwareDefURI":"opentrons/biorad_96_wellplate_200ul_pcr/3"}}}},"metadata":{"protocolName":"","author":"","description":"","source":"Protocol Designer","created":1749064060125,"lastModified":1749068484468}}"""
