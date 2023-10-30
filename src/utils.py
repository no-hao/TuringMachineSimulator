from collections import defaultdict


def read_tm_config(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    num_states = int(lines[0].strip())
    halting_state = int(lines[1].strip())
    transitions = defaultdict(list)

    for line in lines[2:]:
        parts = line.strip().split(" ")
        state, symbol, write_symbol, move, next_state = parts  # Directly unpack
        transitions[(int(state), symbol)].append((write_symbol, move, int(next_state)))

    return {
        "states": list(range(num_states)),
        "halting_state": halting_state,
        "transitions": transitions,
    }
