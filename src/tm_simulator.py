def simulate_tm(tape_input, num_states, halt_state, transitions):
    """
    Simulate the Turing Machine (TM) based on the given parameters.
    This function prints the TM configurations until it reaches the halting state.

    Parameters:
    - tape_input (list): The initial tape configuration including one leading and one trailing blank.
    - num_states (int): The total number of states in the TM.
    - halt_state (int): The halting state of the TM.
    - transitions (dict): The state transition rules.
    """

    # Initialize the tape with the input, which already includes a leading and trailing blank
    tape = list(tape_input)

    # Initialize the head position on the first position of the input
    head = 0

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
        current_symbol = tape[head]
        transition_key = (current_state, current_symbol)

        if transition_key not in transitions:
            print(
                f"No transition defined for state {current_state} and symbol '{current_symbol}'."
            )
            print("Entering error state and stopping.")
            return

        write, move, next_state = transitions[transition_key]

        # Write to the tape and move the head.
        tape[head] = write
        head += 1 if move == "R" else -1

        # Dynamically extend the tape if the head moves beyond the current bounds
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
