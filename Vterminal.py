import sys
import os
import socket
import struct
import time
import platform
import subprocess

# Function to change the current working directory
def cd(path):
    os.chdir(path)

# Function to clear the terminal screen
def clear():
    os.system("clear")

# Function to list the contents of a directory
def ls(path):
    files = os.listdir(path)
    for file in files:
        print(file)

# Function to create a new file
def create_file(filename):
    with open(filename, "w") as f:
        f.write("")
    print(f"Created file {filename}")

# Function to edit the contents of a file
def edit_file(filename):
    with open(filename, "a") as f:
        f.write(input("Enter text to append to file: "))
    print(f"Edited file {filename}")

# Function to rename a file
def rename_file(old_name, new_name):
    os.rename(old_name, new_name)
    print(f"Renamed file {old_name} to {new_name}")

# Function to delete a file
def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Deleted file {filename}")
    else:
        print(f"File '{filename}' does not exist")

# Function to create a new directory
def create_directory(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)
        print(f"Created directory {dirname}")
    else:
        print(f"Directory '{dirname}' already exists")

# Function to delete a directory
def delete_directory(dirname):
    if os.path.exists(dirname):
        os.rmdir(dirname)
        print(f"Deleted directory {dirname}")
    else:
        print(f"Directory '{dirname}' does not exist")

# Function to change the text color
def set_text_color(color):
    if color.lower() == "green":
        print("\033[32m", end="")
    elif color.lower() == "black":
        print("\033[30m", end="")

# Function to change the background color
def set_bg_color(color):
    if color.lower() == "white":
        print("\033[47m", end="")
    elif color.lower() == "black":
        print("\033[40m", end="")

# Function to reset the text and background colors to their defaults
def reset_colors():
    print("\033[0m", end="")

# Function to run a script
def run_script(script_path):
    subprocess.call(["python", script_path])

# Function to install a package
def install_package(package_name):
    subprocess.call(["pip", "install", package_name])

# Function to uninstall a package
def uninstall_package(package_name):
    subprocess.call(["pip", "uninstall", package_name])

# Function to print a list of commands and their descriptions
def print_help():
    print("Commands:")
    print(" create <filename> - create a new file")
    print(" edit <filename> - edit the contents of a file")
    print(" rename <old_name> <new_name> - rename a file")
    print(" delete <filename> - delete a file")
    print(" mkdir <dirname> - create a new directory")
    print(" rmdir <dirname> - delete a directory")
    print(" color <color> - change the text color")
    print(" bgcolor <color> - change the background color")
    print(" reset - reset the text and background colors to their defaults")
    print(" ls [directory] - list the contents of a directory")
    print(" cd <directory> - change the current working directory")
    print(" clear - clear the terminal screen")
    print(" help - display a list of commands and their descriptions")
    print(" exit - exit the VOS shell")

# Main loop
while True:
    # Display the command prompt
    sys.stdout.write("Vt> ")
    sys.stdout.flush()

    # Read the command from the user
    command = input()

    # Split the command into words
    words = command.split()

    # Execute the appropriate function based on the first word of the command
    if words[0] == "create":
        create_file(words[1])
    elif words[0] == "edit":
        edit_file(words[1])
    elif words[0] == "rename":
        rename_file(words[1], words[2])
    elif words[0] == "delete":
        delete_file(words[1])
    elif words[0] == "mkdir":
        create_directory(words[1])
    elif words[0] == "rmdir":
        delete_directory(words[1])
    elif words[0] == "color":
        set_text_color(words[1])
    elif words[0] == "bgcolor":
        set_bg_color(words[1])
    elif words[0] == "reset":   
        reset_colors()
    elif words[0] == "run":
     run_script(words[1])
    elif words[0] == "install":
      install_package(words[1])
    elif words[0] == "uninstall":
       uninstall_package(words[1])
    elif words[0] == "ls":
        if len(words) > 1:
            ls(words[1])
        else:
            ls(".")
    elif words[0] == "cd":
     cd(words[1])
    elif words[0] == "clear":
      clear()
    elif words[0] == "help":
       print_help()
    elif words[0] == "exit":
      break
    else:
       print("Invalid command")
