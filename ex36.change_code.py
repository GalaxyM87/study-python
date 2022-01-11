#这个游戏采用了两种回到一开始的方法，一个为While True:,一直运行，知道exit()

from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")
    
    try:
        how_much = int(input("> "))
    except:
        dead("Man, learn to type a int number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of money")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    print("Please type 'taunt bear' or 'take money'")


    while True:
        choice = input("> ")

        if choice == "take money":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear":
            print("The bear has moved from the door.")
            print("You can go through it now.")
            print("Please type Yes or No.")
            while True:
                choice = input("> ")
                if choice == "Yes":
                    gold_room()
                elif choice == "No":
                    dead("The bear gets pissed off and chews your leg off.")
                else:
                    print("I got no idea what that means.")
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    #同前面的while True效果类似，如果输入的有问题，自动回到函数最开始
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    #只有这里有exit(0)，表示程序结束
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

#进入你的游戏，开始提示玩家操作，dead函数表示最终结束。
start()