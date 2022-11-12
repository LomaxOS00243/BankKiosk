import unittest
import ValidatePAC

class Test_PAC_Validator(unittest.TestCase):

    def test_valid_PAC(self):
        validPAC = ["12345678", "12345679", "12345670", "12345671", "12345672", "12345673", "12345674", "12345675", "12345676", "12345677"]
        for PAC in validPAC:
            self.assertEqual(ValidatePAC.validatePAC(PAC), True)

    def test_invalid_PAC(self):
        invalidPAC = ["a2345678", "1234567", "123456782", "1234567a", "1234567A", "1234567!", "1234567@", "1234567#", "1234567$", "1234567%", "1234567^", "1234567&", "1234567*", "1234567(", "1234567)", "1234567-", "1234567_", "1234567+", "1234567=", "1234567{", "1234567}", "1234567[", "1234567]", "1234567|", "1234567\\", "1234567:", "1234567;", "1234567'", "1234567\"", "1234567<", "1234567>", "1234567,", "1234567.", "1234567?", "1234567/", "1234567`", "1234567~"]
        for PAC in invalidPAC:
            self.assertEqual(ValidatePAC.validatePAC(PAC), False)

    def test_generate_PAC(self):
        self.assertEqual(ValidatePAC.generatePAC().__len__(), 8)
        self.assertEqual(ValidatePAC.generatePAC().isdigit(), True)


if __name__ == "__main__":
    unittest.main()