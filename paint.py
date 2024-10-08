"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()



def draw_circle(start, end): #Había una colisiòn de nombres, por eso lo cambie a draw_cricle, pero funciona - Marce
    """Draw circle from start to end."""    
    up()
    radius = abs(end.x - start.x) / 2
    goto((start.x + end.x) / 2, (start.y + end.y) / 2 - radius)
    down()
    begin_fill()
    circle(radius)
    end_fill()


def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    
    for _ in range(2):
        forward(end.x - start.x)  
        left(90)
        forward(end.y - start.y)  
        left(90)


def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    
    begin_fill()
    x1, y1 = start.x, start.y
    x2, y2 = end.x, start.y
    x3, y3 = (start.x + end.x) / 2, end.y

    
    goto(x2, y2) 
    goto(x3, y3)  
    goto(x1, y1)  
    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('pink'), 'P') #Nuevo color - Marce
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', draw_circle), 'c') #Se aplica el nuevo nombre de la función - Marce
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
