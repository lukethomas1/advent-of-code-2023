import regex as re

DIGIT_WORDS_DICT = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,

    # gg ez
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9
}

DIGIT_OR_WORD_REGEX = '(\d|one|two|three|four|five|six|seven|eight|nine)'


def add_calibration_values(lines):
    values = []
    for line in lines:
        digits = re.findall('\d', line)
        if len(digits) > 0:
            value = int(digits[0]) * 10 + int(digits[-1])
            values.append(value)
    print(f"Sum of calibration values: {sum(values)}")


def substitute_digit_words(lines):
    values = []
    for line in lines:
        digits = re.findall(DIGIT_OR_WORD_REGEX, line, overlapped=True)
        if len(digits) > 0:
            value = DIGIT_WORDS_DICT[digits[0]] * 10 + DIGIT_WORDS_DICT[digits[-1]]
            values.append(value)
    print(f"Sum of word calibration values: {sum(values)}")


if __name__ == "__main__":
    lines = []
    with open("input") as f:
        lines = f.readlines()

    for i in range(len(lines)):
        line = lines[i]
        stripped_line = line.strip()
        lines[i] = stripped_line

    add_calibration_values(lines)
    substitute_digit_words(lines)