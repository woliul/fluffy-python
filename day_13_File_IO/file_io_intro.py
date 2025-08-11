# Day 13: File I/O - Reading and Writing to Files

# File I/O (Input/Output) allows your program to interact with files
# on your computer's storage.

# Best practice: use the 'with open(...)' statement. It automatically
# closes the file for you, even if errors occur.

# 1. Writing to a file using 'w' mode (write)
# The 'w' mode creates the file if it does not exist, or overwrites it if it does.
print("Writing to file...")
with open("notes.txt", "w") as file:
    file.write("Hello, Python learner!\n")
    file.write("This is a new line of text.\n")
    file.write("This information will be saved permanently.")
print("Done writing to notes.txt.")

# 2. Reading from a file using 'r' mode (read)
# The 'r' mode opens the file for reading.
print("\nReading from file...")
with open("notes.txt", "r") as file:
    file_content = file.read() # Reads the entire content as a single string
    print("File content:")
    print(file_content)

# 3. Appending to a file using 'a' mode (append)
# The 'a' mode adds new content to the end of the file without overwriting it.
print("\nAppending to file...")
with open("notes.txt", "a") as file:
    file.write("\nThis is an appended line of text.")
print("Done appending.")

# Let's read the file again to see the appended content
print("\nReading file after appending...")
with open("notes.txt", "r") as file:
    final_content = file.read()
    print("Final file content:")
    print(final_content)
