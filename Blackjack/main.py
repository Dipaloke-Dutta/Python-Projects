from typing import final


from art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        score -= 10 * hand.count(11)
    return score

def show_player_hand():
    print("Your Hand:", user)
    print("Player:", calculate_score(user))

def show_dealer_partial():
    print("Dealer's Hand:", [comp[0], "X"])

def show_dealer_hand():
    print("Dealer's Hand:", comp)
    print("Dealer:", calculate_score(comp))

def deal_hand():
    global user, comp
    user = [random.choice(cards), random.choice(cards)]
    comp = [random.choice(cards), random.choice(cards)]

    show_player_hand()
    show_dealer_partial()

    if calculate_score(user) == 21:
        print("Blackjack! You Win!")
        return True
    return False

def hit():
    user.append(random.choice(cards))
    show_player_hand()

    score = calculate_score(user)
    if score == 21:
        print("You have 21!")
        return True
    elif score > 21:
        print("Bust! You Lose!")
        return True
    return False

def stand():
    user_score = calculate_score(user)
    while calculate_score(comp) < 17:
        comp.append(random.choice(cards))

    show_player_hand()
    show_dealer_hand()

    dealer_score = calculate_score(comp)

    if dealer_score > 21:
        print("Dealer busts! You Win!")
    elif dealer_score == user_score:
        print("It's a Draw!")
    elif user_score == 21 or dealer_score > 21 or (user_score > dealer_score):
        print("You Win!")
    else:
        print("You Lose!")

def blackjack():
    while True:
        print(logo)
        play = input("Do you want to play Blackjack? 'y' or 'n': ").lower()
        if play != 'y':
            print("Thanks for playing!")
            break

        global user, comp
        user = []
        comp = []

        if deal_hand():
            continue

        while True:
            choice = input("Enter 'h' to hit or 's' to stand: ").lower()
            if choice == 'h':
                if hit():
                    break
            elif choice == 's':
                break


        if calculate_score(user) <= 21:
            stand()


blackjack()
