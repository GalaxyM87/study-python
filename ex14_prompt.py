#运行时记得输入参数user_name.
from sys import argv

script, user_name = argv
prompt = '>>>>> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"How old are you? {user_name}")
age = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. You are {int(age)} years old. 
Not sure where that is.
And you have a {computer} computer. Nice.
""")