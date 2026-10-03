with open("file.txt", "w") as f:
    f.write("Hello everyone\n")
    f.write("I am Razak From Burkina Faso\n")
    f.write("Nice to meet you\n")
    f.write("I am 23 years old\n")
print("File created successfully\n")

#Opening the file
file = open("file.txt", "r")
c = file.read()
print(c)