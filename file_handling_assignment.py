
try:
    # Task 1: File Creation
    with open("my_file.txt", "w") as file:
        file.write("Hello, Nathan!\n")
        file.write("12345\n")
        file.write("This is a test file.\n")

    # Task 2: File Reading and Display
    with open("my_file.txt", "r") as file:
        print(file.read())

    # Task 3: File Appending
    with open("my_file.txt", "a") as file:
        file.write("Appending more text.\n")
        file.write("This is another line.\n")
        file.write("End of file.\n")

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("Permission denied.")

finally:
    print("Operation completed!.")