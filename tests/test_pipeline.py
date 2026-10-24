
from src.pipeline import run_pipeline

# Test the run_pipeline function with a valid transfer instruction.
def test_run_pipeline_with_valid_transfer():
    instruction = "Transfer 50 µL from well A1 to well B1."
    success, message = run_pipeline(instruction)

    assert success is True
    assert message == "Transfer simulated successfully."
# Test the run_pipeline function with an invalid transfer instruction.
def test_run_pipeline_with_invalid_transfer():
    instruction = "Transfer 250 µL from well A1 to well B1."
    success, message = run_pipeline(instruction)

    assert success is False
    assert message == "Volume must be greater than 0 and at most 200 µL."

#test ommission of volume
def test_run_pipeline_with_uninterpretable_instruction():
    instruction = "Transfer liquid from well A1 to well B1."

    success, message = run_pipeline(instruction)

    assert success is False
    assert message == "Could not interpret instruction."