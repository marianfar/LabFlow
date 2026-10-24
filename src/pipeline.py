'''
Simulate_transfer(transfer) expects a dictionary.
Pipeline will eventually receive plain English, interpret it into this dictionary, and pass the result to the simulator.
For now, we will test the simulator with a valid dictionary and an invalid dictionary.
'''
from src.simulator import simulate_transfer

def run_pipeline(transfer):
    """Run the pipeline with a given transfer instruction."""
    #Call simulate_transfer(transfer)
    success, message = simulate_transfer(transfer)
    return success, message
