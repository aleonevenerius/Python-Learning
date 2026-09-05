with open("names.csv") as file:
    for line in file:
        row = line.rstrip().split(",") # Remove space strings and dividir using the character "," to separate elements to create a list
        print(f"{row[0]} is in {row[1]}")

print(row)
