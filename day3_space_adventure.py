print("Welcome to Alien Hunt.")
print("You've crashed on an alien planet. Your mission is to find the alien to help you get home.")

crater = input("You arrive at a crater. Do you want to go around it or through it? "
               "Type \"around\" to go around or \"through\" to go through.\n")

if crater == "around":
    cave = input("You find a cave. Do you go past or enter? "
                 "Type \"past\" to go past. "
                 "Type \"enter\" to go inside.\n")

    if cave == "enter":
        gem = input("In the depths of the cave, you find 3 gems—red, blue, and green. "
                    "Type \"red\", \"blue\", or \"green\" to pick a gem.\n")

        if gem == "red" or gem == "blue":
            if gem == "red":
                print("Blasted by a death ray.")
            elif gem == "blue":
                print("You drowned in acid.")
            print("Game over.")  # Consolidated Game Over message
        elif gem == "green":
            print("You found the alien. Congratulations.")
        elif gem != "red" and gem != "blue" and gem != "green":
            print("You chose a colour that doesn't exist. Game over.")  # Handles invalid gem input

    elif cave != "past" and cave != "enter":
        print("Invalid choice. You hesitate and get eaten by a space beasty. Game over.")  # Handles invalid cave input

    else:
        print("Eaten by a space beasty. Game over.")  # Handles "past"

elif crater != "around" and crater != "through":
    print("Invalid choice. Lost and confused, you succumb to the planet's harsh conditions. Game over.")  # Handles invalid crater input

else:
    print("You tumble down the steep slope and break every bone in your body. Game over.")  # Handles "through"