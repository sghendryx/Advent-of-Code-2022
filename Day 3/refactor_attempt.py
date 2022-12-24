import string

def run():
    # Opens puzzle_input.txt
    with open("puzzle_input.txt", "r") as infile:
        rucksack_contents = [l.rstrip() for l in infile]

    compartment_contents(rucksack_contents)
    find_badges(rucksack_contents)

def compartment_contents(list_of_rucksacks):
    common_item_types = []
    for rucksack in list_of_rucksacks:
        # Assigns each letter in rucksack to number. Finds the middle by dividing the rucksack's
        # length by two. Adds the first half to one compartment list, and the second half to the other
        # compartment list.
        compartment_one = []
        compartment_two = []
        for i in range(len(rucksack)):
            if i < (len(rucksack) / 2):
                compartment_one.append(rucksack[i])
            else:
                compartment_two.append(rucksack[i])
        # For each item in each compartment, if the item exists in both compartments, it is assigned to the variable
        # common_item, and added to the common_item_types list.
        common_item = [x for x in compartment_one if x in compartment_one and x in compartment_two]
        common_item_types.append(common_item[0])

    scores = [ total_score(item) for item in common_item_types ]
    print(sum(scores))

def find_badges(list_of_rucksacks):
    # Chunks the rucksacks into sets of 3 and assigns them to the array chunks.
    chunks = []
    for i in range(0, len(list_of_rucksacks), 3):
        chunks.append((list_of_rucksacks[i:i + 3]))
    badges_in_rucksacks = []
    for chunk in chunks:
        # Use the same code as before except now it's comparing three lines instead of 2.
        badge = [x for x in chunk[0] if x in chunk[0] and x in chunk[1] and x in chunk[2]]
        badges_in_rucksacks.append(badge)
    items = []
    for badge in badges_in_rucksacks:
        items.append(badge[0])
    for item in items:
        total_score(item)

def total_score(item):
    priorities = dict()

    for index, letter in enumerate(string.ascii_lowercase):
        priorities[letter] = index + 1
    for index, letter in enumerate(string.ascii_uppercase):
        priorities[letter] = index + 27

    return priorities[item]

run()