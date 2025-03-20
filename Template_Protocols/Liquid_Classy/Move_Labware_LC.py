
from opentrons import protocol_api

# I am going to get added to in the test runner
# uncomment to test
# key = "10ul_C"
# key = "1100ul"
# key = "210ul"
# protocol.override_variable_name = key

from dataclasses import dataclass


@dataclass
class Test:
    key: str
    tiprack_loadname: str
    volume: float
    deckslot: list


"""
deckslot dictionary of all deck slots
"""


Tests = [
    Test(
        key="1000tip",
        tiprack_loadname="opentrons_flex_96_tiprack_1000ul",
        volume=1000,
        deckslot=[
            "A1",
            "A2",
            "A3",
            "A4",
            "B1",
            "B2",
            "B3",
            "B4",
            "C1",
            "C2",
            "C3",
            "C4",
            "D1",
            "D2",
            "D3",
            "D4",
        ],
    ),
    Test(
        key="300tip",
        tiprack_loadname="opentrons_flex_96_tiprack_300ul",
        volume=200,
        deckslot=[
            "A1",
            "A2",
            "A3",
            "A4",
            "B1",
            "B2",
            "B3",
            "B4",
            "C1",
            "C2",
            "C3",
            "C4",
            "D1",
            "D2",
            "D3",
            "D4",
        ],
    ),
    Test(key="50tip", tiprack_loadname="opentrons_flex_96_tiprack_50ul", volume=10, deckslot=[
            "A1",
            "A2",
            "A3",
            "A4",
            "B1",
            "B2",
            "B3",
            "B4",
            "C1",
            "C2",
            "C3",
            "C4",
            "D1",
            "D2",
            "D3",
            "D4",
        ],),
]


def get_test(key):
    matches = [test for test in Tests if test.key == key]
    if not matches:
        raise ValueError(f"No test found with key: {key}")
    if len(matches) > 1:
        raise ValueError(f"Multiple tests found with key: {key}")
    return matches[0]


requirements = {"robotType": "Flex", "apiLevel": "2.23"}
metadata = {
    "protocolName": "96 Channel distribute_liquid all custom tiprack types with all liquid classes"
}


def comment_tip_rack_status(ctx, tip_rack):
    """
    Print out the tip status for each row in a tip rack.
    Each row (A-H) will print the well statuses for columns 1-12 in a single comment,
    with a '🟢' for present tips and a '❌' for missing tips.
    """
    range_A_to_H = [chr(i) for i in range(ord("A"), ord("H") + 1)]
    range_1_to_12 = range(1, 13)

    ctx.comment(f"Tip rack in {tip_rack.parent}")

    for row in range_A_to_H:
        status_line = f"{row}: "
        for col in range_1_to_12:
            well = f"{row}{col}"
            has_tip = tip_rack.wells_by_name()[well].has_tip
            status_emoji = "🟢" if has_tip else "❌"
            status_line += f"{well} {status_emoji}  "

        # Print the full status line for the row
        ctx.comment(status_line)


def is_tip_rack_empty(tip_rack):
    """
    Check if a tip rack is completely empty.
    Args:
        tip_rack: An Opentrons tip rack labware object
    Returns:
        bool: True if the tip rack has no tips, False if it has at least one tip
    """
    range_A_to_H = [chr(i) for i in range(ord("A"), ord("H") + 1)]
    range_1_to_12 = range(1, 13)

    for row in range_A_to_H:
        for col in range_1_to_12:
            well = f"{row}{col}"
            if tip_rack.wells_by_name()[well].has_tip:
                return False

    return True


def is_missing_tips(tip_rack):
    """
    Check if a tip rack is missing any tips.
    Args:
        tip_rack: An Opentrons tip rack labware object
    Returns:
        bool: True if the tip rack is missing at least one tip, False if all tips are present
    """
    range_A_to_H = [chr(i) for i in range(ord("A"), ord("H") + 1)]
    range_1_to_12 = range(1, 13)

    for row in range_A_to_H:
        for col in range_1_to_12:
            well = f"{row}{col}"
            if not tip_rack.wells_by_name()[well].has_tip:
                return True

    return False


def using_96_channel(ctx) -> bool:
    """Check if a 96-channel pipette is loaded in the protocol."""
    for instrument in ctx.loaded_instruments.values():
        if instrument.channels == 8:
            ctx.comment("8 channel pipette is loaded")
            return True
    return False


def load_off_deck_tipracks(ctx, tiprack_loadname, count):
    tipracks = []
    for i in range(count):
        tiprack = ctx.load_labware(tiprack_loadname, protocol_api.OFF_DECK)
        tipracks.append(OffDeckTiprack(tiprack))
    return tipracks


@dataclass
class OffDeckTiprack:
    tiprack: protocol_api.labware.Labware
    used: bool = False


def run(ctx: protocol_api.ProtocolContext):
    # Stock liquid classes
    test = get_test(key="1000tip")
    comment = f"Test: {test.key}, Tiprack: {test.tiprack_loadname}, Volume: {test.volume}, Deck Slots: {test.deckslot[1:]}"
    ctx.comment(comment)
    water_class = ctx.define_liquid_class("water")
    ethanol_class = ctx.define_liquid_class("ethanol_80")
    glycerol_class = ctx.define_liquid_class("glycerol_50")
    tiprack_1 = ctx.load_labware(test.tiprack_loadname, "A1")
    target = ctx.load_labware("nest_96_wellplate_2ml_deep", "A2")
    water_source_1 = ctx.load_labware("nest_1_reservoir_290ml", "B1", "water")
    waste_chute = ctx.load_waste_chute()
    pipette_8 = ctx.load_instrument(instrument_name="flex_8channel_1000",mount="left", tip_racks=[tiprack_1])
    DEST_WELL = 'A1'
    # Liquids to transfer
    # https://labware.opentrons.com/#/?loadName=nest_1_reservoir_290ml
    '''
    Define Liquid class as water and then turn this into a for loop
    '''
    SOURCE_WELL = "A1"  
    water = ctx.define_liquid(name="Aqueous", description="H₂O", display_color="#738ee6")
    water_source_1.wells_by_name()[SOURCE_WELL].load_liquid(liquid=water, volume=1000)
    # Target
    # https://labware.opentrons.com/#/?loadName=nest_96_wellplate_2ml_deep    TARGET_WELL = "A1"  

    pipette_8.transfer_liquid(
		liquid_class=water_class,
		volume=100,
		source=water_source_1[SOURCE_WELL],
		dest=target[DEST_WELL],
		new_tip="once",
		trash_location= waste_chute,
	)
    ctx.move_labware()


    ''' 
    I want to use move the target well loaded in D2 to A1->D4 and test transfer_lidquid within a for loop that loops
    each of the different liquid types.
    
    
    '''
