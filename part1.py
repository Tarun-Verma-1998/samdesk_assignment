total = 0
with open("input.txt") as f:
    for line in f:
        l, w, h = map(int, line.strip().split('x'))
        # Part 1 or Part 2 formula here
        sides = [l*w, w*h, h*l]
        total += 2 * sum(sides) + min(sides)

print(total)
