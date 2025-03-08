import os
def line_num(filee):
    if os.path.exists(filee):
        with open(filee, 'r') as file:
            lines = file.readlines()
            return len(lines)
    else:
        return f"The file '{filename}' does not exist."


      
filename = input("Enter the filename: ")
line_count = line_num(filename)
print(f"Number of lines in the file: {line_count}")
