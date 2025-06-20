requirements = {
    "robotType": "Flex",
    "apiLevel": "2.24"
}

metadata = {
    "protocolName": 'Test cases for P50 Single-channel',
    'author': 'Alex'
}

def add_parameters(parameters):
    parameters.add_str(
        variable_name="tip_strat",
        display_name="Select tip strategy",
        choices=[
            {"display_name": "Always", "value": "always"},
            {"display_name": "Never", "value": "never"},
            {"display_name": "Once", "value": "once"},
        ],
        default="once",
    )

    parameters.add_str(
        variable_name="liquid_strat",
        display_name="Select liquid",
        choices=[
            {"display_name": "All", "value": "all"},
            {"display_name": "Glycerol 50%", "value": "glycerol_50"},
            {"display_name": "Water", "value": "water"},
            {"display_name": "Ethanol 80%", "value": "ethanol_80"},
        ],
        default="all",
    )

def run(protocol_context):

    # Define labware, trash and pipette
    tiprack_1 = protocol_context.load_labware("opentrons_flex_96_tiprack_50ul", "C2")
    tiprack_2 = protocol_context.load_labware("opentrons_flex_96_tiprack_50ul", "C3")
    trash = protocol_context.load_waste_chute()
    pipette_50 = protocol_context.load_instrument("flex_1channel_50", "right", tip_racks=[tiprack_1, tiprack_2])
    nest_plate_source_1 = protocol_context.load_labware("nest_96_wellplate_2ml_deep", "B2")
    nest_plate_source_2 = protocol_context.load_labware("nest_96_wellplate_2ml_deep", "D2")
    nest_plate_dest_1 = protocol_context.load_labware("nest_96_wellplate_2ml_deep", "A2")
    nest_plate_dest_2 = protocol_context.load_labware("nest_96_wellplate_2ml_deep", "B3")
    nest_plate_dest_1.load_empty(nest_plate_dest_1.wells())
    nest_plate_dest_2.load_empty(nest_plate_dest_2.wells())

    Liquid_1 = protocol_context.define_liquid(
    name="Liquid 1",
    description="Green colored water for demo",
    display_color="#00FF00",
        )
    Liquid_2 = protocol_context.define_liquid(
        name="Liquid 2",
        description="Blue colored water for demo",
        display_color="#0000FF",
        )
    for row in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
        for col in range(1, 13):
            well = f"{row}{col}"
            if row in ['A']:
                if col in range(1, 7):
                    nest_plate_source_1[well].load_liquid(Liquid_1, volume=50) # Adjusted volume for P50
                    nest_plate_source_2[well].load_liquid(Liquid_2, volume=50) # Adjusted volume for P50
                elif col in range(7, 11):
                    nest_plate_source_1[well].load_liquid(Liquid_2, volume=50) # Adjusted volume for P50
                    nest_plate_source_2[well].load_liquid(Liquid_2, volume=50) # Adjusted volume for P50
            elif row in ['B', 'C', 'D', 'E', 'F', 'G', 'H']:
                nest_plate_source_1[well].load_liquid(Liquid_1, volume=50) # Adjusted volume for P50
                nest_plate_source_2[well].load_liquid(Liquid_2, volume=50) # Adjusted volume for P50


    # Define liquid classes
    water_liquid_class = protocol_context.get_liquid_class("water")
    glycerol_50_liquid_class = protocol_context.get_liquid_class("glycerol_50")
    ethanol_80_liquid_class = protocol_context.get_liquid_class("ethanol_80")

    liquid_classes_all = [water_liquid_class, glycerol_50_liquid_class, ethanol_80_liquid_class]

    # Transfer volumes
    volumes = [3, 19, 49] # Adjusted volumes for P50
    tip_strategy = protocol_context.params.tip_strat
    liquid_strat = protocol_context.params.liquid_strat

    liquid_class_options = {
        'all': liquid_classes_all,
        'water': [water_liquid_class],
        'glycerol_50': [glycerol_50_liquid_class],
        'ethanol_80': [ethanol_80_liquid_class]
    }

    selected_liquid_classes = liquid_class_options[liquid_strat]

    i_once = -1
    i_never = -1
    i_always = -1

    protocol_context.pause(f'This is the tip strategy we will use: {tip_strategy}')

    for volume in volumes:
        for liquid_class in selected_liquid_classes:
            liquid_class_name = liquid_class.display_name if hasattr(liquid_class, 'display_name') else liquid_class.name
            protocol_context.pause(f'Tip strategy: {tip_strategy}, Liquid class: {liquid_class_name}, Volume: {volume}µL')

            if tip_strategy == 'never':
                source_wells_1 = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9']
                source_wells_2 = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9']
                dest_wells_1 = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9']
                dest_wells_2 = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9']
                i_never += 1
                transfer_set(protocol_context, trash, pipette_50, volume, 'never', liquid_class,
                             nest_plate_source_1, nest_plate_source_2, nest_plate_dest_1,
                             nest_plate_dest_2, source_wells_1[i_never], source_wells_2[i_never],
                             dest_wells_1[i_never], dest_wells_2[i_never])

            elif tip_strategy == 'once':
                source_wells_1 = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9']
                source_wells_2 = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9']
                dest_wells_1 = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9']
                dest_wells_2 = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9']
                i_once += 1
                transfer_set(protocol_context, trash, pipette_50, volume, 'once', liquid_class,
                             nest_plate_source_1, nest_plate_source_2, nest_plate_dest_1,
                             nest_plate_dest_2, source_wells_1[i_once], source_wells_2[i_once],
                             dest_wells_1[i_once], dest_wells_2[i_once])
            else: # tip_strategy == 'always'
                source_wells_1 = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9']
                source_wells_2 = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9']
                dest_wells_1 = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9']
                dest_wells_2 = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9']
                i_always += 1
                transfer_set(protocol_context, trash, pipette_50, volume, 'always', liquid_class,
                             nest_plate_source_1, nest_plate_source_2, nest_plate_dest_1,
                             nest_plate_dest_2, source_wells_1[i_always], source_wells_2[i_always],
                             dest_wells_1[i_always], dest_wells_2[i_always])


