import unittest
import PhoneValidator

class Test_Phone_Validator(unittest.TestCase):

    def test_valid_phone(self):
        validPhone = ["+353872331212", "0872326565"]
        for phone in validPhone:
            self.assertEqual(PhoneValidator.phoneValid(phone), True)

    def test_invalid_phone(self):
        invalidPhone = ["3530872331212", "872326565"]
        for phone in invalidPhone:
            self.assertEqual(PhoneValidator.phoneValid(phone), False)


if __name__ == "__main__":
    unittest.main()