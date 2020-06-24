import random as rd

Xcount,Ocount,Ecount=0,0,9

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
        c1, c2 = str(rd.randint(1, 3)), str(rd.randint(1, 3))
        if (a[d[c1 + c2]] == 'X' or a[d[c1 + c2]] == 'O'):
            print("This cell is occupied! Choose another one!")
            return
        insertXO(a, c1 + c2)
def easy_user(a):
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
        c = input("\nEnter the coordinates: ").split(' ')
        if not ((((int(c[0]) >= 1) and (int(c[0]) <= 3)) and ((int(c[1]) >= 1) and (int(c[1]) <= 3)))):
            print("Coordinates should be from 1 to 3!")
            return
        if (len(c) == 2 and (a[d[c[0] + c[1]]] == 'X' or a[d[c[0] + c[1]]] == 'O')):
            print("This cell is occupied! Choose another one!")
            return
        insertXO(a, c[0] + c[1])

def medium_2(a):
    global Xcount, Ocount, Ecount, d
    printA(a)
    if (Xcount == Ocount):
        print('Making move level "medium"\n')
        if (twostep(a)):
            c = twostep(a)
            if (a[d[c[0]+c[1]]] == 'X' or a[d[c[0]+c[1]]] == 'O'):
                print("This cell is occupied! Choose another one!")
                return
            insertXO(a,c[0]+c[1])
        else:
            c = str(rd.randint(1, 3)) + str(rd.randint(1, 3))
            if (a[d[c[0]+c[1]]] == 'X' or a[d[c[0]+c[1]]] == 'O'):
                print("This cell is occupied! Choose another one!")
                return
            insertXO(a,c[0]+c[1])
    else:
        print('Making move level "medium"\n')
        if (twostep(a)):
            c = twostep(a)
            if (a[d[c[0]+c[1]]] == 'X' or a[d[c[0]+c[1]]] == 'O'):
                print("This cell is occupied! Choose another one!")
                return
            insertXO(a,c[0]+c[1])
        else:
            c = str(rd.randint(1, 3)) + str(rd.randint(1, 3))
            if (a[d[c[0]+c[1]]] == 'X' or a[d[c[0]+c[1]]] == 'O'):
                print("This cell is occupied! Choose another one!")
                return
            insertXO(a,c[0]+c[1])
def user_medium(a):
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
        print('Making move level "medium"\n')
        if (twostep(a)):
            c = twostep(a)
            if (a[d[c[0]+c[1]]] == 'X' or a[d[c[0]+c[1]]] == 'O'):
                print("This cell is occupied! Choose another one!")
                return
            insertXO(a,c[0]+c[1])
        else:
            c = str(rd.randint(1, 3)) + str(rd.randint(1, 3))
            if (a[d[c[0]+c[1]]] == 'X' or a[d[c[0]+c[1]]] == 'O'):
                print("This cell is occupied! Choose another one!")
                return
            insertXO(a,c[0]+c[1])
def medium_user(a):
    global Xcount, Ocount, Ecount, d
    printA(a)
    if (Xcount == Ocount):
        print('Making move level "medium"\n')
        if (twostep(a)):
            c = twostep(a)
            if (a[d[c[0]+c[1]]] == 'X' or a[d[c[0]+c[1]]] == 'O'):
                print("This cell is occupied! Choose another one!")
                return
            insertXO(a,c[0]+c[1])
        else:
            c = str(rd.randint(1, 3)) + str(rd.randint(1, 3))
            if (a[d[c[0]+c[1]]] == 'X' or a[d[c[0]+c[1]]] == 'O'):
                print("This cell is occupied! Choose another one!")
                return
            insertXO(a,c[0]+c[1])
    else:
        c = input("\nEnter the coordinates: ").split(' ')
        if not ((((int(c[0]) >= 1) and (int(c[0]) <= 3)) and ((int(c[1]) >= 1) and (int(c[1]) <= 3)))):
            print("Coordinates should be from 1 to 3!")
            return
        if (len(c) == 2 and (a[d[c[0] + c[1]]] == 'X' or a[d[c[0] + c[1]]] == 'O')):
            print("This cell is occupied! Choose another one!")
            return
        insertXO(a, c[0] + c[1])
