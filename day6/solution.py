import re


def solve_part1(lines):
    times = [int(time) for time in re.findall('\d\d*', lines[0])]
    distances = [int(distance) for distance in re.findall('\d\d*', lines[1])]

    race_wins = []
    for i in range(len(times)):
        ways_to_win = 0
        time = times[i]
        record = distances[i]

        for hold_time in range(time + 1):
            move_time = time - hold_time
            distance_gone = hold_time * move_time
            if distance_gone > record:
                ways_to_win += 1

        print(f"Race {i} has {ways_to_win} win possibilities")
        race_wins.append(ways_to_win)

    product = 1
    for wins in race_wins:
        product = product * wins
        print(str(product))
        
    print(f"Part1: {product}")


def solve_part2(lines):
    time = int("".join(re.findall('\d\d*', lines[0])))
    record = int("".join(re.findall('\d\d*', lines[1])))

    ways_to_win = 0
    for hold_time in range(time + 1):
        move_time = time - hold_time
        distance_gone = hold_time * move_time
        if distance_gone > record:
            ways_to_win += 1

    print(f"Race {i} has {ways_to_win} win possibilities")


if __name__ == "__main__":
    text = ""
    lines = []
    with open("input") as f:
        # text = f.read()
        lines = f.readlines()

    for i in range(len(lines)):
        line = lines[i]
        stripped_line = line.strip()
        lines[i] = stripped_line

    solve_part1(lines)
    solve_part2(lines)