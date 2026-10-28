# Repository Structure

- `apps/m2/`: Task scripts and README for Milestone 2 tasks.
- `bs4/`: Beautiful Soup source code with custom class `SoupReplacer`.
- `bs4/tests/`: 2 `SoupReplacer` tests: `test_soupreplacer1.py` and `test_soupreplacer2.py`.

## Installation

Note: This was ran in Windows 11

1. Install Venv (recommanded)

```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

2. Install the required dependencies:

```
python -m pip install lxml html5lib pytest
```

## Running the Milestone 2 Task files

Replace `<input-file>` with the path to an HTML or XML file.

```
python -m apps.m2.task2 <input-file>
python -m apps.m2.task3 <input-file>
python -m apps.m2.task4 <input-file>
python -m apps.m2.task6 <input-file>
```

## Running the Tests

```
python -m pytest bs4/tests
```

to run only the new tests:

```
python -m pytest bs4/tests/test_soupreplacer1.py bs4/tests/test_soupreplacer2.py
```
