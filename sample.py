def wrapping_paper_needed(dimensions):
    l, w, h = dimensions

    side1 = l * w
    side2 = w * h
    side3 = h * l

    surface_area = 2 * side1 + 2 * side2 + 2 * side3
    slack = min(side1, side2, side3)

    return surface_area + slack


def main():
    total = 0

    with open("input.txt", "r") as file:
        for line in file:
            if line.strip():
                dimensions = list(map(int, line.strip().split("x")))
                total += wrapping_paper_needed(dimensions)

    print(total)


if __name__ == "__main__":
    main()
