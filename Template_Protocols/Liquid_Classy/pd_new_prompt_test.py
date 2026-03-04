import json
from opentrons import protocol_api, types

metadata = {
    "created": "2026-02-28T00:00:00.000Z",
    "internalAppBuildDate": "Thu, 19 Feb 2026 15:56:59 GMT",
    "lastModified": "2026-03-01T00:00:00.000Z",
    "protocolDesigner": "8.8.1",
    "source": "Protocol Designer",
}

requirements = {"robotType": "Flex", "apiLevel": "2.27"}


def run(protocol: protocol_api.ProtocolContext) -> None:

    # 1. Modules
    stacker = protocol.load_module("flexStackerModuleV1", "D1")

    # 2. Adapters
    dest_adapter = protocol.load_adapter(
        "opentrons_96_flat_bottom_adapter", "A1",
        namespace="opentrons", version=1
    )

    # 3. Labware
    source_plate = protocol.load_labware(
        "thermoscientificnunc_96_wellplate_1300ul",
        "B3",
        namespace="thermoscientificnunc",
        version=1
    )

    dest_plate = dest_adapter.load_labware(
        "nest_96_wellplate_200ul_flat",
        namespace="opentrons",
        version=1
    )

    tiprack_l = protocol.load_labware(
        "opentrons_flex_96_filtertiprack_1000ul",
        "B2",
        namespace="opentrons",
        version=1
    )

    tiprack_r = protocol.load_labware(
        "opentrons_flex_96_filtertiprack_50ul",
        "C3",
        namespace="opentrons",
        version=1
    )

    # 4. Pipettes
    left_pipette = protocol.load_instrument(
        "flex_1channel_1000",
        "left",
        tip_racks=[tiprack_l]
    )

    right_pipette = protocol.load_instrument(
        "flex_1channel_50",
        "right",
        tip_racks=[tiprack_r]
    )

    # 5. Trash
    trash_bin = protocol.load_trash_bin("A3")

    # 6. Liquids
    reagent_1 = protocol.define_liquid(
        name="Reagent 1",
        description="Step 1",
        display_color="#007AFF"
    )

    reagent_2 = protocol.define_liquid(
        name="Reagent 2",
        description="Step 2",
        display_color="#FF2D55"
    )

    # 7. Load Liquids (merged correctly)
    source_plate.load_liquid(
        wells=["A7", "A5", "A2"],
        liquid=reagent_1,
        volume=196.0
    )

    source_plate.load_liquid(
        wells=["A6", "A3"],
        liquid=reagent_1,
        volume=196.0
    )

    source_plate.load_liquid(
        wells=["A9", "A12", "A10"],
        liquid=reagent_2,
        volume=8.0
    )

    source_plate.load_liquid(
        wells=["A6", "A3"],
        liquid=reagent_2,
        volume=8.0
    )

    # 8. Liquid Classes
    water_base = protocol.get_liquid_class("water")

    lc_1 = protocol.define_liquid_class(
        name="LC_Step1",
        base_liquid_class=water_base,
        properties={
            "flex_1channel_1000": {
                "opentrons/opentrons_flex_96_filtertiprack_1000ul/1": {
                    "aspirate": {"flow_rate_by_volume": [(0, 478)]},
                    "dispense": {"flow_rate_by_volume": [(0, 478)]}
                }
            }
        }
    )

    lc_2 = protocol.define_liquid_class(
        name="LC_Step2",
        base_liquid_class=water_base,
        properties={
            "flex_1channel_50": {
                "opentrons/opentrons_flex_96_filtertiprack_50ul/1": {
                    "aspirate": {"flow_rate_by_volume": [(0, 57)]},
                    "dispense": {"flow_rate_by_volume": [(0, 57)]}
                }
            }
        }
    )

    # 9. Stacker
    stacker.set_stored_labware(
        load_name="nest_96_wellplate_200ul_flat",
        namespace="opentrons",
        version=1,
        count=5
    )
    stacker.retrieve()

    # 10. Transfers
    left_pipette.transfer_with_liquid_class(
        volume=196.0,
        source=[source_plate[w] for w in ["A7", "A6", "A5", "A2", "A3"]],
        dest=[dest_plate[w] for w in ["A5", "A9", "A1", "A10", "A2"]],
        new_tip="always",
        trash_location=trash_bin,
        keep_last_tip=False,
        tip_racks=[tiprack_l],
        liquid_class=lc_1
    )

    right_pipette.transfer_with_liquid_class(
        volume=8.0,
        source=[source_plate[w] for w in ["A9", "A12", "A6", "A10", "A3"]],
        dest=[dest_plate[w] for w in ["A7", "A11", "A6", "A3", "A9"]],
        new_tip="once",
        trash_location=trash_bin,
        keep_last_tip=False,
        tip_racks=[tiprack_r],
        liquid_class=lc_2
    )


