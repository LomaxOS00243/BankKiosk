import unittest
import RegNumValidation
from Login.src import SendEmailCode, ValidateEmailCode, ValidatePAC, ValidateUserLostAccount


class Test_Registration_Validator(unittest.TestCase):

    def test_valid_Registration(self):
        validRegistration = ["ABC123456"]
        for reg in validRegistration:
            self.assertEqual(RegNumValidation.validateRegNum(reg), True)

    def test_invalid_Registration(self):
        invalidRegistration = ["as", "121", "ABC1234567", "ABC12345", "ABC12345678", "ABC12345s"]
        for reg in invalidRegistration:
            self.assertEqual(RegNumValidation.validateRegNum(reg), False)

    def test_generate_Code(self):
        self.assertEqual(SendEmailCode.generate_code("azureTeamKiosk@gmail.com").__len__(), 8)
        self.assertEqual(SendEmailCode.generate_code("azureTeamKiosk@gmail.com").isdigit(), True)

    def test_Email_Sent(self):
        usercodes = "ABC123456"
        sentcodes = 1212
        self.assertEqual(SendEmailCode.send_content_to_email("azureTeamKiosk@gmail.com", "hello"), True)

    def test_valid_EmailCode(self):
        usercodes = "ABC123456"
        sentcodes = "ABC123456"
        self.assertEqual(ValidateEmailCode.validateEmailCode(usercodes, sentcodes), True)

    def test_invalid_EmailCode(self):
        usercodes = "ABC123456"
        sentcodes = 1212
        self.assertEqual(ValidateEmailCode.validateEmailCode(usercodes, sentcodes), False)

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

    def test_valid_LostAccount(self):
        self.assertEqual(ValidateUserLostAccount.validateUserLostAccount("test", "test"), True)

    def test_invalid_LostAccount(self):
        self.assertEqual(ValidateUserLostAccount.validateUserLostAccount("test", 1212), False)


if __name__ == "__main__":
    unittest.main()