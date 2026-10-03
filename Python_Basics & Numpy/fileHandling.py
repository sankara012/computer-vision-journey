file = open("geek.txt", "r")
#content = file.read()
print(file.read())
print("FileName: ",file.name)
print("Mode:",file.mode)
file.close()
print("Is closed?: ", file.closed)


