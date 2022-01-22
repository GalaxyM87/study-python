#这个游戏采用了两种回到一开始的方法，一个为While True:,一直运行，知道exit()

from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")
    
    choice = input("> ")
    if type(int(choice)) == int:
        how_much = int(choice)
    else:
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
    bear_moved = False

    #此处是一个无限循环，直到跳出为止
    while True:
        choice = input("> ")
        #在这里进行if操作，bear_moved初始值为False。
        #如果我输入take money，就会跳到dead()函数
        if choice == "take money":
            dead("The bear looks at you then slaps your face off.")
        #如果我不输入take money,输入taunt bear,not bear_moved = True,就是执行这一行，然后bear_moved变为True
        #然后跳回while开始，重新执行
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        #如果先输入taunt bear,在输入taunt bear，就会执行这一行，跳到dead()函数
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        #如果先输入taunt bear,在输入open door,就会执行这一行，跳到gold_room()
        #如果一开始就输入open door,因为bear_moved初始值为False,这一行也不会执行，会跳到下行
        elif choice == "open door" and bear_moved:
            gold_room()
        #如果输入的不满足我们的预设条件，就会提示你，并且回到While
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