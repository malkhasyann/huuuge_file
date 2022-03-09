""" This script sorts a huuuge file of integers using less memory than 200MB. """

huge_dict = dict()  # creating a huge dict to track each number entry in the file
for i in range(121):
    huge_dict[i] = 0

with open('huuuge.txt', 'r') as fr, open('sorted_huuuge.txt', 'w') as fw:
    for line in fr:  # read every line
        numbers = [int(x) for x in line.split()]  # cast numbers to int
        for number in numbers:  # add count of each number
            huge_dict[number] += 1

    i = 1  # counter for newline character
    for key in huge_dict:
        while huge_dict[key] > 0: # write huge_dict[key] times key in the new file
            fw.write(f"{key} ")
            if i % 25 == 0:
                fw.write('\n')
            huge_dict[key] -= 1
            i += 1
