# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calculator():

    method = input("What method would you like to use? (add, sub, mult, div) ")
    number_one = input("What is number one? ")
    number_two = input("What is number two? ")
    if method == "add":
        return int(number_one) + int(number_two)
    elif method == "sub":
        return int(number_one) - int(number_two)
    elif method == "mult":
        return int(number_one) * int(number_two)
    elif method == "div":
        return int(number_one) / int(number_two)
    else:
        return "Method unrecognized"

print(calculator());
