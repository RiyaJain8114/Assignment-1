#Program that reads the content of a text file and prints it to the console:
with open("output.txt", "r") as file:
    content = file.read()
print(content)
