# Task Plan: BFV Ciphertext Addition Script

**Branch**: `001-bfv-ciphertext-addition`

This document outlines the tasks required to implement the BFV Ciphertext Addition script.

## Phase 1: Project Setup

- [X] T001 Create project directories: `src/` and `tests/`
- [X] T002 Create empty Python files: `src/main.py` and `tests/test_main.py`
- [X] T003 Create a `requirements.txt` file and add `tenseal` and `pytest`

## Phase 2: User Story 1 - Perform Homomorphic Addition

**Goal**: Implement the core logic for loading data, performing homomorphic addition, and saving the result.
**Independent Test**: The script can be run with mock `public.key` and `[student_id].tenseal` files. A successful run will produce a valid `[student_id]_enc_result.tenseal` file without errors.

### Implementation Tasks
- [X] T004 [US1] In `src/main.py`, implement the logic to load the `public.key` and `[student_id].tenseal` files in binary mode.
- [X] T005 [US1] In `src/main.py`, add logic to accept a student ID, extract the last five digits, and convert them to an integer.
- [X] T006 [US1] In `src/main.py`, initialize the TenSEAL context from the public key and encrypt the student ID integer.
- [X] T007 [US1] In `src/main.py`, perform the homomorphic addition between the two ciphertexts.
- [X] T008 [US1] In `src/main.py`, serialize the resulting ciphertext and save it to the correctly named output file (`[student_id]_enc_result.tenseal`).
- [X] T009 [US1] In `src/main.py`, add a main execution block (`if __name__ == "__main__":`) to orchestrate all the steps and handle potential `FileNotFoundError`.

### Testing Tasks
- [X] T010 [P] [US1] In `tests/`, create mock `public.key` and `[student_id].tenseal` files to be used for testing.
- [X] T011 [P] [US1] In `tests/test_main.py`, write a test to verify that the script successfully creates the output file when the correct inputs are provided.
- [X] T012 [P] [US1] In `tests/test_main.py`, write a test to ensure the script handles `FileNotFoundError` gracefully if an input file is missing.

## Phase 3: Polish & Documentation

- [X] T013 Add type hints, comments, and docstrings to `src/main.py` for clarity.
- [X] T014 Update the root `README.md` with a summary of the project and instructions on how to run the script, referencing the quickstart guide.

## Phase 4: Environment Adaptation & Verification

- [X] T015 Update `src/main.py` to read files from `download/` directory with support for multiple filename formats
- [X] T016 Update documentation (`README.md`, `quickstart.md`) to use `uv` package manager and reference `download/` directory
- [X] T017 Update `quickstart.md` with complete uv setup and usage instructions
- [X] T018 Test the script with actual files from `download/` directory (public.key, ntnu_41173058H.tenseal)
- [X] T019 Verify output file created successfully: `41173058H_enc_result.tenseal` (423KB)
- [X] T020 Add numpy to requirements.txt (required by tenseal)

## Phase 5: Test Suite Fixes

- [X] T021 Analyze test failures caused by download/ directory change
- [X] T022 Fix test fixtures to create download/ subdirectory and update main() to use current working directory
- [X] T023 Verify all tests pass (8/8 passing)

## Dependencies

```mermaid
graph TD
    subgraph Phase 1 - Setup
        T001 --> T002;
        T001 --> T003;
    end

    subgraph Phase 2 - User Story 1
        T004 --> T006;
        T005 --> T006;
        T006 --> T007;
        T007 --> T008;
        T008 --> T009;
    end
    
    subgraph Testing (Parallel)
        T010 --> T011;
        T010 --> T012;
    end

    Phase_1_Setup --> Phase_2_User_Story_1;
    Phase_2_User_Story_1 --> Phase_3_Polish;
    T009 --> T011((Test Success));
    T009 --> T012((Test Failure));

    classDef phase fill:#f9f,stroke:#333,stroke-width:2px;
    class Phase_1_Setup,Phase_2_User_Story_1,Phase_3_Polish phase;
```

## Parallel Execution

Within User Story 1, the testing tasks can be worked on in parallel with the implementation tasks after the initial file structure is in place.

- **Group 1 (Implementation)**: T004, T005, T006, T007, T008, T009
- **Group 2 (Testing Setup)**: T010
- **Group 3 (Testing Logic - depends on Group 2)**: T011, T012

## Implementation Strategy

The implementation will focus on delivering the single user story as a complete MVP.
1.  First, complete the project setup tasks in Phase 1.
2.  Implement the core logic in `src/main.py` as defined in Phase 2.
3.  Concurrently, develop the tests in `tests/test_main.py` to validate the implementation.
4.  Finally, complete the polish and documentation tasks.
