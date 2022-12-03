'''
Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) 
that they say will be sure to help you win. "The first column is what your opponent is going to play: 
A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to 
help with someone's tent.
Part1
The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. 
Winning every time would be suspicious, so the responses must have been carefully chosen.
Part2
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says 
how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, 
and Z means you need to win. Good luck!"
'''

import os

def absolute_file_name(file_name):
    return os.path.join(os.path.dirname(__file__), file_name)


def round_score_calculator_part1(line):
    '''
        A - Rock, B - Paper, C - Sci
        X - Rock, Y - Paper, Z - Sci
        win - 6, draw - 3, lose - 0
    '''
    last_character = line[-1]
    first_character = line[0]
    points = {"X": 1, "Y": 2, "Z": 3}
    score = {"A": {"X" :3, "Y": 6, "Z": 0}, "B": {"X" :0, "Y": 3, "Z": 6}, "C": {"X" :6, "Y": 0, "Z": 3}}

    return points[last_character] + score[first_character][last_character]

def round_score_calculator_part2(line):
    '''
        A - Rock, B - Paper, C - Sci
        X - lose, Y - draw, Z - win
        win - 6, draw - 3, lost - 0
    '''
    last_character = line[-1]
    first_character = line[0]
    points = {"X": 0, "Y": 3, "Z": 6}
    score = {"X": {"A" :3, "B": 1, "C": 2}, "Y": {"A" :1, "B": 2, "C": 3}, "Z": {"A" :2, "B": 3, "C": 1}}

    return points[last_character] + score[last_character][first_character]


def game_score(file_name, part):
    how_to_calculate_score = [round_score_calculator_part1, round_score_calculator_part2]
    round_score = how_to_calculate_score[part-1]
    with open(absolute_file_name(file_name)) as f:
        res = 0
        for line in f:
            line = line.strip('\n')
            res += round_score(line.rstrip())
    
    return res


def main():
    print(f"Game score for first srtategy is {game_score('strategy', 1)}")
    print(f"Game score for second strategy is {game_score('strategy', 2)}")


if __name__ == "__main__":
    main()