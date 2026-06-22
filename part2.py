total = 0
with open("input.txt") as f:
    for line in f:
        l, w, h = map(int, line.strip().split('x'))
        perimeter = 2 * (l + w + h - max(l, w, h))
        total += perimeter + l * w * h

print(total)
