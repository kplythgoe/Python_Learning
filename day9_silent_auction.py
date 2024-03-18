from replit import clear
#HINT: You can call clear() to clear the output in the console.
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
bidders = {}
bidding = True

def find_winner(bidders):
  highest_bid = 0
  winner = ""
  for key in bidders:
    if bidders[key] > highest_bid:
      highest_bid = bidders[key]
      winner = key
      highest_bid = bidders[key]
  print(f"The winner of the auction is {winner} with a bid of £{highest_bid}")

while bidding:
  name = input("Please enter your name: ")
  bid = int(input("Please enter your bid price: £"))
  bidders[name] = bid
  others = input("Are there any other bidders? Type \"yes\" or \"no\": ").lower()
  clear()
  if others == "no":
    bidding = False
    find_winner(bidders)




