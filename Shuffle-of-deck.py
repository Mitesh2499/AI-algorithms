import itertools,random
cards=['Spade','Heart','Diamonds','Club']
deck=list(itertools.product(range(1,14),cards))
random.shuffle(deck)
no_of_cards=int(input("How many cards do you wantto display ? "))
print("You got")
for i,j in deck[:no_of_cards]:
    print(i,j)
