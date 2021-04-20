# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 18:25:32 2020

@author: yonif
"""
import random

suits=('Hearts ♥','Diamond ♦','Spades ♠','Clubs ♣')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
playing=True

class Card:
   def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
   def __str__(self):
        return("{}  {}".format(self.rank,self.suit))

class Deck:
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))                
                
    def __str__(self):
        deck_comp=""
        for card in self.deck:
            deck_comp+='\n'+card.__str__()
        return "Deck: "+deck_comp
        
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        single_card=self.deck.pop()
        return single_card

class Hands:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]
        if card.rank=='Ace':
            self.aces+=1#true meaning
    def adjust_for_ace(self):
        #if im bust and got ace change the ace to 1 instead of 11
        while self.value>21 and self.aces:
            self.value-=10
            self.aces-=1
            
class Chips:
    def __init__(self,total=100):
        self.total=total
        self.bet=0
    def win_bet(self):
        self.total+=self.bet
    def lose_bet(self):
        self.total-=self.bet

def take_bet(Chips):
    while True:
        try:
            Chips.bet=int(input("How much do you want to bet? "))
        except:
            print("Error please enter integer")
        else:
            if Chips.bet>Chips.total:
                print("You need to deposit order to bet this amount, at the moment you have {}".format(Chips.total))
            else:
                break

def Hits(Deck,Hands):
    single_card=Deck.deal()
    Hands.add_card(single_card)
    Hands.adjust_for_ace()

def HitOrStand(Deck,Hands):
    global playing
    while True:
        x=input("Enter Hit or Stand, h or s: ")
        if x[0].lower()=='h':
            Hits(Deck,Hands)
        elif x[0].lower()=='s':
            print("Player stand, Dealer turn")
            playing=False
        else:
            print("Error please enter h or s only!")
            continue
        break
def show_some(player,dealer):
    print("DEALER HAND WITH 1 CARD HIDDEN:")
    print(dealer.cards[1])
    print('\n')
    print('PLAYER HANDS:')
    for card in player.cards:
        print(card)

    
def show_all(player,dealer):
    print('DEALER HANDS:')
    for card in dealer.cards:
        print(card)
    print('\n')
    print('PLAYER HANDS:')
    for card in player.cards:
        print(card)
    pass

def player_bust(player,dealer,Chips):
    print("PLAYER BUSTED!")
    Chips.lose_bet()
    
def player_win(player,dealer,Chips):
    print("PLAYER WON!")
    Chips.win_bet()
    
def dealer_bust(player,dealer,Chips):
    print("PLAYER WON!, DEALER BUSTED")
    Chips.win_bet()
    
def dealer_win(player,dealer,Chips):
    print("DEALER WON!,PLAYER BUSTED")
    Chips.lose_bet()
    
def push(player,dealer):
    print("player and dealer tie!, PUSH")
        
print('♠♡♣♢♥♤♦♧ WELCOME TO BACKJACK ♠♡♣♢♥♤♦♧')
    #chip setup
money=int(input("enter the amount of chips you starting with: "))
player_chips=Chips(money)
while True:
    #make a deck and shuffle it
    deck=Deck()
    deck.shuffle()
    #setup player & dealer and give them 2 cards
    player_hand=Hands()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand=Hands()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    take_bet(player_chips)
    #show cards but for dealer only 1
    show_some(player_hand,dealer_hand)
    #game on
    while playing:
        HitOrStand(deck, player_hand)
        show_some(player_hand, dealer_hand)
        if player_hand.value>21:#if the player lost
            player_bust(player_hand, dealer_hand,player_chips)
            break
    if player_hand.value<=21:
        while dealer_hand.value<player_hand.value:
            Hits(deck, dealer_hand)
        show_all(player_hand, dealer_hand)
        #winning cases
        if dealer_hand.value>21:
            dealer_bust(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_win(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_win(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)
    #game status
    print("\nPlayer Total Chips Are At: {}".format(player_chips.total))
    if player_chips.total<=0:
        print("You lose!")
        new_game=input("Would you like to play again? y/n: ")
        if new_game[0].lower()=='y':
            money=int(input("How much would u like to deposit? "))
            player_chips=Chips(money)
            playing=True
            continue
        else:
            print("Goodbye :)")
            break
        
    #check for new game
    new_game=input("Would you like to play again? y/n: ")
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Goodbye :)")
        break
    


        
    
    
    
    
    
    
    
    
    