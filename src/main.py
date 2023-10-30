from utils import read_tm_config
from turing_machine import (
    TuringMachine,
)  # Make sure to have the updated TuringMachine class


def main():
    # Read configurations
    config = read_tm_config("data/TM.txt")

    # Get user input for tape
    input_string = input(
        "Enter the starting tape with one leading and one trailing blank (_): "
    )

    # Initialize and validate Turing Machine
    tm = TuringMachine(config, initial_tape=input_string)  # Pass the initial tape here

    # Execute Turing Machine
    tm.execute()


if __name__ == "__main__":
    main()
