import turtle
import math

def draw_pythagoras_tree(t, length, level):
    if level == 0:
        t.forward(length)
        t.backward(length)
        return

    t.forward(length)
    t.left(45)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, level - 1)
    t.right(90)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, level - 1)
    t.left(45)
    t.backward(length)

def main():
    level = int(input("Введіть рівень рекурсії: "))
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed("fastest")
    t.left(90)
    draw_pythagoras_tree(t, 100, level)
    turtle.done()

if __name__ == "__main__":
    main()
