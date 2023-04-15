import random
from replit import clear
from art import logo

faces=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
card_types=['Heart','Spade','Clubs','Diamonds']

def create_deck():
  deck=[]
  for face in faces:
    for type in card_types:
      card=face+' '+type
      deck.append(card)
      
  for _ in range(100):
    random.shuffle(deck)
  return deck

deck=create_deck()

def create_reference():
  values={}
  for face in faces:
    if face not in ['J','Q','K','A']:
      values[face]=int(face)
    elif face != 'A':
      values[face]=10
    else:
      values[face]=11
  return values

reference=create_reference()

def draw_card(deck,reference,cards,sums):
  card=random.choice(deck)
  value=reference[card.split()[0]]
  sums+=value
  cards.append(card)
  return cards, sums
    
def deal():  
  print('\nDealing...')
  player_cards=[]
  dealer_cards=[]
  player_sum=0
  dealer_sum=0
  #Draw player's first card
  card, player_sum=draw_card(deck, reference, player_cards,player_sum)
  #Draw dealer's first card
  card, dealer_sum=draw_card(deck, reference, dealer_cards,dealer_sum)
  #Draw player's second card
  card,player_sum=draw_card(deck, reference, player_cards,player_sum)
  #Draw dealers's second card
  card, dealer_sum=draw_card(deck, reference, dealer_cards,dealer_sum)
  print('Table set up is:\n')
  print('Your hand:',player_cards, ' Sum:',player_sum)
  print('Dealer\'s card:',dealer_cards[0],' Sum:', reference[dealer_cards[0].split()[0]])
  return player_cards, dealer_cards, player_sum, dealer_sum

def busted(cards,sum):
  bust=False
  if sum>21:
    #check if aces
    for card_no in range(len(cards)):
      card_selected=cards[card_no]
      face, type_a=card_selected.split() # Split the face value and the type
      if face=='A':
        sum=-10
        cards[card_no] = 'Aused '+type_a #No action required. Still safe
      else:
        pass #The current card isn't an ace. Keep moving
    if sum>21:
      bust=True
  else:
    bust=False
  return cards, sum, bust 

def hit(cards,sum):
  cards,sum=draw_card(deck, reference, cards,sum)
  cards, sum,bust=busted(cards, sum)
  return cards, sum, bust

def dealer_play(cards,sum):
  bust=False
  while sum <16 and not bust:
    cards,sum=draw_card(deck, reference, cards,sum)
    cards, sum,bust=busted(cards, sum)
  return cards, sum, bust
print(logo)
start=input('Do you want to play a game of Blackjack? Type \'y\' or \'n\': \n')
print(start.lower())
if start.lower()=='no' or start.lower()=='n':
  print('OK. Thanks. Goodbye!')
elif start.lower()!='yes' and start.lower()!='y':
  print('Invalid input')
else:
  #Initiate the game
  clear()
  print(logo)
  continue_play=True
  while continue_play:
    player_cards, dealer_cards, player_sum, dealer_sum=deal()
    hit_stat=True
    while hit_stat:
      hit_stand=input('\nDo you want to stand or hit? (S/H)\n')
      if hit_stand=='hit' or hit_stand=='h':
        player_cards, player_sum, player_bust=hit(player_cards, player_sum)
        if player_bust:
          print('Your hand: ',player_cards, '. Your score: ', player_sum)
          print('You are busted! You lost the game!')
          break
        else:
          print('Your hand: ',player_cards, '. Your score: ', player_sum)
      else:
        hit_stat=False
        #print('Your hand: ',player_cards, '. Your score: ', player_sum)
        player_bust=False
    dealer_bust=False
    print('\n')
    if not player_bust:
        print('Dealer playing....')
        dealer_cards,dealer_sum, dealer_bust=dealer_play(dealer_cards,dealer_sum)
        if dealer_bust:
          print('Dealer busted! You won!')
    if not player_bust and not dealer_bust:
      print('\n')
      print('Your hand: ',player_cards, '. Your score: ', player_sum)
      print('Dealer hand: ',dealer_cards, '. Dealer score: ', dealer_sum)
      print('\n')
      if player_sum>dealer_sum:
        print('You beat the dealer !')
      if player_sum<dealer_sum:
        print('The dealer beat you !')
      if player_sum==dealer_sum:
        print('Draw')      
    new_game=input('Would you like to play again? (Y/N)\n')
    if new_game.lower()=='n':
      print('Thank you and goodbye')
      continue_play=False
    else:
      clear()
