def main():
    print('Solution:', solve(get_input()))


def get_input(filepath = 'input.txt'):
    out = []
    with open(filepath, 'r') as f:
        raw = f.readlines()

    for line in raw:
        out.append(line.strip('\n'))
    return out


def solve(puzzle_input):
    last_code = ''
    codes = []
    for code in puzzle_input:
        codes.append(''.join(sorted(code)))
    codes.sort()
    for code in codes:
        if last_code == code:
            print('two codes match')
        else:
            code = last_code

main()
