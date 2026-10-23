#check that the returned dictionary is valid based on defined rules.
#(does not establish that a transfer is safe for every real laboratory setup)
import math


def validate_transfer_all(transfer):
    """Validate a liquid-transfer instruction."""

    if not isinstance(transfer, dict):
        return False, "Transfer must be a dictionary."

    allowed_wells = {"A1", "A2", "B1", "B2"}
    required_keys = {"action", "source", "destination", "volume_ul"}

    # Check that all required keys are present
    if not required_keys.issubset(transfer.keys()):
        return False, "Missing required keys in transfer dictionary."

    # Check the volume type. Booleans must not count as numbers.
    volume = transfer["volume_ul"]
    if isinstance(volume, bool) or not isinstance(volume, (int, float)):
        return False, "Volume must be a number."

    # Reject NaN and infinity.
    if not math.isfinite(volume):
        return False, "Volume must be a finite number."

    # Check source and destination types
    if not isinstance(transfer["source"], str) or not isinstance(
        transfer["destination"], str
    ):
        return False, "Source and destination must be strings."

    # Check action
    if transfer["action"] != "transfer_liquid":
        return False, "Action must be 'transfer_liquid'."

    # Check volume range
    if volume <= 0 or volume > 200:
        return False, "Volume must be greater than 0 and at most 200 µL."

    # Check that both wells are allowed.
    if transfer["source"] not in allowed_wells:
        return False, "Source well is not allowed. Must be one of A1, A2, B1, or B2."

    if transfer["destination"] not in allowed_wells:
        return False, "Destination well is not allowed. Must be one of A1, A2, B1, or B2."

    # A transfer cannot have the same source and destination.
    if transfer["source"] == transfer["destination"]:
        return False, "Source and destination wells cannot be the same."

    return True, "Valid transfer instruction."
