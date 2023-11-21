def simulate_tm(tape_input, num_states, halt_state, transitions):
    """
    Simulate the Turing Machine (TM) based on the given parameters.
    This function prints the TM configurations until it reaches the halting state.

    Parameters:
    - tape_input (list): The initial tape configuration including leading and trailing blanks.
    - num_states (int): The total number of states in the TM.
    - halt_state (int): The halting state of the TM.
    - transitions (dict): The state transition rules.
    """

    # Calculate the number of extra spaces to add based on the length of the input
    inf_tape = len(tape_input)

    # Add extra space before and after the input
    tape = ["_"] * inf_tape + tape_input + ["_"] * inf_tape

    # Initialize the head position at the first blank before the actual binary input
    head = inf_tape

    # Check for invalid input parameters.
    if tape is None or num_states is None or halt_state is None or transitions is None:
        print("Invalid input parameters.")
        return

    # Initialize the current state.
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
            print("Invalid transition. Entering error state and stopping.")
            return

        # Write to the tape and move the head.
        tape[head] = write
        head += 1 if move == "R" else -1

        # Extend the tape if the head moves beyond the current bounds
        if head < 0:
            tape.insert(0, "_")
            head = 0
        elif head >= len(tape):
            tape.append("_")

        # Update the current state.
        current_state = next_state

    # Display the final tape configuration.
    display_tape = "".join(tape)
    head_marker = "[" + tape[head] + "]"
    display_tape = display_tape[:head] + head_marker + display_tape[head + 1 :]
    print(f"{halt_state}: {display_tape}")
    print("[HALT]")
