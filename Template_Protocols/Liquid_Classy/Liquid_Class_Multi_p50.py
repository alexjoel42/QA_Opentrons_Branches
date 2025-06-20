from opentrons import protocol_api

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.24"
}

metadata = {
    "protocolName": 'Test cases for 8-channel P50',
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
        default="always",
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
    # Changed to 50ul tip racks for P50 pipette
    tiprack_1 = protocol_context.load_labware("opentrons_flex_96_tiprack_50ul", "C2")
    tiprack_2 = protocol_context.load_labware("opentrons_flex_96_tiprack_50ul", "C3")
    trash = protocol_context.load_waste_chute()

    # Changed to 8-channel P50 pipette
    pipette_50 = protocol_context.load_instrument("flex_8channel_50", "left", tip_racks=[tiprack_1, tiprack_2])

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
            # Adjusted liquid loading volume to be within P50 range
            nest_plate_source_1[well].load_liquid(Liquid_1, volume=50)
            nest_plate_source_2[well].load_liquid(Liquid_2, volume=50)


    # Define liquid classes
    water_liquid_class = protocol_context.get_liquid_class("water")
    glycerol_50_liquid_class = protocol_context.get_liquid_class("glycerol_50")
    ethanol_80_liquid_class = protocol_context.get_liquid_class("ethanol_80")

    liquid_classes_all = [water_liquid_class, glycerol_50_liquid_class, ethanol_80_liquid_class]

    # Transfer volumes - adjusted for P50 pipette (max 50µL)
    volumes = [5, 20, 50]
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

            # Modified to use columns instead of individual wells for 8-channel pipette
            # Columns are typically referred to by their number (1-12) or letter (A-H) for rows
            # Here we are using string representations of column numbers for clarity
            if tip_strategy == 'never':
                source_cols_1 = ['1', '2', '3'] # Reduced number of columns to demonstrate
                source_cols_2 = ['1', '2', '3']
                dest_cols_1 = ['1', '2', '3']
                dest_cols_2 = ['1', '2', '3']
                i_never = (i_never + 1) % len(source_cols_1) # Cycle through available columns

                transfer_set_multichannel(protocol_context, trash, pipette_50, volume, 'never', liquid_class,
                                         nest_plate_source_1, nest_plate_source_2, nest_plate_dest_1,
                                         nest_plate_dest_2, source_cols_1[i_never], source_cols_2[i_never],
                                         dest_cols_1[i_never], dest_cols_2[i_never])

            elif tip_strategy == 'once':
                source_cols_1 = ['4', '5', '6'] # Different set of columns
                source_cols_2 = ['4', '5', '6']
                dest_cols_1 = ['4', '5', '6']
                dest_cols_2 = ['4', '5', '6']
                i_once = (i_once + 1) % len(source_cols_1)

                transfer_set_multichannel(protocol_context, trash, pipette_50, volume, 'once', liquid_class,
                                         nest_plate_source_1, nest_plate_source_2, nest_plate_dest_1,
                                         nest_plate_dest_2, source_cols_1[i_once], source_cols_2[i_once],
                                         dest_cols_1[i_once], dest_cols_2[i_once])
            else: # tip_strategy == 'always'
                source_cols_1 = ['7', '8', '9'] # Another set of columns
                source_cols_2 = ['7', '8', '9']
                dest_cols_1 = ['7', '8', '9']
                dest_cols_2 = ['7', '8', '9']
                i_always = (i_always + 1) % len(source_cols_1)

                transfer_set_multichannel(protocol_context, trash, pipette_50, volume, 'always', liquid_class,
                                         nest_plate_source_1, nest_plate_source_2, nest_plate_dest_1,
                                         nest_plate_dest_2, source_cols_1[i_always], source_cols_2[i_always],
                                         dest_cols_1[i_always], dest_cols_2[i_always])


def transfer_set_multichannel(
    protocol_context: protocol_api.ProtocolContext,
    trash: protocol_api.WasteChute,
    pipette_50: protocol_api.InstrumentContext, # Changed pipette to 50µL
    volume: float,
    tip_strategy: str,
    liquid_class: protocol_api.LiquidClass,
    nest_plate_source_1: protocol_api.Labware,
    nest_plate_source_2: protocol_api.Labware,
    nest_plate_dest_1: protocol_api.Labware,
    nest_plate_dest_2: protocol_api.Labware,
    source_col_1: str,
    source_col_2: str,
    dest_col_1: str,
    dest_col_2: str,
):
    """Performs a transfer, distribute, and consolidate liquid handling set with 8-channel P50 pipette.

    Args:
        protocol_context: The Opentrons protocol context.
        trash: The waste chute labware object.
        pipette_50: The 50ul 8-channel pipette instrument context.
        volume: The volume of liquid to handle in each step.
        tip_strategy: The tip strategy ('always', 'once', 'never').
        liquid_class: The liquid class to use for the operations.
        nest_plate_source_1: The first source plate labware object.
        nest_plate_source_2: The second source plate labware object.
        nest_plate_dest_1: The first destination plate labware object.
        nest_plate_dest_2: The second destination plate labware object.
        source_col_1: The column number in nest_plate_source_1 for the consolidate source.
        source_col_2: The column number in nest_plate_source_2 for transfer, distribute, and consolidate source.
        dest_col_1: The column number in nest_plate_dest_1 for distribute and consolidate destination.
        dest_col_2: The column number in nest_plate_dest_2 for transfer and distribute destination.
    """

    if tip_strategy != 'never':
        protocol_context.comment(f'Transfer Liquid: {volume}µL')
        pipette_50.transfer_with_liquid_class(
            liquid_class=liquid_class,
            volume=volume,
            source=nest_plate_source_2.columns_by_name()[source_col_2],
            dest=nest_plate_dest_2.columns_by_name()[dest_col_2],
            new_tip=tip_strategy,
            trash_location=trash,
        )

        protocol_context.comment(f'Distribute Liquid: {volume}µL')
        if tip_strategy == 'always':
            pass
        else: # This applies to 'once'
            pipette_50.distribute_with_liquid_class(
                liquid_class=liquid_class,
                volume=volume,
                source=nest_plate_source_2.columns_by_name()[source_col_2],
                dest=[
                    nest_plate_dest_1.columns_by_name()[dest_col_1],
                    nest_plate_dest_2.columns_by_name()[dest_col_2]
                ],
                new_tip=tip_strategy,
                trash_location=trash,
            )

        if tip_strategy == 'always':
            pass
        else: # This applies to 'once'
            protocol_context.comment(f'Consolidate Liquid: {volume}µL')
            pipette_50.consolidate_with_liquid_class(
                liquid_class=liquid_class,
                volume=volume,
                source=[
                    nest_plate_source_1.columns_by_name()[source_col_1],
                    nest_plate_source_2.columns_by_name()[source_col_2]
                ],
                dest=nest_plate_dest_1.columns_by_name()[dest_col_1],
                new_tip=tip_strategy,
                trash_location=trash,
            )
    else: # tip_strategy == 'never'
        pipette_50.pick_up_tip()
        protocol_context.comment(f'Transfer Liquid: {volume}µL')
        pipette_50.transfer_with_liquid_class(
            liquid_class=liquid_class,
            volume=volume,
            source=nest_plate_source_2.columns_by_name()[source_col_2],
            dest=nest_plate_dest_2.columns_by_name()[dest_col_2],
            new_tip='never', # 'never' means it won't pick up a new tip for this specific transfer action
            trash_location=trash,
        )

        protocol_context.comment(f'Distribute Liquid: {volume}µL')
        pipette_50.distribute_with_liquid_class(
            liquid_class=liquid_class,
            volume=volume,
            source=nest_plate_source_2.columns_by_name()[source_col_2],
            dest=[
                nest_plate_dest_1.columns_by_name()[dest_col_1],
                nest_plate_dest_2.columns_by_name()[dest_col_2]
            ],
            new_tip='never',
            trash_location=trash,
        )

        protocol_context.comment(f'Consolidate Liquid: {volume}µL')
        pipette_50.consolidate_with_liquid_class(
            liquid_class=liquid_class,
            volume=volume,
            source=[
                nest_plate_source_1.columns_by_name()[source_col_1],
                nest_plate_source_2.columns_by_name()[source_col_2]
            ],
            dest=nest_plate_dest_1.columns_by_name()[dest_col_1],
            new_tip='never',
            trash_location=trash,
        )
        pipette_50.drop_tip()