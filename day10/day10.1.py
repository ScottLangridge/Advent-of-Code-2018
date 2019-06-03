import time


def main():
    print('Test:', solve(get_input('example1.txt')), '\n')
    # print('Solution:', solve(get_input()))
    pass


def get_input(filepath='input.txt'):
    out = []
    with open(filepath, 'r') as f:
        raw = f.readlines()

    for line in raw:
        pos = line[10:16].replace(' ', '').split(',')
        vel = line[-8:-2].replace(' ', '').split(',')
        out.append([[int(pos[0]), int(pos[1])], [int(vel[0]), int(vel[1])]])
    return out


def solve(puzzle_input):
    while True:
        print_sky(puzzle_input)
        puzzle_input = run_tick(puzzle_input)
        input('Hit enter for more.')


def run_tick(stars):
    for i in range(len(stars)):
        for j in range(2):
            stars[i][0][j] += stars[i][1][j]

    return stars


def print_sky(stars):
    # Normalise start positions so that grid can start at (0,0)
    min_x = max_x = stars[0][0][0]
    min_y = max_y = stars[0][0][1]

    for star in stars[1:]:
        if star[0][0] < min_x:
            min_x = star[0][0]
        elif star[0][0] > max_x:
            max_x = star[0][0]
        if star[0][1] < min_y:
            min_y = star[0][1]
        elif star[0][1] > max_y:
            max_y = star[0][1]

    max_x += -min_x
    max_y += -min_y

    for i in range(len(stars)):
        stars[i][0][0] += -min_x
        stars[i][0][1] += -min_y

    # Generate list for sky image
    star_map = []
    for y in range(max_y + 1):
        star_map.append([])
        for x in range(max_x + 1):
            star_map[-1].append('.')

    for star in stars:
        star_map[star[0][1]][star[0][0]] = '#'

    # Draw sky
    out = ''
    for row in star_map:
        for val in row:
            out = out + val
        out = out + '\n'
    print(out)


start_time = time.time()
main()
end_time = time.time()
print('\n' + ''.join(['-'] * 26) + '\nFINISHED\nTIME:', end_time - start_time,
      '\n' + ''.join(['-'] * 26))
input()
