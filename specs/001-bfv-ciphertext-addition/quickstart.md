# Quickstart: BFV Ciphertext Addition Script

This guide explains how to set up and run the Python script for the BFV Homomorphic Encryption assignment.

## Prerequisites

- Python 3.9 or higher
- `uv` package manager (recommended) or `pip`

## 1. Installation

### Using uv (Recommended)

First, install `uv` if you don't have it:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then set up the project:

```bash
# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

### Using pip (Traditional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 2. Setup

Before running the script, ensure you have the following files:

1. **TA-provided files** in the `download/` directory:
   - `public.key`
   - `ntnu_[your_student_id].tenseal` (e.g., `ntnu_41173058H.tenseal`)

2. **Your student ID** in `student-id.txt` in the project root

## 3. Running the Script

### Using uv

```bash
# Without activating virtual environment
uv run python src/main.py

# Or with activated environment
source .venv/bin/activate
python src/main.py
```

### Using traditional Python

```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
python src/main.py
```

The script will perform the following steps:
1. Load the `public.key` and your student-specific `.tenseal` file from `download/`
2. Encrypt the last five digits of your student ID
3. Perform homomorphic addition
4. Save the result

## 4. Output

Upon successful execution, a new file will be created in the project root directory:
`[your_student_id]_enc_result.tenseal`

This is the file you need to submit for the assignment.

## 5. Testing

Run the test suite to verify everything works:

```bash
# Using uv
uv run pytest tests/

# Using traditional Python
pytest tests/
```

## Troubleshooting

- **File not found errors**: Ensure files are in the `download/` directory and `student-id.txt` is in the project root
- **Import errors**: Make sure you've activated the virtual environment or use `uv run`
- **TenSEAL installation issues**: Contact the TA if you encounter problems installing the `tenseal` package
