def simulate_tm(tape, num_states, halt_state, transitions):
    """
    Simulate the Turing Machine (TM) based on the given parameters.
    This function prints the TM configurations until it reaches the halting state.

    Parameters:
    - tape (list): The initial tape configuration.
    - num_states (int): The total number of states in the TM.
    - halt_state (int): The halting state of the TM.
    - transitions (dict): The state transition rules.
    """

    # Check for invalid input parameters.
    if tape is None or num_states is None or halt_state is None or transitions is None:
        print("Invalid input parameters.")
        return

    # Initialize head position and current state.
    head = 0
    current_state = 0

    # Main simulation loop.
    while current_state != halt_state:
        # Create and display the current tape configuration.
        display_tape = "".join(tape)
        head_marker = "[" + tape[head] + "]"
        display_tape = display_tape[:head] + head_marker + display_tape[head + 1 :]
        print(f"{current_state}: {display_tape}")

        # Retrieve the transition rule for the current state and tape symbol.
        write, move, next_state = transitions.get(
            (current_state, tape[head]), (None, None, None)
        )

        # Check for invalid transition.
        if write is None:
            print("Invalid transition. Halting.")
            return

        # Write to tape and move head.
        tape[head] = write
        head += 1 if move == "R" else -1

        # Check for out-of-bounds head movement.
        if head < 0 or head >= len(tape):
            print("Head moved out of tape bounds. Halting.")
            return

        # Update the current state.
        current_state = next_state

    # Display the final tape configuration.
    display_tape = "".join(tape)
    head_marker = "[" + tape[head] + "]"
    display_tape = display_tape[:head] + head_marker + display_tape[head + 1 :]
    print(f"{halt_state}: {display_tape}")
    print("[HALT]")
