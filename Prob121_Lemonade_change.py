bills=[5,5,5,10,20]
#per glass lemonade price is 5 rupees
purse={}
n=len(bills)
dol5,dol10,dol20=[],[],[]
i=0
while i<n:
    if bills[i]==5:
        dol5.append(bills[i])
        i+=1
    elif bills[i]==10:
        if len(dol5)==0:
            print (False)
            break
        else:
            dol5.pop()
            dol10.append(bills[i])
            i+=1
    elif bills[i]==20:
        if len(dol5)>=3:
            dol5.pop()
            dol5.pop()
            dol5.pop()
            dol20.append(bills[i])
        elif len(dol5)>=1 and len(dol10)>=1:
            dol5.pop()
            dol10.pop()
            dol20.append(bills[i])
            i+=1
        else:
            print(False)
            break
    else:
        print(False)
        break
else:
    print(True)


