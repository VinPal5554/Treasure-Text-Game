import ASCII

print(ASCII.ASCIIART[0])
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_or_right = input("You are at a cross road. Where do you want to go? Type 'left' or 'right' ")

if left_or_right == "left":
    print(ASCII.ASCIIART[1])
    wait_or_swim = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ")
    if wait_or_swim == "wait":
        print(ASCII.ASCIIART[2])
        red_yellow_blue = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")
        if red_yellow_blue == "blue":
            print(ASCII.ASCIIART[4])
            print("You enter a room of beasts. Game Over.")
        elif red_yellow_blue == "red":
            print(ASCII.ASCIIART[6])
            print("You enter a room full of fire. Game Over.")
        else:
            print(ASCII.ASCIIART[7])
            print("You have made it to safety. You Win.")
    else:
        print(ASCII.ASCIIART[3])
        print("You were eaten by sharks. Game Over.")
else:
    print(ASCII.ASCIIART[5])
    print("You stumble and fall off a cliff. Game Over.")