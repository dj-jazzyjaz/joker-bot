import numpy as np
import time
CENTER_CARD_X = 0
CENTER_CARD_Y = 0

def get_results(qCard):
    """Get the card name and center point."""
    x = qCard.center[0]
    y = qCard.center[1]

    rank_name = qCard.best_rank_match
    suit_name = qCard.best_suit_match

    return x, y, rank_name, suit_name

def get_rank_int(rank):
    d={'Ace':1,'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,
   'Ten':10,'Jack':11,'Queen':12,'King':13, 'Unknown': -1}
    return d[rank]
def sort_cards_by_x(cards):
    x = np.array([card.center[0] for card in cards])
    x_argsort = np.argsort(x)
    cards_sorted = np.array([cards[i] for i in x_argsort])
    ranks_sorted = np.array([get_rank_int(cards[i].best_rank_match) for i in x_argsort])
    print(cards_sorted, ranks_sorted)
    return cards_sorted, ranks_sorted

def get_swap_sequence(card_ranks):
    swap_sequence = []
    sorted = np.sort(card_ranks)

    for i in range(len(card_ranks)):
        if card_ranks[i] != sorted[i]:
            correct_index = np.where(sorted == card_ranks[i])[0][0]

            actual_index1 = i
            actual_index2 = correct_index
            if correct_index > 1:
                actual_index2 += 1

            if i > 1:
                actual_index1 += 1

            swap_sequence.append((actual_index1, actual_index2))
            temp = card_ranks[i]
            card_ranks[i] = card_ranks[correct_index]
            card_ranks[correct_index] = temp
    return swap_sequence

def execute_swap_sequence(swap_sequence,arm,vert,succ):
    TMP_CARD=2
    for (pos1, pos2) in swap_sequence:
        move_card(pos1,TMP_CARD,arm,vert,succ)
        move_card(pos2,pos1,arm,vert,succ)
        move_card(TMP_CARD,pos2,arm,vert,succ)

def pos2pwm(pos):
    #degree is arc from left side
    deg=45*pos
    return 180-deg

def move_card(from_ind, to_ind,arm,vert,succ):
    #arm, vert, succ correspond to the servos
    #move arm to position
    t = 1
    up_pos = 45
    down_pos = 130
    arm.write(pos2pwm(from_ind))
    time.sleep(t)
    #lower the boy
    vert.write(down_pos)
    time.sleep(t)
    #succ
    succ.write(170)
    time.sleep(t)
    #raise the boy
    vert.write(up_pos)
    time.sleep(t)
    #move arm to position
    arm.write(pos2pwm(to_ind))
    time.sleep(t)
    #drop again
    vert.write(55)
    time.sleep(t)
    #de-succ
    succ.write(20)
    time.sleep(t)
    #move arm back up
    vert.write(up_pos)
    time.sleep(t)