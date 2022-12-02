import csv

total_score = []

ELF_CHOICE = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
}

YOUR_CHOICE = {
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
}

ROUND_RESULT_POINTS = {
    'loss': 0,
    'draw': 3,
    'win': 6
}

YOUR_CHOICE_POINTS = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

def rock_paper_scissors(elf_selected_shape, shape_you_selected):
    if elf_selected_shape == shape_you_selected:
        draw(shape_you_selected)

    elif elf_selected_shape == 'rock':
        if shape_you_selected == 'scissors':
            lose(shape_you_selected)
        else:
            win(shape_you_selected)

    elif elf_selected_shape == 'paper':
        if shape_you_selected == 'rock':
            lose(shape_you_selected)
        else:
            win(shape_you_selected)

    elif elf_selected_shape == 'scissors':
        if shape_you_selected == 'paper':
            lose(shape_you_selected)
        else:
            win(shape_you_selected)

def win(shape_you_selected):
    total_score.append(
        YOUR_CHOICE_POINTS[shape_you_selected] + ROUND_RESULT_POINTS['win']
    )
def lose(shape_you_selected):
    total_score.append(
        YOUR_CHOICE_POINTS[shape_you_selected] + ROUND_RESULT_POINTS['loss']
    )
def draw(shape_you_selected):
    total_score.append(
        YOUR_CHOICE_POINTS[shape_you_selected] + ROUND_RESULT_POINTS['draw']
    )

def run():
    # Opens puzzle_input.txt as a list of lists
    round_data = list(csv.reader(open('encrypted_strategy_guide.txt', 'r'), delimiter='|'))

    # Converts list of lists to list of strings
    # using list comprehension + join()
    encrypted_strategy_guide = [''.join(rounds) for rounds in round_data]

    for rounds in encrypted_strategy_guide:
        rock_paper_scissors(ELF_CHOICE[rounds[0]], YOUR_CHOICE[rounds[-1]])

    print(sum(total_score))

run()