class Claim:
    def __init__(self, claim_string):
        split_claim = claim_string.split(' ')
        self.id = int(split_claim[0][1:])
        self.left_margin = int(split_claim[2].split(',')[0])
        self.top_margin = int(split_claim[2].split(',')[1][:-1])
        self.width = int(split_claim[3].split('x')[0])
        self.height = int(split_claim[3].split('x')[1])
        self.corners = self.get_corners()
        print(self.corners)

    def get_corners(self):
        return [(self.left_margin, self.top_margin),
                (self.left_margin + self.width - 1, self.top_margin),
                (self.left_margin, self.top_margin + self.height - 1),
                (self.left_margin + self.width - 1, self.top_margin + self.height - 1)]
