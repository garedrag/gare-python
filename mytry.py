# coding:utf-8
import random

CLUBS = 1
DIAMONDS = 2
HEARTS = 3
SPADES = 4
SUITS = (CLUBS, DIAMONDS, HEARTS, SPADES)
SUITS_SYMBOLS = {
        CLUBS: "♣",
        DIAMONDS: "♦",
        HEARTS: "♥",
        SPADES: "♠",
        }

JACK = 11
QUEEN = 12
KING = 13
ACE = 14
RANKS = (JACK, QUEEN, KING, ACE)
RANKS_SYMBOLS = {
        JACK: 'J',
        QUEEN: 'Q',
        KING: 'K',
        ACE: 'A',
        }


class Card:
    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.rank[self.rank] + " of " + self.suit[self.suit])

    def __cmp__(self, other):
        if self.rank > other.rank:
            return 1
        elif self.rank < other.rank:
            return -1
        else:
            return 0


class Deck:
    def __init__(self):
        self.cards = [r+s for r in RANKS for s in SUITS]

    def shuffle(self):
        random.shuffle(self.cards)

class Hand:
     def __init__(self):
         
         def add(self, card):
             self.cards.appernd(card)

         def give(self, card, other_hand):
             self.cards.remove(card)
             other_hand.add(card)
        
             
             
        
    
             
             
             
             
