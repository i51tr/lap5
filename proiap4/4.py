# Open the "data.txt" file in read mode
file_name = "data.txt"
file = open(file_name, "r")

# Use the seek() method to move the file pointer to the 10th byte position
file.seek(10)

# Use the tell() method to determine the current file position and store it in a variable named position
position = file.tell()

# Read and store the content from the current position to the end of the file in a variable named remaining_content
remaining_content = file.read()

# Close the file
file.close()

# Print the value of position
print("Position:", position)

# Print the contents of remaining_content
print("Remaining Content:")
print(remaining_content)