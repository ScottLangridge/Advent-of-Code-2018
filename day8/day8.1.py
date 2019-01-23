import time


def main():
    print('Test:', solve_node(get_input('example1.txt')),'\n')
    # print('Solution:', solve_node(get_input()))
    pass


def get_input(filepath='input.txt'):
    with open(filepath, 'r') as f:
        raw = f.readline()
    out = raw.split(' ')
    out = list(map(int, out))
    return out


def solve_node(puzzle_input):
    # Add root node metadata + remove root
    num_children = puzzle_input[0]
    out = sum(puzzle_input[- puzzle_input[1]:])
    puzzle_input = puzzle_input[2:-puzzle_input[1]]

    # Split input into several child node inputs
    children = []
    i = 0
    print(puzzle_input)
    while num_children != 0:
        subnodes = puzzle_input[i]
        i += puzzle_input[i+1] + 1
        print(i)
        input()


start_time = time.time()
main()
end_time = time.time()
print('\n' + ''.join(['-'] * 26) + '\nFINISHED\nTIME:', end_time - start_time,
      '\n' + ''.join(['-'] * 26))
input()
