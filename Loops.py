"""
i = 0
while i < 3:
    print("meow")
    i += 1

for i in [0,1,2]:
    print(i)
    print("meow")
# List
for _ in range(3):
    print("meow")

print("meow\n"*3)
""
def main():
    number = getNumber()
    meow(number)

def getNumber():
    while True:
        a = int(input("Number, please: "))
        if a > 0:
            break
            
    return a
            
def meow(a):
    for _ in range(a):
        print("Meow")
        
        
main()


#students = ["Harry", "Hermione", "Ron"]

#for students in students: # You can code like this if you don't know list's size
#   print(students)

#for _ in range(len(students)):
 #   print(_, students[_])

#students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Draco": "Syltherin",
}
print(students)
#print(students["Hermione"])

for student in students:
    print(student, students[student], sep=", ")
"""

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrir"},
    {"name": "Draco", "house": "Slyytherin", "patronus": None}
]

# None: type of date
for student in students:
    print(student["name"],student["house"],student["patronus"], sep=", ")