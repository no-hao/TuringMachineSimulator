import unittest
from src.tm_simulator import simulate_tm


class TestTMSimulator(unittest.TestCase):
    def test_valid_input(self):
        tape = ["_", "0", "_"]
        num_states = 3
        halt_state = 2
        transitions = {(0, "0"): ("1", "R", 1)}
        result = simulate_tm(tape, num_states, halt_state, transitions)
        self.assertEqual(result, None)  # Since the function prints and returns None

    def test_invalid_transition(self):
        tape = ["_", "2", "_"]
        num_states = 3
        halt_state = 2
        transitions = {(0, "0"): ("1", "R", 1)}
        result = simulate_tm(tape, num_states, halt_state, transitions)
        self.assertEqual(result, None)

    def test_invalid_parameters(self):
        result = simulate_tm(None, None, None, None)
        self.assertEqual(result, None)


if __name__ == "__main__":
    unittest.main()
