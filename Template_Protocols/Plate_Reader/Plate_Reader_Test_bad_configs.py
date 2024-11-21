from os import system

cmds = ['opentrons.simulate Plate_Reader_Labware_Test_1.py', 'opentrons.simulate Plate_Reader_Labware_Test_2.py',
        'opentrons.simulate Plate_Reader_Labware_Test_3.py', 'Plate_Reader_Bad_Slot_1.py', 'Plate_Reader_Bad_Slot_2.py',
        'opentrons.simulate Plate_Reader_no_initialize.py']

for cmd in cmds:
    Python_env = "/Applications/Opentrons.app/contents/Resources/python/bin/python3 -I -m "
    print("This is the test for", cmd)
    system(Python_env+cmd)

