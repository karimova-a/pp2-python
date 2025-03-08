def file_create():
    for i in range(26):
        file_name = chr(65 + i) + ".txt"
        with open(file_name, 'w') as file:
            file.write(f"This is file {file_name}")

file_create()