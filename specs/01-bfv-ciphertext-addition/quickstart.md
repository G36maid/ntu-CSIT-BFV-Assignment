# Quickstart: BFV Ciphertext Addition Script

This guide explains how to set up and run the Python script for the BFV Homomorphic Encryption assignment.

## Prerequisites

- Python 3.9 or higher
- The `pip` package manager

## 1. Installation

Install the required `tenseal` library using pip:

```bash
pip install tenseal
```

## 2. Setup

Before running the script, place the following files, provided by the TA, in the same directory as the script:

1.  `public.key`
2.  `[your_student_id].tenseal` (e.g., `410785021.tenseal`)

## 3. Running the Script

Execute the script from your terminal:

```bash
python main.py
```

The script will perform the following steps:
1.  Load the `public.key` and your student-specific `.tenseal` file.
2.  Encrypt the last five digits of your student ID.
3.  Perform homomorphic addition.
4.  Save the result.

## 4. Output

Upon successful execution, a new file will be created in the same directory with the name:
`[your_student_id]_enc_result.tenseal`

This is the file you need to submit for the assignment.
