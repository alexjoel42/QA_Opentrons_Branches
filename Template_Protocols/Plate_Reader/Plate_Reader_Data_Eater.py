metadata = {
    "protocolName": "Plate Eater",
    "author": "Alex",
    "description": "Protein samples normalized to a set volume and concentration using data colleted from BCA assay 1",
}

requirements = {"robotType": "Flex", "apiLevel": "2.21"}

########################

VOL_PIPET_LIMIT = 5


def add_parameters(parameters):
    parameters.add_csv_file(
        variable_name="csv_data",
        display_name="Readings of Samples",
        description="Absorbance reading of each sample"
    )
    parameters.add_int(
        variable_name="num_sample",
        display_name="Number of Samples",
        description="Number of samples to be assayed (maximum: 40)",
        default=40,
        minimum=1,
        maximum=40,
    )
    parameters.add_int(
        variable_name="sample_labware",
        display_name="Sample Labware",
        description="Labware used for samples?",
        default=1,
        choices=[{"display_name": "24 Tube Rack with 1.5mL Tubes", "value": 1}, {"display_name": "2mL 96-Well Plate ", "value": 2}],
    )
    parameters.add_float(
        variable_name="std_1",
        display_name="Standard #1",
        description="1st standard concentration (highest)",
        default=1000,
        minimum=20,
        maximum=2000,
        unit="ng/µL",
    )
    parameters.add_float(
        variable_name="std_2",
        display_name="Standard #2",
        description="2nd standard concentration",
        default=500,
        minimum=20,
        maximum=2000,
        unit="ng/µL",
    )
    parameters.add_float(
        variable_name="std_3",
        display_name="Standard #3",
        description="3rd standard concentration",
        default=250,
        minimum=20,
        maximum=2000,
        unit="ng/µL",
    )
    parameters.add_float(
        variable_name="std_4",
        display_name="Standard #4",
        description="4th standard concentration",
        default=125,
        minimum=20,
        maximum=2000,
        unit="ng/µL",
    )
    parameters.add_float(
        variable_name="std_5",
        display_name="Standard #5",
        description="5th standard concentration",
        default=62.5,
        minimum=20,
        maximum=2000,
        unit="ng/µL",
    )
    parameters.add_float(
        variable_name="std_6",
        display_name="Standard #6",
        description="6th standard concentration (lowest)",
        default=31.25,
        minimum=20,
        maximum=2000,
        unit="ng/µL",
    )
    parameters.add_float(
        variable_name="dilution_1",
        display_name="First Dilution",
        description="Samples will be diluted for 1x, 0.5x, 0.2x?",
        default=1,
        choices=[{"display_name": "1x", "value": 1}, {"display_name": "0.5x", "value": 0.5}, {"display_name": "0.2x", "value": 0.2}],
    )
    parameters.add_float(
        variable_name="dilution_2",
        display_name="Second Dilution",
        description="Samples will be diluted for 1x, 0.5x, 0.2x?",
        default=0.5,
        choices=[{"display_name": "1x", "value": 1}, {"display_name": "0.5x", "value": 0.5}, {"display_name": "0.2x", "value": 0.2}],
    )
    parameters.add_int(
        variable_name="vol_final",
        display_name="Normalized Sample Volume",
        description="Target volume of each sample after normalization?",
        default=100,
        minimum=10,
        maximum=100,
        unit="µL",
    )
    parameters.add_int(
        variable_name="amount_final",
        display_name="Protein Amount",
        description="Amount of protein in each sample after normalization?",
        default=100,
        minimum=1,
        maximum=190,
        unit="µg",
    )
    parameters.add_int(
        variable_name="pipet_location",
        display_name="P1000 1-ch Position",
        description="How P1000 single channel pipette is mounted?",
        default=1,
        choices=[{"display_name": "on the right", "value": 1}, {"display_name": "on the left", "value": 2}],
    )


def run(ctx):

    global num_sample
    global sample_labware

    global std_1
    global std_2
    global std_3
    global std_4
    global std_5
    global std_6

    global dilution_1
    global dilution_2

    global vol_final
    global amount_final

    global pipet_location

    parsed_csv = ctx.params.csv_data.parse_as_csv(detect_dialect=False)

    num_sample = ctx.params.num_sample
    sample_labware = ctx.params.sample_labware

    std_1 = ctx.params.std_1
    std_2 = ctx.params.std_2
    std_3 = ctx.params.std_3
    std_4 = ctx.params.std_4
    std_5 = ctx.params.std_5
    std_6 = ctx.params.std_6

    dilution_1 = ctx.params.dilution_1
    dilution_2 = ctx.params.dilution_2

    vol_final = ctx.params.vol_final
    amount_final = ctx.params.amount_final

    pipet_location = ctx.params.pipet_location


    buffer_rack = ctx.load_labware("opentrons_10_tuberack_nest_4x50ml_6x15ml_conical", "A2", "DILUENT")
    diluent = buffer_rack.wells()[2]

    final_plate = ctx.load_labware("opentrons_96_wellplate_200ul_pcr_full_skirt", "C2", "NORMALIZED SAMPLES")
    final = final_plate.wells()[:num_sample]

    ctx.load_trash_bin("A3")

    tips_200 = ctx.load_labware("opentrons_flex_96_tiprack_200ul", "B3", "P200 TIPS")
    # tips_1000_loc = tips_1000.wells()[:96]
    tips_50 = ctx.load_labware("opentrons_flex_96_tiprack_50ul", "C3", "P50 TIPS")
    # tips_50_loc = tips_50.wells()[:96]
    p1k_1 = ctx.load_instrument("flex_1channel_1000", mount = "left")
    #ctx.load_instrument("flex_8channel_1000", p1k_8_loc)
    od_full_plate=[]
    for col in range(12):
        for row in range(8):
            od_full_plate.append(float(parsed_csv[row + 1][col + 1]))
    ctx.comment(str(od_full_plate))
    ctx.comment(str(parsed_csv))


