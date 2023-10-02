# Open the file in read mode
file = open("data.txt", "r")

# Move the file pointer to the 10th byte position
file.seek(10)

# Determine the current file position
position = file.tell()

# Read the content from the current position to the end of the file
remaining_content = file.read()

# Close the file
file.close()

# Print the value of position
print("Current position:", position)

# Print the contents of remaining_content
print("Remaining content:\n", remaining_content)