"""Advent of Code 2022: Day 6 Parts 1 & 2"""

with open("input_6.txt", "r+")as input_file:
    read_string = ''
    start_of_packet = None
    start_of_message = None
    for line in input_file:
        for i, char in enumerate(line):
            # the program iterates thrrough the input character by character,
            # building a new string: this makes searching the last 4 or 14 characters
            # much simpler syntactically
            read_string += char
            if(i + 1) > 4:
                if len(set(read_string[-4:])) == 4 and not start_of_packet:
                    # if the last four characters of the new string are unique, and
                    # the start_of_packet is not set, it is recorded
                    start_of_packet = i + 1
                if len(set(read_string[-14:])) == 14 and not start_of_message:
                    # as with previous if, except for the last fourteen characters
                    start_of_message = i + 1

    print(start_of_packet, start_of_message, sep="\n")
