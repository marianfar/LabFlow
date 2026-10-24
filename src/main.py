
from src.pipeline import run_pipeline


def main():
    instruction = "Transfer 50 µL from well A1 to well B1."

    success, message = run_pipeline(instruction)

    print(f"Instruction: {instruction}")
    print(f"Success: {success}")
    print(f"Result: {message}")


if __name__ == "__main__":
    main()

