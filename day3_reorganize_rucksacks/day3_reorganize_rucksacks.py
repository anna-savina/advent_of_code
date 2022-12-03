'''
'''

import os
from string import ascii_lowercase
from string import ascii_uppercase

def absolute_file_name(file_name):
    return os.path.join(os.path.dirname(__file__), file_name)


def items_prioriry():
    items_by_priority = ['0']
    for c in ascii_lowercase:
        items_by_priority.append(c)
    for C in ascii_uppercase:
        items_by_priority.append(C)

    return items_by_priority


def calculate_priopity_part1(file_name, items_prioriry):
    with open(absolute_file_name(file_name)) as f:
        res = 0
        for line in f:
            line = line.strip('\n')
            length = len(line)
            line_part1 = line[0:int(length/2)]
            line_part2 = line[int(length/2):length]
            for c in line_part1:
                if c in line_part2:
                    res += items_prioriry.index(c)
                    break
    return res


def calculate_priopity_part2(file_name, items_prioriry):
    res = 0
    with open(absolute_file_name(file_name)) as f:
        line = f.readline().strip('\n')
        while line:
            group = []
            for i in range(3):
                group.append(line)
                line = f.readline().strip('\n')
            for c in group[0]:
                if c in group[1]:
                    if c in group[2]:
                        res += items_prioriry.index(c)
                        break
    return res




def main():
    file_name = 'rucksacks_contents_list'
    print(f"The sum of the priorities of item types v.1 is {calculate_priopity_part1(file_name, items_prioriry())}")
    print(f"The sum of the priorities of item types v.2 is {calculate_priopity_part2(file_name, items_prioriry())}")


if __name__ == "__main__":
    main()