#!/usr/bin/env python

import sys
from operator import itemgetter

def process_line(line, prev_index, value_list):
    curr_index, index, value = line.rstrip().split("\t")
    index, value = map(float, [index, value])
    
    if curr_index == prev_index:
        value_list.append((index, value))
    else:
        if prev_index:
            process_and_print_result(prev_index, value_list)
        prev_index = curr_index
        value_list = [(index, value)]
    
    return prev_index, value_list

def process_and_print_result(prev_index, value_list):
    value_list = sorted(value_list, key=itemgetter(0))
    i = 0
    result = 0
    
    while i < len(value_list) - 1:
        if value_list[i][0] == value_list[i + 1][0]:
            result += value_list[i][1] * value_list[i + 1][1]
            i += 2
        else:
            i += 1
    
    print("{},{}".format(prev_index, str(result)))

def main():
    prev_index = None
    value_list = []

    for line in sys.stdin:
        prev_index, value_list = process_line(line, prev_index, value_list)

    if prev_index:
        process_and_print_result(prev_index, value_list)

if __name__ == "__main__":
    main()
