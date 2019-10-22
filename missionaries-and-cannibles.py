import sys
a = ['M', 'M', 'M', 'C', 'C', 'C']
b = []
c = []
ch = 2
print("Rules of Game")
print("1 : Only two or one person can travel by boat forward or reverse direction")
print("2 : M stand for Missionaries")
print("3 : C stand for Cannibles ")
print("4 : If No Cannibles is found more than Missionaries on both side you lose the Game ")


def main():
    send_AtoB = int(input("How many person you want to travel forward by boat? : "))
    if send_AtoB <= ch and send_AtoB != 0:
        for i in range(send_AtoB):
            print("Choose from this : ", a)
            send1 = input("select : ")
            a.remove(send1)
            b.append(send1)
        print("current side : ", a)
        print("another side : ", b)
    else:
        print("only two or one person can travel by boat")
        return main()

    if a.count('M') > 0 and b.count('M'):
        if a.count('C') > a.count('M') or b.count('C') > b.count('M'):
            print("Game Over")
            sys.exit()
    else:
        if a == c or a == b:
            print("You are winner")
            sys.exit()

        else:
            return reverse()


def reverse():
    send_BtoA = int(input("How many person you want to travel reverse by boat? : "))
    if send_BtoA <= ch and send_BtoA != 0:
        for i in range(send_BtoA):
            print("Choose from this : ", b)
            send2 = input("select : ")
            b.remove(send2)
            a.append(send2)
        print("current side : ", b)
        print("another side : ", a)
    else:
        print("only two or one person can travel by boat")
        return reverse()

    if a.count('M') > 0 and b.count('M'):
        if a.count('C') > a.count('M') or b.count('C') > b.count('M'):
            print("Game Over")
            sys.exit()
        else:
            return main()
    else:
        return main()


main()
reverse()
