import random # Import everything about random
import statistics
import sys # System
import cowsay
import requests
#from random import choice
"""
coin = random.choice(["cara", "coroa"])#choice(["cara", "coroa"])
print(coin)

n = random.randint(1,10)
print(n)

cards = ["jack", "queen", "king"]

for card in cards:
    random.shuffle(cards)
    print(cards)
    
#                                                   Statistics
print(statistics.mean([7, 5.5, 3, 6, 9])) # 6.1

#                       Sys
try:
    print("Hello, my name is ", sys.argv[0]) #0 represents the name of file and 1 is your input at command's list
except indexError:
    print("There was a lot of arguments")
    
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    print("There is a lot of arguments")
print("Hello, my name is", sys.argv[1])
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv:
    print("Hello, my name is", arg)

name = input("Tell me your name: ")
cowsay.trex("Hello, ", name) # or cow
"""
#a = input("")#sys.argv(input("")
#print(len(a))
if len(sys.argv) != 2:
    sys.exit("Quantidade incorreta") # Interromper a execução do programa.
    # break é usada para loops 

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term="+ sys.argv[1]) # 'get' logra uma resposta do servidor
o = response.json()
for result in o["results"]:
    print(result["trackName"])