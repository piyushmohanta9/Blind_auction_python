from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

next = True
bidder = {}

def bid(name, money):
  bidder[name] = money
  
while next:
  print(logo)
  print("Welcome to the secret auction program.")
  name = input("What is your name?: ")
  money = int(input("What's your bid? $"))
  bid(name, money)
  status = input("Are there any other bidders? Type \"yes\" or \"no\" ")

  if status.lower() == "no":
    next = False
  clear()

max_bid = 0
winner = ""

for bid in bidder:
  if bidder[bid] > max_bid:
    max_bid = bidder[bid]
    winner = bid
    
print(logo)   
print(f"The winner is {winner} with a bid of ${max_bid}")
print("The auction is over for the day")
print("See you in the next bid")