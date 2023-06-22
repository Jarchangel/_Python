#!/usr/bin/python3
from sys import exit
def house_of_gold():
    print("Please confirm your alias to gain acess into room")
    player = input("> ")
    print(f"Bravo {player}, your courage and resillience has brought you this far")
    print("WELCOME TO THE HOUSE OF GOLD !!!!!!")
    print(f"Take as much Gold as you can {player} but yet! Becareful..... Too much of anything including Gold could be bad for you..")
    print("How much Gold would you want to take?")
    amount = int(input(">> "))
    if amount <= 100:
        print("You are a true soldier with integrity. The House of Gold with everything in it is yours to keep. Bye...")
        exit(0)
    else:
        print("This was also a test you greedy soldier, The house of Gold and everything was meant for you to keep. But since youve choosen to be greedy you will have to exit with what you have at hand. Bye")
        exit(0)

def life():
    print("You still have one life available. \n Do you wish to continue from the start?")
    reply = input("yes or no? : ")
    if reply == "yes" or reply == "Yes":
        start()
    elif reply == "no" or reply == "No":
        exit(0)
    else:
        print("Unkown response!!, please stick to the script")
        life()

def house_of_flames():
    print("Confirm your alias to proceed")
    player = input("> ")
    print(f"{player} welcome to the HOUSE OF FLAMES...")
    print("Is it just me or does someone else feel the cold in here?")
    print(f"Stay focused {player}, remember that the goal is to locate THE ROOM OF GOLD")
    print("There are two doors here. \n In front of door #1 sits a bear of furnance, licking a boiling comb of honey \n Door #2 has a key just in front of the door")
    flames_door = input(f"choose your fate {player}, is it 1 0r 2? :  ")
    if flames_door == "2":
        print(f"If it comes easy, its not worth it {player}, this door leads back to the house of thorns")
        house_of_thorns()
    elif flames_door == "1":
        print(f"{player} the burning bear doesnt seem pleased with you")
        print("What do you do now?")
        print(f"You've come this far {player}, can i give a suggestion?")
        suggest = input("yes or no :  ")
        if suggest == "yes" or suggest == "Yes":
            print("Heros need helping hands too, so dont worry, its nothing")
            print(f"{player}, you can either \"TAUNT\" the burning bear or \"KNEEL\". Your fate depends on your choice {player}")
            fate = input(f"What be your choice {player}?  ")
            if fate == "taunt" or fate == "TAUNT":
                print("The bear tears you into shreads")
                life()
            elif fate == "kneel" or fate == "KNEEL":
                print("A humble man is truely a wise man, BRAVO!")
                house_of_gold()
            else:
                print("Incorrect!! Take a closer look at the tip i gave you, we are running out of time")
                house_of_flames()
        elif suggest == "no" or suggest =="No":
            print(f"Its a Yes day {player}, you cant get past this stage without a yes. Please reenter into the house")
            house_of_flames()
        else:
            print(f"This in an unrecognised option, stick to the script {player}")
            house_of_flames()
    else:
        print(f"what is that {player}?, you are down by one level for not paying attention. \n See you in the HOUSE OF THORNS!")
        house_of_thorns()


def house_of_thorns():
    print("Confirm your alias to proceed")
    player = input("> ")
    print(f"{player} This is the house of thorns where you can survive only if you truely know who you are")
    print("You will have to crack the code to be able to pass through to claim your treasures")
    crack = player[1]
    crack2 = player[-1]
    print("The code is always the second in character from the front and the first character from behind of the player alias")
    print("you've got only two chances soldier, use it properly")
    try1 = input("code1:  ")
    try2 = input("code2:  ")
    if try1 == crack and try2 == crack2:
        print("Bravo soldier, smart choice but you still have to pass through the HOUSE OF FLAMES")
        print("See you in the house of flames!")
        house_of_flames()
    else:
        dead("Truly the gods are not to blame. Try again!")

def dead(why):
    print(why)
    print("GAME OVER!")
    exit(0)

def start():
    print("WELCOME TO GAME OF ROOMS SEASON2!")
    print("Input Player Alias")
    player = input("> ")
    print(f"To continue {player}, press Enter or press 0 to exit")
    prompt = input("> ")
    if prompt == "0":
        exit(0)
    else:
        print(f"{player}, there is a door to your #right and to your #left")
        print("Which door do you enter?")
        next = input("> ")
        if next == "right" or next == "Right":
            house_of_flames()
        elif next == "left" or next == "Left":
            house_of_thorns()
        else:
            dead("This option has not yet been activated for this game, restart and stick to instructions")
start()
