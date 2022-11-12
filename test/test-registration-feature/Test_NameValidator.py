import unittest
import NameValidator 

class Test_IBAN_Validator(unittest.TestCase):

    def test_valid_name(self):
        validNames = ["erick", "bob", "joe", "jim", "jimmy", "Ibrahim", "Mohanghanyriffter"]
        for name in validNames:
            self.assertEqual(NameValidator.nameValid(name), True)

def test_invalid_name(self):
        invalidNames = ["as asa", "ad23x", "qq qs  qeq", "212", "qw#qwq", 1212, "a", "a" * 21, "aa "]
        for name in invalidNames:
            self.assertEqual(NameValidator.nameValid(name), False)


if __name__ == "__main__":
    unittest.main()