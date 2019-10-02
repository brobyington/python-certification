from num2words import num2words

class Helpers():
    num_str = []
    ten = 10
    twenty = 20
    hundred = 100
    thousand = 1000
    ten_thousand = 10000
    hundred_thousand = 100000
    million = 1000000
    zero_to_nine = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', ]
    ten_to_19 = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen',
                 'Nineteen']
    by_tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

    def fibonacci(self, number):
        if number == 1:
            return 0
        elif number == 2:
            return 1
        else:
            return (self.fibonacci(number - 1) + self.fibonacci(number - 2))

    def convert_to_word(self,number):
        num_str = [int(i) for i in str(number)]


        if number < Helpers.ten:
            print(str(number) + " - " + Helpers.zero_to_nine[number])
        elif number >= Helpers.ten and number < Helpers.hundred:
            Helpers.tens(self,number)
        elif number >= Helpers.hundred and number < Helpers.thousand:
            Helpers.hundreds(self,number)
        elif number >= Helpers.thousand and number < Helpers.ten_thousand:
            Helpers.thousands(self, number)
        elif number >= Helpers.ten_thousand and number < Helpers.hundred_thousand:
            if num_str[0] == 1:
                if num_str[3] == 1:
                    print(str(number) + " - " + Helpers.ten_to_19[num_str[1]] + " Thousand " + Helpers.zero_to_nine[num_str[2]] + " Hundred " + Helpers.ten_to_19[num_str[3]])
                elif num_str[3] == 0:
                    print(str(number) + " - " + Helpers.ten_to_19[num_str[1]] + " Thousand " + Helpers.zero_to_nine[num_str[2]] + " Hundred " + Helpers.by_tens[num_str[3]])
                else:
                    print(str(number) + " - " + Helpers.ten_to_19[num_str[1]] + " Thousand " + Helpers.zero_to_nine[num_str[2]] + " Hundred " + Helpers.by_tens[num_str[3]] + " " + Helpers.zero_to_nine[num_str[4]] )

    def tens(self,number):

        num_str = [int(i) for i in str(number)]
        if number >= Helpers.ten and number < Helpers.twenty:
            new_num = number - Helpers.ten
            print(str(number) + " - " + Helpers.ten_to_19[new_num])
        elif number >= Helpers.twenty and number < Helpers.hundred:
            if num_str[1] == 0:
                print(str(number) + " - " + Helpers.by_tens[num_str[0]])
            else:
                print(str(number) + " - " + Helpers.by_tens[num_str[0]] + " " + Helpers.zero_to_nine[num_str[1]])

    def hundreds(self,number):
        num_str = [int(i) for i in str(number)]

        if num_str[1] == 1:
            print(str(number) + " - " + Helpers.zero_to_nine[num_str[0]] + " Hundred " + Helpers.ten_to_19[num_str[2]])
        elif num_str[2] == 0:
            print(
                str(number) + " - " + Helpers.zero_to_nine[num_str[0]] + " Hundred " + Helpers.by_tens[num_str[1]])
        else:
            print(str(number) + " - " + Helpers.zero_to_nine[num_str[0]] + " Hundred " + Helpers.by_tens[
                num_str[1]] + " " + Helpers.zero_to_nine[num_str[2]])

    def thousands(self,number):
        num_str = [int(i) for i in str(number)]
        if num_str[1] == 0:
            if num_str[2] == 1:
                print(str(number) + " - " + Helpers.zero_to_nine[num_str[0]] + " Thousand " +
                      Helpers.ten_to_19[num_str[3]])
            elif num_str[3] == 0:
                print(str(number) + " - " + Helpers.zero_to_nine[num_str[0]] + " Thousand " +
                      Helpers.by_tens[num_str[2]])
            else:
                print(str(number) + " - " + Helpers.zero_to_nine[num_str[0]] + " Thousand " +
                      Helpers.by_tens[num_str[2]] + " " + Helpers.zero_to_nine[num_str[3]])
        elif num_str[2] == 1:
            print(str(number) + " - " + Helpers.zero_to_nine[num_str[0]] + " Thousand " + Helpers.zero_to_nine[
                num_str[1]] + " Hundred " + Helpers.ten_to_19[num_str[3]])
        elif num_str[3] == 0:
            print(str(number) + " - " + Helpers.zero_to_nine[num_str[0]] + " Thousand " + Helpers.zero_to_nine[
                num_str[1]] + " Hundred " + Helpers.by_tens[num_str[2]])

        else:
            print(str(number) + " - " + Helpers.zero_to_nine[num_str[0]] + " Thousand " + Helpers.zero_to_nine[
                num_str[1]] + " Hundred " + Helpers.by_tens[num_str[2]] + " " + Helpers.zero_to_nine[num_str[3]])