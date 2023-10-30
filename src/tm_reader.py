def read_tm_config(file_path):
    """
    Read the Turing Machine (TM) configuration from a file.

    Parameters:
    - file_path (str): The path to the configuration file.

    Returns:
    - num_states (int): The total number of states in the TM.
    - halt_state (int): The halting state of the TM.
    - transitions (dict): A dictionary representing the state transition rules.
    """

    try:
        # Open the configuration file for reading.
        with open(file_path, "r") as file:
            try:
                # Read the total number of states.
                num_states = int(file.readline().strip())

                # Read the halting state.
                halt_state = int(file.readline().strip())

            except ValueError:
                # Handle invalid format for number of states or halting state.
                print("Invalid file format: Couldn't read states or halt state.")
                return None, None, None

            # Initialize an empty dictionary for transitions.
            transitions = {}

            # Read each transition rule line-by-line.
            for line in file:
                try:
                    # Parse the components of a transition rule.
                    src, read, write, move, dest = line.strip().split()

                    # Add the transition rule to the dictionary.
                    transitions[(int(src), read)] = (write, move, int(dest))

                except ValueError:
                    # Handle invalid transition rule format.
                    print("Invalid file format: Error in transition line.")
                    return None, None, None

        # Return the parsed TM configuration.
        return num_states, halt_state, transitions

    except FileNotFoundError:
        # Handle file not found error.
        print("File not found.")
        return None, None, None
