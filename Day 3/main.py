import csv
import string

common_item_types = []
def get_rucksacks():
    # Opens puzzle_input.txt as a list of lists
    rucksack_contents = list(csv.reader(open('puzzle_input.txt', 'r'), delimiter='|'))
    # Converts List of lists to list of Strings
    # using list comprehension + join()
    list_of_strings = [''.join(rucksack) for rucksack in rucksack_contents]
    for rucksack in list_of_strings:
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

# Assigns the appropriate number to the letter value for the priority set by the puzzle.
def priority_values():
    low_priority = dict()
    for index, letter in enumerate(string.ascii_lowercase):
        low_priority[letter] = index + 1

    high_priority = dict()
    for index, letter in enumerate(string.ascii_uppercase):
        high_priority[letter] = index + 27

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

def find_badges():
    # Opens puzzle_input.txt as a list of lists
    rucksack_contents = list(csv.reader(open('puzzle_input.txt', 'r'), delimiter='|'))
    # Converts List of lists to list of Strings
    # using list comprehension + join()
    list_of_strings = [''.join(rucksack) for rucksack in rucksack_contents]
    print(type(list_of_strings))
    
    # Use the same code as before except now it's comparing three lines instead of 2.
    # badges_in_rucksacks = []
    # badge = [x for x in list_of_strings[a] +
    #                     list_of_strings[b] +
    #                     list_of_strings[c]
    # if x in list_of_strings[a] and x in list_of_strings[b] and x in list_of_strings[c]]
    # badges_in_rucksacks.append(badge)

find_badges()
