from helperFunctions import *

def interface():
    stop = False

    while stop != True:
        print()
        print("~~~~~~~~~~~~~~~~~~~~~")
        print("l - load data file")
        print("r - generate random data")
        print("pl - print loaded data sets")
        print("pr - print random data sets")
        print("q - quit")
        print()
        choice = input("what would you like to do: ")
        print("~~~~~~~~~~~~~~~~~~~~~")
        print()

        if choice != "l" and choice != "r":
            if choice != "q" and choice != "pr":
                if choice != "pl":
                    print("invalid option")

        if choice == "l":
            loadData()
        elif choice == "r":
            generateDataMenu()
        elif choice == "pl":
            printLoadedDataSets()
        elif choice == "pr":
            printRandomDataSets()
        elif choice == "q":
            stop = True




interface()
