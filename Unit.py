def main():
    x = int(input("What is x: "))
    print("x squared is ", square(x))

def square(n):
    return n + n # n**2
    
if __name__ == "__main__": # Garantindo que a função main() não seja chamada sempre.
    main()
    