def write_list(filename, list):
    with open(filename, 'w') as file:
        for i in list:
            file.write(f"{i}\n")


n = int(input())
list = []
for i in range(n):
    s = input()
    list.append(s)
    
    
filename = input("Enter the filename to write the list to: ")
    
    
write_list(filename, list)
print(f"The list has been written to '{filename}'.")
