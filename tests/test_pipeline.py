
from src.pipeline import run_pipeline

# Test the run_pipeline function with a valid transfer instruction.
def test_run_pipeline_with_valid_transfer():
    transfer = {
        "action": "transfer_liquid",
        "source": "A1",
        "destination": "B1",
        "volume_ul": 50,
    }

    success, message = run_pipeline(transfer)

    assert success is True
    assert message == "Transfer simulated successfully."
# Test the run_pipeline function with an invalid transfer instruction.
def test_run_pipeline_with_invalid_transfer():
    transfer = {
        "action": "transfer_liquid",
        "source": "A1",
        "destination": "B1",
        "volume_ul": 250,  # Invalid volume
    }

    success, message = run_pipeline(transfer)

    assert success is False
    assert message == "Volume must be greater than 0 and at most 200 µL."