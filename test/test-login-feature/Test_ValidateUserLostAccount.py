import unittest
import ValidateUserLostAccount

class Test_Registration_Validator(unittest.TestCase):

    def test_valid_LostAccount(self):
        self.assertEqual(ValidateUserLostAccount.validateUserLostAccount("test", "test"), True)

    def test_invalid_LostAccount(self):
        self.assertEqual(ValidateUserLostAccount.validateUserLostAccount("test", 1212), False)


if __name__ == "__main__":
    unittest.main()