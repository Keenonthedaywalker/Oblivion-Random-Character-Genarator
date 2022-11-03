menu = [
   "1. Normal Character Generator",
   "2. Advanded Appearance Generator",
]

selected = 0

def display_menu(menu, selected):
    for number, item in enumerate(menu, 1):
        if number == selected:
            print('(X)', item)
        else:
            print('( )', item)

while True:
    display_menu(menu, selected)

    try:
        # don't assign directly to `selected` because user may choose wrong number
        new_selection = int(input("Please choose one of the menu options.\n"))

        if new_selection in (1, 2):
            # assign to `selected` when user choose correct number
            selected = new_selection

            display_menu(menu, selected)
 
            new = input("Would you like to make another selection? [Y/n]").lower()

            if new in ("n", "no"):
                break
        else:
            print("Invalid Choice. Enter one of the menu numbers.")
    except ValueError:
        print("Invalid Choice. Enter one of the menu numbers.")
