#Max Chen
#HW3

#Problem 2


def printBinary(decNumber):
    revBinary = ""
    while decNumber > 0:
        rem = decNumber % 2
        revBinary += str(rem)
        decNumber = decNumber // 2

    binary = revBinary[::-1]

    while len(binary) <= 8:
        binary = "0" + binary
        

    print(binary)

printBinary(57)
printBinary(123)
printBinary(85)
printBinary(38)


#Problem 3

def printHexToAscii(hexString):
    ascString = ""
    
    for originalHex in hexString.split():
        formattedHex = originalHex[2:]
        asc = bytes.fromhex(formattedHex).decode('ascii')
        ascString += asc

    print(ascString)


printHexToAscii("0x41 0x53 0x43 0x49 0x49 0x20 0x77 0x68 0x61 0x74 0x20 0x79 0x6f 0x75 0x20 0x64 0x69 0x64 0x20 0x74 0x68 0x65 0x72 0x65")
printHexToAscii("0x39 0x41 0x4d 0x20 0x69 0x73 0x20 0x74 0x6f 0x6f 0x20 0x65 0x61 0x72 0x6c 0x79 0x20 0x66 0x6f 0x72 0x20 0x63 0x6c 0x61 0x73 0x73")
printHexToAscii("0x43 0x6f 0x6d 0x70 0x75 0x74 0x65 0x72 0x73 0x20 0x61 0x72 0x65 0x20 0x6d 0x61 0x67 0x69 0x63")
printHexToAscii("0x57 0x68 0x61 0x74 0x20 0x74 0x68 0x65 0x20 0x68 0x65 0x78 0x3f")

#Problem 4
def printBinToHex(binString):
    binString = binString.replace(' ', '')
    print(hex(int(binString, 2)))

printBinToHex("0000 1011 1010 1110 1101 1110 1010 1101")
printBinToHex("1100 1010 1111 1110 1111 1010 1100 1110")
printBinToHex("1011 1110 1110 1111 1101 0000 0000 1101")
printBinToHex("1111 1111 1111 1111 1001 0000 0110 0010")
    
#Problem 5
def printOctToDec(octString):
    strLen = len(octString) - 1
    decimalNum = 0
    for digit in octString:
        decimalNum += int(digit) * (pow(8, strLen))
        strLen -= 1
    print(decimalNum)

printOctToDec('10')
printOctToDec("42")
printOctToDec("77")
printOctToDec("113")
