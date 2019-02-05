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
        pos = line[10:16].replace(' ', '').split(',')
        vel = line[-8:-2].replace(' ', '').split(',')
        out.append([[int(pos[0]), int(pos[1])],[int(vel[0]), int(vel[1])]])
    return out


def solve(puzzle_input):
    positions = []
    velocities = []
    for i in puzzle_input:
        positions.append(i[0])
        velocities.append(i[1])

    print_sky(positions)


def print_sky(positions):
    offset_x = positions[0][0]
    offset_y = positions[0][1]
    max_x = positions[0][0]
    max_y = positions[0][1]
    
    for pos in positions[1:]:
        if pos[0] < offset_x:
            offset_x= pos[0]
        if pos[1] < offset_y:
            offset_y = pos[1]
    
    #CURRENTLY WORKING ON THIS LINE
    sky_map = [[]*(max_x - offset_x)]*(max_y - offset_y)
    print(sky_map)    

def run_sim(positions, velocities):
    for i in range(positions):
        positions[i][0] += velocities[i][0]
        positions[i][1] += velocities[i][1]
    return(positions)

start_time = time.time()
main()
end_time = time.time()
print('\n' + ''.join(['-'] * 26) + '\nFINISHED\nTIME:', end_time - start_time,
      '\n' + ''.join(['-'] * 26))
input()
