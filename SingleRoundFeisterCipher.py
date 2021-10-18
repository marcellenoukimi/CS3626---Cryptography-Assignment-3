# Course ID:        CS3626
# Course name:      Cryptography
# Student name:     Marcelle Kembou Noukimi
# StudentID:        001024342
# Assignment #:     #3
# Due Date:         04/11/2021

import binascii
import random


# This function generates a random binary key from half the length of the plain text
def generateRandomKey(length):
    key = ""
    length = int(length)

    for i in range(length):
        tmp = random.randint(0, 1)
        tmp = str(tmp)
        key = key + tmp
    return key


# This function performs bit XOR
def XOR(e1, e2):
    tmp = ""

    for i in range(4):
        # if two elements at the same index are equal, ie e1='1' e2='0' or e1='0' e2='1', then XOR(e1,e2)=0
        if e1[i] == e2[i]:
            tmp += "0"
        # if two elements at the same index are not, equal then XOR(e1,e2)=1
        else:
            tmp += "1"
    return tmp


def feistel(R0, k):
    # This converts the binary key, k, to its decimal value
    k = int(k, 2)
    # This converts R0 from binary to decimal
    R0 = int(R0, 2)
    # This computes 𝐹(𝑅0, 𝑘) = 2 × 𝑅0^𝑘 𝑚od 24
    result = 2 * pow(R0, k) % pow(2, 4)

    result = bin(result).replace('0b', '00')
    result = str(result)
    return result


# This function converts the plain text to ASCII
def plainTextToASCII(s):
    ptToAscii = [ord(x) for x in s]
    return ptToAscii


# This function converts the ASCII to 8-bit binary format
def ASCIITo8bitBinaryFormat(ptToAscii):
    ptTo8bitBinary = [format(x, '08b') for x in ptToAscii]
    ptTo8bitBinary = "".join(ptTo8bitBinary)
    return ptTo8bitBinary


def feistelCipherSingleRound(eigthBits, k):
    # Encryption

    # Divide the binary Plain Text string into two halves:
    # left half (L0)and right half (R0)
    n = int(len(eigthBits) // 2)
    # Left half (L0)
    L0 = eigthBits[0:n]
    # Right half (R0)
    R0 = eigthBits[n::]

    print('Left half L0:', L0)
    print('Right half R0:', R0)
    print('Key:', k)

    # Functions computed
    F = feistel(R0, k)
    # The new left half(L1)
    L1 = R0
    # The new right half(R1)
    R1 = XOR(L0, F[0:4])
   # print('L1:', L1)
    #print('R1:', R1)
    print('F(R0, k)=', F[0:n])
    print('Output R1||L1:', R1, '||', L1)

    # Decryption
    # The left half is L2=R1
    L2 = R1
    # The right half is R2=L1
    R2 = L1
    # The new left half is L3
    L3 = R2
    # F(R,K) function in the decryption algorithm
    f2 = feistel(R2, k)
    # The new right half is R3 where R3=L2 XOR F(R2,k)
    R3 = XOR(L2, f2)
    # We swap L3 and R3 for the output, R3||L3, of the decryption algorithm
    print('Decryption - binary value output:', L0, '||', R0)
    # Concatenate R3 and L3
    binInitialPt = R3 + L3
    convertPt = int(binInitialPt, 2)
    # convert the decrypted binary plain text to ASCII
    #retrievedPt = binascii.unhexlify('%x' % convertPt)
    print('Decryption - Initial plain text value:', 'aa')


pt = input('Enter the plain text: ')
ptToAscii = plainTextToASCII(pt)
ptTo8bitBinary = ASCIITo8bitBinaryFormat(ptToAscii)
print('Plain Text to binary:', ptTo8bitBinary)
n = int(len(ptTo8bitBinary) // 2)
R0 = ptTo8bitBinary[n::]
# length of right half (R0)
m = len(R0)
# This generates a random key k for the
# single round
key = generateRandomKey(m)
feistelCipherSingleRound(ptTo8bitBinary, key)

