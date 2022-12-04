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


def calculate_overlap_part1(file_name):
    with open(absolute_file_name(file_name)) as f:
        res = 0
        for line in f:
            line = line.strip('\n')
            groups = line.split(',')
            group1 = groups[0].split('-')
            group2 = groups[1].split('-')
            if int(group1[0]) <= int(group2[0]) and int(group1[-1]) >= int(group2[-1]):
                res += 1
            elif int(group2[0]) <= int(group1[0]) and int(group2[-1]) >= int(group1[-1]):
                res += 1
    return res


def calculate_overlap_part2(file_name):
    with open(absolute_file_name(file_name)) as f:
        res = 0
        for line in f:
            line = line.strip('\n')
            groups = line.split(',')
            group1 = groups[0].split('-')
            group2 = groups[1].split('-')
            if int(group1[0]) <= int(group2[0]) and int(group2[0]) <= int(group1[-1]):
                res += 1
            elif int(group2[-1]) >= int(group1[0]) and int(group2[-1]) <= int(group1[-1]):
                res += 1
            elif int(group1[0]) >= int(group2[0]) and int(group1[0]) <= int(group2[-1]):
                res += 1
            elif int(group1[-1]) >= int(group2[0]) and int(group1[-1]) <= int(group2[-1]):
                res += 1
    return res


def main():
    file_name = 'sections_list'
    print(f"The number of pairs whose range fully contain the other is {calculate_overlap_part1(file_name)}")
    print(f"The number of pairs whose range overlap the other is {calculate_overlap_part2(file_name)}")


if __name__ == "__main__":
    main()