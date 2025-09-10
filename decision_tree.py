import sys
import time

def type_text(text, delay=0.02, pause=0.6):
    lines = text.split('\n')
    for line in lines:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()  # Move to next line after printing the line
        time.sleep(pause)  # Wait after each line

# yeah AI wrote all that above because i dont know how and i thought it would be cool, all it does is make the text appear as if its being typed out and the new lines have a slight pause in between each one


while True:
    type_text("\n\nToday may be the day you make the most important decision of your existence. This choice may affect you for the rest of your potentially short life. Choose extremely wisely.\n\nYou have just woken up.\nYour room is dark. \nYou look over at the clock, and it reads 3:34 AM. \nYour throat feels a bit parched. \nWhat will you do?")

    while True:
        woken_up = input("1. Get up and get a glass of water\n2. Go back to sleep\n")
        if woken_up == "1" or woken_up == "2":
            break
        else:
            type_text("Please input 1 or 2")

    if woken_up == "1":
        type_text("You stand up. You walk over to the opposite side of your room, where the door is. \nYou open the door.\nAcross from you is the hallway, with what seems to be a lone banana peel on the floor. \nWhat will you do?")
        while True:
            hallway = input("1. Proceed.\n2. Go back to your room.\n")
            if hallway == "1" or hallway == "2":
                break
            else:
                type_text("Please input 1 or 2")
        if hallway == "1":
            type_text("You walk forward, and step on the banana peel. \nNothing happens, because you are not playing mario kart.\nYou walk towards the stairs downstairs. \nThe stairs are stretching down into the darkness of the kitchen. \nYou decide to keep going down the stairs, and reach the bottom.\nThere, you see a perfect glass of water sitting there on the counter. What do you do?\n")
            while True:
                water = input("1. Go forward and attempt to drink the water.\n2. Just kinda stand there\n")
                if water == "1" or water == "2":
                    break
                else:
                    type_text("Please input 1 or 2")
            if water == "1":
                type_text("You walk forward. \nSuddenly, a banana appears in front of you. \nThe world seems to come to a halt as your foot slips. \nIn terror, you look around for something to grab onto. \nThe counter comes into view. What will you do? \n")
                while True:
                    counter = input("1. Grab onto the counter\n2. Do nothing and accept your fate\n")
                    if counter == "1" or counter == "2":
                        break
                    else:
                        type_text("Please input 1 or 2")
                if counter == "1":
                    type_text("You grab onto the counter. \nYou feel a sharp pain in your hand as you grab onto the counter. \nYou look down, and see that you have grabbed onto a butter knife. \nYou are now bleeding out on the floor, as the knife somehow hit a major artery. You take a second to contemplate how there could be a major artery in your hand right before falling into eternal rest. Your face looks stupid.")
                    continue
                elif counter == "2":
                    type_text("You do nothing. \nYou fall over.\n \n \n \n \n \n \nYou hit the floor, get up and grab the glass of water. \nYou drink the water and go back to bed.\nYou win.")
                    continue
            elif water == "2":
                type_text("You just kinda stand there. \nAfter doing that for a while, you wonder if the doctor was lying about the schizophrenia results. \nAfterwards, you go over and grab the glass of water. \nYou lift the glass of water to your mouth, but do not drink it. \nYou put the water glass back down. \nYou go back to your room and see that nothing has changed. You go back to bed.")
                continue
        elif hallway == "2":
            type_text("You decide to go back to your room. You open your door, and discover that there is what seems to be a monkey jumping on your bed. \nHe fell off and bumped his head. You now have a monkey in your room.\nThat is all.")
            continue
    elif woken_up == "2":
        type_text("You close your eyes. \nNothing happens. \nYou open your eyes again, and see that there is a small dog in front of you. \nWhat will you do? ")
        while True:
            dog = input("1. Pet the dog\n2. Ignore the dog\n")
            if dog == "1" or dog == "2":
                break
            else:
                type_text("Please input 1 or 2")
        if dog == "1":
            type_text("You pet the dog, and it lays its head down on your chest. \nNow you definitely wont be able to sleep. \nWhat will you do?")
            while True:
                dog2 = input("1. Move the dogs head away and get up\n2. Sleepless night\n")
                if dog2 == "1" or dog2 == "2" or dog2 == "3":
                    break
                else:
                    type_text("Please input 1 or 2")
            if dog2 == "1":
                type_text("You move the dogs head off of you. \nYou get up, try to walk over to your door, and trip over the dogs tail. \nYou curse before you can think.\nSHE comes. \nYou die.")
                continue
            elif dog2 == "2":
                type_text("You decide to just have a sleepless night. \nIn the morning, you are so extremely tired that you fall down the stairs and hit your head. \nYou are now in eternal rest.")
                continue
            elif dog2 == "3":
                type_text("Crazy? I Was Crazy Once. They Locked Me In A Room. A Rubber Room. A Rubber Room With Rats. And Rats Make Me Crazy\n" * 50)
                exit()
        elif dog == "2":
            type_text("You ignore the dog. \nThe dog looks sad, and walks away. \nYou go back to sleep. \nUnfortunately, you are still thirsty. \nYou might want to get some water before going back to sleep next time. \nsecret: dog1 input \"3\" ")
            continue
    