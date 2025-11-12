<!--
Sync Impact Report:
- Version change: 0.0.0 → 1.0.0
- List of modified principles:
  - [PRINCIPLE_1_NAME] → Correctness
  - [PRINCIPLE_2_NAME] → Security
  - [PRINCIPLE_3_NAME] → Reproducibility and Naming Conventions
- Added sections: None
- Removed sections: [SECTION_2_NAME], [SECTION_3_NAME]
- Templates requiring updates: None
- Follow-up TODOs: None
-->
# BFV Homomorphic Encryption Assignment Constitution

## Core Principles

### Correctness
The Python script MUST correctly perform the following sequence of operations:
1.  Load the provided `public.key` and the student-specific `[your_student_id].tenseal` ciphertext.
2.  Convert the last five digits of the student ID into an integer.
3.  Encrypt this integer into a single-element BFV ciphertext using the public key.
4.  Perform homomorphic addition between the newly encrypted ciphertext and the one provided by the TA.
5.  Serialize and save the resulting ciphertext to a file.

*Rationale: The fundamental goal of the assignment is to produce a valid ciphertext result that can be successfully decrypted and verified by the TA. Any deviation from the specified cryptographic process will result in an incorrect and invalid submission.*

### Security
The script MUST NOT attempt to load, use, or expose any private key. All operations must be performed using only the provided public key and ciphertexts. The `public.key` and `[your_student_id].tenseal` files provided by the TA MUST NOT be modified or exchanged.

*Rationale: Maintaining the integrity of the provided cryptographic materials is essential. This principle ensures that the solution adheres to the security model of public-key cryptography and prevents academic dishonesty.*

### Reproducibility and Naming Conventions
The final output file MUST be named exactly according to the format: `[your_student_id]_enc_result.tenseal`. The script's logic should be deterministic, ensuring that given the same inputs, it always produces the same output.

*Rationale: Strict adherence to naming and output conventions is required for automated processing and grading of the submissions. An incorrect filename may cause the submission to be missed or marked as invalid.*

## Governance
This constitution defines the non-negotiable rules for completing the assignment successfully. Any solution MUST comply with all principles outlined above.

**Version**: 1.0.0 | **Ratified**: 2025-11-12 | **Last Amended**: 2025-11-12
