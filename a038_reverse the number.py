# tzuhao solution for a038 reverse the number
# tip: should delete the 0 if 0 is in front of the number

while True:
    try:
        ls=list(input())
        # print(ls)
        reversels=[]
        for i in range(len(ls)):
            # print(ls[len(ls)-i-1])
            reversels.append(ls[len(ls)-i-1])
        
        while (reversels[0]=='0'):
            if len(reversels)>1:
                reversels.pop(0)
            if len(reversels)==1:     # to prevent the case '0'
                break
        
        print("".join(reversels))
 
    except:
        break
