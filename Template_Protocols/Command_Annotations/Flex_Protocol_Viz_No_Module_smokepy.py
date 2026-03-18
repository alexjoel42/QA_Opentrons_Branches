from opentrons import protocol_api

requirements = {"robotType": "Flex", "apiLevel": "2.29"}


def run(protocol: protocol_api.ProtocolContext):


    tiprack_1 = protocol.load_labware(
        load_name="opentrons_flex_96_tiprack_200ul", location="D2"
    )
    define_liquid = protocol.define_liquid(name="buffer", display_color="#00FF00")
    tc = protocol.load_module(module_name="thermocyclerModuleV2")
    tempdeck = protocol.load_module(module_name="temperatureModuleV2", location="D1")
    tempdeck = tempdeck.load_adapter("opentrons_96_deep_well_temp_mod_adapter")
    deep = tempdeck.load_labware("nest_96_wellplate_2ml_deep")
    plate = tc.load_labware("opentrons_96_wellplate_200ul_pcr_full_skirt")
    plate.load_liquid(
        wells=[plate.wells_by_name()["A1"]], volume=200, liquid=define_liquid
    )
    tc.open_lid()
    trash = protocol.load_trash_bin("A3")
    pipette = protocol.load_instrument(
        instrument_name="flex_1channel_1000", mount="left", tip_racks=[tiprack_1]
    )
    protocol.comment('Use the meniscus to aspirate and dispense)')
    pipette.pick_up_tip()
    pipette.detect_liquid_presence(plate["A1"])
        # 1. Detect the liquid presence in the source well
    # This returns a Meniscus object which stores the height data


    # 2. Aspirate relative to the detected height
    # Use the 'source_meniscus' object directly
    pipette.aspirate(100, plate["A1"].meniscus(z=-4)) 
    # put liquid back in the source well
    pipette.dispense(50, plate["A1"].meniscus(z=-1))
    pipette.dispense(50, plate["A1"].meniscus(z=-2))
    pipette.return_tip()

    protocol.comment(
        "should have 150 in well so volume should takes around 2/3 of the way"
    )
    protocol.comment(
        "should have plate at top z=-2 for aspirate and bottom at z=1 for dispense"
    )
    pipette.pick_up_tip()
    pipette.aspirate(150, plate["A1"].top(z=-2))
    pipette.dispense(50, plate["B1"].bottom(z=1))
    pipette.dispense(50, plate["B1"].bottom(z=1))
    protocol.comment("Should have 50 left")
    pipette.blow_out(plate["B1"].bottom(z=1))
    pipette.drop_tip()
    protocol.comment("mix after please")
    pipette.transfer(100, plate["B1"], plate["A3"], mix_after=(3, 30))
    pipette.pick_up_tip()
    pipette.mix(repetitions=3, volume=30, location=plate["B1"].bottom(z=1), rate=2)
    pipette.return_tip()
    viscous_liquid = protocol.get_liquid_class(name="glycerol_50")
    protocol.comment("Transfer with liquid class")
    with protocol.group_steps("Aspirate and Dispense 1"):
        pipette.transfer_with_liquid_class(
            liquid_class=viscous_liquid, volume=30, source=plate["B1"], dest=plate["A1"]
        )
        pipette.pick_up_tip()
        protocol.comment("Work with Mixing and dispensing onto tempdeck")
        pipette.aspirate(30, plate["B1"].bottom(z=1))
        pipette.dispense(30, deep["A1"].top(z=-2))
        pipette.mix(repetitions=3, volume=30, location=deep["A1"].bottom(z=1), rate=2)
        pipette.return_tip()
