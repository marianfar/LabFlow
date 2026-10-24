#simulator that only performs a simulated transfer if the validator approves it

from src.validator import validate_transfer_all

#function that accepts a transfer dictionary and validates it.
def simulate_transfer(transfer):
    """Simulate a liquid transfer if the instruction is valid."""

    is_valid, message = validate_transfer_all(transfer)

    if not is_valid:
        return False, message

    return True, "Transfer simulated successfully."
