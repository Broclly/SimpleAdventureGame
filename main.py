import time
from colorama import Fore
import os
import random

scoreFiles = "/logs/"
lifeSummary = "null"
questionsCompleted = 0

# Initalizers 

def fileLocator(): # Locates the current directory that the script is being run in (used for making sure the game logs end up in the "logs" folder)
    directoryLocation = os.path.realpath(__file__)
    os.chdir(directoryLocation[0:-8])

def welcome(): # Little welcome program to initalize name
    global username

    type("Welcome to Joshua's Choose Your Own Adventure Story! \n")
    username = input("Please select a username (Your score will be saved under this username + Characters will reference you by this name) ")
    if username == "":
        type("No username selected! Using default name! \n")
        username = "Lorem Ipsum"
    type("Greetings, " + username + " and may lady luck be on your side today!")
    os.system('cls') # Clears screen (this is used a lot, so i'll annotate only this one)


# Main Gameplay

def room1(): # Contains all the info for the first room.
    type('You hear who is talking to you, but you cant see them. They whisper the following to you...\n\n' + '"'+ username + '... I heard about you. You who were destined to be the savior of this world. Go on.. and carry forth your fate! \n"')
    type("You can finally see now, a blinding orb of light appears in front of you labelled \n" + Fore.YELLOW + 'The Parallax Orb \n' + Fore.WHITE)

    type("What shall you do? \n")
    type("1. Destroy the orb \n")
    type("2. Stare at the orb \n")
    type("3. Accept the orb \n")
    decision = inputErrorHandling()
    if decision == 1:
        global lifeSummary
        os.system('cls')
        type("You choose to destroy the orb. The orb mends itself. However reality seems a little distorted, with every 5 seconds turning to static for a split second. Suddenly, a person conjures out of thin air, the same one who said you were 'the savior of this world'\n")
        type('"YOU IMBICILE! DO YOU EVEN KNOW WHAT YOU JUST DID?! THAT ORB IS QUITE LITERALLY THE MAINFRAME FOR THE ENTIRE EXISTENCE OF THIS WORLD!!" He exclaims wildly, as he shakes you. Suddenly the ground cracks below you, and you fall infinitely in a world of deafeningly loud static \n')
        lifeSummary = " destroyed the parallax orb, destroying reality. They fell through a static void for around 10 years (without dying) until they were eventually caught by a time guard. These time guards then sentenced him to eternal damnation by experiencing \n the full pain of being hit by a car for crimes against time."
        gameOver()
    elif decision == 2:
        os.system('cls')
        type("You choose to stare at the orb, mesmerized by it's insane potential. It awakes something in your heart, opening your mind to the endless possibilities of life. It grants you a choice, " + Fore.YELLOW + "to bind the orb to a staff of creation," + Fore.RED + " or to a staff of unlimited power... \n")
        type(Fore.WHITE + "Which will you choose? \n")
        type("1. Staff of Creation \n")
        type("2. Staff of Unlimited Power \n")
        decision = inputErrorHandling()
        if decision == 1:
            os.system('cls')
            type("You bind the orb to a staff of creation. You decide to create a new world. A better one, that can be guided by your divine guidance...\n")
            type("What started out sweetly, quickly devolved into helpless begging for easy to gather materials. Eventually the scientists of the new world find you in person, and trap you in a bubble. They can torture you until they get what they want, and you cannot leave the bubble...\n")
            lifeSummary = " showed sweet respect and mercy to the wrong people, who then took advantage of them. After this happened, they were pretty much screwed as they were stuck in a bubble. They live out the rest of their days (which is eternity thanks to research), making random bullshit that the people of The New Reality don't have time to do. Or doing cleaning jobs (sewage treatment, destroying garbage cleanly, etc)."
            gameOver()
        elif decision == 2:
            os.system('cls')
            type("You bind the orb to a staff of power. It drives you insane, threatening the people of New Earth until they do as you say so...\n")
            type("You become the devil, the unholy beast that kills all without a shred of remorse...\n")
            lifeSummary = " lost it immdiately after getting a stupid amount of power from the staff of power they now own. They basically become Satan 2.0 pretty much. Not even death itself could make bro cry"
            ending()
    elif decision == 3:
        os.system('cls')
        type("You choose to accept the orbs power, and it whispers to you.. \n")
        type("Go! Save the world, and show no mercy to all those that try to stop you! \n")
        room2()
    else:
        screwYou()

