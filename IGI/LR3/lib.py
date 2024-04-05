def int_input ():
    while True:
        try:
            num=int(input("Input integer number"))
            return num
        except ValueError:
            print("Error in input number")

def float_input ():
    while True:
        try:
            float_num = float(input("Input float number"))
            return float_num
        except ValueError:
            print("Error in input number")




