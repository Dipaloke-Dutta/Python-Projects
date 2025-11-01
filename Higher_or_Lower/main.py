import game_data
import art

import random

def higher_or_lower():
    print(art.logo)
    a= random.choice(game_data.data)
    score = 0
    b= random.choice(list(filter(lambda x: x !=a, game_data.data)))
    while True:

        a_dat= list(filter(lambda x: x in a.values(),a.values()))
        b_dat= list(filter(lambda x: x in b.values(),b.values()))
        print(f"Compare A: {a_dat[0]}, a {a_dat[2]} from {a_dat[3]}")
        print(art.vs)
        print(f"Compare B: {b_dat[0]}, a {b_dat[2]} from {b_dat[3]}")
        r= input("Who has more followers? Type 'A' or 'B': ").upper()
        if (r=='A' and a_dat[1]>b_dat[1] )or (r=='B' and b_dat>a_dat):
            score+=1
            print("Correct! Your Score:",score)
            a= b.copy()
            b= random.choice(list(filter(lambda x: x !=a, game_data.data)))
            continue
        else:
            break
    print(f"Wrong! Your final score is: {score}")


if __name__== "__main__":
    while True:
        yn= input("Do you want to play? Enter 'y' or n. ").lower()
        if yn=='y':
            higher_or_lower()
        else:
            break






