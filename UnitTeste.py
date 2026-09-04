import pytest
from Unit import square # Making it, the importation, easer to import the function square
'''
def main():
    test_square()
    
def test_square():
        ''
        if square(2) != 4:
        print("2 doesn't 4")
        if square(3) != 9:
        print("3 doesn't 9")
        ''
        try:
            assert square(2) == 4
        except:
            print("2 doesn't equal to 4")
        try:
            assert square(3) == 9
        except:
            print("3 doesn't equal to 9")
        try:
            assert square(-2) == 4
        except:
            print("-2 doesn't equal to -4")
        try:
            assert square(-3) == -9
        except:
            print("-3 doesn't equal to -9")
              ''
if __name__ == "__main__":
    main()
'''
def positive_test_square():
    assert square(2) == 4
    assert square(3) == 9
def negative_test_square():
    assert square(-2) == 4
    assert square(-3) == 9
def zero():
    assert square(0) == 0
def test_str():
    with pytest.raises(TypeError):
        square("cat")
    #assert square("cat") == 0
# If the output is 'FF.' it's means "aproved"

