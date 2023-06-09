#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    total_index = 0
    for i in range(len(argv) - 1):
        total_index += (int(argv[i + 1]))
    print("{:d}".format(total_index))
