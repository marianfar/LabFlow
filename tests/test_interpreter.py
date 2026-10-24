
from src.interpreter import interpret_instruction

#test the interpreter with a valid transfer instruction
def test_interpreter_with_valid_transfer():
    instruction = "Transfer 50 µL from well A1 to well B1."
    result = interpret_instruction(instruction)

    assert result == {
        "action": "transfer_liquid",
        "source": "A1",
        "destination": "B1",
        "volume_ul": 50
    }


#test the interpreter with an invalid transfer instruction
def test_interpreter_rejects_missing_volume():
    instruction = "Transfer liquid from well A1 to well B1."

    result = interpret_instruction(instruction)

    assert result is None

#test missing source well
def test_interpreter_rejects_missing_well():
    instruction = "Transfer 50 µL from well A1."

    result = interpret_instruction(instruction)

    assert result is None

#test too many wells
def test_interpreter_rejects_extra_wells():
    instruction = "Transfer 50 µL from well A1 to well B1 and well A2."

    result = interpret_instruction(instruction)

    assert result is None

#test negative volume
def test_interpreter_rejects_negative_volume():
    instruction = "Transfer -50 µL from well A1 to well B1."

    result = interpret_instruction(instruction)

    assert result == {
        "action": "transfer_liquid",
        "source": "A1",
        "destination": "B1",
        "volume_ul": -50
    }
#test the interpreter with a non-string input
def test_interpreter_rejects_non_string_input():
    result = interpret_instruction(None)

    assert result is None