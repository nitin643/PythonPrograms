def isbinary(str):
    for i in range(len(str)):
        if str[i]=='0':
            continue
        elif str[i]=='1':
            continue
        else:
            return False
    return True    
test=[1010101010]
print(isbinary(test))