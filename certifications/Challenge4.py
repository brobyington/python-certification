import unittest
from certifications.Helpers import Helpers
from num2words import num2words



class Challenge4(unittest.TestCase):

    def test_challenge4(self):
        helper = Helpers()
        # i = 1300
        # while i < 1401:
        #
        #     helper.convert_to_word(i)
        #     i += 1

        # for i in range(9):
        #     print(str(helper.fibonacci(i))+ " - " + num2words(helper.fibonacci(i)))
        helper.convert_to_word(helper.fibonacci(23))


    if __name__ == '__main__':
     unittest.main()