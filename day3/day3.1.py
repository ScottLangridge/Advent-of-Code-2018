import time

from day3.Claim import Claim


def main():
    print('Test:', solve(get_input('example1.txt')), '\n')
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



start_time = time.time()
main()
end_time = time.time()
print('\n' + ''.join(['-'] * 26) + '\nFINISHED\nTIME:', end_time - start_time,
      '\n' + ''.join(['-'] * 26))
input()
