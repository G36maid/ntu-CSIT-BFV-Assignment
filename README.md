# BFV Homomorphic Encryption Assignment

## What is this?

This project is a Python script that performs homomorphic addition using the BFV encryption scheme from the TenSEAL library. It is designed to fulfill the requirements of the BFV Homomorphic Encryption and Ciphertext Addition Assignment.

The script loads a public key and a pre-encrypted ciphertext provided by the TA, encrypts the last five digits of a student's ID, performs homomorphic addition on the two ciphertexts, and saves the resulting encrypted data to a file.

## How to Use

### 1. Installation

This project uses `uv` for Python package and virtual environment management.

First, install `uv` if you don't have it:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then, set up the project's virtual environment and install dependencies:
```bash
# Create virtual environment
uv venv

# Install dependencies
uv pip install -r requirements.txt
```

### 2. Setup

Before running the script, you need to:

1.  **Place TA-provided files** in the `download/` directory:
    *   `public.key`
    *   `ntnu_[your_student_id].tenseal` (e.g., `ntnu_41173058H.tenseal`)

2.  **Add your student ID** to the `student-id.txt` file in the project root.

### 3. Running the Script

To execute the script and generate your result file, run the following command:

```bash
uv run python src/main.py
```

Upon successful execution, a new file named `[your_student_id]_enc_result.tenseal` will be created in the project root directory. This is the file you need to submit.

### 4. Running Tests

To run the test suite and verify the implementation, use the following command:

```bash
uv run pytest tests/
```

---

## Assignment Details

### Objective
This assignment provides hands-on experience with Homomorphic Encryption, specifically using the BFV encryption scheme from the TenSEAL library. You will encrypt the last five digits of your student ID using a public key, perform ciphertext addition with a randomly encrypted number provided by the TA, and then upload the resulting ciphertext.

### Files Provided by the TA
The following files will be provided:

| Filename                     | Purpose                                          |
| :--------------------------- | :----------------------------------------------- |
| `public.key`                 | Public key used for encryption and addition      |
| `[your_student_id].tenseal`  | A randomly encrypted number (different for each student) |

**Important:** Do not modify these files or exchange them with others.

### What You Need to Do
1.  **Load Files:** Write a Python script to load the provided `public.key` and `[your_student_id].tenseal`.
2.  **Encrypt Student ID:** Convert the last five digits of your student ID to an integer and encrypt it as a single-element ciphertext using BFV.
3.  **Perform Addition:** Add your encrypted number with the provided ciphertext using homomorphic addition.
4.  **Save Result:** Save the result as a file named: `[your_student_id]_enc_result.tenseal`.

### Example
-   **Your student ID:** 410785021 → Last five digits: 85021
-   **TA's random encrypted number (example):** [85684]
-   **Your operation:** Encrypt 85021 and add it to the random encrypted number: `[85021] + [85684] = [170705]`
-   You will not see these actual values, but you will complete the ciphertext addition.
-   **Output filename:** `410785021_enc_result.tenseal`

### Submission Requirements
Please upload the following file:
-   `[your_student_id]_enc_result.tenseal`

**Warning:** Incorrect filenames, wrong ciphertexts, or duplicate content may be considered invalid or plagiarism.
