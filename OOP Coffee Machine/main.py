from menu import *
from coffee_maker import *
from money_machine import *

money_machine= MoneyMachine()
coffee_maker= CoffeeMaker()
menu= Menu()




On=True

if __name__== "__main__":
    while On:
        options= menu.get_items()
        choice= input(f"What would you like yo have? ({options})\n").lower()
        if choice=="off":
            On=False
        elif choice=="report":
            coffee_maker.report()
            money_machine.report()
        else:
            order= menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(order):
                if money_machine.make_payment(order.cost):
                    coffee_maker.make_coffee(order)

