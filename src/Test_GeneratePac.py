import unittest
import generatePAC

class Test_GeneratePAC(unittest.TestCase):

    def test_valid_PAC(self):
        self.assertEqual(generatePAC.generatePAC().__len__(), 8)
        self.assertEqual(generatePAC.generatePAC().isdigit(), True)


if __name__ == "__main__":
    unittest.main()