from opentrons import protocol_api
def transfer_set(
    protocol_context: protocol_api.ProtocolContext,
    trash: protocol_api.WasteChute,
    pipette_50: protocol_api.InstrumentContext,
    volume: float,
    tip_strategy: str,
    liquid_class: protocol_api.LiquidClass,
    nest_plate_source_1: protocol_api.Labware,
    nest_plate_source_2: protocol_api.Labware,
    nest_plate_dest_1: protocol_api.Labware,
    nest_plate_dest_2: protocol_api.Labware,
    source_well_1: str,
    source_well_2: str,
    dest_well_1: str,
    dest_well_2: str,
):
    """Performs a transfer, distribute, and consolidate liquid handling set.

    Args:
        protocol_context: The Opentrons protocol context.
        trash: The waste chute labware object.
        pipette_50: The 50ul single-channel pipette instrument context.
        volume: The volume of liquid to handle in each step.
        tip_strategy: The tip strategy ('always', 'once', 'never').
        liquid_class: The liquid class to use for the operations.
        nest_plate_source_1: The first source plate labware object.
        nest_plate_source_2: The second source plate labware object.
        nest_plate_dest_1: The first destination plate labware object.
        nest_plate_dest_2: The second destination plate labware object.
        source_well_1: The well name in nest_plate_source_1 for the consolidate source.
        source_well_2: The well name in nest_plate_source_2 for transfer, distribute, and consolidate source.
        dest_well_1: The well name in nest_plate_dest_1 for distribute and consolidate destination.
        dest_well_2: The well name in nest_plate_dest_2 for transfer and distribute destination.
    """

    if tip_strategy != 'never':
        protocol_context.comment(f'Transfer Liquid: {volume}µL')
        pipette_50.transfer_with_liquid_class(
            liquid_class=liquid_class,
            volume=volume,
            source=nest_plate_source_2[source_well_2],
            dest=nest_plate_dest_2[dest_well_2],
            new_tip=tip_strategy,
            trash_location=trash,
        )
        protocol_context.comment(f'Distribute Liquid: {volume}µL')
        # Distribute only if tip strategy is not 'always' (meaning 'once')
        if tip_strategy == 'once':
            pipette_50.distribute_with_liquid_class(
                liquid_class=liquid_class,
                volume=volume,
                source=nest_plate_source_2[source_well_2],
                dest=[nest_plate_dest_1[dest_well_1], nest_plate_dest_2[dest_well_2]],
                new_tip=tip_strategy,
                trash_location=trash,
            )
        protocol_context.comment(f'Consolidate Liquid: {volume}µL')
        # Consolidate only if tip strategy is not 'always' (meaning 'once')
        if tip_strategy == 'once':
            pipette_50.consolidate_with_liquid_class(
                liquid_class=liquid_class,
                volume=volume,
                source=[nest_plate_source_1[source_well_1], nest_plate_source_2[source_well_2]],
                dest=nest_plate_dest_1[dest_well_1],
                new_tip=tip_strategy,
                trash_location=trash,
            )
    else: # tip_strategy == 'never'
        pipette_50.pick_up_tip()
        protocol_context.comment(f'Transfer Liquid: {volume}µL')
        pipette_50.transfer_with_liquid_class(
            liquid_class=liquid_class,
            volume=volume,
            source=nest_plate_source_2[source_well_2],
            dest=nest_plate_dest_2[dest_well_2],
            new_tip='never', # 'never' means it won't pick up a new tip for this specific transfer action
            trash_location=trash,
        )
        protocol_context.comment(f'Distribute Liquid: {volume}µL')
        pipette_50.distribute_with_liquid_class(
            liquid_class=liquid_class,
            volume=volume,
            source=nest_plate_source_2[source_well_2],
            dest=[nest_plate_dest_1[dest_well_1], nest_plate_dest_2[dest_well_2]],
            new_tip='never',
            trash_location=trash,
        )
        protocol_context.comment(f'Consolidate Liquid: {volume}µL')
        pipette_50.consolidate_with_liquid_class(
            liquid_class=liquid_class,
            volume=volume,
            source=[nest_plate_source_1[source_well_1], nest_plate_source_2[source_well_2]],
            dest=nest_plate_dest_1[dest_well_1],
            new_tip='never',
            trash_location=trash,
        )
        pipette_50.drop_tip()