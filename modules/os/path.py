import os.path

path = os.path.join("/home/Leonardo", "Desktop", "Python", "file.pdf")
print(path)
directory, file = os.path.split(path)
print(directory)

file_name, extension = os.path.splitext(file)
print(extension)