#install pytest: python -m pip install pytest

#Automated test for the validate_transfer_all function
from src.validator import validate_transfer_all

def test_valid_transfer():
    transfer = {
        "action": "transfer_liquid",
        "source": "A1",
        "destination": "B1",
        "volume_ul": 50,
    }

    is_valid, message = validate_transfer_all(transfer)

    assert is_valid is True
    assert message == "Valid transfer instruction."

#to test the function, run the following command in the terminal:
#python -m pytest -v

#test invalid instructions
def test_rejects_zero_volume():
    transfer = {
        "action": "transfer_liquid",
        "source": "A1",
        "destination": "B1",
        "volume_ul": 0,
    }

    is_valid, message = validate_transfer_all(transfer)

    assert is_valid is False
    assert message == "Volume must be greater than 0 and at most 200 µL."


def test_rejects_same_source_and_destination():
    transfer = {
        "action": "transfer_liquid",
        "source": "A1",
        "destination": "A1",
        "volume_ul": 50,
    }

    is_valid, message = validate_transfer_all(transfer)

    assert is_valid is False
    assert message == "Source and destination wells cannot be the same."


def test_rejects_volume_over_200():
    transfer = {
        "action": "transfer_liquid",
        "source": "A1",
        "destination": "B1",
        "volume_ul": 201,
    }

    is_valid, message = validate_transfer_all(transfer)

    assert is_valid is False
    assert message == "Volume must be greater than 0 and at most 200 µL."


def test_rejects_invalid_source_well():
    transfer = {
        "action": "transfer_liquid",
        "source": "C1",
        "destination": "B1",
        "volume_ul": 50,
    }

    is_valid, message = validate_transfer_all(transfer)

    assert is_valid is False
    assert message == (
        "Source well is not allowed. Must be one of A1, A2, B1, or B2."
    )

