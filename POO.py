import sys

class Students:
    def __init__(self, name, house): # Method is just a function indoors of a class. This method is a initicialize method
        if not name:
            raise ValueError("Missing name") # Solve a except
        if house not in ["Gryffindor", "Mufflepuff", "Ravenclow", "Slytherin"]:
            raise ValueErroreErro("Invalid house")
        self.n = name # Atribute AKA instance variable
        self.h = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    try:
        return Students(name, house) # Contructor = Instanciar
    

if __name__ == "__main__":
    main()
