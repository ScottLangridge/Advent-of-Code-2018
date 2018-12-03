import time

from day3.Claim import Claim


def main():
    # print('Test:', solve(get_input('example1.txt')), '\n')
    print('Solution:', solve(get_input()))


def get_input(filepath='input.txt'):
    out = []
    with open(filepath, 'r') as f:
        raw = f.readlines()

    for line in raw:
        out.append(line.strip('\n'))
    return out


def solve(puzzle_input):
    claims = []
    for claim_string in puzzle_input:
        claims.append(Claim(claim_string))
    return get_overlap(claims)


def get_overlap(claims):
    overlap = 0
    for i in range(len(claims)):
        testing = claims[i]
        for claim in claims[i + 1:]:
            if claims_overlap(testing, claim):
                overlap += measure_overlap(testing, claim)
    return overlap


def claims_overlap(c1, c2):
    for corner in c1.corners:
        if c2.point_is_inside_claim(corner):
            return True
    else:
        return False


def measure_overlap(c1, c2):
    if c1.top_left[0] < c2.top_left[0]:
        start_x = c1.top_left[0]
    else:
        start_x = c2.top_left[0]
    if c1.top_left[1] < c2.top_left[1]:
        start_y = c1.top_left[1]
    else:
        start_y = c2.top_left[1]
    if c1.bottom_right[0] > c2.bottom_right[0]:
        end_x = c1.bottom_right[0]
    else:
        end_x = c2.bottom_right[0]
    if c1.bottom_right[1] > c2.bottom_right[1]:
        end_y = c1.bottom_right[1]
    else:
        end_y = c2.bottom_right[1]

    x = start_x
    overlap = 0
    while x <= end_x:
        y = start_y
        while y <= end_y:
            if c1.point_is_inside_claim((x, y)) and c2.point_is_inside_claim((x, y)):
                overlap += 1
            y += 1
        x += 1
    return overlap


start_time = time.time()
main()
end_time = time.time()
print('\n' + ''.join(['-'] * 26) + '\nFINISHED\nTIME:', end_time - start_time,
      '\n' + ''.join(['-'] * 26))
input()
