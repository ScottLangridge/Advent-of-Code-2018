class Claim:
    def __init__(self, claim_string):
        split_claim = claim_string.split(' ')
        self.id = int(split_claim[0][1:])
        self.left_margin = int(split_claim[2].split(',')[0])
        self.top_margin = int(split_claim[2].split(',')[1][:-1])
        self.width = int(split_claim[3].split('x')[0])
        self.height = int(split_claim[3].split('x')[1])

        print('id', self.id)
        print('left_margin', self.left_margin)
        print('top_margin', self.top_margin)
        print('width', self.width)
        print('height', self.height)
        input()
