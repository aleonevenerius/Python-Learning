"""
print("What is your name?")
input("Tell me your name: ")

# Variables
name = input("Tell me your name: ").strip().title()
#name = name.strip().title() # Remove whitespace from str
#name = name.capitalize() # Capitalize user's name
#name = name.title()

# Split user's name into first name and last name
first, last = name.split(" ") # " " it'll cut the two viariable apartir of.

print(f"Hello, {first}") # You can use the "+" caractere instead of ","
print(f"Hello, mr(s). {last}!")

print("Hi, 'friend'")
print("Hi, \"friend\"") # Escape Caractere
"""
"""
+
-
/
*
% = resto division

x = int(input("What is the value of x?"))                     
y = int(input("What is the value of y?"))

print(x+y)

#print(int(input("What's x?: ")) + int(input("What's y?: ")))

# Float
x = float(input("What is the value of x?")) # 999        
y = float(input("What is the value of y?")) # 1

#z = round(x+y)

#z = round(x/y, 2)

z = x/y
print(f"{z:.2f}") # 1,000

# Def(fine) function

def Main():
    name = input("Tell me your name, please: ")
    Hello(name) #Hello() # Error in the future.
    
 
#Main() # It'll be an error!
def Hello(to="World"):
    print(f"Hello, {to}")

Main()
"""

def main():
    x = int(input("Value of x: "))
    print(f"x squared is: {square(x)}")
    
def square(n):
    return n**2 # Or "pow(n,2)"
main()
