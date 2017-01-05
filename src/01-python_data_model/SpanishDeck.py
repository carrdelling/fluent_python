from collections import namedtuple
from random import choice

Card = namedtuple('Card', ['suit', 'rank'])
suit_values = {'oros': 1, 'copas': 2, 'espadas': 3, 'bastos': 4}


class SpanishDeck:

    suits = ['espadas', 'bastos', 'copas', 'oros']
    ranks = [str(i) for i in range(2, 8)] + list('JQKA')

    def __init__(self):
        self._cards = [Card(suit, rank) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


def spanish_order(card):
    rank_value = SpanishDeck.ranks.index(card.rank)
    return len(suit_values) * rank_value + suit_values[card.suit]


deck = SpanishDeck()

# how many cards are in the deck?
print('The deck has {} cards.'.format(len(deck)))

# what are the last three cards?
print('The last three cards are: ')
print([card for card in deck[-3:]])

# pick a card at random:
print('A random card: ')
print(choice(deck))

# print all the 5's
print('All the 5\'s: ')
for card in deck[3::10]:
    print(card)

# same in reverse order
print('All the 5\'s (reversed): ')
for card in reversed(deck[3::10]):
    print(card)

# do we have a '9' of 'espadas' in the deck?
if Card(suit='espadas', rank='9') in deck:
    print('There is a 9 of espadas in the deck.')
else:
    print('There is no 9 of espadas in the deck.')

# print the last 10 cards sorted
print('Last 10 cards sorted:')
for card in sorted(deck, key=spanish_order)[-10:]:
    print(card)
