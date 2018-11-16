import time

from PIL import Image
from mesh_model import MeshModel
import pygame
import sys


rendering_triangles = []

def main():
    pygame.init()
    im = Image.open('data/small_owl.jpg')
    width, height = im.size
    model = MeshModel(im)
    screen = pygame.display.set_mode((width, height))

    while (True):
        # check for quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for triangle in model.get_triangles():
            pygame.draw.polygon(screen, triangle.color, [triangle.p1, triangle.p2, triangle.p3], 0)
            pygame.draw.polygon(screen, (0, 0, 0), [triangle.p1, triangle.p2, triangle.p3], 1)

        pygame.display.update()
        model.find_and_split_triangle()
        time.sleep(0.1)


if __name__ == '__main__':
    main()