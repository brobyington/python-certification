import unittest
from certifications.Helpers import Helpers
from num2words import num2words



class Challenge4(unittest.TestCase):

    def test_challenge4(self):
        helper = Helpers()
        cont_val = ""
        while(cont_val.upper() != "N"):
            value = input("What number in the fibonacci sequence do you want? ")
            try:
                helper.convert_to_word(helper.fibonacci(int(value)))
            except ValueError:
                print("Input isn't a number ")
            cont_val= input("Want to enter another value? Y or N? ")
            while cont_val.upper() != "Y" and cont_val.upper() != "N":
                cont_val = input("Invalid response, enter Y or N please! ")


    if __name__ == '__main__':
     unittest.main()