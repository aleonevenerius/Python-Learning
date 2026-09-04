def main():
    name = input("Your name:")
    print(hello(name))
    
def hello(to="world"):
    #print("Hello, ", to)
    #return 
    return f"Hello, {to}"

if __name__ == "__main__":
    main()