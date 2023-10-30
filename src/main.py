import os
from tm_reader import read_tm_config
from tm_simulator import simulate_tm

if __name__ == "__main__":
    print(">>>Reading TM.txt...")

    # Get the directory where main.py is located
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Construct the path to TM.txt
    data_path = os.path.join(dir_path, "..", "data", "TM.txt")

    # Now use data_path in the read_tm_config function
    num_states, halt_state, transitions = read_tm_config(data_path)

    tape_input = input(
        ">>>Enter the starting tape with one leading and one trailing blank (_): "
    )
    tape = list(tape_input)
    print(">>>Processing...")
    simulate_tm(tape, num_states, halt_state, transitions)
