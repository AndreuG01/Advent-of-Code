import sys
from collections import Counter

file_content = open(sys.argv[1]).read().strip()
initial_secrets = [int(line) for line in file_content.splitlines()]

PRUNE = 16777216


def next_secret(secret: int) -> int:
    secret = (secret ^ (secret * 64)) % PRUNE
    secret = (secret ^ (secret // 32)) % PRUNE
    secret = (secret ^ (secret * 2048)) % PRUNE
    return secret


def secret_after(secret: int, steps: int) -> int:
    for _ in range(steps):
        secret = next_secret(secret)
    return secret


# Sanity check with the sequence given in the statement for a secret of 123
assert next_secret(123) == 15887950 and secret_after(123, 10) == 5908254

part_1_res = 0
for secret in initial_secrets:
    final = secret_after(secret, 2000)
    part_1_res += final

print(f"Part 1 res: {part_1_res}")

# Part 2: the price is the last digit of each secret. For every buyer note
# the price the first time each sequence of four changes appears (that is
# when the monkey would sell), and add it to that sequence's total.
bananas = Counter()
for secret in initial_secrets:
    prices = [secret % 10]
    for _ in range(2000):
        secret = next_secret(secret)
        prices.append(secret % 10)
    changes = [b - a for a, b in zip(prices, prices[1:])]

    seen = set()
    for i in range(len(changes) - 3):
        sequence = tuple(changes[i:i + 4])
        if sequence not in seen:
            seen.add(sequence)
            bananas[sequence] += prices[i + 4]

best_sequence, part_2_res = bananas.most_common(1)[0]
print(f"Best sequence: {best_sequence}")
print(f"Part 2 res: {part_2_res}")
