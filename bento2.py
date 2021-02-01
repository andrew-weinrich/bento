#!/usr/bin/python3

import sys
import os

def main():
    if len(sys.argv) != 2:
        raise Exception("Invalid number of parameters: should be bento2.py string")
        
    chars = list()
    
    string = sys.argv[1]
    
    previousChar = ''
    charCount = 0
    
    currentChar = ('', 0)
    
    for char in string:
        if char != previousChar:
            currentChar = (char, 1)
            chars.append(currentChar)
        else:
            currentChar = (char, currentChar[1] + 1)
            chars[-1] = currentChar
        previousChar = char
    
    for char in chars:
        if char[1] == 1:
            print(char[0], end='')
        else:
            print(char[0] + str(char[1]), end='')
    print()


if __name__ == "__main__": 
    main()
