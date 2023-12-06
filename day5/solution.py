import re


class MapDirectory:
    def __init__(self, map_input):
        self.source_to_dest = {}
        self.source_to_range = {}
        self.dest_to_source = {}
        self.dest_to_range = {}

        lines = map_input.splitlines()
        self.name = lines.pop(0).strip()
        self.fill_maps(lines)

    def fill_maps(self, lines):
        for line in lines:
            split = line.split(" ")
            dest = int(split[0])
            source = int(split[1])
            range = int(split[2])
            self.source_to_dest[source] = dest
            self.source_to_range[source] = range
            self.dest_to_source[dest] = source
            self.dest_to_range[dest] = range

    def get_source_given_dest(self, target_dest):
        source = target_dest
        for dest, range in self.dest_to_range.items():
            if target_dest >= dest and target_dest < dest + range:
                offset = target_dest - dest
                source = self.dest_to_source[dest] + offset
            
        # print(f"{self.name}")
        # print(f"    {target_dest} -> {dest}\n")
        return source
    
    def get_dest_given_source(self, target_source):
        dest = target_source
        for source, range in self.source_to_range.items():
            if target_source >= source and target_source < source + range:
                offset = target_source - source
                dest = self.source_to_dest[source] + offset
            
        # print(f"{self.name}")
        # print(f"    {target_source} -> {dest}\n")
        return dest


def get_seed_number_given_location_number(maps, location_num):
    # start at target_dest 0 because we want location 0
    target = location_num
    for map in reversed(maps):
        target = map.get_source_given_dest(target)
    return target


def parse_seeds_and_maps(text):
    split = text.split('\n\n')
    print(len(split))

    seed_text = split.pop(0)
    seed_numbers = [int(num) for num in re.findall('\d\d*', seed_text)]
    print(str(seed_numbers))

    maps = []
    for map_input in split:
        maps.append(MapDirectory(map_input))
    return seed_numbers, maps


def get_location_given_seed(maps, seed):
    target = seed
    for map in maps:
        target = map.get_dest_given_source(target)
    return target


def get_lowest_location(maps, seeds):
    locations = {}
    lowest_location = None
    for seed in seeds:
        location = get_location_given_seed(maps, seed)
        locations[location] = seed
        # print(f"Seed {seed} corresponds to location {location}")
        if lowest_location is None or location < lowest_location:
            lowest_location = location

    print(f"Part1 lowest location {lowest_location} corresponds to seed {locations[lowest_location]}")


def is_seed_within_a_range(seed_tuples, seed):
    for range_start, range_len in seed_tuples:
        if seed >= range_start and seed < range_start + range_len:
            return True


def part2(maps, seeds):
    """
    Strategy:
    1. Start from location 0, increment by (lowest_seed_range - 1)
    2. Find seed corresponding to each location
    3. If seed is in one of the original ranges, increment backwards till finding the lowest location that is still in that range
    """

    seed_ranges = [seeds[i + 1] for i in range(0, len(seeds), 2)]
    seed_tuples = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]
    increment = min(seed_ranges) - 1

    print(f"Smallest range = {increment + 1}")

    location = 0
    while True: # random large number that probably wont be reached
        seed = get_seed_number_given_location_number(maps, location)
        sanity = get_location_given_seed(maps, seed)
        if sanity != location:
            print("wtf")
            break

        if is_seed_within_a_range(seed_tuples, seed):
            break
        location += increment

    # increment backwards to find lowest location
    for i in range(increment):
        location = location - 1
        seed = get_seed_number_given_location_number(maps, location)

        if not is_seed_within_a_range(seed_tuples, seed):
            break

    location = location + 1
    seed = get_seed_number_given_location_number(maps, location)

    # sanity check
    if not is_seed_within_a_range(seed_tuples, seed):
        print("rip")
    else:
        print(f"Part2 lowest location {location} corresponds to seed {seed}")

    
if __name__ == "__main__":
    text = ""
    lines = []
    with open("input") as f:
        text = f.read()
        lines = f.readlines()

    for i in range(len(lines)):
        line = lines[i]
        stripped_line = line.strip()
        lines[i] = stripped_line

    seeds, maps = parse_seeds_and_maps(text)
    get_lowest_location(maps, seeds)
    part2(maps, seeds)
