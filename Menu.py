#Aiden Allison
#2/6/2024
#working with dictionarys and lists
def display_menu():
    print(' MENU')
    print("1)Calculate wait time")
    print("2)Calculate wait time")
    print("3)Calculate wait time")
    print("4)Calculate wait time")
    print("5)Quit")
    selectmenu = input("Menu choice:")
    return selectmenu
def main():
    menu = display_menu()
    while menu != "5":
        print(menu)
        if menu == "1":
            pass
        elif menu == "2":
            pass
        elif menu == "3":
            pass
        elif menu == "4":
            pass
        elif menu == "5":
            print("quitting program....")
        else:
            print("error no number to select menu")
        menu = display_menu()
if __name__ == "__main__":
        main()
