#                                               SyntaxeError
# ValueError
def main():
    x = getInt()
    print(x)

def getInt():
    while True:
        try:
            x = int(input("The value of x: "))
        except ValueError:
            #print("Tell me a int number!")
            pass
        else:
            #break # Don't need
            return x
    
main()