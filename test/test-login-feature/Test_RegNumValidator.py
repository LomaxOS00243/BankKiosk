import unittest
import RegNumValidation

class Test_Registration_Validator(unittest.TestCase):

    def test_valid_Registration(self):
        validRegistration = ["ABC123456"]
        for reg in validRegistration:
            self.assertEqual(RegNumValidation.validateRegNum(reg), True)

    def test_invalid_Registration(self):
        invalidRegistration = ["as", "121", "ABC1234567", "ABC12345", "ABC12345678", "ABC12345s"]
        for reg in invalidRegistration:
            self.assertEqual(RegNumValidations.validateRegNum(reg), False)

if __name__ == "__main__":
    unittest.main()