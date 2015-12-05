from helperFunctions import *

# software user-interface
def interface():
    stop = False

    while stop != True:
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("l - load data file")
        print("r - generate random data")
        print("pl - print loaded data sets")
        print("pr - print random data sets")
        print("s - statistical analysis")
        print("q - quit")
        print()
        choice = input("what would you like to do: ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()

        if choice != "l" and choice != "r" and choice != "q":
            if choice != "pr" and choice != "pl" and choice != "s":
                print("invalid option")
                interface()

        if choice == "l":
            loadData()
        elif choice == "r":
            generateDataMenu()
        elif choice == "pr":
            printRandomDataSets()
        elif choice == "pl":
            printLoadedDataSets()
        elif choice == "s":
            statAnalysisMenu()
            writeTestsMenu()
        elif choice == "q":
            stop = True


if __name__ == "__main__":
	interface()
