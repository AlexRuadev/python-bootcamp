f = open('practice.txt','w+')
f.write('this is a test string')
f.close()

import os

# get the current working directory
a = os.getcwd()
print(a)
# list items in a directory
b = os.listdir()
print(b)

# list items in a specific directory (users)
b = os.listdir('C:\\Users')
print(b)

#  Moving files in different location. Moving our practice file from 14folder to python-bootcamp folder
import shutil
# shutil.move('practice.txt', 'C:\\xampp\\htdocs\\python-bootcamp\\')

# Will put deleted files   in the trash
import send2trash
send2trash.send2trash('practice.txt')

# using os.walk
file_path= 'C:\\xampp\\htdocs\\python-bootcamp\\toplevel'

for folder, sub_folders, files in os.walk(file_path):

    print(f"Currently looking at {folder}")
    print("\n")
    print(f"The subfolders are: ")
    for sub_fold in sub_folders:
        print(f"\t Subfolder: {sub_fold}")

    print("\n")
    print(f"The files are: ")
    for f in files:
        print(f"\t files: {f}")

    print("\n")



