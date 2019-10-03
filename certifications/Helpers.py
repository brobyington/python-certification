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
        final_str = ""

        if number < Helpers.ten:
            print(str(number) + " - " + Helpers.zero_to_nine[number])
        elif number >= Helpers.ten and number < Helpers.hundred:
            final_str = Helpers.tens(self,number)
            print(str(number) + " - " + final_str)
        elif number >= Helpers.hundred and number < Helpers.thousand:
            final_str = Helpers.hundreds(self,number)
            print(str(number) + " - " + final_str)
        elif number >= Helpers.thousand and number < Helpers.ten_thousand:
            final_str =  Helpers.thousands(self, number)
            print(str(number) + " - " + final_str)
        elif number >= Helpers.ten_thousand and number < Helpers.hundred_thousand:
            final_str =  Helpers.ten_thousands(self, number)
            print(str(number) + " - " + final_str)
        elif number >= Helpers.hundred_thousand and number < Helpers.million:
            final_str = Helpers.hundred_thousands(self,number)

    def tens(self,number):
        ret_str = ""
        num_str = [int(i) for i in str(number)]
        if number >= Helpers.ten and number < Helpers.twenty:
            new_num = number - Helpers.ten
            return Helpers.ten_to_19[new_num]
        elif number >= Helpers.twenty and number < Helpers.hundred:
            if num_str[1] == 0:
                new_str = Helpers.by_tens[num_str[0]]
                ret_str = ret_str + new_str
                return ret_str
            else:
                new_str = Helpers.by_tens[num_str[0]] + " " + Helpers.zero_to_nine[num_str[1]]
                ret_str = ret_str + new_str
                return ret_str

    def hundreds(self,number):
        num_str = [int(i) for i in str(number)]
        new_num = str(number)
        pass_tens = int(new_num[1:3])
        hundred_num = Helpers.zero_to_nine[num_str[0]]
        ret_str = " " + hundred_num + " Hundred "
        if num_str[1] == 1:
           new_str = Helpers.tens(self,pass_tens)
           ret_str = ret_str + new_str
           return ret_str
        elif num_str[2] == 0:
            new_str = Helpers.by_tens[num_str[1]]
            ret_str = ret_str + new_str
            return ret_str
        else:
            new_str = (Helpers.by_tens[num_str[1]] + " " + Helpers.zero_to_nine[num_str[2]])
            ret_str = ret_str + new_str
            return ret_str

    def thousands(self,number):
        num_str = [int(i) for i in str(number)]
        new_num = str(number)
        pass_huns = int(new_num[1:4])
        pass_tens = int(new_num[2:4])
        thousand_num = Helpers.zero_to_nine[num_str[0]]
        ret_str = " " + thousand_num + " thousand "

        if num_str[1] == 0:
            if num_str[2] == 1:
                new_str = Helpers.tens(self, pass_tens)
                ret_str = ret_str + new_str
                return ret_str
            elif num_str[3] == 0:
                new_str = Helpers.by_tens[num_str[2]]
                ret_str = ret_str + new_str
                return ret_str
            else:
                new_str = (Helpers.by_tens[num_str[2]] + " " + Helpers.zero_to_nine[num_str[3]])
                ret_str = ret_str + new_str
                return ret_str
        else:
            new_str = Helpers.hundreds(self, pass_huns)
            ret_str = ret_str + new_str
            return ret_str

    def ten_thousands(self,number):
        num_str = [int(i) for i in str(number)]
        new_num = str(number)
        pass_thous = int(new_num[1:5])
        pass_huns = int(new_num[2:5])
        pass_tens = int(new_num[3:5])
        if num_str[0] == 1:
            thousand_num = Helpers.ten_to_19[num_str[1]]
            ret_str = " " + thousand_num + " thousand "
        elif num_str[1] == 0:
            thousand_num = Helpers.by_tens[num_str[0]]
            ret_str = " " + thousand_num + " thousand "
        else:
            thousand_num = Helpers.by_tens[num_str[0]]
            sec_num = Helpers.zero_to_nine[num_str[1]]
            ret_str = " " + thousand_num + " " + sec_num + " thousand "

        if num_str[2] == 0:
            if num_str[3] == 1:
                new_str = Helpers.tens(self, pass_tens)
                ret_str = ret_str + new_str
                return ret_str
            elif num_str[4] == 0:
                new_str = Helpers.by_tens[num_str[3]]
                ret_str = ret_str + new_str
                return ret_str
            else:
                new_str = (Helpers.by_tens[num_str[3]] + " " + Helpers.zero_to_nine[num_str[4]])
                ret_str = ret_str + new_str
                return ret_str
        else:
            new_str = Helpers.hundreds(self, pass_huns)
            ret_str = ret_str + new_str
            return ret_str

    def hundred_thousands(self, number):
        num_str = [int(i) for i in str(number)]
        new_num = str(number)
        pass_thous = int(new_num[2:6])
        pass_huns = int(new_num[3:6])
        pass_tens = int(new_num[4:6])