import re
import time

from day3.Claim import Claim


def main():
    # print('Test 1:', solve([1,1,1]))
    # print('Test 2:', solve([1,1,-2]))
    # print('Test 3:', solve([-1,-2,-3]))
    print('\nSolution:', solve(get_input()))


def get_input():
    out = []
    with open('input.txt', 'r') as f:
        raw = f.readlines()

    for line in raw:
        out.append(line.strip('\n'))
    return out


def solve(puzzle_input):
    claims = []
    for claim_string in get_input():
        claims.append(Claim(claim_string))








start_time = time.time()
main()
end_time = time.time()
print('\n' + ''.join(['-']*26) + '\nFINISHED\nTIME:', end_time - start_time, '\n' + ''.join(['-']*26))
input()
