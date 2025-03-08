import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print("The file has been deleted")
        else:
            print("The file is not writable ")
    else:
        print("The file does not exist.")


path = input("Enter the file path to delete: ")
    
    
delete_file(path)
