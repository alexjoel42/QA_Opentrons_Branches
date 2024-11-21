from typing import cast
from opentrons import protocol_api
from opentrons.protocol_api.module_contexts import AbsorbanceReaderContext

from opentrons import protocol_api
from opentrons.protocol_api import SINGLE, ALL

requirements = {"robotType": "Flex", "apiLevel": "2.20", "ProtocolName":"plate_rdaer"}

def run(protocol: protocol_api.ProtocolContext):
    partial_rack = protocol.load_labware(
        load_name="opentrons_flex_96_tiprack_1000ul",
        location="D3"
    )
    trash = protocol.load_trash_bin("A3")
    pipette = protocol.load_instrument(
        instrument_name="flex_8channel_1000",
        mount="left"
    )
    pipette.configure_nozzle_layout(
        style=SINGLE,
        start="H12",
        tip_racks=[partial_rack]
    )
    mod = cast(AbsorbanceReaderContext, protocol.load_module("absorbanceReaderV1", "D3"))
    plate = protocol.load_labware("nest_96_wellplate_200ul_flat", "C2")
    tiprack_1000 = protocol.load_labware(load_name='opentrons_flex_96_tiprack_1000ul', location="B2")
    trash_labware = protocol.load_trash_bin("B3")
    instrument = protocol.load_instrument("flex_8channel_1000", "right", tip_racks=[tiprack_1000])
    instrument.trash_container = trash_labware

    # pick up tip and perform action
    instrument.pick_up_tip(tiprack_1000.wells_by_name()['A1'])
    instrument.aspirate(100, plate.wells_by_name()['A1'])
    instrument.dispense(100, plate.wells_by_name()['B1'])
    instrument.return_tip()

    # Initialize to a single wavelength with reference wavelength
    # Issue: Make sure there is no labware here or youll get an error
    mod.close_lid()
    mod.initialize('single', [600], 450)

    # NOTE: CANNOT INITIALIZE WITH THE LID OPEN

    # Remove the Plate Reader lid using the Gripper.
    mod.open_lid()
    protocol.move_labware(plate, mod, use_gripper=True)
    instrument.pick_up_tip(tiprack_1000.wells_by_name()['A1'])
    instrument.aspirate(100, plate.wells_by_name()['A1'])
    instrument.dispense(100, plate.wells_by_name()['B1'])
    instrument.return_tip()
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
    protocol.pause(msg="Select the estop")

    mod.close_lid()

    mod.initialize('multi', [450, 570, 600])

    # Open the lid and move the labware into the reader
    mod.open_lid()
    protocol.move_labware(plate, mod, use_gripper=True)

    # pick up tip and perform action on labware inside plate reader
    instrument.pick_up_tip(tiprack_1000.wells_by_name()['A1'])
    instrument.aspirate(100, plate.wells_by_name()['A1'])
    instrument.dispense(100, plate.wells_by_name()['B1'])
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
    protocol.move_labware(plate, "C2", use_gripper=True)
    mod.close_lid()

    mod.read(export_filename="csv_name.csv")


