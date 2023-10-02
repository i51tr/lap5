# Create the "studentData.txt" file with the given content
file_name = "studentData.txt"
file_content = """Nada 123
Meto 234
lelo 345
Maha 678"""

with open(file_name, "w") as file:
    file.write(file_content)

# Open the "studentData.txt" file in read mode
with open(file_name, "r") as file:
    # Read the content of the file line by line and store each line in a list
    names_list = file.read().splitlines()

# Print the contents of the names_list to the console
for line in names_list:
    print(line)