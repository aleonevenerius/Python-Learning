"""
>
>=
<
<=
==
!=

x = int(input("Tell me a value to x: "))
y = int(input("Tell me a value to y: "))

if x > y:
    print(f"{x} is greater than {y}")
    
elif x < y:
    print(f"{x} is less than {y}")
if x!=y: #x<y or x>y: 
    print(f"{x} isn't equal to {y}")
else:
    print(f"{x} is equal to {y}")
    
    
""
    
score = float(input("Score: "))

if 100 >= score >= 90:
    print("Grade A")
elif 90 >= score >= 80:
    print("Grade B")
elif 80 >= score >= 70:
    print("Grade C")
else:
    print("Grade F")
    


def main():
    x = int(input("Tell me a int number, please: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n%2==0
    #if n%2 == 0: # return True if n % 2 == 0 else False
       # return True
    #else:
     #   return False
        
main()
"""

name = input("Tell me your name: ")

match name:
    case "Harry" | "Ron" | "Hermione":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")