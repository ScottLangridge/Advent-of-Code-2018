import time

from day3.Claim import Claim


def main():
    # print('Test 1:', solve(get_input('example1.txt')))
    print('\nSolution:', solve(get_input()))


def get_input(filename='input.txt'):
    out = []
    with open(filename, 'r') as f:
        raw = f.readlines()

    for line in raw:
        out.append(line.strip('\n'))
    return out


def solve(puzzle_input):
    claims = []
    for claim_string in puzzle_input:
        claims.append(Claim(claim_string))

    overlaps = 0
    for x in range(1000):
        print('Completion: ' + str(100 * x / 1000) + '%')
        for y in range(1000):
            contains_point = 0
            for claim in claims:
                if claim.contains_point((x, y)):
                    contains_point += 1
            if contains_point > 1:
                overlaps += 1
    return overlaps


def count_overlaps(claims):
    if len(claims) == 1:
        return 0

    overlap = 0
    checking = claims[0]
    for claim in claims[1:]:
        overlap += checking.claim_overlap(claim)
    return overlap + count_overlaps(claims[1:])


start_time = time.time()
main()
end_time = time.time()
print('\n' + ''.join(['-'] * 26) + '\nFINISHED\nTIME:', end_time - start_time, '\n' + ''.join(['-'] * 26))
input()
