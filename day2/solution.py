import re


MAX_CUBES = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def sum_valid_game_ids(lines):
    valid_ids = []

    for line in lines:
        game_id = int(line.split(":")[0].split(" ")[-1])

        red_counts = [int(val) for val in re.findall('(\d*?) red', line) if int(val) > MAX_CUBES['red']]
        blue_counts = [int(val) for val in re.findall('(\d*?) blue', line) if int(val) > MAX_CUBES['blue']]
        green_counts = [int(val) for val in re.findall('(\d*?) green', line) if int(val) > MAX_CUBES['green']]

        if len(red_counts) == 0 and len(blue_counts) == 0 and len(green_counts) == 0:
            valid_ids.append(game_id)

    print(f"Part1 sum: {sum(valid_ids)}")


def sum_cube_powers(lines):
    powers = []

    for line in lines:
        game_id = int(line.split(":")[0].split(" ")[-1])

        red_counts = [int(val) for val in re.findall('(\d*?) red', line)]
        blue_counts = [int(val) for val in re.findall('(\d*?) blue', line)]
        green_counts = [int(val) for val in re.findall('(\d*?) green', line)]

        power = max(red_counts) * max(blue_counts) * max(green_counts)

        powers.append(power)

    print(f"Part2 sum: {sum(powers)}")


if __name__ == "__main__":
    lines = []
    with open("input") as f:
        lines = f.readlines()

    for i in range(len(lines)):
        line = lines[i]
        stripped_line = line.strip()
        lines[i] = stripped_line

    sum_valid_game_ids(lines)
    sum_cube_powers(lines)