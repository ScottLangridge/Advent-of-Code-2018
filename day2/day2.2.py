def main():
    print('Test:', solve(get_input('example2.txt')),'\n')
    print('Solution:', solve(get_input()))


def get_input(filepath = 'input.txt'):
    out = []
    with open(filepath, 'r') as f:
        raw = f.readlines()

    for line in raw:
        out.append(line.strip('\n'))
    return out


def solve(puzzle_input):
    assert codes_are_unique_without_regard_to_letter_order(puzzle_input)

    sorted_codes = []
    for code in puzzle_input:
        sorted_codes.append(sorted(code))
    sorted_codes.sort()

    print (sorted_codes)
    input()

def break_codes_into_groups(codes):
    print(codes)
    current = ''
    groups = []
    for key in (codes):
        if codes[key][0] == current:
            groups[-1][key] = codes[key][1:]
        else:
            groups.append({key:codes[key][1:]})
            current = codes[key][0]

    print(groups)
    input()
    

def codes_are_unique_without_regard_to_letter_order(input_codes):
    last_code = ''
    codes = []
    for code in input_codes:
        codes.append(sorted(code))
    codes.sort()
    for code in codes:
        if last_code == code:
            return False
        else:
            last_code = code
    return True


main()