DESIGNER_APPLICATION = """{
  "robot": { "model": "OT-3 Standard" },
  "designerApplication": {
    "name": "opentrons/protocol-designer",
    "version": "8.8.1",
    "data": {
      "pipetteTiprackAssignments": {
        "pipette-l": ["opentrons/opentrons_flex_96_filtertiprack_1000ul/1"],
        "pipette-r": ["opentrons/opentrons_flex_96_filtertiprack_50ul/1"]
      },
      "dismissedWarnings": { "form": [], "timeline": [] },
      "ingredients": {
        "0": { "displayName": "Reagent 1", "displayColor": "#007AFF", "liquidGroupId": "0" },
        "1": { "displayName": "Reagent 2", "displayColor": "#FF2D55", "liquidGroupId": "1" }
      },
      "ingredLocations": {
        "src-plate:thermoscientificnunc/thermoscientificnunc_96_wellplate_1300ul/1": {
          "A7": { "0": { "volume": 196 } },
          "A5": { "0": { "volume": 196 } },
          "A2": { "0": { "volume": 196 } },
          "A6": { "0": { "volume": 196 }, "1": { "volume": 8 } },
          "A3": { "0": { "volume": 196 }, "1": { "volume": 8 } },
          "A9": { "1": { "volume": 8 } },
          "A12": { "1": { "volume": 8 } },
          "A10": { "1": { "volume": 8 } }
        }
      },
      "savedStepForms": {
        "__INITIAL_DECK_SETUP_STEP__": {
          "stepType": "manualIntervention",
          "id": "__INITIAL_DECK_SETUP_STEP__",
          "labwareLocationUpdate": {
            "src-plate:thermoscientificnunc/thermoscientificnunc_96_wellplate_1300ul/1": "B3",
            "dest-adap:opentrons/opentrons_96_flat_bottom_adapter/1": "A1",
            "dest-plate:opentrons/nest_96_wellplate_200ul_flat/1": "dest-adap:opentrons/opentrons_96_flat_bottom_adapter/1",
            "tiprack-l:opentrons/opentrons_flex_96_filtertiprack_1000ul/1": "B2",
            "tiprack-r:opentrons/opentrons_flex_96_filtertiprack_50ul/1": "C3"
          },
          "pipetteLocationUpdate": {
            "pipette-l": "left",
            "pipette-r": "right"
          },
          "moduleLocationUpdate": {
            "stacker:flexStackerModuleType": "D1"
          },
          "moduleStateUpdate": {},
          "trashBinLocationUpdate": {
            "trash:trashBin": "cutoutA3"
          },
          "wasteChuteLocationUpdate": {},
          "stagingAreaLocationUpdate": {},
          "gripperLocationUpdate": {}
        },
        "step-0": {
          "stepType": "flexStacker",
          "id": "step-0",
          "flexStackerFormType": "retrieve",
          "moduleId": "stacker:flexStackerModuleType"
        },
        "step-1": {
          "stepType": "moveLiquid",
          "id": "step-1",
          "pipette": "pipette-l",
          "volume": 196,
          "changeTip": "always",
          "aspirate_wells": ["A7", "A6", "A5", "A2", "A3"],
          "dispense_wells": ["A5", "A9", "A1", "A10", "A2"],
          "aspirate_labware": "src-plate:thermoscientificnunc/thermoscientificnunc_96_wellplate_1300ul/1",
          "dispense_labware": "dest-plate:opentrons/nest_96_wellplate_200ul_flat/1",
          "liquidClass": "water",
          "liquidClassesSupported": true,
          "nozzles": null,
          "path": "single",
          "tip_tracking": false,
          "tiprack_selected": "tiprack-l:opentrons/opentrons_flex_96_filtertiprack_1000ul/1",
          "tips_selected": [],
          "preWetTip": false,
          "pushOut_checkbox": false,
          "pushOut_volume": 0,
          "conditioning_checkbox": false,
          "conditioning_volume": 0,
          "disposalVolume_checkbox": false,
          "disposalVolume_volume": 0
        },
        "step-2": {
          "stepType": "moveLiquid",
          "id": "step-2",
          "pipette": "pipette-r",
          "volume": 8,
          "changeTip": "once",
          "aspirate_wells": ["A9", "A12", "A6", "A10", "A3"],
          "dispense_wells": ["A7", "A11", "A6", "A3", "A9"],
          "aspirate_labware": "src-plate:thermoscientificnunc/thermoscientificnunc_96_wellplate_1300ul/1",
          "dispense_labware": "dest-plate:opentrons/nest_96_wellplate_200ul_flat/1",
          "liquidClass": "water",
          "liquidClassesSupported": true,
          "nozzles": null,
          "path": "single",
          "tip_tracking": false,
          "tiprack_selected": "tiprack-r:opentrons/opentrons_flex_96_filtertiprack_50ul/1",
          "tips_selected": [],
          "preWetTip": false,
          "pushOut_checkbox": false,
          "pushOut_volume": 0,
          "conditioning_checkbox": false,
          "conditioning_volume": 0,
          "disposalVolume_checkbox": false,
          "disposalVolume_volume": 0
        }
      },
      "orderedStepIds": ["step-0", "step-1", "step-2"],
      "pipettes": {
        "pipette-l": { "pipetteName": "p1000_single_flex" },
        "pipette-r": { "pipetteName": "p50_single_flex" }
      },
      "modules": {
        "stacker:flexStackerModuleType": { "model": "flexStackerModuleV1" }
      },
      "labware": {
        "src-plate:thermoscientificnunc/thermoscientificnunc_96_wellplate_1300ul/1": {
          "displayName": "Src",
          "labwareDefURI": "thermoscientificnunc/thermoscientificnunc_96_wellplate_1300ul/1"
        },
        "dest-adap:opentrons/opentrons_96_flat_bottom_adapter/1": {
          "displayName": "Adap",
          "labwareDefURI": "opentrons/opentrons_96_flat_bottom_adapter/1"
        },
        "dest-plate:opentrons/nest_96_wellplate_200ul_flat/1": {
          "displayName": "Dest",
          "labwareDefURI": "opentrons/nest_96_wellplate_200ul_flat/1"
        },
        "tiprack-l:opentrons/opentrons_flex_96_filtertiprack_1000ul/1": {
          "displayName": "Tips L",
          "labwareDefURI": "opentrons/opentrons_flex_96_filtertiprack_1000ul/1"
        },
        "tiprack-r:opentrons/opentrons_flex_96_filtertiprack_50ul/1": {
          "displayName": "Tips R",
          "labwareDefURI": "opentrons/opentrons_flex_96_filtertiprack_50ul/1"
        }
      }
    }
  },
  "metadata": {
    "protocolName": "RT Example 18 Final",
    "author": "",
    "description": "",
    "source": "Protocol Designer",
    "created": 1772236800000,
    "lastModified": 1772236800000
  }
}"""