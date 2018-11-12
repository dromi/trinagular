import math

import numpy as np


class MeshModel(object):

    def __init__(self, image):
        self.image = image
        self.width, self.height = self.image.size
        self.height -= 1
        self.width -= 1

        # Setup initial Triangles
        it0 = ((0,0), (0, self.height), (self.width, self.height))
        it1 = ((0,0), (self.width, 0), (self.width, self.height))
        self.current_triangles = [
            self._construct_new_triangle(it0),
            self._construct_new_triangle(it1)
        ]

    def get_triangles(self):
        return self.current_triangles

    def find_and_split_triangle(self):
        # Find triangle with highest stddev
        # Split it
        # store new triangles and delete the old one
        # repeat
        split_candidate = self.get_next_triangle()
        new_triangle1, new_triangle2 = split_candidate.get_split_children()
        self.current_triangles.append(self._construct_new_triangle(new_triangle1))
        self.current_triangles.append(self._construct_new_triangle(new_triangle2))
        self.current_triangles.remove(split_candidate)

    def get_next_triangle(self):
        """
        Finds triangle with highest stddev and returns it
        :return:
        """
        return max(self.current_triangles, key = lambda x: x.stddev)

    def _construct_new_triangle(self, p):
        pix0 = self.image.getpixel(p[0])
        pix1 = self.image.getpixel(p[1])
        pix2 = self.image.getpixel(p[2])

        r = round((pix0[0]+pix1[0]+pix2[0])/3)
        g = round((pix0[1]+pix1[1]+pix2[1])/3) 
        b = round((pix0[2]+pix1[2]+pix2[2])/3)

        stddev = np.std(np.array([pix0, pix1, pix2]))
        return Triangle(p[0], p[1], p[2], (r, g, b), stddev)
    

class Triangle(object):

    def __init__(self, p1, p2, p3, color, stddev):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.color = color
        self.stddev = stddev

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
