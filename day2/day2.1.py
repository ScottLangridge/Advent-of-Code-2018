def main():
    solve(get_input())

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
        triple = has_triple(code)
        if triple != False:
            code = remove_element(code, triple)
            
            
            

def has_pair(code):
    pass

def has_triple(code):
    pass

main()
