import subprocess
import csv 


import opentrons 

requirements = {
    'robotType': 'Flex',
    'apiLevel': '2.27',
}

def run(protocol: opentrons.protocol_api.ProtocolContext):
    fixed_trash = protocol.load_waste_chute()
    labware = protocol.load_labware('