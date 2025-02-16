import os
from searchlogic import *
def main():
    print("INITIALIAZING FILE EXPLORER")
    cwd= os.getcwd()
    show(cwd)
    print(f"INIT AT {cwd}")
    while True:
        print("SELECT AN OPTION: \n 1.TRAVEL THROUGH FILE SYSTEM ")
        input("Placeholder Response")
        cwd=navegation("..", cwd)
        show(cwd)
  
main()