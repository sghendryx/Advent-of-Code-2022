ROUND_RESULT = {
    'X' : 'LOSE',
    'Y' : 'DRAW',
    'Z' : 'WIN'
}

ROCK = {
    'WIN' : 'paper',
    'DRAW' : 'rock',
    'LOSE' : 'scissors'
}

PAPER = {
    'WIN' : 'scissors',
    'DRAW' : 'paper',
    'LOSE' : 'rock'
}

SCISSORS = {
    'WIN' : 'rock',
    'DRAW' : 'scissors',
    'LOSE' : 'paper'
}

def player_move(elf_choice, round_result):
    expected_result = ROUND_RESULT[round_result]
    if elf_choice == 'A':
        return ROCK[expected_result]
    elif elf_choice == 'B':
        return PAPER[expected_result]
    else:
        return SCISSORS[expected_result]

print(player_move('A', 'Z'))