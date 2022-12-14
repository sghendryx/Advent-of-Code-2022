import csv

def main():
    # Opens puzzle_input.txt as a list of lists
    food_items = list(csv.reader(open('puzzle_input.txt', 'r'), delimiter='|'))

    # Converts list of lists to list of strings
    # using list comprehension + join()
    list_of_strings = [''.join(item) for item in food_items]

    calories_per_elf = []
    all_calorie_totals = []
    
    for calorie_value in list_of_strings:
        # For every calorie_value, it takes that string value and turns it into an integer, and adds it to the list
        # calories_per_elf.
        if bool(calorie_value) == True:
            calorie_value = int(calorie_value)
            calories_per_elf.append(calorie_value)
        else:
        # When it comes across an empty list value, it sums up the calorie values it has so far in calories_per_elf, adds
        # that total to the empty array all_calorie_totals, and then clears the calories_per_elf list.
            elf_calorie_sum = sum(calories_per_elf)
            all_calorie_totals.append(elf_calorie_sum)
            calories_per_elf.clear()

    # Now all we need to do is find the largest number in the new list!
    all_calorie_totals.sort()
    print("Elf with the highest calorie value is: ", all_calorie_totals[-1])
    print("Sum of the calories for the 3 elves with the most calories: ", sum(all_calorie_totals[-3:]))

main()
