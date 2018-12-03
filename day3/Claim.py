class Claim:
    def __init__(self, claim_string):
        claim_string = claim_string.split(' ')
        self.id = claim_string[0][1:]
        margins = claim_string[2].split(',')
        self.left_margin = margins[0]
        self.right_margin = margins[1][:-1]
        dimensions = claim_string[3].split('x')
        self.width = dimensions[0]
        self.height = dimensions[1]