import os
def copyfile(file1, file2):
    if os.path.exists(file1):
        with open(file1, 'r') as file1:
            with open(file2, 'w') as file2:
                lines = file1.read()
                file2.write(lines)
        print("copied")
    else:
        print(f"The file does not exist.")


    
   
file1 = input("Enter the first file: ")
file2 = input("Enter the second file: ")
    
    
copyfile(file1, file2)
