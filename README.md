# LabFlow

LabFlow is a Python prototype exploring how natural-language instructions can be translated into structured laboratory workflows. It focuses on liquid-transfer instructions and demonstrates a simple approach to interpretation, validation, and simulation.

## Features

- **Rule-based interpretation:** Extracts liquid volume and well names from simple natural-language instructions.
- **Input validation:** Checks required fields, data types, allowed wells, volume limits, and source/destination constraints.
- **Transfer simulation:** Simulates valid transfers without controlling physical laboratory equipment.
- **Pipeline:** Connects interpretation, validation, and simulation.
- **LLM-ready utilities:** Builds structured JSON requests and parses JSON responses in preparation for future LLM integration.
- **Automated tests:** Uses pytest to test valid instructions, invalid inputs, and error handling.

## Project structure

```text
LabFlow/
├── src/
│   ├── interpreter.py
│   ├── validator.py
│   ├── simulator.py
│   ├── pipeline.py
│   ├── llm_client.py
│   └── main.py
├── tests/
│   ├── test_interpreter.py
│   ├── test_validator.py
│   ├── test_simulator.py
│   ├── test_pipeline.py
│   └── test_llm_client.py
├── README.md
├── LICENSE
└── .gitignore
```

## Requirements

- Python 3.10 or later
- pytest

Install pytest if necessary:

```bash
python -m pip install pytest
```

## Run the prototype

From the repository root, run:

```bash
python -m src.main
```

The example instruction is interpreted, validated, and passed to the simulator.

## Run the tests

```bash
python -m pytest -v
```

## Current limitations

- The rule-based interpreter supports only a narrow instruction format.
- LLM integration is not yet active. The current LLM utilities prepare requests and parse JSON responses but do not call an external model.
- The simulated workflow does not control physical laboratory equipment.
- The configured wells and volume limits are illustrative project constraints, not validated specifications for real laboratory instruments.

## Future work

- Integrate an LLM to interpret more varied natural-language instructions.
- Evaluate interpretation accuracy using a collection of valid, invalid, and ambiguous instructions.
- Improve error handling and structured output validation.

## Safety

LabFlow is an educational software prototype. Its outputs must not be treated as validated laboratory procedures or used to control real laboratory equipment.
