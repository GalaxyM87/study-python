#if/else/else语句只要找到一个True就会停止
#在if中调用if可以实现从一个分支引向另一个分支
print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == '1':
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    elif bear == "3":
        print("The bear eats your ankle off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
    
elif door == "2":
        print("You stare into the endless abyss at Cthulhu's retina.")
        print("1. Blueberries.")
        print("2. Yellow jacket clothespins.")
        print("3. Understanding revolvers yelling melodies.")

        insanity = input("> ")

        if insanity == "1" or insanity == "2":
            print("Your body survives powerd by a mind of jello.")
            print("Good job!")
        else:
            print("The insanity rots your eyes into a pool of muck.")
            print("Good job!")

else:
    print("Your stumble around and fall on a knife and die. Good job!")