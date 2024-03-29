
#Beginning of code, with plaintext and key predefined

roundNumber = 1
C = [] #KeyLeft
D = [] #KeyRight
L = [] #PlainLeft
R = [] #PlainRight
temp = []
roundKey =[]

RoundShift= [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

K= [0,0,0,0,0,0,0,1,  0,0,1,0,0,0,1,1,  0,1,0,0,0,1,0,1,  0,1,1,0,0,1,1,1,  1,0,0,0,1,0,0,1,  1,0,1,0,1,0,1,1,  1,1,0,0,1,1,0,1,  1,1,1,0,1,1,1,1]
plainText = [0,0,0,0,0,0,0,1,  0,0,1,0,0,0,1,1,  0,1,0,0,0,1,0,1,  0,1,1,0,0,1,1,1,  1,0,0,0,1,0,0,1,  1,0,1,0,1,0,1,1,  1,1,0,0,1,1,0,1,  1,1,1,0,1,1,1,1]

#All givens


S1= [
    [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
    [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
    [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
    [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
    ]
S2= [
    [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
    [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
    [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
    [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
    ]
S3= [
    [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
    [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
    [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
    [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
    ]
S4= [
    [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
    [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
    [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
    [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
    ]
S5= [
    [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
    [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
    [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
    [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
    ]
S6= [
    [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
    [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
    [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
    [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
    ]
S7= [
    [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
    [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
    [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
    [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
    ]
S8= [
    [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
    [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
    [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
    [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
    ]

SBox = {'S1': S1,
'S2': S2,
'S3': S3,
'S4': S4,
'S5': S5,
'S6': S6,
'S7': S7,
'S8': S8}


#Key
permutationChoice1 = [57, 49, 41, 33, 25, 17, 9,
                    1, 58, 50, 42, 34, 26, 18,
                    10, 2, 59, 51, 43, 35, 27,
                    19, 11, 3, 60, 52, 44, 36,
                    63, 55, 47, 39, 31, 23, 15,
                    7, 62, 54, 46, 38, 30, 22,
                    14, 6, 61, 53, 45, 37, 29,
                    21, 13, 5, 28, 20, 12, 4]
permutationChoice2 = [14, 17, 11, 24, 1, 5, 3, 28,
                    15, 6, 21, 10, 23, 19, 12, 4,
                    26, 8, 16, 7, 27, 20, 13, 2,
                    41, 52, 31, 37, 47, 55, 30, 40,
                    51, 45, 33, 48, 44, 49, 39, 56,
                    34, 53, 46, 42, 50, 36, 29, 32]

#a
initialPermutation = [58, 50, 42, 34, 26, 18, 10, 2,
                      60, 52, 44, 36, 28, 20, 12, 4,
                      62, 54, 46, 38, 30, 22, 14, 6,
                      64, 56, 48, 40, 32, 24, 16, 8,
                      57, 49, 41, 33, 25, 17, 9, 1,
                      59, 51, 43, 35, 27, 19, 11, 3,
                      61, 53, 45, 37, 29, 21, 13, 5,
                      63, 55, 47, 39, 31, 23, 15, 7]
#b
inverseInitialPermutation = [40, 8, 48, 16, 56, 24, 64, 32,
                            39, 7, 47, 15, 55, 23, 63, 31,
                            38, 6, 46, 14, 54, 22, 62, 30,
                            37, 5, 45, 13, 53, 21, 61, 29,
                            36, 4, 44, 12, 52, 20, 60, 28,
                            35, 3, 43, 11, 51, 19, 59, 27,
                            34, 2, 42, 10, 50, 18, 58, 26,
                            33, 1, 41, 9, 49, 17, 57, 25]
#c
expansionPermutation     = [32, 1, 2, 3, 4, 5,
                            4, 5, 6, 7, 8, 9,
                            8, 9, 10, 11, 12, 13,
                            12, 13, 14, 15, 16, 17,
                            16, 17, 18, 19, 20, 21,
                            20, 21, 22, 23, 24, 25,
                            24, 25, 26, 27, 28, 29,
                            28, 29, 30, 31, 32, 1]
#d
permutationFunction = [16, 7, 20, 21, 29, 12, 28, 17,
                        1, 15, 23, 26, 5, 18, 31, 10,
                        2, 8, 24, 14, 32, 27, 3, 9,
                        19, 13, 30, 6, 22, 11, 4, 25]                           


#DES Functions

def PC(Key, pcNumber): #PermutationChoice
    permutationChoice = []
    if(pcNumber == 1):
        permutationChoice = permutationChoice1
    else:
        permutationChoice = permutationChoice2


    arr = []
    for i in range(len(permutationChoice)):
       arr.append(Key[permutationChoice[i] -1])
    # for i in range(0, len(arr),8):
    #     print(arr[i],arr[i+1],arr[i+2],arr[i+3],arr[i+4],arr[i+5],arr[i+6],arr[i+7])
    return arr

def IP(Plaintext): #InitialPermutation
    
    arr = []
    for i in range(len(initialPermutation)):
       arr.append(Plaintext[initialPermutation[i] -1])
    # for i in range(0, len(arr),8):
    #     print(arr[i],arr[i+1],arr[i+2],arr[i+3],arr[i+4],arr[i+5],arr[i+6],arr[i+7])
    return arr
def EP(rightPlaintext): #ExpansionPermutation
    
    arr = []
    for i in range(len(expansionPermutation)):
       arr.append(rightPlaintext[expansionPermutation[i] -1])
    # for i in range(0, len(arr),6):
    #     print(arr[i],arr[i+1],arr[i+2],arr[i+3],arr[i+4],arr[i+5])
    return arr

def PF(Sbox): #PermutationFunction
    
    arr = []
    for i in range(len(permutationFunction)):
       arr.append(Sbox[permutationFunction[i] -1])
    # for i in range(0, len(arr),8):
    #     print(arr[i],arr[i+1],arr[i+2],arr[i+3],arr[i+4],arr[i+5],arr[i+6],arr[i+7])
    return arr
def inverseIP(Plaintext): #PermutationFunction
    
    arr = []
    for i in range(len(inverseInitialPermutation)):
       arr.append(Plaintext[inverseInitialPermutation[i] -1])
    for i in range(0, len(arr),8):
        print(arr[i],arr[i+1],arr[i+2],arr[i+3],arr[i+4],arr[i+5],arr[i+6],arr[i+7])
    return arr

def roundKeyFunc():
    roundKey = []
    for i in range(RoundShift[roundNumber  -1]):
        C.append(C.pop(0)) #Circular Shift Left of Left Key
        D.append(D.pop(0)) #Circular Shift Left of Right Key
    for i in range(len(C)):
        roundKey.append(C[i])
    for i in range(len(D)):
        roundKey.append(D[i])

    roundKey = PC(roundKey,2)
    # for i in range(0, len(roundKey),6):
    #     print(roundKey[i],roundKey[i+1],roundKey[i+2],roundKey[i+3],roundKey[i+4],roundKey[i+5])
    return roundKey  

def Sbox(ExorK):
    arr = []
    row = 0
    column = 0
    for i in range(0,len(ExorK),6):
        row = int(f"{ExpansionXorKey[i]}{ExpansionXorKey[i+5]}",2)
        column = int(f"{ExpansionXorKey[i+1]}{ExpansionXorKey[i+2]}{ExpansionXorKey[i+3]}{ExpansionXorKey[i+4]}",2)
        value = SBox[f"S{int(i/6 + 1)}"][row][column]
        # print(f"S{int(i/6 + 1)}")
        # print(f"row = {row} \t column = {column} \t value = {value}")
        temp= bin(value)
        binaryNumber = temp[2:]
        binaryNumber = list(map(int, list(binaryNumber)))
        if(len(binaryNumber)==4):
            arr.append(binaryNumber[0])
            arr.append(binaryNumber[1])
            arr.append(binaryNumber[2])
            arr.append(binaryNumber[3])
        if(len(binaryNumber)==3):
            arr.append(0)
            arr.append(binaryNumber[0])
            arr.append(binaryNumber[1])
            arr.append(binaryNumber[2])
        if(len(binaryNumber)==2):
            arr.append(0)
            arr.append(0)
            arr.append(binaryNumber[0])
            arr.append(binaryNumber[1])
        if(len(binaryNumber)==1):
            arr.append(0)
            arr.append(0)
            arr.append(0)
            arr.append(binaryNumber[0])
            
    # for i in range(0, len(arr),4):
    #     print(arr[i],arr[i+1],arr[i+2],arr[i+3])
    return arr

#Additional Functions

def XOR(arr1, arr2):
    arr = []
    # print(len(arr1))
    # print(len(arr2))
    if(len(arr1)!=len(arr2)):
        return
    for i in range(len(arr1)):
        if(arr1[i]==arr2[i]):
            arr.append(0)
        else: 
            if(arr1[i] or arr2[i]):
                arr.append(1)
            else:
                arr.append(0)


    # for i in range(0, len(arr),6):
    #     print(arr[i],arr[i+1],arr[i+2],arr[i+3],arr[i+4],arr[i+5])

    # for i in range(0, len(arr),8):
    #     print(arr[i],arr[i+1],arr[i+2],arr[i+3],arr[i+4],arr[i+5],arr[i+6],arr[i+7])
    return arr

    
def roundPlainText():
    plainText = []
    for i in range(len(L)):
        plainText.append(L[i])
    for i in range(len(R)):
        plainText.append(R[i])
    for i in range(0, len(plainText),8):
            print(plainText[i],plainText[i+1],plainText[i+2],plainText[i+3],plainText[i+4],plainText[i+5],plainText[i+6],plainText[i+7])







##############################################################################################

#CODE




#Permutation Choice 1 happens only once
Key = PC(K,1)
C = Key[:28]
D = Key[28:]
#Initial Permutation happens only once
Initial = IP(plainText)
L=Initial[:32]
R=Initial[32:]


while(roundNumber<=16):
    print(f"\nroundNumber:{roundNumber}")
    roundKey = roundKeyFunc() #gets key for round
    # roundKey = [0,0,0,0,0,0,0,1,  0,0,1,0,0,0,1,1,  0,1,0,0,0,1,0,1,  0,1,1,0,0,1,1,1,  1,0,0,0,1,0,0,1,  1,0,1,0,1,0,1,1]

    Expansion = EP(R)

    ExpansionXorKey = XOR(Expansion, roundKey)

    Sboxed = Sbox(ExpansionXorKey)

    Permutation = PF(Sboxed)

    temp = PermutationXorLeft = XOR(Permutation, L)
    L=[]
    for i in range(len(R)):
        L.append(R[i])
    R=[]
    for i in range(len(temp)):
        R.append(temp[i])
    
    plainText = roundPlainText()
    
    roundNumber+=1

# print(len(plainText),plainText)
cipherText = inverseIP(plainText)