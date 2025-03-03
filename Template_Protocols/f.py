from opentrons import protocol_api
# metadata
metadata = {
    'protocolName': 'multiple manual moves',
    'author': 'Sara Kowalski',
    'description': 'Simple Protocol that user can use to Phase 1 & 2 Error Recovery options for single and multi channel pipettes. NOTE: YOU WILL NEED A MODIFIED PIPETTE (NO SHROUD), and changed order of operations to reduce impact of dispense ER failure',
}
requirements = {
    "robotType": "Flex",
    "apiLevel": "2.22",
}
DRYRUN = 'NO'
USE_GRIPPER = True
def run(protocol: protocol_api.ProtocolContext):
    # modules/fixtures
    trashbin = protocol.load_waste_chute()
    #modules
    td_module = protocol.load_module("temperature module gen2", "D1")
    td_adptr = td_module.load_adapter("opentrons_96_well_aluminum_block")
    hs_module = protocol.load_module("heaterShakerModuleV1", "C1")
    hs_adptr = hs_module.load_adapter("opentrons_96_pcr_adapter")
    #labware
    sample_plate = td_adptr.load_labware('armadillo_96_wellplate_200ul_pcr_full_skirt')
    hs_module.open_labware_latch()
    protocol.move_labware(
        labware=sample_plate, 
        new_location=hs_adptr, 
    )
    protocol.move_labware(
        labware=sample_plate, 
        new_location="C2", 
    )
    protocol.move_labware(
        labware=sample_plate, 
        new_location=td_adptr, 
    )
    protocol.move_labware(
        labware=sample_plate, 
        new_location="B2", 
    )
    hs_module.close_labware_latch()