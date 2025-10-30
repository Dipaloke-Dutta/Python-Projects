from os import system
from art import logo
print(logo)
bids= {}
new_person= True
while(new_person):
    name= input("Enter your name: ")
    price= input("What's your bid: $")
    bids[name]= price
    person= input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if person =="yes":
        system("cls")
    else:
        new_person= False
max_price= max(bids.values())
key_max= next((key for key, value in bids.items() if value==max_price),None)
print(f"{key_max} is the winner!")



