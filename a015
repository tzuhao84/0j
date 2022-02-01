def transpose(m,n):
    m=int(m)        # m: Row number
    n=int(n)        # n: Column number
    matrix=[]
    matrixT=[[0 for x in range(m)] for x in range(n)]
    #print(matrixT)

    counter=0
    while counter<m:
        ele=input() #ele: elements
        ele=list(map(int,ele.split()))
        #print('ele=',ele)
        matrix.append(ele)
        #print('matrix=',matrix)
        counter=counter+1
        
    for i in range(n):
        if  i>0:
                print('')
        for j in range(m):
                matrixT[i][j]=matrix[j][i]
                print(matrixT[i][j],end=' ')
    print('\n')       
    #print(matrixT)

    

while True:
    try:
        row,col=list(map(int,input().split()))
        #print(col)
        transpose(row,col)
        #rowcol=input()
    except EOFError:
        break
        
