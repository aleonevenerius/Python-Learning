import os
'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
'''

'''
f = open("File.txt")
print(f.read()) # read() to reading the file
f.close() # It closes your file 
# In some cases, changes may not show until you close the file. Consequentely, you should always close them
'''
#with open("File.txt") as f: # You don't hava to be unsettled about closing your files.
#    print(f.read()) # it specifys how many characters you want to return
'''
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content
'''
'''
with open("File.txt", "w") as f:
    f.write("\nI just singing in the rain!")

with open("File.txt") as f:
    print(f.read())
''
try:
    f = open("myfile.txt", "x") # Create - will create a file, returns an error if the file exists
except:
    print("Ops! This file exists.")
else:
    print("Nothing wrong at the moment!")

'''
f = input("Inform a file name: ")
if os.path.exists(f+".txt"):
    os.remove(f+".txt")
else:
    print("It doesn't exist!")
try:
    os.rmdir("Folder")
except:
    print("It doesn't exist")
else:
    print("Fine")
