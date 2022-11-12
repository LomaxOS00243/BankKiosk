import unittest
import ValidateEmailCode

class Test_EmailCode_Validator(unittest.TestCase):

    def test_valid_EmailCode(self):
        usercodes = "ABC123456"
        sentcodes = "ABC123456"
        self.assertEqual(ValidateEmailCode.validateEmailCode(usercodes, sentcodes), True)

    def test_invalid_EmailCode(self):
        usercodes = "ABC123456"
        sentcodes = 1212
        self.assertEqual(ValidateEmailCode.validateEmailCode(usercodes, sentcodes), False)

if __name__ == "__main__":
    unittest.main()