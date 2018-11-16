import time

from PIL import Image

import error
from mesh_model import MeshModel
import pygame
import sys

IMAGE = 'data/small_owl.jpg'
OUTLINE = False
ERROR_METRIC = error.stddev_avg_times_size
SLEEP_TIME = 0.0
SPLIT_PR_ROUND = 20

def main():
    pygame.init()
    im = Image.open(IMAGE)
    width, height = im.size
    model = MeshModel(im, ERROR_METRIC)
    screen = pygame.display.set_mode((width, height))

    while (True):
        # check for quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for triangle in model.current_triangles:
            pygame.draw.polygon(screen, triangle.color, [triangle.p1, triangle.p2, triangle.p3], 0)
            if OUTLINE:
                pygame.draw.polygon(screen, (0, 0, 0), [triangle.p1, triangle.p2, triangle.p3], 1)

        pygame.display.update()
        for i in range(SPLIT_PR_ROUND):
            model.find_and_split_triangle()
        time.sleep(SLEEP_TIME)


if __name__ == '__main__':
    main()