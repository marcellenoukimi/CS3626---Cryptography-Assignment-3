# CS3626---Cryptography-Assignment-3
**Problems:**

The aim of this assignment is to implement a Feistel cipher round function (single round)
which consists of the following steps:

**1. Implementing a Feistel Cipher β 70 points**

Step 1: The function takes as input 8 bits and the 4-bit key _k_.

Step 2: The binary is divided into two halves (πΏ0 and R0).

Step 3: The function computes L1 = R0 and R1 = L0 β F(R0,π), where
        F(R0, k)= 2 Γ R0^k mod 2^4
        
Step 4: The function performs a swapping of L1 and R1, then outputs R1||L1.

**2. Combining with Assignment 1 β 20 points**

Improve your implementation for 1 by using your Text Converter, so it can handle a
string from a user and output a string.

Hint: you can execute the Feistel function once for each letter, i.e., the plaintext βhelloβ
needs five executions.

**3. Make some test codes to show the correctness of your implementation β 10 points**

Note: It is recommended to exchange a ciphertext generated by the implementation with your
friend and check the decryption algorithm successfully recovers the original plaintext
