# Feature Specification: BFV Ciphertext Addition Script

**Feature Branch**: `001-bfv-ciphertext-addition`  
**Created**: 2025-11-12  
**Status**: Draft  
**Input**: User description: "1. Write a Python script to load the provided `public.key` and `[your_student_id].tenseal`. 2. Convert the last five digits of your student ID to an integer and encrypt it as a single-element ciphertext using BFV. 3. Add your encrypted number with the provided ciphertext using homomorphic addition. 4. Save the result as a file named: `[your_student_id]_enc_result.tenseal`."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Perform Homomorphic Addition (Priority: P1)

A student runs the Python script to perform the required homomorphic addition for their assignment. The script handles all the steps from loading files to saving the final result, producing a valid ciphertext for submission.

**Why this priority**: This is the core functionality of the assignment. Without it, the assignment cannot be completed.

**Independent Test**: The script can be tested by running it with a valid `public.key` and a dummy `[student_id].tenseal` file. The output should be a new `.tenseal` file.

**Acceptance Scenarios**:

1. **Given** a `public.key` and `[student_id].tenseal` file are in the same directory as the script, **When** the script is executed, **Then** a new file named `[student_id]_enc_result.tenseal` is created.
2. **Given** the script is executed, **When** the `public.key` or `[student_id].tenseal` file is missing, **Then** the script prints an informative error message and exits gracefully.

---

### Edge Cases

- What happens when the student ID has fewer than 5 digits? (The script should handle this gracefully, though the assignment implies a standard format).
- How does the system handle a corrupted or invalid `.tenseal` or `.key` file? (The TenSEAL library should raise an error, which the script should catch).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The script MUST load a public key from a file named `public.key`.
- **FR-002**: The script MUST load a BFV ciphertext from a file named `[your_student_id].tenseal`.
- **FR-003**: The script MUST extract the last five digits from a given student ID string.
- **FR-004**: The script MUST convert these five digits into an integer.
- **FR-005**: The script MUST encrypt the integer into a single-element BFV ciphertext using the loaded public key.
- **FR-006**: The script MUST perform homomorphic addition between the student's encrypted number and the TA's provided ciphertext.
- **FR-007**: The script MUST serialize the resulting ciphertext.
- **FR-008**: The script MUST save the serialized result to a file named `[your_student_id]_enc_result.tenseal`.

### Key Entities *(include if feature involves data)*

- **public.key**: The public key for BFV encryption provided by the TA.
- **[your_student_id].tenseal**: The encrypted random number provided by the TA.
- **Student ID Number**: The integer representation of the last five digits of the student's ID.
- **[your_student_id]_enc_result.tenseal**: The final encrypted result of the homomorphic addition.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: The script successfully executes from start to finish without crashing.
- **SC-002**: The output file is named exactly according to the specified format `[your_student_id]_enc_result.tenseal`.
- **SC-003**: The output file contains a valid BFV ciphertext that can be deserialized and decrypted by the TA's private key.
- **SC-004**: The decrypted result correctly corresponds to the sum of the student's encrypted number and the TA's encrypted number.
