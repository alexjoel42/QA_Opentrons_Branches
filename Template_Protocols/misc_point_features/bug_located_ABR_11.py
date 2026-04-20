
from opentrons import protocol_api
requirements = {
    "robotType": "Flex",
    "apiLevel": "2.28"}
def run(protocol: protocol_api.ProtocolContext):
            adapter = protocol.load_adapter('opentrons_flex_96_tiprack_adapter', 'B2')
            tiprack_200_X = adapter.load_labware('opentrons_flex_96_tiprack_200ul')
            p1000= protocol.load_instrument('flex_96channel_1000', 'right', tip_racks=[tiprack_200_X])
            protocol.comment("--> ETOH Wash 2")
            ETOHMaxVol = 150
            p96x_200_flow_rate_aspirate_default = 716
            p96x_200_flow_rate_dispense_default = 716
            p96x_200_flow_rate_blow_out_default = 716
             # ===============================================
            p1000.flow_rate.aspirate = p96x_200_flow_rate_aspirate_default * 0.5
            p1000.flow_rate.dispense = p96x_200_flow_rate_dispense_default
            p1000.flow_rate.blow_out = p96x_200_flow_rate_blow_out_default
            ETOH_Reservoir = protocol.load_labware('nest_96_wellplate_2ml_deep', 'D2')
            CleanupPlate_2 = protocol.load_labware('opentrons_96_wellplate_200ul_pcr_full_skirt', 'C2')
            trash = protocol.load_waste_chute()
            dot_bottom = 0.1
            # ===============================================
            p1000.pick_up_tip(tiprack_200_X["A1"])
            p1000.aspirate(ETOHMaxVol + 10, ETOH_Reservoir["A1"].bottom(z=dot_bottom))
            p1000.move_to(ETOH_Reservoir["A1"].top(z=0))
            p1000.move_to(ETOH_Reservoir["A1"].top(z=-5))
            p1000.move_to(CleanupPlate_2["A1"].top(z=2))
            p1000.dispense(ETOHMaxVol)
            p1000.return_tip()