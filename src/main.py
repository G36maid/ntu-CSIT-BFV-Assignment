"""
BFV Homomorphic Encryption Assignment
This script performs homomorphic addition using the BFV encryption scheme.
"""

import tenseal as ts
from pathlib import Path
from typing import Tuple


# Configuration
DOWNLOAD_DIR = Path(__file__).parent.parent / "download"


def load_files(
    student_id: str, download_dir: Path = DOWNLOAD_DIR
) -> Tuple[bytes, bytes]:
    """
    Load the public key and TA's ciphertext from files.

    Args:
        student_id: The student's ID string
        download_dir: Directory containing the download files

    Returns:
        A tuple containing (public_key_data, ta_ciphertext_data)

    Raises:
        FileNotFoundError: If required files are not found
    """
    # Load public key
    public_key_path = download_dir / "public.key"
    with open(public_key_path, "rb") as f:
        public_key_data = f.read()

    # Try multiple possible ciphertext filename formats
    possible_names = [
        f"ntnu_{student_id}.tenseal",  # NTNU format
        f"{student_id}.tenseal",  # Direct format
    ]

    ta_ciphertext_data = None
    for filename in possible_names:
        try:
            ciphertext_path = download_dir / filename
            with open(ciphertext_path, "rb") as f:
                ta_ciphertext_data = f.read()
            print(f"  Loaded ciphertext from: {filename}")
            break
        except FileNotFoundError:
            continue

    if ta_ciphertext_data is None:
        raise FileNotFoundError(
            f"Could not find ciphertext file for {student_id}. "
            f"Tried: {', '.join(possible_names)}"
        )

    return public_key_data, ta_ciphertext_data


def extract_last_five_digits(student_id: str) -> int:
    """
    Extract the last five digits from the student ID and convert to integer.

    Args:
        student_id: The student's ID string (may contain letters)

    Returns:
        The last five digits as an integer
    """
    # Extract only numeric characters
    digits_only = "".join(c for c in student_id if c.isdigit())
    # Get the last five digits
    last_five = digits_only[-5:]
    return int(last_five)


def encrypt_student_number(context: ts.Context, student_number: int) -> ts.BFVVector:
    """
    Encrypt the student number using the BFV context.

    Args:
        context: The TenSEAL BFV context
        student_number: The number to encrypt

    Returns:
        An encrypted BFV vector containing the student number
    """
    return ts.bfv_vector(context, [student_number])


def perform_homomorphic_addition(ciphertext1: ts.BFVVector, ciphertext2: ts.BFVVector):
    """
    Perform homomorphic addition between two ciphertexts.

    Args:
        ciphertext1: First encrypted vector
        ciphertext2: Second encrypted vector

    Returns:
        The homomorphic sum of the two ciphertexts
    """
    return ciphertext1 + ciphertext2


def main() -> int:
    """
    Main execution function that orchestrates the homomorphic encryption process.

    Returns:
        0 on success, 1 on error
    """
    # Use current working directory as project root (allows tests to override)
    project_root = Path.cwd()
    download_dir = project_root / "download"

    try:
        # Determine student ID file path
        student_id_path = project_root / "student-id.txt"

        # Read student ID from file
        with open(student_id_path, "r") as f:
            student_id = f.read().strip()

        print(f"Student ID: {student_id}")
        print(f"Download directory: {download_dir}")

        # Load public key and TA's ciphertext
        print("Loading files from download/...")
        public_key_data, ta_ciphertext_data = load_files(student_id, download_dir)

        # Initialize TenSEAL context from public key
        print("Initializing context...")
        context = ts.context_from(public_key_data)

        # Extract last five digits and convert to integer
        student_number = extract_last_five_digits(student_id)
        print(f"Last five digits: {student_number}")

        # Encrypt the student number
        print("Encrypting student number...")
        student_ciphertext = encrypt_student_number(context, student_number)

        # Deserialize TA's ciphertext
        print("Deserializing TA's ciphertext...")
        ta_ciphertext = ts.bfv_vector_from(context, ta_ciphertext_data)

        # Perform homomorphic addition
        print("Performing homomorphic addition...")
        result_ciphertext = perform_homomorphic_addition(
            student_ciphertext, ta_ciphertext
        )

        # Save the result to project root
        print("Saving result...")
        output_path = project_root / f"{student_id}_enc_result.tenseal"
        result_data = result_ciphertext.serialize()
        with open(output_path, "wb") as f:
            f.write(result_data)

        print(f"Success! Result saved to: {output_path}")

    except FileNotFoundError as e:
        print(f"Error: Required file not found - {e}")
        print("Please ensure the following files exist:")
        print(f"  - {project_root}/student-id.txt")
        print(f"  - {project_root}/download/public.key")
        print(
            f"  - {project_root}/download/ntnu_[student_id].tenseal or [student_id].tenseal"
        )
        return 1
    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
