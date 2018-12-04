import time
from random import shuffle


def main():
    print('Test:', solve(get_input('example1.txt')),'\n')
    # print('Solution:', solve(get_input()))
    pass

def get_input(filepath='input.txt'):
    out = []
    with open(filepath, 'r') as f:
        raw = f.readlines()

    for line in raw:
        out.append(line.strip('\n'))
    return out


def solve(puzzle_input):
    pass


def debug():
    raw = get_input('rand_example1.txt')
    parse_input(raw)


def parse_input(puzzle_input):
    records = []
    for line in puzzle_input:
        # Split into datetime and string
        line = line[1:]
        split_line = line.split('] ')
        records.append([split_line[0], split_line[1]])

    records.sort()

    for line in records:
        print(line)







def scramble_example():
    with open('example1.txt', 'r') as f:
        lines = f.readlines()
        shuffle(lines)
    with open('rand_example1.txt','w') as f:
        f.writelines(lines)


start_time = time.time()
debug()
# main()
end_time = time.time()
print('\n' + ''.join(['-'] * 26) + '\nFINISHED\nTIME:', end_time - start_time,
      '\n' + ''.join(['-'] * 26))
input()
