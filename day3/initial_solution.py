# SYMBOLS = ['+', '*', '-', '/', '=', '%', '$', '#', '@', '&']

SYMBOLS = [
    '#',
    '%',
    '@',
    '+',
    '*',
    '$',
    '-',
    '/',
    '&',
    '='
]

def parse_input(filename):
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            print(str(line))

def parse_unique_characters(text):
    unique_set = set()
    for character in text:
        unique_set.add(character)

    for character in unique_set:
        print(character)
    return unique_set

def check_for_nearby_symbol(lines, x, y, x_max, y_max):
    vals = [-1, 0, 1]

    for d_x in vals:
        for d_y in vals:
            x_new = x + d_x
            y_new = y + d_y

            if x_new < 0 or x_new >= x_max or y_new < 0 or y_new >= y_max:
                continue

            if lines[y_new][x_new] in SYMBOLS:
                return True
    return False

def check_for_number_to_right(lines, x, y, x_max, y_max):
    x_new = x + 1

    if x_new >= x_max:
        return False
    
    right_character = lines[y][x_new]
    try:
        int_val = int(right_character)
        # there is a number to the right
        return True
    except:
        # not a number to the right
        return False
    
def check_for_number_to_left(lines, x, y, x_max, y_max):
    x_new = x - 1

    if x_new < 0:
        return False
    
    left_character = lines[y][x_new]
    try:
        int_val = int(left_character)
        return True
    except:
        return False
    
def check_for_symbols_near_number(lines, x, y, x_max, y_max):
    """Return tuple (boolean, number)

    Args:

    Returns:
        (boolean, number): boolean represents whether there is a symbol nearby, number represents the total value of the number so far
    """
    # Get current number int_val
    int_val = int(lines[y][x])
    nearby_symbol = False
    current_val = 0

    # Check for number to left first
    if check_for_number_to_left(lines, x, y, x_max, y_max):
        (nearby_symbol, current_val) = check_for_symbols_near_number(lines, x - 1, y, x_max, y_max)

    # Check if symbol near this number
    if check_for_nearby_symbol(lines, x, y, x_max, y_max):
        nearby_symbol = True

    return_val = [nearby_symbol, current_val * 10 + int_val]
    return return_val

def add_numbers(text):
    lines = []
    with open("input") as f:
        lines = f.readlines()

    for i in range(len(lines)):
        line = lines[i]
        stripped_line = line.strip()
        lines[i] = stripped_line

    y_max = len(lines)
    x_max = len(lines[0])
    print(f"y_max: {y_max}")
    print(f"x_max: {x_max}")

    sum_total = 0

    for y_val in range(y_max):
        for x_val in range(x_max):
            character = lines[y_val][x_val]

            try:
                int_val = int(character)
            except:
                # not a number
                continue

            # x, y coords represent an integer
            if check_for_number_to_right(lines, x_val, y_val, x_max, y_max):
                # if number to right, skip counting this one
                continue

            # no number to right, this is single-digits place, now count number
            (nearby_symbol, int_val) = check_for_symbols_near_number(lines, x_val, y_val, x_max, y_max)
            if nearby_symbol:
                sum_total += int_val
    
    print(f"Final sum: {sum_total}")


if __name__ == "__main__":
    filename = "input"

    with open(filename) as f:
        text = f.read()
        # parse_unique_characters(text)
        add_numbers(text)