import unittest
from src.utils import read_tm_config


class TestUtils(unittest.TestCase):
    def test_read_tm_config(self):
        # The path to your TM.txt file. Adjust accordingly.
        file_path = "data/TM.txt"

        config = read_tm_config(file_path)

        expected_states = list(range(6))
        expected_halting_state = 5

        # Replace these expected_transitions with the transitions you expect from TM.txt
        expected_transitions = {
            (0, "_"): [("_", "R", 1)],
            (1, "1"): [("0", "R", 1)],
            (1, "0"): [("1", "R", 1)],
            (1, "_"): [("_", "L", 2)],
            (2, "1"): [("0", "L", 2)],
            (2, "0"): [("1", "R", 3)],
            (3, "0"): [("0", "R", 3)],
            (3, "1"): [("1", "R", 3)],
            (3, "_"): [("_", "L", 4)],
            (4, "0"): [("1", "L", 4)],
            (4, "1"): [("0", "L", 4)],
            (4, "_"): [("_", "R", 5)],
        }

        self.assertEqual(config["states"], expected_states)
        self.assertEqual(config["halting_state"], expected_halting_state)
        self.assertEqual(config["transitions"], expected_transitions)


if __name__ == "__main__":
    unittest.main()
