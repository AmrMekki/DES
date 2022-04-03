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
    
    

