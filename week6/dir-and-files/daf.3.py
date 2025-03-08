import os

def check(path):
    if os.path.exists(path):
        print("The path exists.")
        
        directory = os.path.dirname(path)
        print(f"Directory: {directory}")
        
    
        filename = os.path.basename(path)
        print(f"Filename: {filename}")
    else:
        print(f"The path does not exist.")


path = input("Enter path: ")
check(path)
