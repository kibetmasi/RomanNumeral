from collections import OrderedDict #OrderedDict is a dictionary subclass that remembers the orders in which its contents are added

def convert_to_roman(num):
   
    #this function takrs in an integer and returns its Roman equivalent
    roman = OrderedDict()
    roman[1000] = "M"
    roman[500] = "D"
    roman[100] = "C"
    roman[50] = "L"
    roman[10] = "X"
    roman[5] = "V"
    roman[1] = "I"

    def roman_number(num):
        for i in roman.keys(): #keys because of orderedDict
            x, y = divmod(num, i)
            yield roman[i] * x
            num -= (i * x)
            if num <= 0:
                break
    
    return "".join([a for a in roman_number(num)])

    
num = int(input("Enter number: "))
print(convert_to_roman(num))