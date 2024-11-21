from typing import cast
from opentrons import protocol_api
from opentrons.protocol_api.module_contexts import AbsorbanceReaderContext

# metadata
metadata = {
    'protocolName': 'Absorbance Reader Multi read/csv smoke p50 multi no 570',
    'author': 'Platform Expansion',
}

requirements = {
    "robotType": "OT-2",
    "apiLevel": "2.21",
}


# protocol run function
def run(protocol: protocol_api.ProtocolContext):
    mod = protocol.load_module("absorbanceReaderV1", "D3")
    plate = protocol.load_labware("nest_96_wellplate_200ul_flat", "1")

    mod.close_lid()
    mod.initialize('single', [600], 450)

    # NOTE: CANNOT INITIALIZE WITH THE LID OPEN

    # Remove the Plate Reader lid using the Gripper.
    mod.open_lid()
    protocol.move_labware(plate, mod, use_gripper = False)
    mod.close_lid()

    # Take a reading and show the resulting absorbance values.
    # Issue: cant read before you initialize or you an get an error
    result = mod.read()
    msg = f"single: {result}"
    protocol.comment(msg=msg)
    protocol.pause(msg=msg)

    # Initialize to multiple wavelengths
    protocol.pause(msg="Perform Multi Read")
    mod.open_lid()
    protocol.move_labware(plate, "C2", use_gripper=True)

    mod.close_lid()

    # mod.initialize('multi', [450, 570, 600])
    mod.initialize('multi', [450, 600])
    # Open the lid and move the labware into the reader
    mod.open_lid()
    protocol.move_labware(plate, mod, use_gripper=False)

    # pick up tip and perform action on labware inside plate reader
    instrument.pick_up_tip(tiprack_1000.wells_by_name()['A1'])
    instrument.aspirate(30, plate.wells_by_name()['A1'])
    instrument.dispense(30, plate.wells_by_name()['B1'])
    instrument.return_tip()

    mod.close_lid()

    # Take reading
    result = mod.read()
    msg = f"multi: {result}"
    protocol.comment(msg=msg)
    protocol.pause(msg=msg)

    # Take a reading and save to csv
    protocol.pause(msg="Perform Read and Save to CSV")
    result = mod.read(export_filename="plate_reader_csv.csv")
    msg = f"csv: {result}"
    protocol.pause(msg=msg)

    # Place the Plate Reader lid back on using the Gripper.
    mod.open_lid()
    protocol.move_labware(plate, "C2", use_gripper=False)
    mod.close_lid()

    mod.read(export_filename="csv_name.csv")


