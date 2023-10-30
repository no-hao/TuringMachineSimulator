class TuringMachine:
    def __init__(self, config, initial_tape):
        self.states = config["states"]
        self.halting_state = config["halting_state"]
        self.transitions = config["transitions"]
        self.current_state = 0  # Start state is always 0
        self.head_position = initial_tape.index(
            "_"
        )  # Assuming ear s always a leading '_'
        self.tape = list(initial_tape)  # Initialize the tape

    def execute(self):
        step = 0
        while self.current_state != self.halting_state:
            # Boundary check
            if self.head_position < 0 or self.head_position >= len(self.tape):
                print("Head out of bounds")
                print("[HALT]")
                return

            # Debug information
            print(
                f"Debug: State={self.current_state}, Symbol={self.tape[self.head_position]}"
            )

            current_tape_str = "".join(self.tape)
            print(
                f"{step}: {current_tape_str[:self.head_position]}[{self.current_state}]{current_tape_str[self.head_position:]}"
            )

            current_symbol = self.tape[self.head_position]
            transition_key = (self.current_state, current_symbol)

            if transition_key not in self.transitions:
                print("Undefined transition")
                print("[HALT]")
                return

            # Debug information
            print(f"Debug: Transition={self.transitions[transition_key]}")

            # This line will get the first element (which is a tuple) from the list
            write_symbol, move_direction, next_state = self.transitions[transition_key][
                0
            ]

            # Update tape, head position, and state
            print(f"Debug Before Write: {self.tape[self.head_position]}")
            self.tape[self.head_position] = write_symbol
            print(f"Debug After Write: {self.tape[self.head_position]}")
            self.head_position += 1 if move_direction == "R" else -1
            self.current_state = next_state
            step += 1

        print("[HALT]")
