# API level must be 2.23
requirements = {"robotType": "Flex", "apiLevel": "2.23"}


def run(protocol):
    """Load Flex Stacker."""
    trash = protocol.load_trash_bin("A3")
    stacker_c = protocol.load_module("flexStackerModuleV1", "C4")
    stacker_d = protocol.load_module("flexStackerModuleV1", "D4")
    
    """Load labware into the Flex Stacker tower."""
    stacker_c.load_labware_to_hopper( "opentrons_flex_96_tiprack_1000ul", 2, lid="opentrons_flex_tiprack_lid")
    stacker_d.load_labware_to_hopper( "corning_96_wellplate_360ul_flat", 2)

    """Using stacker as a staging area."""
    stacker_c.enter_static_mode()
    tiprack_d = stacker_c.load_labware("opentrons_flex_96_tiprack_1000ul")
    protocol.move_lid(tiprack_d, trash, use_gripper=True)
    protocol.move_labware(tiprack_d, "B2", use_gripper=True)
    stacker_c.exit_static_mode()
    
    """Retreving and moving tipracks from the stacker"""
    tiprack = stacker_c.retrieve()
    protocol.move_lid(tiprack, trash, use_gripper=True)
    protocol.move_labware(tiprack, "C2", use_gripper=True)

    """Retreving and moving labware from the stacker"""
    plate = stacker_d.retrieve()
    protocol.move_labware(plate, "D2", use_gripper=True)

    """Moving and storing tipracks to the stacker"""
    protocol.move_labware(tiprack, stacker_c, use_gripper=True)
    stacker_c.store(tiprack)

    """Moving and storing labware to the stacker"""
    protocol.move_labware(plate, stacker_d, use_gripper=True)
    stacker_d.store(plate)

    """Moving tip racks stacker staging area."""
    protocol.move_labware(tiprack_d, stacker_c, use_gripper=True)

