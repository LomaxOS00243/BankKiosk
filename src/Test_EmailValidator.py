import unittest
import EmailValidator

class Test_EmailValidator(unittest.TestCase):
    def test_valid_email(self):
        validEmails = ["wowthis@gmail.com", "wow.thsi.cxs@gmail.con.con", "da@da.com"]
        for email in validEmails:
            self.assertEqual(EmailValidator.emailValid(email), True)

    def test_inValid_email(self):
        validEmails = ["@as.ca", "wowthis@faf", "wowthis@faf."]
        for email in validEmails:
           self.assertEqual(EmailValidator.emailValid(email), False)


if __name__ == "__main__":
    unittest.main()

    