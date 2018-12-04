class Claim:
    def __init__(self, claim_string):
        split_claim = claim_string.split(' ')
        self.id = int(split_claim[0][1:])
        self.left_margin = int(split_claim[2].split(',')[0])
        self.top_margin = int(split_claim[2].split(',')[1][:-1])
        self.width = int(split_claim[3].split('x')[0])
        self.height = int(split_claim[3].split('x')[1])
        self.corners = self.get_corners()

    def get_corners(self):
        return [(self.left_margin, self.top_margin),
                (self.left_margin + self.width - 1, self.top_margin),
                (self.left_margin, self.top_margin + self.height - 1),
                (self.left_margin + self.width - 1, self.top_margin + self.height - 1)]

    def get_points(self):
        points = []
        x = self.corners[0][0]
        while x <= self.corners[3][0]:
            y = self.corners[0][1]
            while y <= self.corners[3][1]:
                points.append((x, y))
                y += 1
            x += 1
        return points

    def claim_overlap(self, claim):
        overlap_exists = False
        for corner in claim.corners:
            if self.contains_point(corner):
                overlap_exists = True

        if overlap_exists:
            overlap = 0
            for point in claim.get_points():
                if self.contains_point(point):
                    overlap += 1
            return overlap
        return 0

    def contains_point(self, point):
        if self.corners[0][0] <= point[0] <= self.corners[3][0] \
                and self.corners[0][1] <= point[1] <= self.corners[3][1]:
            return True
        else:
            return False
