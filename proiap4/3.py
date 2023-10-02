# Create the filename
file_name = "exampleQ3.txt"

# Open the file 
with open(file_name, "w") as file:
    # Prompt the user to enter three lines of text
    lines = []
    for i in range(3):
        line = input("Enter line {}: ".format(i+1))
        lines.append(line)

    # Write each of the three lines 
    file.write("\n".join(lines))

# Print a message confirming that the file has been successfully 
print("File {} has been successfully created and written to.".format(file_name))

# Print the content of the file
with open(file_name, "r") as file:
    content = file.read()
    print("File content:")
    print(content)