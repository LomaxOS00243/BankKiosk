import unittest

from src import EmailValidator, generatePAC, IBAN_Validator, NameValidator, PhoneValidator, RegistrationNumGenerator


class Test_Registration(unittest.TestCase):
    def test_validate_email_True(self):
        validEmails = ["wowthis@gmail.com", "wow.thsi.cxs@gmail.con.con", "da@da.com"]
        for email in validEmails:
            self.assertEqual(EmailValidator.emailValid(email), True)

    def test_validate_email_False(self):
        validEmails = ["@as.ca", "wowthis@faf", "wowthis@faf."]
        for email in validEmails:
            self.assertEqual(EmailValidator.emailValid(email), False)

    def test_valid_PAC(self):
        self.assertEqual(generatePAC.generatePAC().__len__(), 8)
        self.assertEqual(generatePAC.generatePAC().isdigit(), True)

    def test_valid_IBAN(self):
        validIBANs = ["IE12ABCF12341234567891"]
        for IBAN in validIBANs:
            self.assertEqual(IBAN_Validator.IBANValid(IBAN), True)

    def test_invalid_IBAN(self):
        validIBANs = ["iE12ABCF12341234567891", "Ie12ABCF12341234567891", "IEABCF12341234567891", "IE1aABCF12341234567891", "IE12ABCF123412345678as1"]
        for IBAN in validIBANs:
            self.assertEqual(IBAN_Validator.IBANValid(IBAN), False)

    def test_valid_name(self):
        validNames = ["erick", "bob", "joe", "jim", "jimmy", "Ibrahim", "Mohanghanyriffter"]
        for name in validNames:
            self.assertEqual(NameValidator.nameValid(name), True)

    def test_invalid_name(self):
        invalidNames = ["as asa", "ad23x", "qq qs  qeq", "212", "qw#qwq", 1212, "a", "a" * 21, "aa "]
        for name in invalidNames:
            self.assertEqual(NameValidator.nameValid(name), False)

    def test_valid_phone(self):
        validPhone = ["+353872331212", "0872326565"]
        for phone in validPhone:
            self.assertEqual(PhoneValidator.phoneValid(phone), True)

    def test_invalid_phone(self):
        invalidPhone = ["3530872331212", "872326565"]
        for phone in invalidPhone:
            self.assertEqual(PhoneValidator.phoneValid(phone), False)

    def test_valid_Registration(self):
        validRegistration = ["ABC123456"]
        for reg in validRegistration:
            self.assertEqual(RegistrationNumGenerator.RegistrationValid(reg), True)

    def test_invalid_RegistrationNum(self):
        invalidRegistration = ["as", "121", "ABC1234567", "ABC12345", "ABC12345678", "ABC12345s"]
        for reg in invalidRegistration:
            self.assertEqual(RegistrationNumGenerator.RegistrationValid(reg), False)

    def test_valid_registrationGen(self):
        self.assertEqual(RegistrationNumGenerator.RegistrationGen().__len__(), 9)
        self.assertEqual(RegistrationNumGenerator.RegistrationGen().isalnum(), True)

if __name__ == "__main__":
    unittest.main()
