# Define file path
filename = "./my_file.txt"
# Creates a new text file named "my_file.txt" in write mode ('w').
try:
    with open(filename, "w") as file:
        # Write at least three lines of text to the file, including a mix of strings and numbers.
        file.write("The wind does not stop,\n")
        file.write("I run to cover and I hide\n")
        file.write("I pray for the end\n")
except  IOError:
    print("Error: could not create file " + filename)
    
# Read the contents of "my_file.txt" and display them on the console.
try:
    with open("my_file.txt", "r") as file:
        text = file.read()
        print(text)
except  IOError:
    print("Error: could not open file " + filename)
# Open "my_file.txt" in append mode ('a').
try:
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text to the existing content.
        file.write("\n")
        file.write("Soon the wind,\n")
        file.write("I walk out of my cover\n")
        file.write("Bid the end away\n")
except IOError:
    print("Error: could not edit file " + filename)
