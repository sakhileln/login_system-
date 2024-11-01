"""
Test cases for the login system module.
"""

from password_validator import (
    check_length,
    check_case,
    check_digit,
    check_punctuation,
    is_secure,
)
from username_validator import check_length_user
import unittest


class TestLoginSystem(unittest.TestCase):
    """
    Test cases for modules
    """

    def test_short_password(self):
        """
        Test short password
        """
        self.assertFalse(check_length("short"))

    def test_long_passowrd(self):
        """
        Test long password
        """
        self.assertTrue("longpassword")

    def test_only_lowercase(self):
        """
        Test lowercase password
        """
        self.assertEqual(check_case("lowercase"), False)

    def test_only_uppercase(self):
        """
        Test uppercase password.
        """
        self.assertEqual(check_case("UPPERCASE"), False)

    def test_mix_case(self):
        """
        Test uppercase and lowercase
        """
        self.assertEqual(check_case("miXcAsE"), True)

    def test_no_digit(self):
        """
        Test password without a digit
        """
        self.assertEqual(check_digit("nodigit"), False)

    def test_with_digit(self):
        """
        Test password with digit
        """
        self.assertEqual(check_digit("withdigit9"), True)

    def test_no_punctuation(self):
        """
        Test password without special characters.
        """
        self.assertEqual(check_punctuation("nopunctuation"), False)

    def test_spaces_check(self):
        """
        Test for password with spaces.
        """
        self.assertEqual(check_punctuation("with spaces "), False)

    def test_with_punctuation(self):
        """
        Test for password with punctuation
        """
        self.assertEqual(check_punctuation("with!punc%tuation@"), True)

    def test_not_sucure(self):
        """
        Test not secure password
        """
        self.assertFalse(is_secure("No#t Secu!r3"))

    def test_secure_pasword(self):
        """
        Test secure password
        """
        self.assertTrue(is_secure("sEcur3p@W0rd"))

    def test_short_usernames(self):
        """
        Test short username
        """
        self.assertEqual(check_length_user("sl"), False)

    def test_long_username(self):
        """
        Test long username
        """
        self.assertFalse(check_length_user("abcdefghijklmnopqrstuvxyz"))

    def test_valid_length_username(self):
        """
        Test valid valid length password
        """
        self.assertTrue(check_length_user("sakhile"))


if __name__ == "__main__":
    unittest.main()
