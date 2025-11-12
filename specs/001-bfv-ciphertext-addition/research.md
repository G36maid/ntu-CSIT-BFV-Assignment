# Research: BFV Ciphertext Addition Script

## Technology Choices

### Cryptographic Library: TenSEAL

- **Decision**: The `tenseal` Python library will be used for all homomorphic encryption operations.
- **Rationale**: This is a hard requirement of the assignment. The library provides the necessary BFV encryption scheme, context management, and ciphertext operations (addition, serialization).
- **Alternatives considered**: None. The assignment explicitly specifies the use of TenSEAL.

## Best Practices

### TenSEAL Context Management

- **Finding**: The `tenseal` context should be initialized once from the public key. This context is then used for all subsequent operations, including encrypting the student ID vector and deserializing the TA's ciphertext. This ensures both ciphertexts are compatible for addition.

### File I/O

- **Finding**: Key and ciphertext files must be read in binary mode (`"rb"`). The resulting ciphertext must be written in binary mode (`"wb"`) after being serialized.
