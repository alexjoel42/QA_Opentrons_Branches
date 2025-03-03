from opentrons import protocol_api

requirements = {"robotType": "Flex", "apiLevel": "2.21"}

def run(protocol: protocol_api.ProtocolContext):
    # load tip rack in deck slot D3
    tiprack = protocol.load_labware(
        load_name="opentrons_flex_96_tiprack_50ul", location="A2"
    )
    # attach pipette to left mount
    pipette = protocol.load_instrument(
        instrument_name="flex_8channel_50",
        mount="right",
        tip_racks=[tiprack]
    )
    # load well plate in deck slot D2
    plate = protocol.load_labware(
        load_name="corning_96_wellplate_360ul_flat", location="D2"
    )
    # load reservoir in deck slot D1
    reservoir = protocol.load_labware(
        load_name="usascientific_12_reservoir_22ml", location="D1"
    )
    # load trash bin in deck slot A3
    trash = protocol.load_trash_bin(location="A3")
    pr_mod = protocol.load_module(
        module_name="absorbanceReaderV1",
        location="D3"
    )

    tc_mod = protocol.load_module(module_name="thermocyclerModuleV2")
    plate = tc_mod.load_labware(name="opentrons_96_wellplate_200ul_pcr_full_skirt")
    tc_mod.close_lid()
    tc_mod.open_lid()
    # Put protocol commands here
    protocol.home()
    pipette.pick_up_tip()
    pipette.aspirate(30, plate["A1"])
    pipette.dispense(30, plate["B1"])
    pipette.return_tip()
    pr_mod.close_lid()
    pr_mod.initialize(mode="single", wavelengths=[450])
    pr_data = pr_mod.read()



