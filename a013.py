# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

Rn={'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000,} # 字典：羅馬數字對應的阿拉伯數字
An={k:v for v, k in Rn.items()}                      # 字典：key, value 互換
An_keys=sorted(An.keys(),reverse=True)               # 字典的key是阿拉伯數字，使用sort+reverse:從大排到小

def Rn2An(rn):                 #羅馬數字==>阿拉伯數字
    An=0
    lrn=list(rn)               #把羅馬數字拆開成單一數字的陣列
    lan=[Rn[x] for x in lrn]   #列出對應的阿拉伯數字  
    for i in range(len(lan)-1):
        if lan[i]>=lan[i+1]:
            An=An+lan[i]
        else:
            An=An-lan[i]
    An=An+lan[-1]
    return An

def An2Rn(an):                  #阿拉伯數字==>羅馬數字
    Rn=[]
    for i in range(len(An_keys)):
        if an >= An_keys[i]:
            a=divmod(an,An_keys[i])
            Rn.append(An[An_keys[i]]*a[0])
            an=a[1]
    Rn="".join(Rn)
    return Rn
def diff(num1,num2):
    num1=Rn2An(num1)
    num2=Rn2An(num2)
    diff=abs(num1-num2)
    if diff==0:
        return 'ZERO'
    else:
        return An2Rn(diff)

lines=[]
quiz=str(input())
while(quiz!='#'):
    lines.append(quiz)
    quiz=input()
# print(lines)
for i in range(len(lines)):
    a,b = list(map(str,lines[i].split()))
    # print(a,b)
    print(diff(a,b))