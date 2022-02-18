from functions import showMenu, isValidChoice, selectAfunction

while 1:
    showMenu()
    option = input("Please select a function from menu: ")
    if isValidChoice(option):
        selectAfunction(option)