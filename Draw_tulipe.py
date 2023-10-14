import turtle

def draw_tulip(size):
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)

def draw_flower(size):
    for _ in range(4):
        draw_tulip(size)
        turtle.right(90)

def draw_tulip_field(size):
    turtle.right(360 / 10)
    for _ in range(3):
        draw_flower(size)
        turtle.right(360 / 10)

def main():
    turtle.speed(10)
    draw_tulip_field(50)
    turtle.done()

if __name__ == "__main__":
    main()