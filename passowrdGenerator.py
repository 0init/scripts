#/usr/bin/python3
import string
import random

banner= """
██████╗  █████╗ ███████╗███████╗ ██████╗ ███████╗███╗   ██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝ ██╔════╝████╗  ██║
██████╔╝███████║███████╗███████╗██║  ███╗█████╗  ██╔██╗ ██║
██╔═══╝ ██╔══██║╚════██║╚════██║██║   ██║██╔══╝  ██║╚██╗██║
██║     ██║  ██║███████║███████║╚██████╔╝███████╗██║ ╚████║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                           

Password Generator v1.0
Coded By: Mido0x0x @0init
"""

print(banner)


s1= list(string.ascii_lowercase)
s2= list(string.ascii_uppercase)
s3= list(string.digits)
s4= list(string.punctuation)


Characters_number = input("How many characters do you want in your password? ")

while True:
    try:
        Characters_number = int(Characters_number)
        if Characters_number < 6 :
            print("Password must be at least 6 characters long")
            Characters_number = input("Please enter a number greater than 6: ")
        else:
            break
    except:
        print("Please enter a number Only")
        Characters_number = input("Please enter a number greater than 6: ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(Characters_number * 0.30)
part2 = round(Characters_number * 0.30)

password = []

for i in range(part1):
    password.append(s1[i])
for i in range(part2):
    password.append(s2[i])
for i in range(Characters_number - part1 - part2):
    password.append(s3[i])
for i in range(Characters_number - part1 - part2):
    password.append(s4[i])
random.shuffle(password)

print("Your password is: "+ "".join(password))


