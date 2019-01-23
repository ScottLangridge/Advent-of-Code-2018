import time


def main():
    print('Test:', solve(get_input('example1.txt')), '\n')
    # print('Solution:', solve(get_input()))
    pass


def get_input(filepath='input.txt'):
    with open(filepath, 'r') as f:
        raw = f.readline()
    out = raw.split(' ')
    out = list(map(int, out))
    return out


# Node = [Children, Metadata

def get_nodes(puzzle_input):
    children = puzzle_input[0]

    if children == 0:
        return [None, puzzle_input[2: 2 + puzzle_input[1]]], puzzle_input[2 + puzzle_input[1]:]
    else:
        meta = puzzle_input[- puzzle_input[1]:]
        puzzle_input = puzzle_input[2:- len(meta)]

    out = [[], meta]
    for i in range(children):
        result = get_nodes(puzzle_input)
        out[0].append(result[0])
        puzzle_input = result[1]
    return out, puzzle_input


def solve(puzzle_input):
    root = get_nodes(puzzle_input)[0]
    return sum_metas(root)


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
