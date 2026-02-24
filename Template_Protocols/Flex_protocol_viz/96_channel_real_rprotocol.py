import json
from opentrons import protocol_api, types
from opentrons.types import Point
from opentrons.protocol_api import ALL, COLUMN, ROW, SINGLE
import math

metadata = {
    "protocolName": "IDX Bead Cleanup"
}

requirements = {"robotType": "Flex", "apiLevel": "2.25"}

waste_track = 0

def add_parameters(p):
    p.add_bool(
        display_name="Dry Run",
        variable_name="dry_run",
        default=False,
        description="Will this be a dry run? Incubations and mixing will be shortened."
    )
    p.add_int(
        display_name="Number of Sample Columns?",
        variable_name="samp_cols",
        default=12,
        choices=[
            {"display_name": "3 Columns (24 Samples)","value": 3},
            {"display_name": "6 Columns (48 Samples)","value": 6},
            {"display_name": "12 Columns (96 Samples)","value": 12}
        ],
        description="How many columns of samples are being processed?"
    )
    p.add_int(
        display_name="Pooling Column",
        variable_name="pool_col",
        default=1,
        minimum=1,
        maximum=12,
        description="Which column should the samples be pooled to?"
    )
    # p.add_str(
    #     display_name="Which Working Plate?",
    #     variable_name="w_plate",
    #     default="abgene_96_deep_wellplate_800ul",
    #     choices=[
    #         {"display_name": "Abgene","value": "abgene_96_deep_wellplate_800ul"},
    #         {"display_name": "Nest","value": "nest_96_wellplate_2ml_deep"}
    #     ],
    #     description="Which kind of deepwell plate will the samples be processed in?"
    # )

