from search import *

def printMenu():
    print("Welcome! AirLine Program")
    print("=======MENU======")
    print("1. search:  s")
    print("2. print:  p")
    print("=================")

def launcherFuntion(menu):
    if menu=='s':
       parsing()

    else:
        print("error")

while(1):
    printMenu()
    menuKey=str(input("select Menu:"))
    launcherFuntion(menuKey)