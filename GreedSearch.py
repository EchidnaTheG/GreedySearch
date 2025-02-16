import os
from searchlogic import *
def main():
    print("INITIALIAZING FILE EXPLORER")
    print("COMMANDS!\ncd -> change into a dir\n.. -> change into previous dir\nexit() -> Exit Program")
    cwd= os.getcwd()
    print(f"INIT AT {cwd}")
    show(cwd)
    program_on= True
    while program_on:
        command=input("TYPE A COMMAND: ")
        if command =="exit()":
            program_on= False
            break
        cwd=navegation(command, cwd)
        show(cwd)
  
main()