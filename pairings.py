import random


#assigned pairings
pairs = []

def pair_random(players): 
    if len(players)%2 != 0: players.append('None')
    random.shuffle(players)

    #create pairing tuples and add to pairings list
    while len(players) > 1 :  
        pairs.append((players[0], players [-1]))
        players.pop(-1)
        players.pop(0)
    return pairs