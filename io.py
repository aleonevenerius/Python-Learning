'''
names = []

for _ in range(3):
    names.append(input("Name: "))

for name in sorted(names):
    print(f"Hello, {name}")
'''
#name = input("Name: ")

'''
file = open("C:/Users/alexa/OneDrive/Documents/Programação/Aprendendo/names.txt", "a")
file.write(f"{name}\n")
file.close()
'''

# This function opens and closes the files
#with open("C:/Programming/Learning/names.txt", "a") as file: # w = write; a = append
    #file.write(f"{name}\n")

with open("C:/Programming/Learning/names.txt", "r") as file:
    #lines = file.readlines() # Read all file's lines and return a list.
    for line in file:
        print("Hello,", line.rstrip()) # rstrip => right(end); lstrip => left(begining)