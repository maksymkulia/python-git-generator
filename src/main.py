# Importing modules
import os

# Providing params
name = input("Name of reposiory: ")
parent_dir = input("Provide path (without name of repo): ")

path = os.path.join(parent_dir, name)
os.mkdir(path)

print("Empty project created")

# Creating files
readme = "README.md"
f = open(os.path.join(path, readme), "w")
f.write("# " + name)
f.close()

# Creating git repo
os.chdir(path)
os.system("git init")
