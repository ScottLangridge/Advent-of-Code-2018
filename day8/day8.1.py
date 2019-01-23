import time


def main():
    # print('Test:', solve(get_input('example1.txt')), '\n')
    # print('Test:', solve(get_input('example2.txt')), '\n')
    print('Solution:', solve(get_input()))
    pass


def get_input(filepath='input.txt'):
    with open(filepath, 'r') as f:
        raw = f.readline()
    out = raw.split(' ')
    out = list(map(int, out))
    return out


# Node = [[Children], [Metadata]]

def get_nodes(puzzle_input):
    children = puzzle_input[0]
    meta = puzzle_input[1]
    i = 0
    offset = 0
    running_total = 0
    for branch in range(children):
        i += 2
        result = get_nodes(puzzle_input[i:])
        running_total += result[0]
        i += result[1]
        offset += result[1] + 2
    i += 2
    for meta in range(meta):
        running_total += puzzle_input[i]
        offset += 1
        i += 1
    return running_total, offset



def solve(puzzle_input):
    root = get_nodes(puzzle_input)[0]
    print(root)


def sum_metas(node):
    running_sum = sum(node[1])
    if node[0] is None:
        return running_sum
    else:
        for i in node[0]:
            running_sum += sum_metas(i)
        return running_sum



start_time = time.time()
main()
end_time = time.time()
print('\n' + ''.join(['-'] * 26) + '\nFINISHED\nTIME:', end_time - start_time,
      '\n' + ''.join(['-'] * 26))
input()
