import sys
import os
from pathlib import Path

projectDir = os.path.dirname(os.path.realpath(__file__))

def main():
    # Resolving arguments
    aV = readArgs()
    
    inputFile = aV[0]
    outputFile = aV[1]

    cDecimal = aV[2]
    cHex = aV[3]
    cChar = aV[4]
    cBit = aV[5]

    spacing = aV[6]

    # Handle
    file = open(inputFile, "rb")
    out = open(outputFile, "w")

    i = 0
    while 1:
        b = file.read(1)
        if (b == b''):
            break
        line = ""
        lineNumber = str(i) + ":"
    
        line += lineNumber + getSpace(lineNumber, spacing, 2)

        if (cDecimal):
            decimal = str(int.from_bytes(b, "big", signed = "False"))
            line += decimal + getSpace(decimal, spacing, 2)

        if (cHex):
            hexcode = b.hex()
            line += hexcode + getSpace(hexcode, spacing, 2)

        if (cChar):
            if (b == b'\n'):
                char = "\\n"
            elif(b == b'\t'):
                char = "\\t"
            else:
                char = b.decode("utf-8")
            line += char + getSpace(char, spacing, 1)

        if (cBit):
            bit = bin(int.from_bytes(b))[2:]
            line += bit

        out.write(line + "\n")
        i += 1


def readArgs():
    inputFile = None
    outputFile = None

    cDecimal = False
    cHex = False
    cChar = False
    cBit = False

    spacing = 5

    i = 1
    while (i < len(sys.argv)):
        arg = sys.argv[i]
        match arg:
            case "--input" | "-i":
                if (i + 1 == sys.argv):
                    print("input is not defined")
                    sys.exit()
                inputFile = sys.argv[i + 1]
                i += 2
                continue
            
            case "--output" | "-o":
                if (i + 1 == sys.argv):
                    print("output is not defined")
                    sys.exit()
                outputFile = sys.argv[i + 1]
                i += 2
                continue

            case "--spacing" | "-s":
                if (i + 1 == sys.argv):
                    print("spacing is not defined")
                    sys.exit()
                spacing = sys.argv[i + 1]
                i += 2
                continue

            case "--decimal" | "-d":
                cDecimal = True
                i += 1
                continue

            case "--hex" | "-h":
                cHex = True
                i += 1
                continue
            
            case "--char" | "-c":
                cChar = True
                i += 1
                continue
            
            case "--bit" | "-b":
                cBit = True
                i += 1
                continue

        match i:
            case 1:
                inputFile = arg
            case 2:
                outputFile = arg

        i += 1

    if (inputFile == None):
        print("input is not defined")
        sys.exit()

    if (not inputFile.startswith("./") and not inputFile.startswith("/")):
        inputFile = projectDir + "/" + inputFile
        
    if (outputFile == None):
        outputFile = projectDir + "/out.txt"
    elif (not outputFile.startswith("./") and not outputFile.startswith("/")):
        outputFile = projectDir + "/" + outputFile

    return [inputFile, outputFile, cDecimal, cHex, cChar, cBit, spacing]

def getSpace(string, spacing, minimum):
    space = "" 
    for i in range(spacing - (len(string) - minimum)):
        space += ' '
    return space

if __name__ == "__main__":
    main()
