from pyfiglet import figlet_format
from requests import get
from random import choice
from termcolor import colored

url="https://icanhazdadjoke.com/search"
another=""

while another!="N" and another!="n":
    title=figlet_format("Dad jokes!")
    title=colored(title,color="magenta")
    print(title)
    param=input("Give me a topic: ")          
    try:
        response=get(
            url,
            headers={"Accept":"application/json"},  #read the website API documentation
            params={"term":param}
        ).json()
        
        quantity=response["total_jokes"]
        rand_joke=choice(response["results"])
        joke_only=rand_joke["joke"]
        print(f"I've got {quantity} joke(s) about {param}. Here's one:\n{joke_only}")            
    except IndexError:
        print(f"I don't know any jokes on {param}")
    another=input("Another? Y/N: ")
print("Jokes on you, then")
