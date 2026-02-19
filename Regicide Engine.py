# Regicide

import random
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        return (f"({self.rank} of {self.suit})")
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"
class Deck:
    def __init__(self):
        self.cards = []
        self.discard = []
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        for suit in suits:
            for rank in ranks:
                newCard = Card(rank, suit)
                self.cards.append(newCard)
    def shuffle(self):
        random.shuffle(self.cards)
    def draw(self):
        drawn = self.cards.pop(0)
        return drawn
class PlayerHand:
    def __init__(self, maxSize=8):
        self.maxSize = maxSize
        self.cards = []
class Boss:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        if self.rank == "J":
            self.health = 20
            self.attack = 10
        elif self.rank == "Q":
            self.health = 30
            self.attack = 15
        elif self.rank == "K":
            self.health = 40
            self.attack = 20
    def __str__(self):
        return (f"{self.rank} of {self.suit} (HP: {self.health}; ATK: {self.attack})")
def build_Boss_Deck():
    ranks = ["J", "Q", "K"]
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"] 
    bossDeck = []
    jackDeck = []
    queenDeck = []
    kingDeck = []
    for rank in ranks:
        for suit in suits:
            newBoss = Boss(rank, suit)
            if newBoss.rank == "J":
                jackDeck.append(newBoss)
            elif newBoss.rank == "Q":
                queenDeck.append(newBoss)
            elif newBoss.rank == "K":
                kingDeck.append(newBoss)
    random.shuffle(jackDeck)
    random.shuffle(queenDeck)
    random.shuffle(kingDeck)
    bossDeck = jackDeck + queenDeck + kingDeck
    return bossDeck

def info(boss):
    
    print("Current enemy:", boss)
    print(f"Cards left in deck: {len(deck.cards)}")
    for i in range(len(hand.cards)):
        print(i+1, ": ", str(hand.cards[i]))
    
def chooseAttack():
    if len(hand.cards) == 0:
        print("You have no more cards to discard.")
        print("Game over!")
        exit()
    while True:
        try:
            print("Which card will you play? ( 1 -", len(hand.cards), ")")
            played = int(input()) - 1
            if 0 <= played < len(hand.cards):
                break
            else:
                print("Invalid choice, try again.")
        except ValueError:
            print("Enter a number!")
    currentCard = hand.cards.pop(played)
    deck.discard.append(currentCard)
    return currentCard
    
    
def attack(card, boss, damage):

        boss.health -= damage
        print("Dealt", damage, "damage to the Boss!")
        
def draw():
    
    card = deck.draw()
    hand.cards.append(card)
    
def suitpower(card, boss):
    
    if card.rank != "A":
        cardAttack = int(card.rank)
    else:
        cardAttack = 1
    if card.suit == "Clubs":
        
        if boss.suit != "Clubs":
            print("Clubs power! Attack doubled!")
            cardAttack *= 2
        else:
            print("Suit power negated!")
            
    elif card.suit == "Spades":
        
        if boss.suit != "Spades":
            print(f"Spades power! Enemy attack reduced by {cardAttack}!")
            boss.attack -= cardAttack
            if boss.attack < 0:
                boss.attack = 0
        else:
            print("Suit power negated!")    
    attack(card, boss, cardAttack)
    
    if card.suit == "Diamonds":
        
        if boss.suit != "Diamonds":
            drawnCards = 0
            for i in range (cardAttack):
                if len(hand.cards) < hand.maxSize and len(deck.cards) > 0:
                    draw()
                    drawnCards += 1
            print(f"Diamonds power! Drew {drawnCards} card(s)!")

        else:
            print("Suit power negated!")   
            
    elif card.suit == "Hearts":
        
        if boss.suit != "Hearts":
            random.shuffle(deck.discard)
            returned = min(cardAttack, len(deck.discard))
            for _ in range (returned):
                card = deck.discard.pop()
                deck.cards.append(card)
            print(f"Hearts power! {returned} cards added to deck!")
        else: 
            print("Suit power negated!")
            
def bossTurn(boss):
    if boss.health > 0:
        print("The boss did", boss.attack, "damage to you!")
        discarded = 0
        while discarded < boss.attack:
            if len(hand.cards) == 0:
                print("You have no more cards to discard.")
                print("Game over!")
                exit()
            while True:
                print("You must take", boss.attack - discarded, "more damage.")
                for i in range(len(hand.cards)):
                    print(i+1, ": ", str(hand.cards[i]))
                try:
                    print("Which card will you discard? ( 1 -", len(hand.cards), ")")
                    played = int(input()) - 1
                    if 0 <= played < len(hand.cards):
                        break
                    else:
                        print("Invalid choice, try again.")
                except ValueError:
                        print("Enter a number!")
            card = hand.cards.pop(played)
            discarded += int(card.rank)
            deck.discard.append(card)
    else:
        print("Enemy defeated!")   
bossDeck = build_Boss_Deck() 
deck = Deck()
deck.shuffle()
hand = PlayerHand()
for i in range(hand.maxSize):
    draw()
    
# -----------------GAME LOOP-------------------------
for i in range (len(bossDeck)): # number of bosses
    
    currentBoss = bossDeck[i]
    while currentBoss.health > 0:
        info(currentBoss)
        currentCard = chooseAttack()
        suitpower(currentCard, currentBoss)
        bossTurn(currentBoss)
print("Wow! You defeated all the bosses... You win!") 