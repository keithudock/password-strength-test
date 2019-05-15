import unittest, re

class TestPassword(unittest.TestCase):

    def testing(self):
        numRegex = re.compile(r'''(
        .*[0-9]{1,}.*
        )''',re.VERBOSE)

        capRegex = re.compile(r'''(
        .*[A-Z]{1,}.*
        )''',re.VERBOSE)

        lowerRegex = re.compile(r'''(
        .*[a-z].*
        )''',re.VERBOSE)

        password = 'password1R'

        if len(password) >= 8:
            if numRegex.search(password) is not None:
                if capRegex.search(password) is not None:
                    if lowerRegex.search(password) is not None:
                        passBool = True
                    else:
                        passBool = False
                else:
                    passBool = False
            else:
                passBool = False
        else:
            passBool = False

        self.assertTrue(passBool)

if __name__ == '__main__':
    unittest.main()
    