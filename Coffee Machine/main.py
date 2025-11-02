from art import logo
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}

money=1000
change=0

def resource_report():
    global money
    for k, v in resources.items():
        print(f"{k}: {v}")
    money= round(money,2)
    print(f"money: {money}")

def resource_present(st):
    if (resources['water']>= menu[st]['ingredients']['water']) and (resources['milk']>= menu[st]['ingredients']['milk']) and (resources['coffee']>= menu[st]['ingredients']['coffee']):
        print(f"All resources are present.")
        return True
    else:
        return False

def resource_absent(st):
    if resources['water'] >= menu[st]['ingredients']['water']:
        print("Sorry there is not enough water")
        return
    elif resources['coffee'] >= menu[st]['ingredients']['coffee']:
        print("Sorry there is not enough coffee")
        return
    elif resources['milk'] >= menu[st]['ingredients']['milk']:
        print("Sorry there is not enough milk")
        return



def take_money(st):
    global money
    global change
    q = float(input("Enter quarters: "))
    di = float(input("Enter dimes: "))
    n = float(input("Enter nickles: "))
    p = float(input("Enter pennies: "))
    d = float(input("Enter dollars: "))
    m_in = 0.25 * q + 0.1 * di + 0.05 * n + 0.01 * p + d
    if m_in==menu[st]['cost']:
        money+=m_in
        return True
    elif menu[st]['cost']<=m_in:
        change= m_in- menu[st]['cost']
        money= money+ m_in - change
        return True
    elif m_in< menu[st]['cost']:
        return False



def make_order(st):
    resources["water"]-= menu[st]["ingredients"]['water']
    resources["coffee"] -= menu[st]["ingredients"]['coffee']
    resources["milk"] -= menu[st]["ingredients"]['milk']
    print(f"Here's your ☕ {st}. Enjoy!")

def coffee_machine():
    global change
    while True:
        order= input("What would you like?(espresso/latte/cappuccino)\n").lower()
        if order=='off':
            exit(0)
        elif order=="report":
            resource_report()
        else:
            if resource_present(order):
                if take_money(order):
                    if change!= 0:
                        change= round(change,2)
                        print(f"Here is ${change} in change.")
                        change=0
                    print(f"Making one {order} for you")
                    make_order(order)
                else:
                    print("Sorry there's not enough money. Money refunded.")
                    continue
            else:
                resource_absent(order)
                continue


if __name__== "__main__":
    print(logo)
    coffee_machine()












