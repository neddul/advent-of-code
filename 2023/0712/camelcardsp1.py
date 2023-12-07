with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')
rows = [x.split() for x in rows]


strength = {'A' : 14, 'K' : 13, 'Q' : 12, 'J' : 11, 'T':10, '9':9,'8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}
hands = []

for hand in rows:
    my_dict = {}
    my_hand = hand[0]
    for x in my_hand:
        if x in my_dict:
            my_dict[x] +=1
        else:
            my_dict[x] = 1
    my_dict['bet'] = int(hand[1])
    my_dict['hand'] = hand[0]
    hands.append(my_dict)

score = []
for hand in hands:
    if len(hand) - 2 == 5: #High card
        hand['score'] = 1
    elif len(hand) - 2 == 4: #Pair
        hand['score'] = 2
    elif len(hand) - 2 == 3 and 3 not in hand.values(): #Two pair
        hand['score'] = 3
    elif len(hand) - 2 == 3 and 2 not in hand.values(): #3 of a kind
        hand['score'] = 4
    elif len(hand) - 2 == 2 and 2 not in hand.values(): #4 of a kind
        hand['score'] = 6
    elif len(hand) - 2 == 2 and 2 in hand.values(): # Full house
        hand['score'] = 5
    else: #5 of a kind
        hand['score'] = 7

def compare_cards(hand1, hand2):
    for c1, c2 in zip(hand1, hand2):
        if strength[c1] > strength[c2]:
            return 1 #If the card was bigger
        elif strength[c1] < strength[c2]:
            return 0 #If the card was smaller


for i in range(len(hands)):
    dict1 = hands[i]
    dict1['multiplier'] = 1
    for j in range(len(hands)):
        dict2 = hands[j]
        if dict1['hand'] != dict2['hand']:
            if dict1['score'] > dict2['score']:
                dict1['multiplier'] += 1
            elif dict1['score'] == dict2['score']: #Compare cards
                dict1['multiplier'] += compare_cards(dict1['hand'],dict2['hand'])


sum = 0
for hand in hands:
    sum += hand['bet'] * hand['multiplier']

print(sum)