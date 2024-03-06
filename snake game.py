from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -385 < head.x < 370 and -320 < head.y < 320


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return
    snake.append(head)
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
    clear()
    for body in snake:
        square(body.x, body.y, 9, 'green')
    square(food.x, food.y, 9, 'red')
    update()
    ontimer(move, 80)


hideturtle()
tracer(False)  # it brings the elements into is's initial state
listen()  # it's update the game per second
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

move()
done()
