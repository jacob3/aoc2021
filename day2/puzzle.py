f = open("input.txt", "r")
pi = list(f.read().splitlines())

# part 1
horizontal, vertical = [0, 0]

for x in pi:
    direction, value = x.split(' ')

    if direction == "forward":
        horizontal += int(value)
    if direction == "up":
        vertical -= int(value)
    if direction == "down":
        vertical += int(value)

part1 = horizontal * vertical

# part 2
horizontal, vertical, aim = [0, 0, 0]
for x in pi:
    direction, value = x.split(' ')

    if direction == "forward":
        horizontal += int(value)
        vertical += aim * int(value)
    if direction == "up":
        aim -= int(value)
    if direction == "down":
        aim += int(value)

part2 = horizontal * vertical

print(part1)
print(part2)
