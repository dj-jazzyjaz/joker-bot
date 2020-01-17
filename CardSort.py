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

def sort_cards_by_x(cards):
    x = np.array([card.center[0] for card in cards])
    x_argsort = np.argsort(x)
    cards_sorted = np.array([cards[i] for i in x_argsort])
    ranks_sorted = np.array([cards[i].best_rank_match for i in x_argsort])
    print(cards_sorted, ranks_sorted)
    return cards_sorted, ranks_sorted

def get_swap_sequence(card_ranks):
    swap_sequence = []
    sorted = np.sort(card_ranks)

    for i in range(4):
        if card_ranks[i] != sorted[i]:
            correct_index = np.where(sorted == card_ranks[i])[0][0]
            swap_sequence.append((i, correct_index))
            temp = card_ranks[i]
            card_ranks[i] = card_ranks[correct_index]
            card_ranks[correct_index] = temp
    return swap_sequence

def execute_swap_sequence(swap_sequence):
    TMP_CARD=2
    for (pos1, pos2) in swap_sequence:
        move_card(pos1,TMP_CARD)
        move_card(pos2,pos1)
        move_card(TMP_CARD,pos1)

def pos2pwm(pos):
    #degree is arc from left side
    deg=36*pos
    return (deg/180)*255

def move_card(from_ind, to_ind,arm,vert,succ):
    #arm, vert, succ correspond to the servos
    #move arm to position
    arm.write(pos2pwm(from_ind))
    time.sleep(1)
    #lower the boy
    vert.write(0)
    time.sleep(1)
    #succ
    succ.write(200)
    time.sleep(1)
    #raise the boy
    vert.write(0)
    time.sleep(1)
    #move arm to position
    arm.write(pos2pwm(to_ind))
    time.sleep(1)
    #de-succ
    succ.write(20)