# 1. The Shuffle

# write  a function get_shuffled_cards()

# Inside the function create  a 52-card list of tuples [("2", "diamonds ♦"), ("2", "hearts ♥"), ....., ("A", "spades ♠"), ("A", "clubs ♣")]

# The function returns a shuffled set of cards - the same list with tuples but shuffled!

# Find the correct method from built in random library.

# you can use a loop or use something from the library

# BONUS: Something can be useful from here: https://docs.python.org/3/library/itertools.html
import itertools
import random
def get_shuffled_cards():
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    faces = ["diamonds ♦", "hearts ♥", "spades ♠", "clubs ♣"]
    deck = list(itertools.product(values, faces)) # gerai nesupratau kaip sitas veikia
    shuf_deck = random.sample(deck, len(deck))
    return shuf_deck
    

print(get_shuffled_cards())
# nu OK suveike, bet nepaziuredama i atsakyma nebuciau padarius

 #2. Deck - probably for homework, see how far you get

# write a class Deck with the following attributes(variables)

# available - contains list of card tuples that can be used

# spent - contains list of card tuples that have been used

# there should be following methods:

# constructor (__init__) method

# initializes available with full 52 card list of tuples

# initializes spent with empty list

# shuffle(self):

# # shuffles available cards - works just like 1st function but works on available

# get_cards(self, count=1):
# # gets some number(default 1) of cards from available 
# adds these cards to spent
# returns these cards

# # you can add other methods and/or attributes if you wish to Deck class

# example usage:
# my_deck = Deck()
# print(my_deck.available) # 52
# print(my_deck.spent) # 0
# my_deck.shuffle() # shuffles available
# print(my_deck.available) # 52
# print(my_deck.spent) # 0
# my_cards = my_deck.get_cards(5) # gets 5 cards from available
# print(my_cards) # 5 cards like (3, 'hearts ♥'), (6, 'diamonds ♦'), (3, 'spades ♠'), (5, 'clubs ♣'), (7, 'hearts ♥'
# single_card = my_deck.get_cards() # gets 1 card from available
# print(single_card) # 1 card like (4, 'diamonds ♦')
# print(my_deck.available) # 46 because we got 6 cards
# print(my_deck.spent) # 6 because we got 6 cards