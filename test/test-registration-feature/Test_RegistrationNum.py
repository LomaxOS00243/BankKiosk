import unittest
import RegistrationNumGenerator as rgn

class Test_Registration_Validator(unittest.TestCase):

    def test_valid_Registration(self):
        validRegistration = ["ABC123456"]
        for reg in validRegistration:
            self.assertEqual(rgn.RegistrationValid(reg), True)

    def test_invalid_Registration(self):
        invalidRegistration = ["as", "121", "ABC1234567", "ABC12345", "ABC12345678", "ABC12345s"]
        for reg in invalidRegistration:
            self.assertEqual(rgn.RegistrationValid(reg), False)

    def test_valid_registration(self):
        self.assertEqual(rgn.RegistrationGen().__len__(), 9)
        self.assertEqual(rgn.RegistrationGen().isalnum(), True)
       

if __name__ == "__main__":
    unittest.main()