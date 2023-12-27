import sys
from functools import cmp_to_key

file_content = open(sys.argv[1]).read().strip().splitlines()

strength_part1 = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
strength_part2 = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

def occurences_hand(hand_str):
    hand_map = {}
    for letter in hand_str:
        if letter not in hand_map:
            hand_map[letter] = 1
        else:
            hand_map[letter] += 1
    
    # Sort letters based on their occurrences
    hand_map = sorted(hand_map.items(), key=lambda x: x[1], reverse=True)
    hand_map = [list(elem) for elem in hand_map]
    return hand_map


def assign_j(hand_map):
    num_j = 0
    for elem in hand_map:
        if elem[0] == "J":
            num_j = elem[1]
            elem[1] -= num_j
    
    if hand_map[0][0] == "J" and len(hand_map) > 1:
        hand_map[1][1] += num_j
    else:
        hand_map[0][1] += num_j

        

    return hand_map

def has_five(hand_map):
    for elem in hand_map:
        if elem[1] == 5:
            return True
    return False

def has_four(hand_map):
    for elem in hand_map:
        if elem[1] == 4:
            return True   
    return False

def has_three(hand_map):
    for elem in hand_map:
        if elem[1] == 3:
            return True    
    return False

def has_two(hand_map):
    for elem in hand_map:
        if elem[1] == 2:
            return True  
    return False

def has_two_pair(hand_map):
    two_pairs = []
    for elem in hand_map:
        if elem[1] == 2:
            two_pairs.append(elem)
    return len(two_pairs) == 2



def assign_score(hand_map):
    if has_five(hand_map):
        # Five of a kind: 6
        return 6
    elif has_four(hand_map):
        # Four of a kind: 5
        return 5
    elif has_three(hand_map) and has_two(hand_map):
        # Full house (3 + 2): 4
        return 4
    elif has_three(hand_map):
        # Three of a kind: 3
        return 3
    elif has_two_pair(hand_map):
        # Two pair: 2
        return 2
    elif has_two(hand_map):
        # One pair: 1
        return 1
    else:
        # High card: 0
        return 0


def compare_hands_part1(hand1, hand2):
    if hand1[1] > hand2[1]:
        return -1
    elif hand1[1] < hand2[1]:
        return 1
    else:
        for i in range(len(hand1[0])):
            if hand1[0][i] != hand2[0][i]:
                if strength_part1.index(hand1[0][i]) > strength_part1.index(hand2[0][i]):
                    return -1
                elif strength_part1.index(hand1[0][i]) < strength_part1.index(hand2[0][i]):
                    return 1
    return 0

def compare_hands_part2(hand1, hand2):
    if hand1[1] > hand2[1]:
        return -1
    elif hand1[1] < hand2[1]:
        return 1
    else:
        for i in range(len(hand1[0])):
            if hand1[0][i] != hand2[0][i]:
                if strength_part2.index(hand1[0][i]) > strength_part2.index(hand2[0][i]):
                    return -1
                elif strength_part2.index(hand1[0][i]) < strength_part2.index(hand2[0][i]):
                    return 1
    return 0

hand_scores_part1 = []
hand_scores_part2 = []
bids = {}

for line in file_content:
    hand = line.split(" ")[0]
    bids[hand] = int(line.split(" ")[1])
    hand_scores_part1.append((hand, assign_score(occurences_hand(hand))))
    hand_scores_part2.append((hand, assign_score(assign_j(occurences_hand(hand)))))

hand_scores_part1.sort(key=cmp_to_key(compare_hands_part1))
hand_scores_part2.sort(key=cmp_to_key(compare_hands_part2))


total_cards = len(hand_scores_part1)

part1_res = 0
part2_res = 0

for i, (hand_part1, hand_part2) in enumerate(zip(hand_scores_part1, hand_scores_part2)):
    part1_res += bids[hand_part1[0]] * (total_cards - i)
    part2_res += bids[hand_part2[0]] * (total_cards - i)

print(f"Part 1 res: {part1_res}")
print(f"Part 2 res: {part2_res}")
