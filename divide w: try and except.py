def divide(num1,num2):
    try:
        return num1/num2
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"

#if only one argument is passed => TypeError
#Python doesn't enter the body of the function w/o the 2 positional arguments

#source: https://stackoverflow.com/questions/61405090/why-do-i-get-a-typeerror-if-i-pass-only-one-argument?noredirect=1#comment108626086_61405090
