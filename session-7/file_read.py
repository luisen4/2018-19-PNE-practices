# Example of reading a file located
# in our local filesystem

NAME = "mynotes.txt"
# Open the file
# Open function creates an object
myfile = open(NAME, 'r')

print("File opened: {}".format(myfile.name))

contents = myfile.read()

print("The file contents are: {}".format(contents))

myfile.close()

f = open(NAME, "a")
# a mode: adds information to the last line of the file.
f.write("THIS IS A TEXT EXAMPLE FOR ADDING TO MY FILE")
f.close()
print("The end")
