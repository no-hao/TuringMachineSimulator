
# Turing Machine Simulator

This project is a Turing Machine Simulator that reads machine configurations from a text file and simulates the machine based on user input.

## Project Structure

The project has the following directory structure:

```
TuringMachineSimulator/
|-- src/
|   |-- __init__.py
|   |-- main.py
|   |-- tm_reader.py
|   |-- tm_simulator.py
|-- tests/
|   |-- __init__.py
|   |-- test_tm_reader.py
|   |-- test_tm_simulator.py
|-- data/
|   |-- TM.txt
|-- README.md
```

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/no-hao/TuringMachineSimulator.git
    ```
2. Navigate to the project directory:
    ```bash
    cd TuringMachineSimulator
    ```

### Configuration File

Place your Turing Machine configuration file (`TM.txt`) in the `data/` directory. The format should be as follows:

- First line: Number of states
- Second line: Halting state
- Subsequent lines: Transitions, formatted as `source_state read_symbol write_symbol move_direction destination_state`

Example:
```
3
2
0 0 1 R 1
```

### Running the Simulator

1. Navigate to the `src/` directory:
    ```bash
    cd src
    ```
2. Run `main.py`:
    ```bash
    python3 main.py
    ```

### Running Tests

1. Navigate to the project root directory:
    ```bash
    cd TuringMachineSimulator
    ```
2. Run the tests:
    ```bash
    python3 -m unittest discover tests
    ```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

