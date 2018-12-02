def main():
    print('Solution:', solve(get_input())

def get_input():
    out = []
    with open('input.txt', 'r') as f:
        raw = f.readlines()

    for line in raw:
        out.append(line.strip("\n"))
    return out


def solve(puzzle_input):
    pairs = 0
    triples = 0
    
    for code in puzzle_input:
        code = sorted(code)

        if has_triple(code):
            triples += 1
        if has_pair(code):
            pairs += 1

    return(pairs * triples)
    

def has_pair(code):
    pass

def has_triple(code):
    pass

main()