def room2(): # Sends you to the broken world
    os.system('cls')
    global lifeSummary
    type("The skies are black, polluted with catastrophe and anarchy. You were destined to bring order to this world, but how you will do that is your choice completely. The orb's power is simply a medium of change, and you are its commander.. \n")
    type("A couple ideas immdiately jump into your head, you could try and use this orbs power to bring about a new civilization, appoinated by a leader of your choice. Or y'know, you could always... do a proper cleansing. \n")
    type("With these options in mind, how will you choose to bring order to this world? \n")
    type("1. New civilzation \n")
    type("2. Gentle nudge into perfection \n")
    decision = inputErrorHandling()
    if decision == 1:
        os.system('cls')
        type("You decide to descend down to select a leader for your new civilization. After long consideration, 3 possible leaders stand out to you. \n")
        type("The first, Chloe Patterson, is a diplomat that can persuade pratically anyone with her impressive charisma... \n")
        type("The second, Kanye West, is a radical thinker who's musical talent is considered by many to be the absolute best... \n")
        type("And the last, Milton McRyker, is a force to be reckoned with, told to have the physical power to bring multiple gangs to their knees... \n")
        type("Having gotten to know these people, who will you choose to lead the new city? Who do you trust with half of the orbs power? \n")
        type("1. Chloe Patterson \n")
        type("2. Kanye West \n")
        type("3. Milton McRyker \n")
        decision = inputErrorHandling()
        if decision == 1:
            type("You choose Chloe Patterson, and grant her with half of your power...\n")
            type('"Great choice"' + username + '", you wont regret it. Or will you?"\n')
            type("And with that, Chloe Patterson transfers all her energy into one concussive blast, immdiately rendering you unconcious...\n")
            type('You gain conciousness for a couple seconds, to hear her say "Hah, deus ex machina  my ass. Look at how powerful you are now...\n"')
            lifeSummary = " was kidnapped by Chloe's followers and quickly sent to a facility to be stored. After a couple years, they were brought down to the core of New Earth. Instead of molten lava, they found a reactor chamber, in which they were placed inside. From that point onwards, they were strapped to a rejuvenation bed, keeping them in their prime forever, permeantly exerting the orbs energy to fuel the increasing demand for power in New Earth..."
            gameOver()
        elif decision == 2:
            type("You choose Kanye West, and grant him with half of your power...\n")
            type('"Dont you worry man, Ill produce an absolute masterpiece for you..."\n')
            type("With that, you use your remainder of the your power to skip time until civilization is rebuilt.")
            room3()
        elif decision == 3:
            type("You choose Milton McRyker and grant him with half of your power... \n")
            type('"Ill harness this energy to create the most unified force of New Earth! Thank you, please come back soon!"\n')
            type("And with that, you are confident McRyker will lead New Earth to become a Type I civilization...\n")
            room4()
        else:
            screwYou()
    if decision == 2:
        type("The orb's power's poision your line of thought, and you create a divine beam of cleansing, that scrapes off every piece of life in the planet. You use the rest of your power to create self-fufilling factories, and use the planet as a mine...\n")
        lifeSummary = " stopped thinking for a bit after getting their newfound power and instead killed everyone to save this timeline. This in turn created a dead planet filled with mineral resources that they drained for their own self gain..."
        ending()
    else:
        screwYou()
        

def room3(): # Kanye West's perfect world
    global lifeSummary
    os.system('cls')
    type("Everything is perfect in this new world, piano tiles as roads with treble clef cars riding along. And a massive stuffed bear that is wearing sunglasses...\n")
    type('Kanye walks up to you. "Pretty sweet huh? I designed it all myself, and even added the bear from my hit 3 hit albums!"\n')
    type("Kanye seems overjoyed, and even wants to show you a story he's working on. It's called 'Rogue.py' and he seems highly passionate about it... \n")
    type("Knowing Kanye's feelings about his work, do you try the game? \n")
    type("1. Yes \n")
    type("2. No \n")
    decision = inputErrorHandling()
    if decision == 1:
        os.system('cls')
        type("The story was so masterful that you cried in front of Kanye West. \n")
        type('"Hey, hey, dont worry dude. Lets get married ok? Imagine it.. "' + username + ' West. Doesnt it have a ring to it?"')
        lifeSummary = " experienced peak cinema to the point where they couldn't stop anymore. So instead, they got married to Kanye west. They took Kanye's last name, and their name is now" + username + " West"
        ending()
    elif decision == 2:
        os.system('cls')
        type("Enraged, Kanye dropped a diss track so detrimental to you that it caused you to die. \n")
        lifeSummary = " pissed off Kanye West. So used astral powers to pull up bro's search history, creating a diss track on that premise. Due to this, the diss track was ranked a SSS tier, immdiately vaporising them. A statue was created of them to be publically urinated on."
        gameOver()
    else:
        screwYou()

