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
    for i in range(N_CIRCLES):
        draw_random_circle(canvas)


def draw_random_circle(canvas):
    """
    # Use create_oval method
    """
    circle_color = random_color()

    x1 = random.randint(0, CANVAS_WIDTH)
    y1 = random.randint(0, CANVAS_HEIGHT)

    x2 = x1 + CIRCLE_SIZE
    y2 = y1 + CIRCLE_SIZE

    canvas.create_oval(x1, y1, x2, y2, color=circle_color)

    
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
