class Claim:
    def __init__(self, claim_string):
        claim_string = claim_string.split(' ')
        self.id = claim_string[0][1:]
        margins = claim_string[2].split(',')
        self.left_margin = int(margins[0])
        self.top_margin = int(margins[1][:-1])
        dimensions = claim_string[3].split('x')
        self.width = int(dimensions[0])
        self.height = int(dimensions[1])
        self.top_left = (self.left_margin, self.top_margin)
        self.top_right = (self.left_margin + self.width - 1, self.top_margin)
        self.bottom_left = (self.left_margin, self.top_margin + self.height - 1)
        self.bottom_right = (self.left_margin + self.width - 1, self.top_margin + self.height - 1)
        self.corners = [self.top_left, self.top_right, self.bottom_left, self.bottom_right]

    def point_is_inside_claim(self, point):
        if self.top_left[0] <= point[0] <= self.bottom_right[0] \
                and self.top_left[1] <= point[1] <= self.bottom_right[1]:
            return True
        else:
            return False
