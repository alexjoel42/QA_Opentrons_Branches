
from opentrons import protocol_api

from opentrons import types


metadata = {
    'protocolName': 'transfer',
    'author': 'Opentrons ',
    'source': 'Custom Protocol Request',
    'description': 'p1000_96'
}

requirements = {
    "robotType": "OT-3",
    "apiLevel": "2.21"
}


def run(ctx: protocol_api.ProtocolContext):
    # <---Modules&labware--->
    ctx.load_waste_chute()  # waste chute
    h_s_1 = ctx.load_module('heaterShakerModuleV1', '1')
    hs_1_adapter = h_s_1.load_adapter('opentrons_96_deep_well_adapter')
    h_s_2 = ctx.load_module('heaterShakerModuleV1', '4')
    hs_2_adapter = h_s_2.load_adapter('opentrons_96_deep_well_adapter')
    manifold_base = ctx.load_labware("millipore_vacuum_manifold_base", "A3")
    dummy_collection_plate = manifold_base.load_labware("nest_96_pcr_vacuum_collection_plate", 'dummy_collection_plate')
    manifold_holder = ctx.load_labware("millipore_vacuum_manifold_holder", "A4")
    manifold_collar = manifold_holder.load_labware('millipore_vacuum_manifold_collar_standard')
    filter_plate = manifold_collar.load_labware("attractspe_c18_filter_plate", 'filter_plate')
    mag_1 = ctx.load_module('magneticBlockV1', 2)
    mag_2 = ctx.load_module('magneticBlockV1', 5)
    deep_well_plate_1 = mag_1.load_labware('nest_96_wellplate_2ml_deep', 'sample_plate_1')
    collection_plate = mag_2.load_labware('nest_96_pcr_vacuum_collection_plate', 'collection_plate')
    reagent_res = ctx.load_labware("cellpro_4_reservoir_50000ul", 7, 'reagents')  # ABC, DTT, IAA, SP3 beads  # noqa
    ethanol_res = ctx.load_labware('ccp1000tiprack_1_reservoir_500000ul', 10, 'ethanol')
    
    