import math


class Triangle(object):

    def __init__(self, p1, p2, p3, color, error):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.color = color
        self.error = error

    def unpack_position(self):
        return (self.p1[0], self.p1[1],
                self.p2[0], self.p2[1],
                self.p3[0], self.p3[1])

    def unpack_color(self):
        return (self.color[0], self.color[1], self.color[2],
                self.color[0], self.color[1], self.color[2],
                self.color[0], self.color[1], self.color[2])

    def get_split_children(self):
        # Find longest line
        dists = [
            (self.p1, self.p2, math.hypot(self.p2[0] - self.p1[0], self.p2[1] - self.p1[1])),
            (self.p3, self.p2, math.hypot(self.p3[0] - self.p2[0], self.p3[1] - self.p2[1])),
             (self.p1, self.p3, math.hypot(self.p1[0] - self.p3[0], self.p1[1] - self.p3[1]))
        ]
        longest = max(dists, key = lambda x: x[2])
        # Find point on the middle of this
        new_p = (round((longest[0][0] + longest[1][0])/2), round((longest[0][1] + longest[1][1])/2))
        # Find the point opposite to the new point
        opposite_p = list({self.p1, self.p2, self.p3} - {longest[0], longest[1]})[0]
        # return new points
        return (longest[0], new_p, opposite_p), (longest[1], new_p, opposite_p)

    def get_center(self):
        return round((self.p1[0] + self.p2[0] + self.p3[0])/3), round((self.p1[1] + self.p2[1] + self.p3[1])/3)
