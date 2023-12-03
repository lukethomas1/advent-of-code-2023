
SYMBOLS = ['#', '%', '@', '+', '*', '$', '-', '/', '&', '=']
GEAR_SYMBOL = '*'

class EngineNumber:
    def __init__(self, lines, x, y, x_max, y_max):
        self.x, self.y = self.find_rightmost_digit(lines, x, y, x_max)
        self.value = self.find_value(lines, self.x, x_max)
        self.symbol_nearby = self.is_nearby_a_symbol(lines, self.x, x_max, y_max)

    def __eq__(self, __value: object) -> bool:
        return self.x == __value.x and self.y == __value.y
    
    def __hash__(self):
        return self.value * (self.x + 1) * (self.y + 1)
    
    def __mul__(self, other):
        return self.value * other.value

    def find_rightmost_digit(self, lines, x, y, x_max):
        rightmost = False

        while not rightmost:
            if x >= x_max:
                break

            character = lines[y][x]
            if is_char_a_digit(character):
                x = x + 1
            else:
                break
        return x - 1, y
    
    def find_value(self, lines, x, x_max):
        my_value = int(lines[self.y][x])
        if check_for_number_to_left(lines, x, self.y):
            return self.find_value(lines, x - 1, x_max) * 10 + my_value
        return my_value
    
    def is_nearby_a_symbol(self, lines, x, x_max, y_max):
        while is_char_a_digit(lines[self.y][x]):
            if check_for_nearby_symbol(lines, x, self.y, x_max, y_max):
                return True
            if x == 0:
                return False
            x = x - 1
        return False


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


def is_char_a_digit(character):
    for i in range(10):
        if character == str(i):
            return True
    return False


def check_for_number_to_left(lines, x, y):
    x_new = x - 1

    if x_new < 0:
        return False
    
    left_character = lines[y][x_new]
    try:
        int_val = int(left_character)
        return True
    except:
        return False


def get_list_of_nearby_numbers(lines, x, y, x_max, y_max):
    vals = [-1, 0, 1]

    numbers = set()
    for d_x in vals:
        for d_y in vals:
            x_new = x + d_x
            y_new = y + d_y

            if x_new < 0 or x_new >= x_max or y_new < 0 or y_new >= y_max:
                continue

            character = lines[y_new][x_new]
            if is_char_a_digit(character):
                new_number = EngineNumber(lines, x_new, y_new, x_max, y_max)
                numbers.add(new_number)

    return list(numbers)


def add_numbers(lines):
    y_max = len(lines)
    x_max = len(lines[0])

    sum_total = 0

    numbers = set()
    for y_val in range(y_max):
        for x_val in range(x_max):
            character = lines[y_val][x_val]

            if is_char_a_digit(character):
                numbers.add(EngineNumber(lines, x_val, y_val, x_max, y_max))
    
    for number in numbers:
        if number.symbol_nearby:
            sum_total += number.value
    return sum_total


def add_gear_ratios(lines):
    y_max = len(lines)
    x_max = len(lines[0])

    sum_total = 0

    for y_val in range(y_max):
        for x_val in range(x_max):
            character = lines[y_val][x_val]

            if character == GEAR_SYMBOL:
                nearby_numbers = get_list_of_nearby_numbers(lines, x_val, y_val, x_max, y_max)

                if len(nearby_numbers) == 2:
                    product = nearby_numbers[0] * nearby_numbers[1]
                    sum_total += product
    return sum_total


if __name__ == "__main__":
    lines = []
    with open("input") as f:
        lines = f.readlines()

    for i in range(len(lines)):
        line = lines[i]
        stripped_line = line.strip()
        lines[i] = stripped_line

    part_number_sum = add_numbers(lines)
    gear_ratio_sum = add_gear_ratios(lines)

    print(f"Sum of part_numbers: {part_number_sum}")
    print(f"Sum of gear ratios: {gear_ratio_sum}")