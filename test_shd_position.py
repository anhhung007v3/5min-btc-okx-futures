from brain.position.stage_engine import (
    Stage,
    StageEngine
)


def main():

    print("===== SHD STAGE ENGINE TEST =====")


    engine = StageEngine()


    current_stage = Stage.STAGE_0


    print("\nCURRENT:")
    print(current_stage)


    print("\nTEST 1:")
    print("movement=False protection=False")


    new_stage = engine.evaluate_stage(
        current_stage=current_stage,
        movement_ok=False,
        protection_ok=False
    )


    print("RESULT:")
    print(new_stage)



    print("\nTEST 2:")
    print("movement=True protection=True")


    new_stage = engine.evaluate_stage(
        current_stage=new_stage,
        movement_ok=True,
        protection_ok=True
    )


    print("RESULT:")
    print(new_stage)



    print("\nTEST 3:")
    print("add_position_ok=True")


    new_stage = engine.evaluate_stage(
        current_stage=new_stage,
        movement_ok=False,
        protection_ok=False,
        add_position_ok=True
    )


    print("RESULT:")
    print(new_stage)



if __name__ == "__main__":
    main()