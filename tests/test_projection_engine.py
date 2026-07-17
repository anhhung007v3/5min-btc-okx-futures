from brain.projection.projection_engine import ProjectionEngine


engine = ProjectionEngine()

events = [
    {
        "type": "POSITION_OPENED",
        "data": {
            "side": "LONG",
            "price": 65000,
            "size": 0.001
        }
    },
    {
        "type": "STAGE_CHANGED",
        "data": {
            "stage": 2
        }
    }
]

engine.replay(events)

position = engine.get_projection("position").get_position()
stage = engine.get_projection("stage").get_stage()

print("Position:", position)
print("Stage:", stage)