import os

## A menu that is displayed in the terminal window.
class Menu : 
    ## Constructs a menu with no options.
    def __init__(self) :
        self._options = []

    ## Adds an option to the end of this menu.
    #  @param option the option to add
    def addOption(self, option) :
        self._options.append(option)

    ## Displays the menu, with options numbered starting with 1, and prompts
    #  the user for input. Repeats until a valid input is supplied.
    #  @return the number that the user supplied
    def getInput(self) :
        while True:
            for i, option in enumerate(self._options, 1):
                print(f"{i} {option}")
            
            user_input = input("\nEnter choice: ").strip().lower()

            if user_input in ['4', 'q']:
                return 4
            
            try:
                choice = int(user_input)
                if 1 <= choice <= len(self._options):
                    return choice
                else:
                    print(f"Invalid choice. Please enter 1-{len(self._options)}.")
            except ValueError:
                print("Proper usage: Please enter a numeric value or 'Q' to quit.")

def run_bash_cmd(some_choice):
    print('-' * 80, '\n')
    print('You entered #', some_choice)
    
    # Refactored: Replaced if/elif with a dictionary mapping
    commands = {
        1: ("The available memory is", "free -tmh"),
        2: ("The current network connections include:", "netstat -an | grep -i Estab | cut -d ':' -f 2,3 | gawk '{print $2}' | grep [0-9] | uniq"),
        3: ("Available file space is:", "df -h | grep \"Filesystem\|root\"")
    }
    
    if some_choice in commands:
        label, cmd = commands[some_choice]
        print(label)
        os.system(cmd)
    return 