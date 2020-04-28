from pyfiglet import figlet_format
from termcolor import colored

msg=input("What would you like to print? ")
colour=input("Choose a colour: red, green, yellow, blue, magenta, cyan, white\n")

while colour not in ("red","green","yellow","blue","magenta","cyan","white"):
        print("Invalid colour")
        colour=input("Choose a colour: red, green, yellow, blue, magenta, cyan, white\n")
ascii_art=figlet_format(msg)
coloured_ascii=colored(ascii_art,color=colour)
print(coloured_ascii)


