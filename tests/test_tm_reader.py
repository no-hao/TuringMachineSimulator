import unittest
from src.tm_reader import read_tm_config
import os


class TestTMReader(unittest.TestCase):
    def test_valid_file(self):
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, "valid_file.txt")
        num_states, halt_state, transitions = read_tm_config(file_path)

    def test_invalid_file_format(self):
        num_states, halt_state, transitions = read_tm_config("invalid_file.txt")
        self.assertIsNone(num_states)
        self.assertIsNone(halt_state)
        self.assertIsNone(transitions)

    def test_nonexistent_file(self):
        num_states, halt_state, transitions = read_tm_config("nonexistent_file.txt")
        self.assertIsNone(num_states)
        self.assertIsNone(halt_state)
        self.assertIsNone(transitions)


if __name__ == "__main__":
    unittest.main()
