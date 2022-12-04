'''
Part1
In how many assignment pairs does one range fully contain the other?

Part2
In how many assignment pairs do the ranges overlap?

'''

import os
from string import ascii_lowercase
from string import ascii_uppercase

def absolute_file_name(file_name):
    return os.path.join(os.path.dirname(__file__), file_name)


def convert_data_to_int(line):
    groups = line.split(',')
    group1 = groups[0].split('-')
    group2 = groups[1].split('-')
    for i in range(2):
        group1[i] = int(group1[i])
        group2[i] = int(group2[i])
    
    return [group1, group2]


def calculate_overlap_part1(file_name):
    with open(absolute_file_name(file_name)) as f:
        res = 0
        for line in f:
            line = line.strip('\n')
            groups = convert_data_to_int(line)
            if groups[0][0] <= groups[1][0] and groups[0][-1] >= groups[1][-1]:
                res += 1
            elif groups[1][0] <= groups[0][0] and groups[1][-1] >= groups[0][-1]:
                res += 1
    return res


def calculate_overlap_part2(file_name):
    with open(absolute_file_name(file_name)) as f:
        res = 0
        for line in f:
            line = line.strip('\n')
            groups = convert_data_to_int(line)
            if range(max(groups[1][0], groups[0][0]), min(groups[1][-1], groups[0][-1])+1):
                res += 1
    return res


def main():
    file_name = 'sections_list'
    print(f"The number of pairs whose range fully contain the other is {calculate_overlap_part1(file_name)}")
    print(f"The number of pairs whose range overlap the other is {calculate_overlap_part2(file_name)}")


if __name__ == "__main__":
    main()