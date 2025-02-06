import os
from art import logo
print(logo)
auction_over = False
auction_dic= {}

while not auction_over: 
    name = input("Please enter your name : ")
    bid = int(input("Enter your bid : "))
    auction_dic[name]=bid 
    choice = input("Are there more bidders : ").lower()
    if choice == "yes":
        os.system('cls')
    elif choice == "no":
        auction_over=True
    else :
        print("Please enter a valid response")

max_bidder = max(auction_dic ,key= auction_dic.get )
max_bid = auction_dic[max_bidder]

print(f"{max_bidder} made the highest bid of {max_bid}")
