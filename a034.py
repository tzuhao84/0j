# tzuhao solution for zerojudge a034(binary)

while True:
    try:
        dec=int(input())
        index=0
        while(dec//(2**index)>1):
            # print('index=',index)
            # print('dec//(2**index)=',dec//(2**index))
            index=index+1   
        # print('highest digit=',index)
        binarylist=[]
        for i in range(index,-1,-1):
            modulus=dec%(2**index)
            # print('modulus=',modulus)
            tobinary=dec//(2**index)
            binarylist.append(tobinary)
            dec=modulus
            # print('dec=',dec)
            index=index-1

        binarylist=[str(i) for i in binarylist]
        # print('binarylist=',binarylist)
        s="".join(binarylist)
        print(s)

    except:
        break