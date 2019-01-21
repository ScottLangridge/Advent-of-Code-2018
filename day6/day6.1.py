import time


def main():
    print('Test:', solve(get_input('example1.txt')),'\n')
    # print('Solution:', solve(get_input()))
    pass


def get_input(filepath='input.txt'):
    out = []
    with open(filepath, 'r') as f:
        raw = f.readlines()

    for line in raw:
        str_coord = line.strip('\n').split(',')
        out.append([int(str_coord[0]), int(str_coord[1])])
    return out


def solve(puzzle_input):
    print(find_extremes(puzzle_input))
    

def find_extremes(input):
    low_x = input[0][0]
    high_x = input[0][0]
    low_y = input[0][1]
    high_y = input[0][1]

    for coord  in input[1:]:
        x = coord[0]
        y = coord[1]
        
        if x < low_x: low_x = x
        if y < low_y: low_y = y
        if x > high_x: high_x = x
        if x > high_y: high_y = y

    return [low_x, high_x, low_y, high_y]

start_time = time.time()
main()
end_time = time.time()
print('\n' + ''.join(['-'] * 26) + '\nFINISHED\nTIME:', end_time - start_time,
      '\n' + ''.join(['-'] * 26))
input()
