import itertools, random

nums = range(1, 14)
cards = ['Heart', 'Spade', 'Diamond', 'Club']

deck = list(itertools.product(nums, cards))
random.shuffle(deck)

print("Your cards : ")
for i in range(5):
    print(deck[i][0], "OF", deck[i][1])