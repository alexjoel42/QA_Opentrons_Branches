"""
Command annotations stress test — productive break scenarios.
Run on Flex with allowStepGrouping enabled. Uncomment "Nested" to trigger ValueError.
"""
from opentrons import protocol_api
metadata = {
    "protocolName": "Command Annotations Stress Test",
    "author": "QA",
    "description": "Stress step groups: many, empty, unicode, mixed API.",
}
requirements = {"robotType": "Flex", "apiLevel": "2.29"}
def run(protocol: protocol_api.ProtocolContext) -> None:
    trash = protocol.load_trash_bin("A3")
    tiprack = protocol.load_labware("opentrons_flex_96_tiprack_200ul", "C2")
    source = protocol.load_labware("nest_96_wellplate_2ml_deep", "D1")
    dest = protocol.load_labware("nest_96_wellplate_2ml_deep", "D3")
    pipette = protocol.load_instrument(
        "flex_1channel_1000", mount="right", tip_racks=[tiprack]
    )
    sample = protocol.define_liquid(
        name="Sample", description="Aqueous sample", display_color="#0088FF"
    )
    source["A1"].load_liquid(liquid=sample, volume=500)
    water = protocol.get_liquid_class(name="water")
    # --- 1. Many sequential groups (e.g. 25) — stress DB, run log, GET /commandAnnotations ---
    for i in range(25):
        with protocol.group_steps(f"Transfer batch {i + 1}", description=f"Batch {i + 1}"):
            pipette.pick_up_tip()
            pipette.aspirate(50, source["A1"].bottom(z=1))
            pipette.dispense(50, dest["A1"].bottom(z=1))
            pipette.drop_tip(location=trash)
    # --- 2. Empty group_steps — valid? ---
    with protocol.group_steps("Empty group", description="No commands inside"):
        pass
    # --- 3. Single-command group ---
    with protocol.group_steps("Single command group", description="One command only"):
        protocol.comment("Only comment in this group.")
    # --- 4. Long + unicode name/description ---
    long_name = "Step α—β 日本 \u200b zwsp " + "x" * 200
    long_desc = "Description with unicode: 日本語 and emoji 🧪 " + "y" * 500
    with protocol.group_steps(long_name, description=long_desc):
        protocol.comment("Unicode/long annotation test.")
    # --- 5. create_and_start_step_group with multiple commands then end_group ---
    step_group = protocol.create_and_start_step_group(
        "Manual step group",
        description="We touch_tip before drop.",
    )

    
    pipette.pick_up_tip()
    pipette.aspirate(50, source["A1"].bottom(z=1))
    pipette.dispense(50, dest["B1"].bottom(z=1))
    pipette.touch_tip()
    pipette.drop_tip(location=trash)
    step_group.end_group()
    # --- 6. Alternating group_steps and create_and_start_step_group ---
    for i in range(1000):
        with protocol.group_steps("Context group A", description="First"):
            protocol.comment("In context group A.")
    sg = protocol.create_and_start_step_group("Manual group B", description="Second")
    protocol.comment("In manual group B.")
    sg.end_group()
    with protocol.group_steps("Context group C", description="Third"):
        protocol.comment("In context group C.")
    # --- OPTIONAL: Nested group_steps — raises ValueError. Uncomment to test. ---
    # with protocol.group_steps("Outer"):
    #     protocol.comment("Before nested.")
    #     with protocol.group_steps("Inner nested"):
    #         protocol.comment("This line never runs.")
    #     protocol.comment("After nested.")
    pipette.pick_up_tip()
    pipette.return_tip()