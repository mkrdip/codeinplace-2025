from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
N_CIRCLES = 20


def main():
    # print('Random Circles')
    # When you use a function or important, try assigning it to a variable
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # Extension 1
    num_circles = random.randint(1, N_CIRCLES)
    for i in range(num_circles):
        draw_random_circle(canvas)


def draw_random_circle(canvas):
    """
    # Use create_oval method
    """
    circle_color = random_color()
    circ_size = random_size()

    # extension 2 and 3
    x1 = random.randint(0, CANVAS_WIDTH - circ_size)
    y1 = random.randint(0, CANVAS_HEIGHT - circ_size)

    x2 = x1 + circ_size
    y2 = y1 + circ_size

    canvas.create_oval(x1, y1, x2, y2, color=circle_color)


def random_size():
    circ_size = random.randint(5, 50)
    return circ_size

    
def random_color():
    """
    This is a function to use to get a random color for each circle. We have
    defined this for you and there is no need to edit code in this function,
    but feel free to read it over if you are interested. 
    """
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)

if __name__ == '__main__':
    main()

