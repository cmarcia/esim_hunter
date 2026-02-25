#!/usr/bin/env python
import sys
from esim_hunter.crew import EsimHunter

def run():
    """
    Run the crew.
    """
    inputs = {
        'location': 'Japan',
        'duration': '14'
    }
    EsimHunter().crew().kickoff(inputs=inputs)

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'location': 'Japan',
        'duration': '14'
    }
    try:
        EsimHunter().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

if __name__ == "__main__":
    run()