def room4(): # McRyker's Frantic Math Frenzy
    global lifeSummary
    questionsCompleted = 0
    os.system('cls')
    type("When you arrive back, after a long absence, you are immdiately greeted by multiple armed men running towards you.\n")
    type('They exclaim "You must help us! McRyker is using all of his power to try and defend us from the giant hand in the sky, but it isnt enough!!"\n')
    type("You thought they were crazy, but sure enough, McRyker is using what looks like a fist made of light to push back this floating hand in the sky.\n")
    type('McRyker shouts, "Quickly! Use your powers to help me out!" He throws some sort of device at you. "All you have to do is solve a couple math problems in order to charge it up! It runs off of brain power!"\n')
    type("You don't really seem convinced, but he's frantic, and he has half of your power, so you play along.\n")
    os.system('cls')
    type("This is a minigame! You must solve all the following math problems, any wrong and you'll fail the skill check (womp womp :p)\n")
    input("Ready to start?")
    while questionsCompleted != 3:
        x = random.randint(1,100)
        y = random.randint(1,100)
        answer = int(input("What is " + str(x) + " multiplied by " + str(y) + " equal to?"))
        if answer != (x * y):
            type("The machine immdiately blows up in your hand. You die. And McRyker's world is destroyed by the hand.")
            lifeSummary = " returned back to McRyker's creation, only to be suprised by the massive hand attempting to kill McRyker. Unfortunately," + username + "was a dumbass, and couldn't figure out how to solve basic arthimitic. And so, they sealed the fate of the world..."
            gameOver()
        else:
            type("Correct! The machine is powering up...\n")
            questionsCompleted += 1
    type("The machine powers up successfully, blasting away the hand. You are given a medal of valor, and a sacred artifact from the civilization. You decide it's best to get a house here and live here. \n")
    type("Life is peaceful for you, and you eventually pass away, happy...")
    lifeSummary = " returned back to McRyker's creation, only to be suprised by the massive hand attempting to kill McRyker. " + username + " clutched up, and got a dub for the whole planet to enjoy. They died peacefully in their sleep with their lover, Kanye West."
    ending()

    



# Special Functions
        
def gameOver(): # Runs an ending message if you died
    os.system('cls')
    type("Your decisions led you on the wrong path, forever. Although your current character is in eternal suffering (thanks to you!) this program will save their lifespan's data as a textfile! From there, you can regenerate a character by re-running this program to simulate another person. Enjoy, you monster..")
    input("Press enter to terminate this program...")
    fileSaving()
def ending(): # Runs an ending message if you were alive still, got an ending
    os.system('cls')
    type("Your decisions led you on the correct path, creating a change for this world. Whether or not that change was good or not is up to you to determine (or you already have determined since you acted in such a manner). This program will however, save a record of all that has happened. Re-running this program will allow you to get a different ending with a new iteration of person. Enjoy!")
    input("Press enter to terminate this program...")
    fileSaving()
def fileSaving(): # Saves a recap to a file with a name
    f = open("logs/" + username + ".txt", "w")
    f.write("Game Over! Here's the deets: \n" + username + lifeSummary)
    f.close()
def screwYou(): # Pretty much an error catcher
    type("That isn't a valid number! Y'know what? Screw you...")
    time.sleep(1)
    quit()
def inputErrorHandling(): # Error handling incase the player inputs a string or null type 
    global decision
    invalidEntry  = 1
    while invalidEntry == 1: 
        try:
            decision = int(input("What action shall you do?"))
            invalidEntry = 0
            return(decision)
        except ValueError:
            type("That is an invalid data type, try again! \n")
            invalidEntry = 1
def type(text): # Special code to add some flair to typing (all credits to coby for this one)
    speed = 0.04

    for char in text:
        print(char, end='', flush=True)
        if char in {'.', '?', '!'}:
            time.sleep(0.5)
        elif char == ",":
            time.sleep(0.2)
        elif char == "\n":
            print()
        time.sleep(speed)
    return

fileLocator()
welcome()
room1()
