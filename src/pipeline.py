'''
Simulate_transfer(transfer) expects a dictionary.
Pipeline receives plain English, interpret it into this dictionary, and pass the result to the simulator.
'''
from src.simulator import simulate_transfer
from src.interpreter import interpret_instruction

def run_pipeline(instruction):
    """Run the pipeline with a natural-language instruction."""
    #Call interpret_instruction
    transfer = interpret_instruction(instruction)
    if transfer is None:
        return False, "Could not interpret instruction."
    
    #Call simulate_transfer(transfer)
    success, message = simulate_transfer(transfer)
    return success, message
