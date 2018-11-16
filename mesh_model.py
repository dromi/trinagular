from triangle import Triangle


class MeshModel(object):

    def __init__(self, image, error_metric):
        self.image = image
        self.width, self.height = self.image.size
        self.height -= 1
        self.width -= 1
        self.error_metric = error_metric

        # Setup initial Triangles
        it0 = ((0,0), (0, self.height), (self.width, self.height))
        it1 = ((0,0), (self.width, 0), (self.width, self.height))
        self.current_triangles = [
            self._construct_new_triangle(it0),
            self._construct_new_triangle(it1)
        ]

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
        Finds triangle with highest error and returns it
        :return:
        """
        return max(self.current_triangles, key=lambda x: x.error)

    def _construct_new_triangle(self, p):
        pix0 = self.image.getpixel(p[0])
        pix1 = self.image.getpixel(p[1])
        pix2 = self.image.getpixel(p[2])

        r = round((pix0[0]+pix1[0]+pix2[0])/3)
        g = round((pix0[1]+pix1[1]+pix2[1])/3) 
        b = round((pix0[2]+pix1[2]+pix2[2])/3)

        e2 = self.error_metric([pix0, pix1, pix2], p)


        return Triangle(p[0], p[1], p[2], (r, g, b), e2)
