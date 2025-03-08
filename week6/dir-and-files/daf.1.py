import os

def directories(path):
    return [i for i in os.listdir(path) if os.path.isdir(os.path.join(path, i))]

def files(path):
    return [i for i in os.listdir(path) if os.path.isfile(os.path.join(path, i))]

def boh_d_f(path):
    return os.listdir(path)


path = input("Enter the path: ")
    
if os.path.exists(path):
    print("\nDirectories:")
    directoriess = directories(path)
    for directory in directoriess:
        print(directory)
        
    print("\nFiles:")
    filess = files(path)
    for file in filess:
        print(file)
        
    print("\nAll items (Directories and Files):")
    both = boh_d_f(path)
    for item in both:
        print(item)
else:
    print("The specified path does not exist.")
