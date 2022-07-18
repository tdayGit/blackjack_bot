# Welcome to blackjack_bot.py

# This bot's directive is to be a blackjack dealer.
# Players can win money in gaming sessions.
# Single Deck Blackjack rules

# Imports
import random

# .pop() .append()

player_hand = []
dealer_hand = []
deck = []
discard = []
revealed = False

def main():

	# Create Deck

	'''
		Black Jack Deck Rules:

		Single Deck
		1-10, J, Q, K, A - H.C.S.D

		deck array = [{'value' => 1-10.J.Q.K.A, 'suit' => H.C.S.D}]
	'''

	for x in range(10):
		y = x + 1
		deck.append({'value': y, 'suit': 'h'});
		deck.append({'value': y, 'suit': 'c'});
		deck.append({'value': y, 'suit': 's'});
		deck.append({'value': y, 'suit': 'd'});
	else:
		deck.append({'value': 'j', 'suit': 'h'})
		deck.append({'value': 'j', 'suit': 'c'})
		deck.append({'value': 'j', 'suit': 's'})
		deck.append({'value': 'j', 'suit': 'd'})
		deck.append({'value': 'q', 'suit': 'h'})
		deck.append({'value': 'q', 'suit': 'c'})
		deck.append({'value': 'q', 'suit': 's'})
		deck.append({'value': 'q', 'suit': 'd'})
		deck.append({'value': 'k', 'suit': 'h'})
		deck.append({'value': 'k', 'suit': 'c'})
		deck.append({'value': 'k', 'suit': 's'})
		deck.append({'value': 'k', 'suit': 'd'})
		deck.append({'value': 'a', 'suit': 'h'})
		deck.append({'value': 'a', 'suit': 'c'})
		deck.append({'value': 'a', 'suit': 's'})
		deck.append({'value': 'a', 'suit': 'd'})
		random.shuffle(deck)
		print_cards([deck[0], deck[1]], False)

def print_cards(cards, isDealer):
	# Define variable that will be printed
	print_me = ""

	'''
	for x in range(40):
		if x == 0: # Top of card
			for y in cards:
				print_me = print_me + top() + card_break()
		elif x >= 1 && x < 10: # After top
			first = isDealer
			for y in cards:
				if first: # First dealer card is hidden
					first = False
				else:
					print_me = print_me + left() + print_corner(y['suit'], x) + spacer() + print_corner(y['value'], x) + right() + card_break()
		elif x >= 10 && x < 30: # Middle of card
			for y in cards:
				print_me = print_me + print_art() + card_break()
		elif x >= 30 && x < 39: # After middle
			first = isDealer
			for y in cards:
				if first: # First dealer card is hidden
					first = False
				else:
					print_me = print_me + left() + print_corner(y['value'], x) + spacer() + print_corner(y['suit'], x) + right() + card_break()
		elif x == 39: # Bottom of card
			for y in cards:
				print_me = print_me + bottom() + card_break()

		print(print_me)
		print_me = ""
	'''


	for x in cards:
		print(" _____________________")
		if x['suit'] == 'h':# 8 wide
			print("|  __  __             |")
			print("| |  \\/  |            |")
			print("| |      |            |")
			print("| \\     /             |")
			print("|  \\   /              |")
			print("|   \\ /               |")
			print("|    v                |")
		elif x['suit'] == 'c':# 13 wide
			print("|     ___             |")
			print("|    |   |            |")
			print("| ___|   |___         |")
			print("||           |        |")
			print("||___     ___|        |")
			print("|    |___|            |")
			print("|                     |")
		elif x['suit'] == 's':# 7 wide
			print("|    ^                |")
			print("|   / \\               |")
			print("|  /   \\              |")
			print("| |     |             |")
			print("| |     |             |")
			print("| |_   _|             |")
			print("|   |_|               |")
		elif x['suit'] == 'd':# 7 wide
			print("|    ^                |")
			print("|   / \\               |")
			print("|  /   \\              |")
			print("| /     \\             |")
			print("| \\     /             |")
			print("|  \\   /              |")
			print("|   \\ /               |")
			print("|    v                |")
		print("|_____________________|")

# Define card arts
heart = [
	
]

# Define function to print card corner
def print_corner(cardvalue, linenum):
	return arts[str(cardvalue)][linenum]

# Define function to print card art
def print_art(linenum):
	return arts['jester']

# Define functions* to print top and bottom sides of card respectively
def top():
	return " _____________________"

def bottom():
	return "|_____________________|"
# Define functions* to print left and right sides of card respectively
def left():
	return "|   "

def right():
	return "   |"

# Define function to return set amount of spaces
def spacer():
	return "          "
def card_break():
	return " "

main()