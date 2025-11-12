# Data Model: BFV Ciphertext Addition Script

This feature does not involve a traditional database model. The key entities are files on the filesystem.

## Key Entities

### 1. Public Key

- **Name**: `public.key`
- **Format**: Binary
- **Description**: A file containing the BFV public key used for encryption and homomorphic operations. It is provided by the TA.

### 2. TA's Ciphertext

- **Name**: `[your_student_id].tenseal`
- **Format**: Binary (Serialized TenSEAL BFV ciphertext)
- **Description**: A file containing a random number encrypted by the TA using the BFV scheme. The filename is specific to each student.

### 3. Student ID Number

- **Name**: N/A (In-memory variable)
- **Format**: Integer
- **Description**: The last five digits of the student's ID, converted to an integer. This number is encrypted by the script.

### 4. Result Ciphertext

- **Name**: `[your_student_id]_enc_result.tenseal`
- **Format**: Binary (Serialized TenSEAL BFV ciphertext)
- **Description**: The final output of the script. It contains the homomorphic sum of the student's encrypted ID and the TA's encrypted number.
