import random as rd

Xcount, Ocount, Ecount = 0, 0, 9
d = {'11': '31', '12': '21', '13': '11', '21': '32', '22': '22', '23': '12', '31': '33', '32': '23', '33': '13'}
def insertXO(a,cc):
    global Xcount, Ocount, Ecount
    if (Xcount == Ocount):
        a[d[cc]] = 'X'
        Xcount += 1
        Ecount -= 1
    else:
        a[d[cc]] = 'O'
        Ocount += 1
        Ecount -= 1


def printA(a):
    print("-" * 9)
    for i in ['1','2','3']:
        print("| ", end="")
        for j in ['1','2','3']:
            if(a[i+j]==''):
                print('','',end='')
            print(a[i+j],'', end="")
        print("|\n")
    print("-" * 9)

def winner(a):
    if (a['13'] == a['23'] and a['23'] == a['33'] and a['33'] == a['13'] and (a['13'] == 'X' or a['13'] == 'O')):
        return a['13']
    elif (a['12'] == a['22'] and a['22'] == a['32'] and a['32'] == a['12'] and (a['12'] == 'X' or a['12'] == 'O')):
        return a['12']
    elif (a['11'] == a['21'] and a['21'] == a['31'] and a['31'] == a['11'] and (a['11'] == 'X' or a['11'] == 'O')):
        return a['11']
    elif (a['13'] == a['12'] and a['12'] == a['13'] and a['13'] == a['11'] and (a['13'] == 'X' or a['13'] == 'O')):
        return a['13']
    elif (a['23'] == a['22'] and a['22'] == a['21'] and a['21'] == a['23'] and (a['23'] == 'X' or a['23'] == 'O')):
        return a['23']
    elif (a['33'] == a['32'] and a['32'] == a['31'] and a['31'] == a['33'] and (a['33'] == 'X' or a['33'] == 'O')):
        return a['33']
    elif (a['13'] == a['22'] and a['22'] == a['31'] and a['31'] == a['13'] and (a['13'] == 'X' or a['13'] == 'O')):
        return a['13']
    elif (a['33'] == a['22'] and a['22'] == a['11'] and a['11'] == a['33'] and (a['33'] == 'X' or a['33'] == 'O')):
        return a['33']
    else:
        return False


def user_2(a):
    global Xcount, Ocount, Ecount, d
    printA(a)
    if (Xcount == Ocount):
        c = input("\nEnter the coordinates: ").split(' ')
        if not ((((int(c[0]) >= 1) and (int(c[0]) <= 3)) and ((int(c[1]) >= 1) and (int(c[1]) <= 3)))):
            print("Coordinates should be from 1 to 3!")
            return
        if (len(c) == 2 and (a[d[c[0] + c[1]]] == 'X' or a[d[c[0] + c[1]]] == 'O')):
            print("This cell is occupied! Choose another one!")
            return
        insertXO(a, c[0] + c[1])
    else:
        c = input("\nEnter the coordinates: ").split(' ')
        if not ((((int(c[0]) >= 1) and (int(c[0]) <= 3)) and ((int(c[1]) >= 1) and (int(c[1]) <= 3)))):
            print("Coordinates should be from 1 to 3!")
            return
        if (len(c) == 2 and (a[d[c[0] + c[1]]] == 'X' or a[d[c[0] + c[1]]] == 'O')):
            print("This cell is occupied! Choose another one!")
            return
        insertXO(a, c[0] + c[1])
def easy_2(a):
    global Xcount, Ocount, Ecount, d
    printA(a)
    if (Xcount == Ocount):
        print('Making move level "easy"\n')
        c1, c2 = str(rd.randint(1, 3)), str(rd.randint(1, 3))
        if (a[d[c1 + c2]] == 'X' or a[d[c1 + c2]] == 'O'):
            print("This cell is occupied! Choose another one!")
            return
        insertXO(a, c1 + c2)
    else:
        print('Making move level "easy"\n')
        c1, c2 = str(rd.randint(1, 3)), str(rd.randint(1, 3))
        if (a[d[c1 + c2]] == 'X' or a[d[c1 + c2]] == 'O'):
            print("This cell is occupied! Choose another one!")
            return
        insertXO(a, c1 + c2)
def user_easy(a):
    global Xcount, Ocount, Ecount, d
    printA(a)
    if (Xcount == Ocount):
        c = input("\nEnter the coordinates: ").split(' ')
        if not ((((int(c[0]) >= 1) and (int(c[0]) <= 3)) and ((int(c[1]) >= 1) and (int(c[1]) <= 3)))):
            print("Coordinates should be from 1 to 3!")
            return
        if (len(c) == 2 and (a[d[c[0] + c[1]]] == 'X' or a[d[c[0] + c[1]]] == 'O')):
            print("This cell is occupied! Choose another one!")
            return
        insertXO(a, c[0] + c[1])
    else:
        print('Making move level "easy"\n')
        c1,c2=str(rd.randint(1,3)),str(rd.randint(1,3))
        print(c1,c2)
        if (a[d[c1 + c2]] == 'X' or a[d[c1 + c2]] == 'O'):
            print("This cell is occupied! Choose another one!")
            return
        insertXO(a, c1 + c2)

def easy_user(a):
    global Xcount, Ocount, Ecount, d
    printA(a)
    if (Xcount == Ocount):
        print('Making move level "easy"\n')
        c1, c2 = str(rd.randint(1,3)), str(rd.randint(1,3))
        if (a[d[c1 + c2]] == 'X' or a[d[c1 + c2]] == 'O'):
            print("This cell is occupied! Choose another one!")
            return
        insertXO(a, c1 + c2)
    else:
        c = input("\nEnter the coordinates: ").split(' ')
        if not ((((int(c[0]) >= 1) and (int(c[0]) <= 3)) and ((int(c[1]) >= 1) and (int(c[1]) <= 3)))):
            print("Coordinates should be from 1 to 3!")
            return
        if (len(c) == 2 and (a[d[c[0] + c[1]]] == 'X' or a[d[c[0] + c[1]]] == 'O')):
            print("This cell is occupied! Choose another one!")
            return
        insertXO(a, c[0] + c[1])


def start(a,a1,a2):
    w = False
    if(a1==a2 and a1=='user'):
        while (w == False):
            user_2(a)
            w = winner(a)
            if (Ecount == 0):
                break

    elif(a1==a2 and a1=='easy'):
        while (w == False):
            easy_2(a)
            w = winner(a)
            if (Ecount == 0):
                break
    elif(a1=='user' and a2=='easy'):
        while (w == False):
            user_easy(a)
            w = winner(a)
            if (Ecount == 0):
                break
    else:
        while (w == False):
            easy_user(a)
            w = winner(a)
            if (Ecount == 0):
                break
    if(w != False):
        print(w,"wins")
        return
    if (Ecount == 0):
        print("Draw")



while(1):
    D = {'11': '', '12': '', '13': '', '21': '', '22': '', '23': '', '31': '', '32': '', '33': ''}
    s = input("Input command: ").split(' ')
    if (len(s)==3):
        for i in s:
            if (i in ['start','easy','user','exit']):
                continue
            else:
                break
        if ((s[0] == 'start') and ((s[1] == 'user' or s[1] == 'easy') and (s[2] == 'user' or s[2] == 'easy'))):
            start(D,s[1],s[2])
        else:
            print("Bad parameters!")
    elif(len(s)==1):
        if(s[0]=='exit'):
            exit()
    else:
        print("Bad parameters!")




