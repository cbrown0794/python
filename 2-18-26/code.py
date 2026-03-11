# Use the following code on the next page and add 3 choices to the getInput method to test for userChoice.
# Add questions to the buildOptions function with mainMenu.addOption


class Menu:
    ## Constructs a menu with no options.
    #
    def __init__(self):
        self._options = []

    ## Adds an option to the end of menu.
    #  @param option the option to add
    #
    def addOption(self, option):
        self._options.append(option)

    ## Displays the menu, with options numbered starting with 1, and prompts
    #  the user for input. Repeats until a valid input is supplied.
    #  @return the number that the user supplied
    #
    def getInput(self):
        done = False
        while not done:
            print('-' * 80, '\n')
            for i in range(len(self._options)):
                print("%d %s" % (i + 1, self._options[i]))

            userChoice = int(input())
            if userChoice == 1:
                print("Testing choice 1")
            if userChoice == 2:
                print("Testing choice 2")
            if userChoice == 3:
                print("Testing choice 3")
            if userChoice < 1 or userChoice > len(self._options):
                print('Enter a 1-3 only')
                continue
                    
            else:
                return userChoice

def main():
    mainMenu = Menu()

    def buildOptions():
        mainMenu.addOption("What is 2 + 2?")
        mainMenu.addOption("What is the capital of France?")
        mainMenu.addOption("Who invented Python?")

    buildOptions()
    choice = mainMenu.getInput()

if __name__ == '__main__':
    main()