def run(ctx: protocol_api.ProtocolContext) -> None:
    # Import Parameters:
    dry_run = ctx.params.dry_run
    samp_cols = ctx.params.samp_cols
    pool_col = ctx.params.pool_col - 1 # adjust for 0 indexing
    w_plate = "abgene_96_deep_wellplate_800ul" #ctx.params.w_plate
    
    num_samps = samp_cols * 8  # 8 samples per column

    report = True  # if True, protocol will print extra info for troubleshooting

    # Load Modules:
    mag = ctx.load_module("magneticBlockV1", "C1")

    # will only need to load stacker if 96 tips
    c_stacker = ctx.load_module("flexStackerModuleV1", "C4")

    d_stacker = ctx.load_module("flexStackerModuleV1", "D4")
    
    # Load Labware:
    working_plate = ctx.load_labware(
        w_plate,
        location="B3",
        label="Thermo Deep Well Plate"
    )
    res_plate = ctx.load_labware(
        "nest_96_wellplate_2ml_deep",
        location="D1",
        label="Reservoir Plate"
    )
    tube_rack = ctx.load_labware(
        "opentrons_24_tuberack_nest_1.5ml_snapcap",
        location="B1",
        label="Tube Rack"
    )
    starting_plate = ctx.load_labware(
        "vwrplateappliedbiosystembase_96_wellplate_200ul",
        location="C2",
        label="Tag Plate - VWR Tecan"
    )
    elution_plate = ctx.load_labware(
        "biorad_96_wellplate_200ul_pcr",
        location="B4",
        label="BioRad Norm"
    )
    pooling_plate = ctx.load_labware(
        "biorad_96_wellplate_200ul_pcr",
        location="C3", # should be A4
        label="BioRad Pooling"
    )

    # Load Tips:
    tiprack_200_single = ctx.load_labware(
        "opentrons_flex_96_tiprack_200ul", 
        location="A3", 
        label="200µL Tip Rack #1"
    )
    tip_col_200 = tiprack_200_single.rows()[0][-3::-3] # select every third tip in reverse order for column pickup
    tiprack_200 = c_stacker.load_labware(
        "opentrons_flex_96_tiprack_200ul",
        label="200µL Tip Rack #2"
    )
    tip_rem_200 = tiprack_200.rows()[0][-3::-3]
    if samp_cols > 6: # only load third tiprack if more than 48 samples
        c_stacker.set_stored_labware(
            "opentrons_flex_96_tiprack_200ul",
            count=1
        )
    
    tiprack_50 = [ctx.load_labware(
        "opentrons_flex_96_tiprack_50ul", 
        location="A1", 
        label="50µL Tip Rack #1"
    )]
    tip_col_50 = tiprack_50[0].rows()[0][-3::-3] # select every third tip in reverse order for column pickup
    tiprack_52 = d_stacker.load_labware(
            "opentrons_flex_96_tiprack_50ul",
            label="50µL Tip Rack #2"
        )
    tiprack_50 += [tiprack_52]
    tip_col_50 += tiprack_52.rows()[0][-3::-3] # add reversed list to 50 ul tip rack
    if samp_cols > 3: # only load second tiprack if more than 24 samples
        d_stacker.set_stored_labware(
            "opentrons_flex_96_tiprack_50ul",
            count=1 if samp_cols == 6 else 3
        )

    print(f'\n50 ul tipracks: {tiprack_50}\n\n50 ul col tips: {tip_col_50}\n\n200 ul tiprack: {tiprack_200_single}\n\n200 ul col tips: {tip_col_200}\n')

    # Load Pipettes:
    pip = ctx.load_instrument(
        "flex_96channel_200", tip_racks=[],
    )

    # Load Waste Chute:
    waste_chute = ctx.load_waste_chute()

    # Locate Buffers
    beads_ = tube_rack.wells_by_name()["D6"]

    pooling_tube = tube_rack.wells_by_name()["A1"]

    te_buffer = res_plate.rows()[0][3] # will be columns 4-6, but only using 1 column but only need access to first well
    
    ethanol = res_plate.wells()[0] # will be first 3 columns, but only need access to first well

    waste = res_plate.rows()[0][-3] # 96 ch pipette will aim for A10

    # Buffer Volumes:
    bead_vol = 9
    te_vol = 25
    etoh_vol = 150

    bead_tube_vol = 270*(samp_cols/3) if samp_cols < 12 else 1000
    te_well_vol = te_vol*(samp_cols/3)+25 #6*(samp_cols/3)
    etoh_well_vol = 300*(samp_cols/3)+100

    # Define Wells:
    start_samps = starting_plate.rows()[0][:samp_cols:3] # for transferring samples out of sample plate

    single_samps = working_plate.wells()[:num_samps] # for single channel pipetting - adding beads or TE

    multi_samps = working_plate.rows()[0][:samp_cols:3] # for multi channel pipetting - removing liquids and adding ethanol

    print(f'\nStart wells: {start_samps}\n\nsingle wells: {single_samps}\n\nmulti wells: {multi_samps}\n')

    # Define Liquids:
    etoh_liq = ctx.define_liquid(
        "Wash Buffer (70% Ethanol)",
        display_color="#6af1f8",
    )
    bead_liq = ctx.define_liquid(
        "Ampure XP Beads",
        display_color="#412c04",
    )
    te_liq = ctx.define_liquid(
        "TE Buffer (PH 8.0)",
        display_color="#d4db0b",
    )
    samp_liq = ctx.define_liquid(
        "Starting Samples",
        display_color="#5bdb0b",
    )
    no_liq = ctx.define_liquid(
        "Empty",
        display_color="#FFFFFF",
    )

    # Load Liquids:
    tube_rack.wells()[0].load_liquid(liquid=no_liq, volume=0) # empty tube for pooling
    beads_.load_liquid(liquid=bead_liq, volume=bead_tube_vol)
    for well in res_plate.wells()[24:48]:
        well.load_liquid(liquid=te_liq, volume=te_well_vol)
    for well in res_plate.wells()[:24]:
        well.load_liquid(liquid=etoh_liq, volume=etoh_well_vol)
    for well in starting_plate.wells()[:num_samps]:
        well.load_liquid(liquid=samp_liq, volume=15)
    # ============================== Stacker Information ==============================
    # # Load Stacking Area:
    # # Loads a Stacker Module, ("item name", "position, A4-D4")
    
    # # Loads labware into the Stacker, ("item name", "count", "lid")
    # # Item name = Labware, stackers can have only 1 type
    # # Count = depends on labware, can fit max 6 opentrons tipracks, ~12 deepwells, etc
    # # lid = opentrons tipracks require lids in order to be stacked.
    # # Gripper cannot move labware with lid on it, it has to first discard/move the lid
    # c_stacker.set_stored_labware("opentrons_flex_96_tiprack_200ul", count=6, lid="opentrons_flex_tiprack_lid")
    # d_stacker.set_stored_labware("opentrons_flex_96_tiprack_200ul", count=0)
    # # Loading a tiprack on the moveable shuttle, Position "A4-D4"
    # # Does not have to match the labware in the stacker (example putting a p50 tiprack on the shuttle of a p200 tiprack stacker)
    # # Labware has to be cleared before using the stacker
    # tiprack_50 = c_stacker.load_labware('opentrons_flex_96_tiprack_50ul')

    # # PROTOCOL STEPS

    # # MOVING: tiprack_50 = d_stacker00_A4 --> A3
    # ctx.move_labware(labware=tiprack_50,new_location='A3',use_gripper=True)

    # def replace_tip_rack():
    #     tiprack = c_stacker.retrieve() # This is pulling the tiprack down from the stacker
    #     ctx.move_lid(tiprack, waste_chute, use_gripper=True)
    #     # MOVING: tiprack --> B1
    #     ctx.move_labware(labware=tiprack,new_location='B1',use_gripper=True)
    #     return tiprack 

    # # # This is pulling the first tiprack from the stacker and placing it on the shuttle which is located at A4 

    # tiprack_200_1 = replace_tip_rack()
    # # tiprack_200_1 = c_stacker.retrieve()
    # # ctx.move_lid(tiprack_200_1, waste_chute, use_gripper=True)
    # # # MOVING: tiprack_200_1 = d_stacker00_A4 --> B1
    # # ctx.move_labware(labware=tiprack_200_1,new_location='B1',use_gripper=True)

    # for i in range(12):
    #     pipette_left.pick_up_tip(tiprack_200_1)
    #     pipette_left.aspirate(100, reservoir_1.wells()[0])
    #     pipette_left.dispense(100, well_plate_1.wells()[i*8])
    #     pipette_left.drop_tip()

    # # Storing tiprack_200_1
    # # MOVING: tiprack_200_1 = B1 --> d_stacker and store
    # ctx.move_labware(labware=tiprack_200_1, new_location=d_stacker, use_gripper=True)
    # tiprack_200_1 = d_stacker.store()

    # # # This is pulling the second tiprack from the stacker and placing it on the shuttle which is located at A4 

    # tiprack_200_2 = replace_tip_rack()

    # for i in range(12):
    #     pipette_left.pick_up_tip(tiprack_200_2)
    #     pipette_left.aspirate(100, reservoir_1.wells()[1])
    #     pipette_left.dispense(100, well_plate_1.wells()[i*8])
    #     pipette_left.drop_tip()

    # # Storing tiprack_200_2
    # ctx.move_labware(labware=tiprack_200_2, new_location=d_stacker, use_gripper=True)
    # tiprack_200_2 = d_stacker.store()

    # ctx.move_labware(labware=tiprack_50,new_location=c_stacker,use_gripper=True)

    # ============================== END Stacker Information ==============================
    
    # ================ Helper Functions ================
    def slow_withdraw(well, z, rate=6):
        """
        well: well to be withdrawn from
        z: height to be withdrawn to (relative to top)
        rate: factor to slow down the withdrawal
        """
        pip.default_speed /= rate
        pip.move_to(well.top(z))
        pip.default_speed *= rate

    def divide_list(l,n):
        """
        l: list to divide
        n: size of chunk
        """
        for i in range(0, len(l), n):
            yield l[i:i+n]

    def toss(tiprack):
        """
        tiprack: tiprack to be thrown in the waste chute
        """
        ctx.move_labware(labware=tiprack,new_location = waste_chute,use_gripper=True)

    def remove_supernatant(vol : int, tip_list : list, w  = waste, last_eth = False):
        """
        vol: volume to be removed from each well
        tip_list: list of tips to be used
        """
        global waste_track

        old_arate = pip.flow_rate.aspirate
        old_drate = pip.flow_rate.dispense
        pip.flow_rate.aspirate = vol - 5 if vol > 10 else vol - 2# = ~1 s aspiration
        pip.flow_rate.dispense = vol # = 1 s dispense

        wording = 'Removing Supernatant From Samples' if w == waste else 'Transferring Eluate to Elution Plate'

        ctx.comment(f'\n{wording}\n')
        for i, s in enumerate(multi_samps):
            pip.pick_up_tip(tip_list.pop(0))
            pip.aspirate(vol - 15 if last_eth else vol, s.bottom(1.3), rate = 1 if w == waste else 0.3)
            ctx.delay(seconds=1)
            if last_eth:
                pip.aspirate(20, s.bottom(1.1), rate=0.05)
                ctx.delay(seconds=1)
            slow_withdraw(s, z=-2)
            pip.air_gap(10)
            pip.dispense(pip.current_volume, w.top(-2) if w == waste else w[i].bottom(3))
            ctx.delay(seconds=1)
            if w == waste:
                pip.blow_out(w.top(-2))
                pip.air_gap(10)
            else:
                pip.move_to(w[i].bottom().move(types.Point(x=1.25,y=0,z=4)))
            pip.drop_tip()
            ctx.comment('\n')
            if w == waste:
                waste_track += vol
        if report and w == waste:
            ctx.comment(f'\nTotal Waste Volume per Well: {waste_track}µL\n')

        pip.flow_rate.aspirate = old_arate
        pip.flow_rate.dispense = old_drate
    
    def bead_mixing(well, reps=6, high_speed=False):
        """
        well: Well to be mixed in, should also inclue a .bottom(z)
        reps: Number of mixing repetitions
        """
        pip.flow_rate.aspirate = 35 if high_speed else 10
        pip.flow_rate.dispense = 40 if high_speed else 15
        aloc1 = well.bottom().move(types.Point(x=0,y=0,z=4)) # full aspiration
        aloc2 = well.bottom().move(types.Point(x=0,y=0,z=6)) # half aspiration
        dloc1 = well.bottom().move(types.Point(x=0,y=0,z=6))
        dloc2 = well.bottom().move(types.Point(x=0,y=0,z=10))
        dloc3 = well.bottom().move(types.Point(x=1,y=1,z=5))
        dloc4 = well.bottom().move(types.Point(x=-1,y=-1,z=4))
        for x in range(reps if not dry_run else 1):
            pip.aspirate(190-pip.current_volume, aloc1)
            pip.dispense(190, dloc1,push_out=0)
            pip.aspirate(100, aloc2)
            pip.dispense(100, dloc2,push_out=0)
            pip.aspirate(190, aloc1)
            pip.dispense(190, dloc3,push_out=0)
            pip.aspirate(100, aloc2, rate=0.4 if x == reps-1 else 1)
            pip.dispense(100, dloc4,rate=0.5 if x == reps-1 else 1, push_out=0)
        
        pip.flow_rate.aspirate = 20
        pip.flow_rate.dispense = 30
    # ================ Begin Protocol ================
    ctx.pause(msg='Please make sure to have an empty tube in A1 of the Tube Rack in Deck Slot B1 for Pooling.')
    pip.flow_rate.aspirate = 20
    pip.flow_rate.dispense = 30
    # ================== Mix Beads and Transfer to Working Plate ================
    print(f'\n Blow out speed: {pip.flow_rate.blow_out}\n')
    
    pip.configure_nozzle_layout(
        style=SINGLE,
        start='A12',
        tip_racks=[tiprack_200_single]
    )
    print(f'\n On Deck Labware: {ctx.loaded_labwares}\n')
    ctx.comment(f'\nMixing Beads\n')
    pip.pick_up_tip()
    bead_mixing(beads_,reps=3 if samp_cols==12 else 2, high_speed=True)
    chunks = list(divide_list(single_samps, 180//bead_vol))
    for x, chunk in enumerate(chunks):
        if x > 0:
            pip.dispense(pip.current_volume, beads_.bottom(4), push_out=0)
            pip.aspirate(bead_vol*len(chunk)+20, beads_.bottom(4), rate=0.5)
            pip.dispense(pip.current_volume, beads_.bottom(6), push_out=0)
        pip.aspirate(bead_vol*len(chunk)+20, beads_.bottom(3), rate=0.5)
        ctx.delay(seconds=1)
        pip.dispense(5,beads_.bottom(3))
        pip.move_to(beads_.top(-5))
        ctx.delay(seconds=2)
        pip.touch_tip(v_offset=-5, radius=0.7)
        slow_withdraw(beads_, z=-2)
        ctx.comment(f'\nDistributing Beads\n')
        for _,dest in enumerate(chunk):
            first_last = True if _ == 0 or _ == len(chunk)-1 else False
            pip.dispense(bead_vol+2 if first_last else bead_vol, dest.bottom(1.2),rate=0.5)
            slow_withdraw(dest, z=-2)
    pip.blow_out(beads_.top())
    pip.air_gap(10)
    pip.drop_tip()

    # ================== Transfer Samples to Working Plate ================
    pip.configure_nozzle_layout(
        style=SINGLE,
        start='A1',
        tip_racks=tiprack_50
    )
    pip.flow_rate.aspirate = 5
    pip.flow_rate.dispense = 10

    for src, dest in zip(start_samps, multi_samps):
        ctx.comment(f'\nTransferring Samples to Working Plate\n')
        pip.pick_up_tip(tip_col_50.pop(0))
        pip.aspirate(5, src.bottom(1.2))
        ctx.delay(seconds=1)
        slow_withdraw(src, z=-2)
        pip.dispense(5, dest.bottom(2),push_out=0)
        ctx.comment(f'\nMixing Sample\n')
        for _ in range(10):
            pip.aspirate(10, dest.bottom(1.2))
            pip.dispense(10, dest.bottom(3), push_out=0)
        slow_withdraw(dest, z=-5)
        pip.touch_tip(v_offset=-5, radius=0.75)
        pip.blow_out()
        pip.drop_tip()
    
    pip.flow_rate.aspirate = 15
    pip.flow_rate.dispense = 25

    # ================== Replacing 50 ul Tips if necessary ================
    if samp_cols == 12:
        ctx.comment('\nReplacing 50µL Tips\n')
        toss(tiprack_50.pop(0))
        ctx.move_labware(labware=tiprack_50[0],new_location='A1',use_gripper=True)
        inc_time = 4.6 if not dry_run else 0.1
    else:
        inc_time = 5 if not dry_run else 0.1
    # ================ Incubate 5 Minutes ================

    ctx.comment('\n')
    ctx.delay(minutes=inc_time if not dry_run else 0.1, msg='Incubating for 5 minutes at RT')
    ctx.comment('\n')

    # ================== Transfer Samples to Magnet and Incubate ================

    ctx.move_labware(labware=starting_plate,new_location='A4',use_gripper=True)
    ctx.move_labware(labware=working_plate,new_location=mag,use_gripper=True)

    ctx.comment('\n')
    ctx.delay(minutes=2 if not dry_run else 0.1, msg='Incubating on Magnet for 2 minutes')
    ctx.comment('\n')
    
    # ================== Removing Supernatant From Sample ================

    remove_supernatant(9, tip_col_50)

    # ================== Replacing 50 ul Tips if necessary ================
    if samp_cols > 3:
        ctx.comment('\nReplacing 50µL Tips\n')
        toss(tiprack_50.pop(0))
        if samp_cols == 12:
            tiprack_53 = d_stacker.retrieve()
            tiprack_50 += [tiprack_53]
            tip_col_50 += tiprack_53.rows()[0][-3::-3]
            #ctx.move_lid(tiprack_53, waste_chute, use_gripper=True)

        ctx.move_labware(labware=tiprack_50[0],new_location='A1',use_gripper=True)
    
    # ================== Wash Samples with Ethanol ================
    ctx.move_labware(labware=tiprack_200_single,new_location='A2',use_gripper=True)
    ctx.move_labware(labware=tiprack_200,new_location='B2',use_gripper=True)

    for r in range(2 if not dry_run else 1):
        ctx.comment(f'\nAdding Ethanol Wash {r+1}\n')
        pip.configure_nozzle_layout(
            style=SINGLE,
            start='A1',
            tip_racks=tiprack_200
        )
        if samp_cols == 3:
            h = 4
            m = 2
        elif samp_cols == 6:
            h = 8
            m = 4
        else:
            h = 16
            m = 8
        # h = start height; m = multiplier for lowering height based on wash number
        pip.pick_up_tip(tip_col_200.pop(0))
        for i, s in enumerate(multi_samps):
            if i == 0: # pre-wet tip
                pip.aspirate(etoh_vol+20, ethanol.bottom(h-(r*m)), rate=5)
                pip.dispense(pip.current_volume, ethanol.top(-2), rate=5, push_out=0) 
            pip.aspirate(etoh_vol, ethanol.bottom(h-(r*m)-(i*2)), rate=3)
            ctx.delay(seconds=1)
            slow_withdraw(ethanol, z=-2)
            pip.air_gap(10)
            pip.dispense(pip.current_volume, s.top(-2), rate=2)
            ctx.delay(seconds=1)
            pip.blow_out(s.top(-5))
            pip.air_gap(10)
            ctx.comment('\n')
        pip.drop_tip()

        ctx.delay(minutes=1 if not dry_run else 0.1, msg='Incubating for 1 minute')
        ctx.comment('\n')

        remove_supernatant(etoh_vol+10, tip_rem_200, last_eth = True if r > 0 else False)

        if r == 0 and samp_cols == 12:
            ctx.comment('\nReplacing 200µL Tips\n')
            toss(tiprack_200)
            tiprack_201 = c_stacker.retrieve()
            tip_rem_200 = tiprack_201.rows()[0][-3::-3]
            #ctx.move_lid(tiprack_201, waste_chute, use_gripper=True)
            ctx.move_labware(labware=tiprack_201,new_location='B2',use_gripper=True)

    # ================== Dry Beads ================

    # Move tips around while drying
    ctx.move_labware(labware=tiprack_200 if samp_cols <= 6 else tiprack_201,new_location=c_stacker if samp_cols==3 else waste_chute,use_gripper=True)
    ctx.move_labware(labware=tiprack_200_single,new_location='A3',use_gripper=True)

    ctx.comment('\nDrying Beads\n')
    ctx.delay(minutes=2 if not dry_run else 0.1, msg='Incubating for 2 minutes to dry beads')
    ctx.comment('\n')
    ctx.move_labware(labware=working_plate,new_location='B3',use_gripper=True)

    # ================== Transfer TE to Samples ================
    pip.configure_nozzle_layout(
        style=SINGLE,
        start='A1',
        tip_racks=tiprack_50
    )

    for dest in multi_samps:
        ctx.comment(f'\nTransferring TE to Samples\n')
        pip.pick_up_tip(tip_col_50.pop(0))
        pip.aspirate(te_vol, te_buffer.bottom(1.5), rate=0.5)
        ctx.delay(seconds=1)
        slow_withdraw(te_buffer, z=-2)
        pip.dispense(te_vol, dest.bottom(8),push_out=0)
        ctx.comment(f'\nMixing with Sample\n')
        for _ in range(10):
            pip.aspirate(18, dest.bottom(1.3))
            pip.dispense(18, dest.bottom(3), push_out=0)
        slow_withdraw(dest, z=-5)
        pip.blow_out()
        pip.touch_tip(v_offset=-2, radius=0.75)
        pip.drop_tip()

    # ================ Incubate 2 Minutes ================

    ctx.comment('\n')
    ctx.delay(minutes=2 if not dry_run else 0.1, msg='Incubating for 2 minutes at RT')
    ctx.comment('\n')

    # ================== Transfer Samples to Magnet ================

    ctx.move_labware(labware=working_plate,new_location=mag,use_gripper=True)
    ctx.move_labware(labware=elution_plate,new_location='C2',use_gripper=True)

    # ================== Replace 50 ul Tips if necessary ================

    if samp_cols == 12:
        ctx.comment('\nReplacing 50µL Tips\n')
        toss(tiprack_50.pop(0))
        tiprack_54 = d_stacker.retrieve()
        tiprack_50 += [tiprack_54]
        tip_col_50 += tiprack_54.rows()[0][-3::-3]
        #ctx.move_lid(tiprack_54, waste_chute, use_gripper=True)
        ctx.move_labware(labware=tiprack_50[0],new_location='A1',use_gripper=True)
        inc_time = 4.6 if not dry_run else 0.1
    else:
        inc_time = 5 if not dry_run else 0.1
    # ================ Incubate 5 Minutes ================ 

    ctx.delay(minutes=inc_time if not dry_run else 0.1, msg='Incubating on Magnet for 5 minutes')

    # ================== Removing Supernatant From Sample ================

    remove_supernatant(20, tip_col_50, w = elution_plate.rows()[0][::3])

    # ================== Adding Last 50 ul Tip Rack for Pooling ================

    ctx.comment('\nAdding Last 50µL Tip Rack for Pooling\n')
    toss(tiprack_50.pop(0))
    if samp_cols == 3:
        tip_col_50 = tiprack_50[0].rows()[0][-1::-1]
    else:
        last_50 = d_stacker.retrieve()
        tip_col_50 += last_50.rows()[0][-1::-1]
        tiprack_50 += [last_50]
        #ctx.move_lid(last_50, waste_chute, use_gripper=True)
    ctx.move_labware(labware=tiprack_50[0],new_location='A1',use_gripper=True)
    ctx.move_labware(labware=pooling_plate,new_location='B2',use_gripper=True)

    
    # ================== Pooling Samples ================
    pip.configure_nozzle_layout(
        style=SINGLE,
        start='A1',
        tip_racks=tiprack_50
    )
    ctx.comment(f'\nPooling Samples to 1 Column\n')
    for i,s, in enumerate(elution_plate.rows()[0][:samp_cols]):
        pip.pick_up_tip(tip_col_50.pop(0))
        pip.flow_rate.aspirate = 8
        pip.flow_rate.dispense = 10
        pip.aspirate(13, s.bottom(1.2))
        ctx.delay(seconds=1)
        pip.dispense(13, s.bottom(6), push_out=0)
        ctx.delay(seconds=1)
        pip.flow_rate.aspirate = 2
        pip.flow_rate.dispense = 5
        pip.aspirate(3, s.bottom(1.5))
        ctx.delay(seconds=1)
        slow_withdraw(s, z=-2)
        pip.dispense(3, pooling_plate.rows()[0][pool_col].bottom(2+0.25*i))
        ctx.delay(seconds=1)
        pip.blow_out()
        pip.drop_tip()
        ctx.comment('\n')

    
    # move tiprack for last pickup
    ctx.move_labware(labware=tiprack_200_single,new_location='A2',use_gripper=True)

    pip.flow_rate.aspirate = ((3*samp_cols)+5)/2
    pip.flow_rate.dispense = 50

    pip.pick_up_tip(tiprack_200_single.wells_by_name()["H6"])
    chunks = list(divide_list(pooling_plate.columns()[pool_col], 160//(3*samp_cols)))
    ctx.comment(f'\nPooling All Samples to 1 Tube\n')
    for chunk in chunks:
        for c in chunk:
            pip.aspirate((3*samp_cols)+5, c.bottom(0.4))
            ctx.delay(seconds=1)
            slow_withdraw(c, z=-2)
        pip.air_gap(5)
        pip.dispense(pip.current_volume, pooling_tube.bottom(2))
        ctx.delay(seconds=1)
        pip.blow_out(pooling_tube.bottom(5))
        ctx.comment('\n')
    pip.drop_tip()

    ctx.comment('\nProtocol Complete!\n')