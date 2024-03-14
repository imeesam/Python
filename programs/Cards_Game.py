import random 
from pprint import pprint

count_for_player1 , count_for_player2 , tie = 0 , 0 , 0

def shuffling_cards():    
    suits = ['H', 'D', 'C', 'S']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [(r, s) for r in ranks for s in suits]
    random.shuffle(deck)
    return deck


def comparing_both(card_1 , card_2):
    global count_for_player1 , count_for_player2 , tie
    
    cards_value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13 , 'A': 14,}
    rank1 , suit1  = card_1
    rank2 ,suit2 = card_2
    if cards_value[rank1] > cards_value[rank2]:
        print("\tPlayer 1 won")
        count_for_player1 += 1
        
    elif cards_value[rank1] < cards_value[rank2]:
        print("\tPlayer 2 won")
        count_for_player2 += 1
        
    else:
        print("\tOpp's, It's a Tie")
        tie += 1


def start_game():
    shuffled = shuffling_cards() 
    global player_1 ,player_2
    
    player_1 = shuffled[:26]
    player_2 = shuffled[26:]

    print("Player 1's all Card")
    pprint(player_1)
    print("\nPlayer 2's all Card")
    pprint(player_2)

    for i in range(26):
        print("\nRound :", i+1)
        print("\tPlayer 1's turn :\n\t\t\t", player_1[i] )
        print("\tPlayer 2's turn :\n\t\t\t", player_2[i] )
        comparing_both(player_1[i], player_2[i])
        
    print(f"\nPlayer 1 won {count_for_player1} times")
    print(f"\nPlayer 2 won {count_for_player2} times")
    print(f"\nMatch was tie {tie} times")



start_game()
