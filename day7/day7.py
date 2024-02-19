normal_sort_order = list("23456789TJQKA")
joker_sort_order = list("J23456789TQKA")
joker_map = [{5:6,4:6,3:5,2:3,1:1,0:0},{4:6,3:6,2:5,1:3},{3:6,2:5,1:4,0:2},{2:6,1:5,0:3},{},{1:6}]

def find_other_pair(current_pair, hand):
    indices = [i for i, x in enumerate(hand) if x != current_pair]
    if len(indices) <= 1: return 0
    elif len(indices) == 2: return int(hand[indices[0]] == hand[indices[1]])
    else: return int((hand[indices[0]] == hand[indices[1]]) or
                     (hand[indices[1]] == hand[indices[2]]) or
                     (hand[indices[2]] == hand[indices[0]]))

def is_full_house(current_triple, hand):
    if len(hand) != 5: return 0
    indices = [i for i, x in enumerate(hand) if x != current_triple]
    return int(hand[indices[0]] == hand[indices[1]])

def evaluate_hand(hand):
    max_same_count = 0
    max_card = None
    for i, card_i in enumerate(hand):
        same_count = 1
        for j, card_j in enumerate(hand):
            if i != j and card_i == card_j:
                same_count += 1
        if same_count > max_same_count:
            max_same_count = same_count
            max_card = card_i

        if same_count == 5: return 6

    if max_same_count == 4: return 5
    elif max_same_count == 3: return 3 + is_full_house(max_card, hand)
    elif max_same_count == 2: return 1 + find_other_pair(max_card, hand)
    else: return 0

def evaluate_hand_joker(hand: tuple[str]):
    hand_no_jokers = list(filter( lambda x: x != "J", hand))
    value = evaluate_hand(hand_no_jokers)
    try: return joker_map[value][5-len(hand_no_jokers)] 
    except: return value 

def sort_ranks(ranks: list[tuple[str]], sort_order, current_hand_index=0):
    if len(ranks) <= 1 or current_hand_index >= len(ranks[0]): return ranks

    ranks.sort(key=lambda rank: sort_order.index(rank[current_hand_index]))

    output = []
    current_card = ranks[0][current_hand_index]
    last_index = 0
    for i, rank in enumerate(ranks):
        if (rank[current_hand_index] != current_card):
            output += sort_ranks(ranks[last_index:i], sort_order, current_hand_index + 1)
            current_card = rank[current_hand_index]
            last_index = i
    return output + sort_ranks(ranks[last_index:], sort_order, current_hand_index + 1)
        
def rank_cards(inp, sort_order, hand_evaluator):
    ranks = [{} for x in range(7)]
    for x in open(inp, "r").readlines():
        hand_str, bid_str = x.split(" ")
        hand = tuple(hand_str)
        hand_type = hand_evaluator(hand)
        ranks[hand_type][hand] = int(bid_str)

    total_rank = 1
    winning_total = 0
    for rank in ranks:
        sorted_ranks = sort_ranks(list(rank.keys()), sort_order)
        for rank_index, sorted_rank in enumerate(sorted_ranks):
            winning_total += (total_rank + rank_index) * rank[sorted_rank]
        total_rank += len(rank)
    return winning_total

print("part1 test: " + str(rank_cards("input_test.txt", normal_sort_order, evaluate_hand)))
print("part1: " + str(rank_cards("input1.txt", normal_sort_order, evaluate_hand)))

print("part2 test: " + str(rank_cards("input_test.txt", joker_sort_order, evaluate_hand_joker)))
print("part2: " + str(rank_cards("input1.txt", joker_sort_order, evaluate_hand_joker))) 

