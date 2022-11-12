import unittest
import IBAN_Validator

class Test_IBAN_Validator(unittest.TestCase):

    def test_valid_IBAN(self):
        validIBANs = ["IE12ABCF12341234567891"]
        for IBAN in validIBANs:
            self.assertEqual(IBAN_Validator.IBANValid(IBAN), True)

    def test_invalid_IBAN(self):
        validIBANs = ["iE12ABCF12341234567891", "Ie12ABCF12341234567891", "IEABCF12341234567891", "IE1aABCF12341234567891", "IE12ABCF123412345678as1"]
        for IBAN in validIBANs:
            self.assertEqual(IBAN_Validator.IBANValid(IBAN), False)


if __name__ == "__main__":
    unittest.main()