choices=[]
for x in range(0,9):
    choices.append(str(x+1))
playerOneTurn=True
winner=False
def printBoard():
    print('\n-----')
    print('|'+choices[0]+'|'+choices[1]+'|'+choices[2]+'|')
    print('-----')
    print('|'+choices[3]+'|'+choices[4]+'|'+choices[5]+'|')
    print('-----')
    print('|'+choices[6]+'|'+choices[7]+'|'+choices[8]+'|')
    print('-----\n')
while not winner:
    printBoard()
    if playerOneTurn:
        print("player 1:")
    else:
        print("player 2:")
    try:
        choice=int(input(">>"))
        if choices[choice-1]=='X' or choices[choice-1]=='O':
            print("illegal move Try again")
            break
    except exception:
        print("illegal move,please try again")
    if playerOneTurn:
        if choices[choice-1]=='X':
            print("invalid step")
        else:
            choices[choice-1]='X'
    else:
        if choices[choice-1]=='O':
            print("invalid step")
        else:
            choices[choice-1]='O'
    playerOneTurn=not playerOneTurn
    for x in range(0,3):
        y=x*3
        if(choices[y]==choices[(y+1)]and choices[y]==choices[(y+2)]):
            winner=True
            print("player"+str(int(playerOneTurn+1))+"Wins!\n")
        if(choices[x]==choices[(x+3)]and choices[x]==choices[(x+6)]):
            winner=True
            print("player"+str(int(playerOneTurn+1))+"Wins!\n")
    if((choices[0]==choices[4]and choices[0]==choices[8])or(choices[2]==choices[4]==choices[6])):
        winner=True
        print("Player"+str(int(playerOneTurn+1))+"Wins!\n")
