import csv
import string

def get_input():
    # Opens puzzle_input.txt as a list of lists
    rucksack_contents = list(csv.reader(open('puzzle_input.txt', 'r'), delimiter='|'))
    # Converts List of lists to list of Strings
    # using list comprehension + join()
    list_of_rucksacks = [''.join(rucksack) for rucksack in rucksack_contents]
    # rucksack_contents.append(list_of_rucksacks)
    compartment_contents(list_of_rucksacks)
    find_badges(list_of_rucksacks)

def compartment_contents(x):
    for rucksack in x:
        # Assigns each letter in rucksack to number. Finds the middle by dividing the rucksack's
        # length by two. Adds the first half to one compartment list, and the second half to the other
        # compartment list.
        compartment_one = []
        compartment_two = []
        for i in range(len(rucksack)):
            if i < (len(rucksack)/2):
                compartment_one.append(rucksack[i])
            else:
                compartment_two.append(rucksack[i])

        # For each item in each compartment, if the item exists in both compartments, it is assigned to the variable
        # common_item, and added to the common_item_types list.
        common_item_types = []
        common_item = [x for x in compartment_one + compartment_two if x in compartment_one and x in compartment_two]
        common_item_types.append(common_item[0])

        for items in common_item_types:
            total_score(items)
            
def find_badges(x):
    # Chunks the rucksacks into sets of 3 and assigns them to the array chunks.
    chunks = []
    for i in range(0, len(x), 3):
        chunks.append((x[i:i+3]))
    badges_in_rucksacks = []
    for chunk in chunks:
        # Use the same code as before except now it's comparing three lines instead of 2.
        badge = [x for x in chunk[0] + chunk[1] + chunk[2] if x in chunk[0] and x in chunk[1] and x in chunk[2]]
        badges_in_rucksacks.append(badge)
    items = []
    for badge in badges_in_rucksacks:
        items.append(badge[0])
    total_score(items)

def total_score(x):
    low_priority = dict()
    high_priority = dict()
    # Assigns the appropriate number to the letter value for the priority set by the puzzle.
    for index, letter in enumerate(string.ascii_lowercase):
        low_priority[letter] = index + 1
    for index, letter in enumerate(string.ascii_uppercase):
        high_priority[letter] = index + 27
    # Check to see if values from common_item_types exist within our low_priority/high_priority dictionary list.
    # If the value exists, it adds that dictionary value to the empty array score.
    score = []
    if x in low_priority:
        score.append(low_priority[x])
    else:
        score.append(high_priority[x])
    print(score)

get_input()
