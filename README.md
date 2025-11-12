# BFV Homomorphic Encryption and Ciphertext Addition Assignment

## Objective
This assignment provides hands-on experience with Homomorphic Encryption, specifically using the BFV encryption scheme from the TenSEAL library. You will encrypt the last five digits of your student ID using a public key, perform ciphertext addition with a randomly encrypted number provided by the TA, and then upload the resulting ciphertext.

## Files Provided by the TA
The following files will be provided:

| Filename                     | Purpose                                          | Download Link (if provided) |
| :--------------------------- | :----------------------------------------------- | :-------------------------- |
| `public.key`                 | Public key used for encryption and addition      | [Public key link](https://drive.google.com/file/d/1IJMDEnLFHXoR9ueWZ5RHDxKW4ovNUqfr/view)             |
| `[your_student_id].tenseal`  | A randomly encrypted number (different for each student) | [Ciphertext link](https://drive.google.com/drive/folders/1WxeGn9X7xGxGJJt_oagZSqD_59hYvLPG)             |

**Important:** Do not modify these files or exchange them with others.

## What You Need to Do
1.  **Load Files:** Write a Python script to load the provided `public.key` and `[your_student_id].tenseal`.
2.  **Encrypt Student ID:** Convert the last five digits of your student ID to an integer and encrypt it as a single-element ciphertext using BFV.
3.  **Perform Addition:** Add your encrypted number with the provided ciphertext using homomorphic addition.
4.  **Save Result:** Save the result as a file named: `[your_student_id]_enc_result.tenseal`.

## Example
-   **Your student ID:** 410785021 → Last five digits: 85021
-   **TA's random encrypted number (example):** [85684]
-   **Your operation:** Encrypt 85021 and add it to the random encrypted number: `[85021] + [85684] = [170705]`
-   You will not see these actual values, but you will complete the ciphertext addition.
-   **Output filename:** `410785021_enc_result.tenseal`

## Submission Requirements
Please upload the following file:
-   `[your_student_id]_enc_result.tenseal`

**Warning:** Incorrect filenames, wrong ciphertexts, or duplicate content may be considered invalid or plagiarism.

## Installation
Make sure to install TenSEAL in your environment:
```/dev/null/install.sh#L1-1
pip install tenseal
```
If you encounter any installation or execution issues, please contact the TA as soon as possible.

## Deadline
Submit your ciphertext file to NTU COOL before 11:59 PM on Friday, November 14, 2025.
