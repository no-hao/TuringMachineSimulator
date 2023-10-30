class TuringMachine:
    def __init__(self, config, initial_tape):
        self.states = config["states"]
        self.halting_state = config["halting_state"]
        self.transitions = config["transitions"]
        self.current_state = 0  # Start state is always 0
        self.head_position = initial_tape.index(
            "_"
        )  # Assuming there is always a leading '_'
        self.tape = list(initial_tape)  # Initialize the tape

    def execute(self):
        step = 0
        visited_pairs = set()
        while self.current_state != self.halting_state:
            if self.head_position < 0 or self.head_position >= len(self.tape):
                print("Head out of bounds")
                print("[HALT]")
                return

            current_symbol = self.tape[self.head_position]
            transition_key = (self.current_state, current_symbol)

            if transition_key not in self.transitions:
                print("Undefined transition")
                print("[HALT]")
                return

            # If encountering a new state-symbol pair in this cycle, increment the step count and clear visited pairs
            if transition_key not in visited_pairs:
                visited_pairs.add(transition_key)
                step += 1
                visited_pairs.clear()

            visited_pairs.add(transition_key)

            write_symbol, move_direction, next_state = self.transitions[transition_key][
                0
            ]

            current_tape_str = "".join(self.tape)
            print(
                f"{step}: {current_tape_str[:self.head_position]}[{current_symbol}]{current_tape_str[self.head_position + 1:]}"
            )

            self.tape[self.head_position] = write_symbol
            self.head_position += 1 if move_direction == "R" else -1
            self.current_state = next_state

        print("[HALT]")
