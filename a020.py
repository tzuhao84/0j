id_dict={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':34,'J':18,'K':19,'L':20,
              'M':21,'N':22,'O':35,'P':23,'Q':24,'R':25,'S':26,'T':27,'U':28,'V':29,'W':32,'X':30,'Y':31,'Z':33}
#print('Please enter your ID:')
ID = list(map(str,input('please enter your ID number:\n')))
# print(ID)
number = str(id_dict[ID[0]])  # transform the alphabet into number
units=list(map(str,number))[1]
tens =list(map(str,number))[0]
number = int(units)*9+int(tens)

for i in range(1,9):
    #print('9-i=',9-i,'*ID,',int(ID[i]))
    number = number + (9-i)*int(ID[i])
number = number + int(ID[9])
#print(number)
if number%10==0:
    print('real')
else:
    print('fake')
