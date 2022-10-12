input = list(map(int, input().split()))

cards = {1 : 'spades', 2 : 'clubs', 3 : 'diamonds', 4 : 'hearts', 6 : 'six', 7 : 'seven',
8 : 'eight', 9 : 'nine', 10 : 'ten', 11 : 'jack', 12 : 'queen', 13 : 'king', 14 : 'ace'}

print(f"the {cards.get(input[1])} of {cards.get(input[0])}")