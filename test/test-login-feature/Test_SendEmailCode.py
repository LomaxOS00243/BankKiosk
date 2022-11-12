import unittest
import SendEmailCode

class Test_EmailCode_Validator(unittest.TestCase):

    def test_generate_Code(self):
        self.assertEqual(SendEmailCode.generate_code("azureTeamKiosk@gmail.com").__len__(), 8)
        self.assertEqual(SendEmailCode.generate_code("azureTeamKiosk@gmail.com").isdigit(), True)

    def test_Email_Sent(self):
        usercodes = "ABC123456"
        sentcodes = 1212
        self.assertEqual(SendEmailCode.send_content_to_email("azureTeamKiosk@gmail.com", "hello"), True)

if __name__ == "__main__":
    unittest.main()