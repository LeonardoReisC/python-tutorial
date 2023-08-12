from pathlib import Path

path = Path()
print(path.absolute())

path = Path(__file__)
print(path)
print(path.parent)  # parent
print()

# creating a file
new_path = path.parent / "eg.txt"  # concatenation
print(new_path)
new_path.touch()  # creates the file

new_path.write_text("Hello World!")  # writes a text on this path
print(new_path.read_text())

new_path.unlink()  # removes the file

# creating a folder
new_folder = path.parent / "folder_ex"
new_folder.mkdir(exist_ok=True)

new_folder.rmdir()

# home
home = Path.home()
print(home)
