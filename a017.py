#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 21:25:50 2022

@author: tzuhao
"""

# a017 五則運算的ans

operator_0=['(',')']
operator_1=['*','/','%']
operator_2=['+','-']
lb = []
rb = []
#operand = numbers
# function
def multiply(a,b):
    a = int(a)
    b = int(b)
    return a*b
def divide(a,b):
    a = int(a)
    b = int(b)
    return int(a/b)   # 題目說計算過程中不會有小數點
def add(a,b):
    a = int(a)
    b = int(b)
    return a+b
def minus(a,b):
    a = int(a)
    b = int(b)
    return a-b
def mod(a,b):
    a = int(a)
    b = int(b)
    return a%b    

# do calculation
def calc(ls):
    while [True for i in ls if i in operator_1]:
        for i in range(len(ls)):
            if ls[i] == '*':
                ls[i] = multiply(ls[i-1],ls[i+1])
                del ls[i-1:i+2:2]
                break
            if ls[i] == '/':
                ls[i] = divide(ls[i-1],ls[i+1])
                del ls[i-1:i+2:2]
                break
            if ls[i] == '%':
                ls[i] = mod(ls[i-1],ls[i+1])
                del ls[i-1:i+2:2]
                break
                
    while [True for i in ls if i in operator_2]:
        for i in range(len(ls)):
            if ls[i] == '+':
                ls[i] = add(ls[i-1],ls[i+1])
                del ls[i-1:i+2:2]
                break
            if ls[i] == '-':
                ls[i] = minus(ls[i-1],ls[i+1])
                del ls[i-1:i+2:2]
                break
    return ls

def brackets(ls):
    while [True for i in ls if i in operator_0]:
        for i in range(len(ls)):
            if ls[i] == '(':
                lb = i
                continue
            if ls[i] == ')':
                rb = i
                break
        brackets_ls=ls[lb+1:rb]
        ls[rb] = calc(brackets_ls)[0]
        del ls[lb:rb]
    return ls

while True:
    try:
        #quiz=input()
        quiz=list(map(str,input().split()))
        while len(quiz)!= 1:
            brackets(quiz)    # 先作()內運算
            calc(quiz)
        print(quiz[0])
        
    except EOFError:
        break
        