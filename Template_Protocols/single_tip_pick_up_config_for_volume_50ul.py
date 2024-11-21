from opentrons import protocol_api
from opentrons.protocol_api import SINGLE, ALL

requirements = {"robotType": "Flex", "apiLevel": "2.20"}

def run(protocol: protocol_api.ProtocolContext):
    partial_rack_1 = protocol.load_labware(
        load_name="opentrons_flex_96_filtertiprack_50ul",
        location="B2"
    )


    plate = protocol.load_labware(
        load_name = "opentrons_96_wellplate_200ul_pcr_full_skirt",
        location = "C3"
    )
    pipette = protocol.load_instrument(
        instrument_name="flex_8channel_50",
        mount="right")

    trash = protocol.load_trash_bin("A3")

    pipette.configure_nozzle_layout(
        style=SINGLE,
        start="A1",
        tip_racks=[partial_rack_1]
    )
    # Picks up appropriately single-channel
    protocol.comment('before config for volume')
    protocol.comment(str(pipette.active_channels))

    pipette.pick_up_tip()
    pipette.drop_tip()

    pipette.configure_for_volume(6)

    protocol.comment('after config for volume')
    protocol.comment(str(pipette.active_channels))
    pipette.pick_up_tip()
    pipette.aspirate(6, plate["A1"])
    print(pipette.get_current_volume())
    pipette.dispense(6, plate["A1"])

    pipette.drop_tip()

