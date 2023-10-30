# Turing Machine Simulator

print(">>>Reading TM.txt...")

# Read the TM configuration from TM.txt
with open("data/TM.txt", "r") as file:
    num_states = int(file.readline().strip())
    halt_state = int(file.readline().strip())
    transitions = {}
    for line in file:
        src_state, read_char, write_char, move_dir, dest_state = line.strip().split()
        transitions[(int(src_state), read_char)] = (
            write_char,
            move_dir,
            int(dest_state),
        )

# Initialize the tape based on user input
tape_input = input(
    ">>>Enter the starting tape with one leading and one trailing blank (_): "
)
tape = list(tape_input)
head = 0

print(">>>Processing...")

# Initialize the TM
current_state = 0

# Simulation
while current_state != halt_state:
    # Create the display string for the current configuration
    display_tape = "".join(tape)
    head_marker = "[" + tape[head] + "]"
    display_tape = display_tape[:head] + head_marker + display_tape[head + 1 :]

    # Display the current configuration
    print(f"{current_state}: {display_tape}")

    # Perform transition
    write_char, move_dir, next_state = transitions.get(
        (current_state, tape[head]), (None, None, None)
    )

    # Update if transition exists, otherwise halt
    if write_char is not None:
        tape[head] = write_char
        head += 1 if move_dir == "R" else -1
        current_state = next_state
    else:
        break

# Create the display string for the final configuration
display_tape = "".join(tape)
head_marker = "[" + tape[head] + "]"
display_tape = display_tape[:head] + head_marker + display_tape[head + 1 :]

# Display the final halting state
print(f"{halt_state}: {display_tape}")
print("[HALT]")
