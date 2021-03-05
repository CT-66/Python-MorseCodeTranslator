import re
from morse_to_text import morse_to_text
from text_to_morse import text_to_morse

def TextToMorse():
    while True:
        userInput= input(">> ").lower()
        words= userInput.strip()
        words= userInput
        output= ""

        for word in words:
            output += text_to_morse.get(word, word)+ " "
        print(output)
        print()  

def MorseToText():
    while True:
        userInput= input(">> ").lower()
        words= userInput.strip()
        words= re.split(' |/', userInput)
        print(words)
        output= ""

        for word in words:
            output += morse_to_text.get(word)
        print(output)
        print()

question= int(input('''Press the number assigned to each option to begin translation:
1. Morse to Text
2. Text to Morse
>> '''))

if question== 1:
    MorseToText()

elif question== 2:
    TextToMorse()