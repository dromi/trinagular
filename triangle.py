from PIL import Image
from mesh_model import MeshModel
import pyglet

window = pyglet.window.Window()
rendering_triangles = []
fps_display = pyglet.clock.ClockDisplay()
model = None

def main():
    im = Image.open('data/banana.jpg')
    width, height = im.size
    global model
    model = MeshModel(im)

    window.set_size(width, height)
    pyglet.app.run()


@window.event
def on_draw():
    window.clear()
    for triangle in model.get_triangles():
        _draw_triangle(triangle)
    fps_display.draw()
    model.find_and_split_triangle()


def _draw_triangle(tri):
    pyglet.graphics.draw(3, pyglet.gl.GL_TRIANGLES,
                         ('v2i', tri.unpack_position()),
                         ('c3B', tri.unpack_color())
                         )

    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
                         ('v2i', (tri.p1[0], tri.p1[1], tri.p2[0], tri.p2[1])),
                         'c3B', (0, 0, 0, 0, 0, 0)
                         )

    cx, cy = tri.get_center()

    label = pyglet.text.Label(str(tri.stddev),
                          font_name='Times New Roman',
                          font_size=16,
                          x=cx, y=cy,
                          anchor_x='center', anchor_y='center')
    label.draw()



if __name__ == '__main__':
    main()