requirements = {
    'apiLevel': '2.22'
}


def run(protocol_context):
    tip_rack = protocol_context.load_labware('opentrons_flex_96_tiprack_50ul', 'A1')
    # load a schema 3 labware. For this labware, that means version 3. other labware
    # might need other versions. At release, this will be automatic when the api version
    # is high enough.
    plate = protocol_context.load_labware('corning_96_wellplate_360ul_flat', 'D2', version=3)
    # tell the system how much liquid is in the plate. There's also load_liquid_by_well,
    # which gets a dictionary mapping wells to volumes for when wells have different
    # volumes
    water = protocol_context.define_liquid('water')
    plate.load_liquid(['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1'], 200, water)
    # We can query the current liquid height and volume. These will be sourced from either
    # load_liquid or a recent liquid sense pass.
    estimated_height = plate['A1'].current_liquid_height()
    estimated_volume = plate['A1'].current_liquid_volume()
    protocol_context.comment(f'Plate has {estimated_volume}ul in A1 which is {estimated_height}mm tall')
    # tell the system to use liquid level detection. this is automatic in API version 2.21
    # but let's be explicit
    instrument = protocol_context.load_instrument(
        'flex_1channel_1000',
        'left',
        tip_racks=[tip_rack],
        liquid_presence_detection=True)
    instrument.pick_up_tip()
    minimum_liquid_height = instrument.get_minimum_liquid_sense_height()
    protocol_context.comment(f'Instrument can sense heights down to {minimum_liquid_height}mm')
    # at or above api 2.20, this will automatically probe for liquid presence and save the
    # detected height, making this aspirate rely on the sensor's height detection
    instrument.aspirate(20, plate['A1'].meniscus())
    # we can dispense accurately at a well's meniscus because we loaded liquid
    instrument.dispense(20, plate['B1'].meniscus(z=-0.5))
    instrument.drop_tip()
