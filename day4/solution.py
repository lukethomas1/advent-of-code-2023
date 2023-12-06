import re
import math


def count_num_matches(line):
    winning_numbers = [int(num) for num in re.findall('\d\d*', line.split(":")[-1].split("|")[0])]
    our_numbers = [int(num) for num in re.findall('\d\d*', line.split(":")[-1].split("|")[-1])]

    matches = [winner for winner in winning_numbers for ours in our_numbers if winner == ours]
    return len(set(matches))


def tally_winnings(lines):
    wins = []

    for line in lines:
        win = math.floor(math.pow(2, count_num_matches(line) - 1))
        wins.append(win)
    print(f"Part1 sum: {sum(wins)}")


def count_total_cards_won(lines):
    # dynamic programming
    memoized = {}
    # base case
    memoized[len(lines)] = 0

    total_cards = 0

    # start from last card
    for i, line in reversed(list(enumerate(lines))):
        card_num = i + 1
        num_matches = count_num_matches(line)

        cards_gained = 0
        for j in range(num_matches):
            next_card_num = card_num + j + 1
            if next_card_num <= len(lines):
                # add 1 for the copy of the card
                cards_gained += memoized[next_card_num] + 1
            else:
                break

        memoized[card_num] = cards_gained
        # add 1 for the original card
        total_cards += cards_gained + 1
        # print(f"Card {card_num} has {num_matches} matches and counts for {cards_gained + 1} each instance")

    print(f"Part2 sum: {total_cards}")


if __name__ == "__main__":
    lines = []
    with open("input") as f:
        lines = f.readlines()

    for i in range(len(lines)):
        line = lines[i]
        stripped_line = line.strip()
        lines[i] = stripped_line

    tally_winnings(lines)
    count_total_cards_won(lines)