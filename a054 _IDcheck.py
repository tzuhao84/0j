# tzuhao solution for zerojudge a054
id2num={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':34,'J':18,'K':19,'L':20,
        'M':21,'N':22,'O':35,'P':23,'Q':24,'R':25,'S':26,'T':27,'U':28,'V':29,'W':32,'X':30,'Y':31,'Z':33}
num2id={v:k for k,v in id2num.items()}  # to exchange the value and key in dictionary
# print(num2id)

# for i in range()
num2sum={}
for key in num2id.keys(): # keys()方法會讓for迴圈將每個鍵存到key變數中
    # print("key : ",key) # 印出鍵
    ls=list(str(key))
    # print(ls)
    sum=int(ls[0])*1+int(ls[1])*9
    num2sum[key]=sum
# print(num2sum)
sum2num={v:k for k,v in num2sum.items()}  # to exchange the value and key in dictionary
# print(sum2num)

sum2id={}
for key in sum2num.keys():
    sum2id[key]=num2id.get(sum2num.get(key))
# print(sum2id)

while True:
    try:
        ID=list(map(int,input()))
        sum=0
        factor=8
        for i in range(0,8):
            sum=sum+ID[i]*(factor-i)
        
        ck=ID[8] # ck for check number
        ans=[]
        for key in sum2id.keys():
            if (key+sum)%10 == (10-ck):
                ans.append(sum2id.get(key))
        print("".join(ans))
        # print(sum)
    except EOFError:
        break