import os
def show(dir):
    list_of_dirs=os.listdir(dir)
    print(list_of_dirs)
    return list_of_dirs
def navegation(command,dir):
    try:
        if command == "..":
            new_dir= "/".join(dir.split("/")[:-1]) or "/"
            os.chdir(new_dir)
            print(f"Now at{new_dir}")
            return new_dir
        if command == "cd":
            path=input("WHERE TO?: ")
            os.chdir(path)
            print(f"Now at{path}")
            return path
    except:
        print("ERROR")
