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
    pass


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