def easy_medium(a):
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
        print('Making move level "medium"\n')
        if (twostep(a)):
            c = twostep(a)
            if (a[d[c[0]+c[1]]] == 'X' or a[d[c[0]+c[1]]] == 'O'):
                print("This cell is occupied! Choose another one!")
                return
            insertXO(a,c[0]+c[1])
        else:
            c = str(rd.randint(1, 3)) + str(rd.randint(1, 3))
            if (a[d[c[0]+c[1]]] == 'X' or a[d[c[0]+c[1]]] == 'O'):
                print("This cell is occupied! Choose another one!")
                return
            insertXO(a,c[0]+c[1])
def medium_easy(a):
    if (Xcount == Ocount):
        print('Making move level "medium"\n')
        if (twostep(a)):
            c = twostep(a)
            if (a[d[c[0]+c[1]]] == 'X' or a[d[c[0]+c[1]]] == 'O'):
                print("This cell is occupied! Choose another one!")
                return
            insertXO(a,c[0]+c[1])
        else:
            c = str(rd.randint(1, 3)) + str(rd.randint(1, 3))
            if (a[d[c[0]+c[1]]] == 'X' or a[d[c[0]+c[1]]] == 'O'):
                print("This cell is occupied! Choose another one!")
                return
            insertXO(a,c[0]+c[1])
    else:
        print('Making move level "easy"\n')
        c1, c2 = str(rd.randint(1, 3)), str(rd.randint(1, 3))
        if (a[d[c1 + c2]] == 'X' or a[d[c1 + c2]] == 'O'):
            print("This cell is occupied! Choose another one!")
            return
        insertXO(a, c1 + c2)
