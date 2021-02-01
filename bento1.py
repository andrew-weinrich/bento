#!/usr/bin/python3

import sys
import os

def main():
    if len(sys.argv) != 2:
        raise Exception("Invalid number of parameters: should be bento1.py directory")
    
    files = list()
    
    for rootDir, dirs, fileName in os.walk(sys.argv[1], topdown=False):
       for fileName in fileName:
           fullPath = os.path.join(rootDir, fileName)
           fileStat = os.stat(str(fullPath))
           fileSize = fileStat.st_size
           fileData = (fileName)
           files.append( (fullPath, fileName, fileSize) )
    
    sortedFiles = sorted(files, key = lambda fileDatum : fileDatum[2])
    
    for fileData in sortedFiles:
        print(f"{fileData[0]}\t{fileData[1]}\t{fileData[2]}")


if __name__ == "__main__": 
    main()
