from typing import cast
from opentrons import protocol_api
from opentrons.protocol_api.module_contexts import AbsorbanceReaderContext

# metadata
metadata = {
    'protocolName': 'Absorbance Reader Multi read/csv smoke p50 multi no 570',
    'author': 'Platform Expansion',
}

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.21",
}


# protocol run function
def run(protocol: protocol_api.ProtocolContext):
    greenWater = protocol.define_liquid(
        name="Green water",
        description="Green colored water for demo",
        display_color="#00FF00",
    )
    mod = protocol.load_module("absorbanceReaderV1", "C3")
    mod_2 = protocol.load_module("absorbanceReaderV1", "D3")


    plate = protocol.load_labware("nest_96_wellplate_200ul_flat", "C2")
    plate['A1'].load_liquid(liquid=greenWater, volume=50)
    plate_2 = protocol.load_labware("nest_96_wellplate_200ul_flat", "C1")

    tiprack_1000 = protocol.load_labware(load_name='opentrons_flex_96_tiprack_50ul', location="B2")
    trash_labware = protocol.load_trash_bin("A3")
    instrument = protocol.load_instrument("flex_8channel_50", "right", tip_racks=[tiprack_1000])

    # pick up tip and perform action
    instrument.pick_up_tip(tiprack_1000.wells_by_name()['A1'])
    instrument.aspirate(30, plate.wells_by_name()['A1'])
    instrument.dispense(30, plate.wells_by_name()['A1'])
    instrument.return_tip()

    protocol.comment("We're going to do them serially")
    for modi, plate in zip([mod, mod_2], [plate, plate_2]):
        # Initialize to a single wavelength with reference wavelength
        modi.close_lid()
        modi.initialize('single', [600])  # Make sure no extra parameter like 450 is passed

        # Remove the Plate Reader lid using the Gripper.
        modi.open_lid()

        # Move the labware only once into the module
        # No need to move it again if it's already moved
        protocol.move_labware(plate, modi, use_gripper=True)

        modi.close_lid()

        # Take a reading and show the resulting absorbance values.
        result = modi.read()  # Ensure mod is fully initialized before reading
        msg = f"single: {result}"
        protocol.comment(msg)
        protocol.pause(msg)

        # Initialize to multiple wavelengths after performing the single read
        protocol.pause(msg="Perform Multi Read")
        modi.open_lid()

        # Move the labware into the reader after the pause
        if plate == plate_2:
            protocol.move_labware(plate, "D1", use_gripper=True)
        else:

            protocol.move_labware(plate, "C2", use_gripper=True)

        modi.close_lid()

    protocol.comment("we're now going to do them in parallel")
    # Mod 1 for multiple wavelengths
    mod.initialize('multi', [450, 562, 600])
    # Mod 2 with a different filter
    protocol.comment("OG with the different filter")
    mod_2.initialize('multi', [450, 562, 600])

    # Open the lids for both mods and move the labware into the readers
    mod.open_lid()
    protocol.comment("open the mod_2 lid now!")
    mod_2.open_lid()

    protocol.move_labware(plate, mod, use_gripper=True)
    protocol.move_labware(plate_2, mod_2, use_gripper=True)

    # pick up tip and perform action on labware inside plate reader
    instrument.pick_up_tip(tiprack_1000.wells_by_name()['A1'])
    instrument.aspirate(20, plate.wells_by_name()['A1'])
    instrument.aspirate(20, plate_2.wells_by_name()['A1'])
    instrument.dispense(20, plate.wells_by_name()['A1'])
    instrument.dispense(20, plate_2.wells_by_name()['A1'])
    instrument.return_tip()


    mod.close_lid()
    mod_2.close_lid()

    # Take reading
    result = mod.read()
    result_2 = mod_2.read()
    msg = f"multi: {result}"
    protocol.comment(msg=msg)
    msg_2 = f"multi: {result_2}"
    protocol.comment(msg=msg)

    protocol.pause(msg=msg)

    # Take a reading and save to csv
    protocol.pause(msg="Perform Read and Save to CSV")
    result = mod.read(export_filename="plate_reader_csv_1.csv")
    protocol.pause(msg="Perform Read and Save to CSV")
    result_2 = mod_2.read(export_filename="plate_reader_csv_2.csv")
    msg = f"csv: {result}"
    protocol.pause(msg=msg)
    msg = f"csv: {result_2}"
    protocol.pause(msg=msg_2)

    # Place the Plate Reader lid back on using the Gripper.
    mod.open_lid()
    mod_2.open_lid()
    protocol.move_labware(plate, "C1", use_gripper=True)
    protocol.move_labware(plate_2, "D1", use_gripper=True)
    mod.close_lid()
    mod_2.close_lid()
    mod.read(export_filename="csv_name_1.csv")
    mod_2.read(export_filename="csv_name_2.csv")



