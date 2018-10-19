# This is a tool for decrypt messages
# Author : Menuka Rathnayake
# https://www.xenonstaforums.ga/
alphabet = "TaRbcYSGdBeQJfgFDhENiWOgZXkPIlAMmHnUopVKqrstCuvwLxyz"
key = 17
newMessage = ''

print('This tool made by Menuka.\n')
message = input('Please enter the message you want to decrypt > ')

for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position - key)%52
        newCharacter = alphabet[newPosition]
        newMessage += newCharacter
    else:
        newMessage += character
        
print('Decrypted seccessfully.\nYour Decrypted message is:', newMessage)

import os
import sys

restart = input("\nDo you want to decrypt another mesage? [y/n] > ")

if restart == "y":
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 
else:
    print("\nThe programm will be closed...")
    sys.exit(0)
