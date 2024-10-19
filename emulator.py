from zipfile import ZipFile

filepath = "test.zip"
user = "admin"
computer = "test_computer"
name_of_system = "Linux"
# Simulate present working directory (initially root "/")
current_dir = "/"


# Function to display current working directorypt
def get_current_dir():
    return current_dir


def change_directory(new_dir, zip_file):
    global current_dir

    # Ensure directory starts from root if it begins with '/'
    if new_dir.startswith("/"):
        temp_dir = new_dir
    else:
        # Otherwise, navigate relative to the current directory
        temp_dir = f"{current_dir}/{new_dir}".strip("/")

    # Check if the directory exists in the zip file
    possible_dirs = [
        file
        for file in zip_file.namelist()
        if file.startswith(temp_dir.strip("/") + "/")
    ]

    if possible_dirs:
        # Update current directory if it exists
        current_dir = "/" + temp_dir.strip("/")
    else:
        print(f"cd: no such directory: {new_dir}")


# Open the ZIP file (virtual file system)
with ZipFile(filepath, "r") as zip_file:
    while True:
        command = input(f"{user}:{computer}$ ")

        if command == "exit":
            break

        elif command == "ls":
            print(zip_file.namelist())

        elif command == "pwd":
            # Print the current working directory
            print(get_current_dir())

        elif command == "cd":
            # Extract the target directory from the command
            _, new_dir = command.split(" ", 1)
            change_directory(new_dir, zip_file)

        elif command == "uname":
            print(f"{name_of_system}  {user} {computer}")

        elif command.startswith("cat "):
            _, filename = command.split(" ", 1)
            if filename in zip_file.namelist():
                with zip_file.open(filename) as file:
                    print(file.read().decode())
            else:
                print(f"cat: {filename}: Нет такого файла в архиве")
            #чтение

        elif command.startswith("rev "):
            _, argument = command.split(" ", 1)
            reversed_argument = reverse_string(argument)
            print(reversed_argument)

        elif command == "datetime":
            current_time = datetime.datetime.now().time()
            print(current_time)

        elif command == "tree":
            for tree in (zip_file.namelist()):
                print(tree)

        elif command.startswith("touch "):
            _, filename = command.split(" ", 1)
            touch(filename, zip_file)

        elif command == "mkdir":
            import os
            my_cwd = os.getcwd()
            new_dir = input()
            path = os.path.join(my_cwd, new_dir)
            if not os.path.exists(path):
                os.mkdir(path)
                print(os.listdir())
            #создание новой папки
            
        #elif command == "rm":
        import os
        os.rmdir("D:/dir/1.txt")
        if filename in zip_file.namelist():
            with zip_file.rm(filename) as file:
                    print(file.delete().decode())

        #elif command == "mv":

        
        elif command == "exit":
            # Exit the shell
            break

        else:
            # Handle invalid commands
            print("Enter a valid command (ls, pwd, exit, uname, cat, mkdir, touch)")