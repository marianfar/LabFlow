#test a valid transfer simulation

from src.simulator import simulate_transfer


def test_simulate_valid_transfer():
    transfer = {
        "action": "transfer_liquid",
        "source": "A1",
        "destination": "B1",
        "volume_ul": 100,
    }

    success, message = simulate_transfer(transfer)

    assert success is True
    assert message == "Transfer simulated successfully."


#test an invalid transfer simulation

def test_reject_invalid_transfer():
    transfer = {
        "action": "transfer_liquid",
        "source": "A1",
        "destination": "A1",
        "volume_ul": 50,
    }

    success, message = simulate_transfer(transfer)

    assert success is False
    assert message == "Source and destination wells cannot be the same."

