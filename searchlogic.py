import os
def show(dir):
    list_of_dirs=os.listdir(dir)
    print(list_of_dirs)

def navegation(command,cwd):
    if command == "..":
        new_cwd= "/".join(cwd.split("/")[:-1]) or "/"
        os.chdir(new_cwd)
        print(f"Now at{new_cwd}")
        return new_cwd
