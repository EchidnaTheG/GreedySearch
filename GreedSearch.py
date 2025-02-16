import os
from searchlogic import *
def main():
    print("INITIALIAZING FILE EXPLORER")
    cwd= os.getcwd()
    show(cwd)
    print(f"INIT AT {cwd}")
    while True:
        command=input("TYPE A COMMAND: ")
        cwd=navegation(command, cwd)
        show(cwd)
  
main()