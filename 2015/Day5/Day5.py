import sys

file_content = open(sys.argv[1]).read().splitlines()





def three_vowels(string: str) -> bool:
    vowels = ["a", "e", "i", "o", "u"]
    return len([char for char in string if char in vowels]) >= 3


def repeated_chars(string: str) -> bool:
    for i in range(1, len(string)):
        if string[i] == string[i - 1]: return True
    return False

def substrings(string: str) -> bool:
    for sub in ["ab", "cd", "pq", "xy"]:
        if sub in string: return False
    return True


def two_grams(string: str) -> bool:
    first_seen = {}
    for i in range(len(string) - 1):
        pair = string[i:i + 2]
        if pair in first_seen and i - first_seen[pair] >= 2:
            return True
        first_seen.setdefault(pair, i)
    return False


def three_grams(string: str) -> bool:
    three_gram_dict = {}
    for i in range(len(string) - 2):
        three_gram = string[i:i + 3]
        if three_gram in three_gram_dict:
            three_gram_dict[three_gram] += 1
        else:
            three_gram_dict[three_gram] = 1
    
    return any([elem[0] == elem[-1] for elem in three_gram_dict.keys()])

part_1_res = 0
part_2_res = 0


for string in file_content:
    if three_vowels(string) and repeated_chars(string) and substrings(string):
        part_1_res += 1
    if two_grams(string) and three_grams(string):
        part_2_res += 1


print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
