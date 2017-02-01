import sys
"""arg[0]: scriptName    arg[1]:fileName"""


def read_nth_line(num, file_name):
    f = open(file_name, 'r')
    content = f.readlines()
    return content[num - 1]
if __name__ == '__main__':
    num = input('Enter the line number\n')
    line = read_nth_line(num, sys.argv[1])
    print(line)

