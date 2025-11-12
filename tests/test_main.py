import os
import sys
import pytest
import tempfile
import shutil

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

try:
    import tenseal as ts
    from main import (
        extract_last_five_digits,
        encrypt_student_number,
        perform_homomorphic_addition,
        main,
    )

    TENSEAL_AVAILABLE = True
except ImportError:
    TENSEAL_AVAILABLE = False
    pytestmark = pytest.mark.skip(reason="tenseal not installed")


class TestExtractLastFiveDigits:
    """Test the extract_last_five_digits function."""

    def test_with_letter_suffix(self):
        """Test extraction with alphanumeric student ID."""
        assert extract_last_five_digits("41173058H") == 73058

    def test_with_numbers_only(self):
        """Test extraction with numeric-only student ID."""
        assert extract_last_five_digits("410785021") == 85021

    def test_with_less_than_five_digits(self):
        """Test extraction when fewer than 5 digits available."""
        assert extract_last_five_digits("123") == 123


@pytest.mark.skipif(not TENSEAL_AVAILABLE, reason="tenseal not installed")
class TestMainWithMockFiles:
    """Test the main function with mock files."""

    @pytest.fixture
    def setup_test_environment(self):
        """Create a temporary directory with mock test files."""
        # Create temporary directory
        test_dir = tempfile.mkdtemp()
        original_dir = os.getcwd()
        os.chdir(test_dir)

        # Create mock student-id.txt
        with open("student-id.txt", "w") as f:
            f.write("41173058H")

        # Create download subdirectory
        download_dir = os.path.join(test_dir, "download")
        os.makedirs(download_dir, exist_ok=True)

        # Create a real BFV context and mock files
        context = ts.context(
            ts.SCHEME_TYPE.BFV, poly_modulus_degree=4096, plain_modulus=1032193
        )
        context.generate_galois_keys()
        context.generate_relin_keys()

        # Save public context in download directory
        public_context = context.serialize(save_secret_key=False)
        with open(os.path.join(download_dir, "public.key"), "wb") as f:
            f.write(public_context)

        # Create and save a mock ciphertext in download directory
        mock_value = ts.bfv_vector(context, [12345])
        with open(os.path.join(download_dir, "41173058H.tenseal"), "wb") as f:
            f.write(mock_value.serialize())

        yield test_dir

        # Cleanup
        os.chdir(original_dir)
        shutil.rmtree(test_dir)

    def test_main_success(self, setup_test_environment):
        """Test that main() successfully creates the output file."""
        result = main()

        # Check that main returned success
        assert result == 0

        # Check that output file was created
        assert os.path.exists("41173058H_enc_result.tenseal")

        # Check that output file is not empty
        assert os.path.getsize("41173058H_enc_result.tenseal") > 0

    def test_main_missing_public_key(self, setup_test_environment):
        """Test that main() handles missing public.key gracefully."""
        os.remove(os.path.join("download", "public.key"))
        result = main()

        # Should return error code
        assert result == 1

    def test_main_missing_ciphertext(self, setup_test_environment):
        """Test that main() handles missing ciphertext file gracefully."""
        os.remove(os.path.join("download", "41173058H.tenseal"))
        result = main()

        # Should return error code
        assert result == 1


@pytest.mark.skipif(not TENSEAL_AVAILABLE, reason="tenseal not installed")
class TestCryptographicOperations:
    """Test cryptographic operations."""

    @pytest.fixture
    def context(self):
        """Create a test BFV context."""
        ctx = ts.context(
            ts.SCHEME_TYPE.BFV, poly_modulus_degree=4096, plain_modulus=1032193
        )
        ctx.generate_galois_keys()
        ctx.generate_relin_keys()
        return ctx

    def test_encrypt_student_number(self, context):
        """Test encrypting a student number."""
        student_number = 73058
        ciphertext = encrypt_student_number(context, student_number)

        # Decrypt to verify
        decrypted = ciphertext.decrypt()
        assert decrypted[0] == student_number

    def test_homomorphic_addition(self, context):
        """Test homomorphic addition of two ciphertexts."""
        value1 = 100
        value2 = 200

        ct1 = ts.bfv_vector(context, [value1])
        ct2 = ts.bfv_vector(context, [value2])

        result = perform_homomorphic_addition(ct1, ct2)

        # Decrypt to verify
        decrypted = result.decrypt()
        assert decrypted[0] == value1 + value2
