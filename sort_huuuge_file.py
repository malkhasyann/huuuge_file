""" This script creates the sorted copy of the huuuge file. """

# create a huge dict to track each number entry count in the file
huge_dict = {i: 0 for i in range(121)}

with open('huuuge.txt', 'r', encoding='utf-8') as fr, open('sorted_huuuge.txt', 'w', encoding='utf-8') as fw:
    for line in fr:  # read every line
        numbers = [int(x) for x in line.split()]  # convert numbers to int
        for number in numbers:  # add 1 to the counter if the number appeared
            huge_dict[number] += 1

    i = 1  # counter for newline character
    for key in huge_dict:  # write each number in new file
        while huge_dict[key] > 0:  # as many times they appear in the initial file
            fw.write(f'{key} ')
            huge_dict[key] -= 1
            if i % 25 == 0:
                fw.write('\n')
            i += 1
