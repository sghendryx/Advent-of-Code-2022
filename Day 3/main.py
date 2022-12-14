import csv
import string

common_item_types = []
def get_rucksacks():
    # Opens puzzle_input.txt as a list of lists
    rucksack_contents = list(csv.reader(open('puzzle_input.txt', 'r'), delimiter='|'))
    # Converts List of lists to list of Strings
    # using list comprehension + join()
    list_of_rucksacks = [''.join(rucksack) for rucksack in rucksack_contents]
    for rucksack in list_of_rucksacks:
        # Assigns each letter in rucksack to number. Finds the middle by dividing the rucksack's
        # length by two. Adds the first half to one compartment list, and the second half to the other
        # compartment list.
        compartment_one = []
        compartment_two = []
        for i in range(len(rucksack)):
            if i < (len(rucksack)/2):
                compartment_one.append(rucksack[i])
                # print(i, rucksack[i])
            else:
                compartment_two.append(rucksack[i])

        # For each item in each compartment, if the item exists in both compartments, it is assigned to the variable
        # common_item.

        common_item = [x for x in compartment_one + compartment_two if x in compartment_one and x in compartment_two]
        common_item_types.append(common_item[0])

low_priority = dict()
high_priority = dict()
def priority_values():
    # Assigns the appropriate number to the letter value for the priority set by the puzzle.
    for index, letter in enumerate(string.ascii_lowercase):
        low_priority[letter] = index + 1
    for index, letter in enumerate(string.ascii_uppercase):
        high_priority[letter] = index + 27

def score_for_items():
    # Check to see if values from common_item_types exist within our low_priority/high_priority dictionary list.
    # If the value exists, it adds that dictionary value to the empty array score.
    score = []
    for item in common_item_types:
        if item in low_priority:
            score.append(low_priority[f'{item}'])
        else:
            score.append(high_priority[f'{item}'])

    # Then we just take the sum of the score.
    print(sum(score))

items = []
def find_badges():
    # Opens puzzle_input.txt as a list of lists
    rucksack_contents = list(csv.reader(open('puzzle_input.txt', 'r'), delimiter='|'))
    # Converts List of lists to list of Strings
    list_of_rucksacks = [''.join(rucksack) for rucksack in rucksack_contents]

    # Chunks the rucksacks into sets of 3 and assigns them to the array chunks.
    chunks = []
    for i in range(0, len(list_of_rucksacks), 3):
        chunks.append((list_of_rucksacks[i:i+3]))

    badges_in_rucksacks = []
    for chunk in chunks:
        # Use the same code as before except now it's comparing three lines instead of 2.
        badge = [x for x in chunk[0] +
                            chunk[1] +
                            chunk[2]
        if x in chunk[0] and x in chunk[1] and x in chunk[2]]
        badges_in_rucksacks.append(badge)

    for badge in badges_in_rucksacks:
        items.append(badge[0])

    priority_values()
    score_for_badges()

# Check to see if values from common_item_types exist within our low_priority/high_priority dictionary list.
# If the value exists, it adds that dictionary value to the empty array score.
score = []
def score_for_badges():
    for item in items:
        if item in low_priority:
            score.append(low_priority[f'{item}'])
        else:
            score.append(high_priority[f'{item}'])

    # Then we just take the sum of the score.
    print(sum(score))


get_rucksacks()
priority_values()
score_for_items()
find_badges()
