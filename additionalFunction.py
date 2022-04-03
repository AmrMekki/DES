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