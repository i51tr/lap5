# Create a new text file named "output.txt" 
file_name = "output.txt"
file = open(file_name, "w")

# Write the three lines to the "output.txt" 
lines = [
    "This is the first line.",
    "Writing to files is easy.",
    "Python is great for file handling."
]
for line in lines:
    file.write(line + "\n")

# Close the "output.txt" 
file.close()

# Confirm that the file has been successfully created and written to
print("File created and written successfully.")