def twostep(a):
    #d = {'11': '31', '12': '21', '13': '11', '21': '32', '22': '22', '23': '12', '31': '33', '32': '23', '33': '13'}
    if ((a['13'] == a['23'] and a['23'] != a['33']) and (a['13'] == 'X' or a['13'] == 'O') and a['33']==''):
        print(1)
        return('31')
    elif ((a['23'] == a['33'] and a['33'] != a['13']) and (a['23'] == 'X' or a['23'] == 'O') and a['13']==''):
        print(2)
        return('33')
    elif ((a['13'] == a['33'] and a['33'] != a['23']) and (a['23'] == 'X' or a['23'] == 'O') and a['23']==''):
        print(3)
        return('32')
    elif ((a['12'] == a['22'] and a['22'] != a['32']) and (a['12'] == 'X' or a['12'] == 'O') and a['32']==''):
        print(4)
        return('21')
    elif ((a['22'] == a['32'] and a['32'] != a['12']) and (a['22'] == 'X' or a['22'] == 'O') and a['12']==''):
        print(5)
        return('23')
    elif ((a['12'] == a['32'] and a['32'] != a['22']) and (a['12'] == 'X' or a['12'] == 'O') and a['22']==''):
        print(6)
        return('22')
    elif ((a['11'] == a['21'] and a['21'] != a['31']) and (a['11'] == 'X' or a['11'] == 'O') and a['31']==''):
        print(7)
        return('11')
    elif ((a['21'] == a['31'] and a['31'] != a['11']) and (a['21'] == 'X' or a['21'] == 'O') and a['11']==''):
        print(8)
        return('13')
    elif ((a['11'] == a['31'] and a['31'] != a['21']) and (a['11'] == 'X' or a['11'] == 'O') and a['21']==''):
        print(9)
        return('12')
    elif ((a['11'] == a['12'] and a['12'] != a['13']) and (a['11'] == 'X' or a['11'] == 'O') and a['13']==''):
        print(10)
        return('33')
    elif ((a['13'] == a['12'] and a['12'] != a['11']) and (a['13'] == 'X' or a['13'] == 'O') and a['11']==''):
        print(11)
        return('13')
    elif ((a['13'] == a['11'] and a['11'] != a['12']) and (a['13'] == 'X' or a['13'] == 'O') and a['12']==''):
        print(12)
        return('23')
    elif ((a['21'] == a['22'] and a['22'] != a['23']) and (a['21'] == 'X' or a['22'] == 'O') and a['23']==''):
        print(13)
        return('32') 
    elif ((a['23'] == a['22'] and a['22'] != a['21']) and (a['23'] == 'X' or a['23'] == 'O') and a['21']==''):
        print(14)
        return('12')
    elif ((a['21'] == a['23'] and a['23'] != a['22']) and (a['21'] == 'X' or a['22'] == 'O') and a['22']==''):
        print(15)
        return('22')
    elif ((a['31'] == a['32'] and a['32'] != a['33']) and (a['31'] == 'X' or a['31'] == 'O') and a['33']==''):
        print(16)
        return('31')
    elif ((a['33'] == a['32'] and a['32'] != a['31']) and (a['33'] == 'X' or a['33'] == 'O') and a['31']==''):
        print(17)
        return('11')
    elif ((a['31'] == a['33'] and a['33'] != a['32']) and (a['31'] == 'X' or a['31'] == 'O') and a['32']==''):
        print(18)
        return('21')
    elif ((a['13'] == a['22'] and a['22'] != a['31']) and (a['13'] == 'X' or a['13'] == 'O') and a['31']==''):
        print(19)
        return('11')
    elif ((a['22'] == a['31'] and a['31'] != a['13']) and (a['22'] == 'X' or a['22'] == 'O') and a['13']==''):
        print(20)
        return('33')
    elif ((a['13'] == a['31'] and a['31'] != a['22']) and (a['13'] == 'X' or a['13'] == 'O') and a['22']==''):
        print(21)
        return('22')
    elif ((a['11'] == a['22'] and a['22'] != a['33']) and (a['11'] == 'X' or a['11'] == 'O') and a['33']==''):
        print(22)
        return('31')
    elif ((a['33'] == a['22'] and a['22'] != a['11']) and (a['33'] == 'X' or a['33'] == 'O') and a['11']==''):
        print(23)
        return('13')
    elif ((a['11'] == a['33'] and a['33'] != a['22']) and (a['11'] == 'X' or a['11'] == 'O') and a['22']==''):
        print(24)
        return('22')
    else:
        return False
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
    elif(a1=='easy' and a2=='user'):
        while (w == False):
            easy_user(a)
            w = winner(a)
            if (Ecount == 0):
                break
    elif(a1==a2 and a1=='medium'):
        while (w == False):
            medium_2(a)
            w = winner(a)
            if (Ecount == 0):
                break
    elif(a1=='medium' and a2=='user'):
        while (w == False):
            medium_user(a)
            w = winner(a)
            if (Ecount == 0):
                break
    elif(a1=='user' and a2=='medium'):
        while (w == False):
            user_medium(a)
            w = winner(a)
            if (Ecount == 0):
                break
    elif(a1=='medium' and a2=='easy'):
        while (w == False):
            medium_easy(a)
            w = winner(a)
            if (Ecount == 0):
                break
    else:
        while (w == False):
            medium_easy(a)
            w = winner(a)
            if (Ecount == 0):
                break
    if(w != False):
        printA(a)
        print(w,"wins")
        return
    print(Ecount)
    if (Ecount == 0):
        printA(a)
        print("ecount=0")
        print("Draw")
while(1):
    D = {'11': '', '12': '', '13': '', '21': '', '22': '', '23': '', '31': '', '32': '', '33': ''}
    s = input("Input command: ").split(' ')
    if (len(s)==3):
        for i in s:
            if (i in ['start','easy','user','exit','medium']):
                continue
            else:
                break
        if ((s[0] == 'start') and ((s[1] == 'user' or s[1] == 'easy' or s[1] == 'medium') and (s[2] == 'user' or s[2] == 'easy' or s[2] == 'medium'))):
            Xcount, Ocount, Ecount = 0, 0, 9
            start(D,s[1],s[2])
        else:
            print("Bad parameters!")
    elif(len(s)==1):
        if(s[0]=='exit'):
            exit()
        else:
            print('Bad parameters!')
    else:
        print("Bad parameters!")