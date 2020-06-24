Xcount,Ocount,Ecount=0,0,0

def insertXO(a):
    global Xcount,Ocount,Ecount
    c = input("\nEnter the coordinates: ").split(' ')
    if(len(c)==2):
        c1,c2=c[0],c[1]
        cc=c1+c2
    if not((c[0].isdigit() and c2.isdigit())):
        print("You should enter numbers!")
        return 1
    if not((((int(c1)>=1) and (int(c1)<=3)) and ((int(c2)>=1) and (int(c2)<=3)))):
        print("Coordinates should be from 1 to 3!")
        return 1
    if (a[cc]=='X' or a[cc]=='O'):
        print("This cell is occupied! Choose another one!")
        insertXO(a)
    else:
        if(Xcount==Ocount):
            a[cc]='X'
            Xcount+=1
            Ecount-=1
        else:
            a[cc]='O'
            Ocount+=1
            Ecount-=1
    return a
            
def printA(a):
    print("-"*9)
    for i in ['3','2','1']:
        print("| ",end="")
        for j in ['1','2','3']:
            print(a[j+i],'',end="")
        print("|\n")
    print("-"*9)
    
def winner(a):
    if(a['13']==a['23'] and a['23']==a['33'] and a['33']==a['13'] and (a['13']=='X' or a['13']=='O')):
        return a['13']
    elif(a['12']==a['22'] and a['22']==a['32'] and a['32']==a['12'] and (a['12']=='X' or a['12']=='O')):
        return a['12']
    elif(a['11']==a['21'] and a['21']==a['31'] and a['31']==a['11'] and (a['11']=='X' or a['11']=='O')):
        return a['11']
    elif(a['13']==a['12'] and a['12']==a['13'] and a['13']==a['11'] and (a['13']=='X' or a['13']=='O')):
        return a['13']
    elif(a['23']==a['22'] and a['22']==a['21'] and a['21']==a['23'] and (a['23']=='X' or a['23']=='O')):
        return a['23']
    elif(a['33']==a['32'] and a['32']==a['31'] and a['31']==a['33'] and (a['33']=='X' or a['33']=='O')):
        return a['33']
    elif(a['13']==a['22'] and a['22']==a['31'] and a['31']==a['13'] and (a['13']=='X' or a['13']=='O')):
        return a['13']
    elif(a['33']==a['22'] and a['22']==a['11'] and a['11']==a['33'] and (a['33']=='X' or a['33']=='O')):
        return a['33']
    else:
        return False

    

str=input("Enter cells: ")
d={}
a=1
ind=0
for i in ['3','2','1']:
    for j in ['1','2','3']:
        if(str[ind]=='_'):
            d[j+i]=' '
            Ecount+=1
        elif(str[ind]=='X'):
            d[j+i]='X'
            Xcount+=1
        else:
            d[j+i]='O'
            Ocount+=1
        ind+=1
printA(d)
while(a==1):
    a=insertXO(d)
printA(d)
w=winner(d)
if(w!=False):
    print(w,"wins")
if(w==False):
    if(Ecount!=0):
        print("Game not finished")
    else:
        print("Draw")