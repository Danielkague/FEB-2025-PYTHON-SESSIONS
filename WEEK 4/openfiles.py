# Open the file in read mode
with open("example.txt", "r") as file:
    # Read and print the content of the file
    content = file.read()
    print(content)


with open("output.txt", "w") as file:
    file.write("Hello, python!, this a test file")