import math
import sys

f = open("input.txt", "r")
pi = list(f.read().splitlines())

# part 1
occurrences = [0 for _ in range(len(pi[0]))]
gamma = []
epsilon = []
for x in pi:
    for index, digit in enumerate(x):
        occurrences[index] += int(digit)

for o in occurrences:
    dominance = o > math.floor(len(pi) / 2)
    epsilon.append(int(dominance))
    gamma.append(int(not dominance))

gamma_decimal = int(''.join(str(e) for e in epsilon), 2)
epsilon_decimal = int(''.join(str(g) for g in gamma), 2)

part1 = gamma_decimal * epsilon_decimal

# part 2
sys.setrecursionlimit(1500)


def recursive_check(measurements, inverted, equality_bit, idx=0):
    if len(measurements) > 1:
        count_positives = sum(
            [int(binary_digit[idx]) for binary_digit in [measurement for measurement in measurements]])
        if count_positives == len(measurements) / 2:
            dominance = equality_bit
        else:
            dominance = int(count_positives > math.floor(len(measurements) / 2))
            dominance = int(not dominance) if inverted else dominance

        return recursive_check([measurement for measurement in measurements if int(measurement[idx]) == dominance],
                               inverted, equality_bit, idx + 1)
    else:
        in_decimal = int(''.join(str(m) for m in measurements[0]), 2)
        return in_decimal


oxygen_generator_rating = recursive_check(pi, False, 1)
co2_scrubber_rating = recursive_check(pi, True, 0)

part2 = oxygen_generator_rating * co2_scrubber_rating

print(part1)
print(part2)
