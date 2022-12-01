'''
This list represents the Calories of the food carried by five Elves:

The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
The second Elf is carrying one food item with 4000 Calories.
The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
The fifth Elf is carrying one food item with 10000 Calories.
In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
'''

import os

def absolute_file_name(file_name):
    return os.path.join(os.path.dirname(__file__), file_name)


def save_max_items(max_items, current_value, current_index):
    for i in range(3):
        if max_items[i]['value'] < current_value:
            j = 2
            while j > i:
                max_items[j]['value'] = max_items[j-1]['value']
                max_items[j]['index'] = max_items[j-1]['index']
                j -= 1
            max_items[i]['value'] = current_value
            max_items[i]['index'] = current_index
            break
    return max_items


def elf_with_max_calories(file_name):
    with open(absolute_file_name(file_name)) as f:
        current_index = 1
        current_value = 0
        max_items = [{'value': 0, 'index': 0}, {'value': 0, 'index': 0}, {'value': 0, 'index': 0}]

        for line in f:
            line = line.strip('\n')
            # sum each line until not empty line
            if line:
                current_value += int(line)
            else:
                # save value and index of maximum
                max_items = save_max_items(max_items, current_value, current_index)
                current_value = 0
                current_index += 1

    max_items = save_max_items(max_items, current_value, current_index)

    return max_items


def sum_calories(max_calories):
    return sum(item['value'] for item in max_calories)


def print_result(max_calories):
    print("Three elves with the most calories are:")
    for item in max_calories:
        print(f"{item['value']}, carried by the {item['index']} Elf")
    print(f"Tatal amount of calories is {sum_calories(max_calories)}") 


def main():
    print_result(elf_with_max_calories('calories_list'))


if __name__ == "__main__":
    main()
