f = open("input.txt", "r")
pi = list(map(int, f.read().splitlines()))

part1 = sum([current > previous for previous, current in zip(pi, pi[1:])])

part2 = 0
for x in range(len(pi) - 3):
    if sum(pi[x:x + 3]) < sum(pi[x + 1:x + 4]):
        part2 += 1

print(part1)
print(part2)
