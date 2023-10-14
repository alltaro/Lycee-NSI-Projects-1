import turtle

def draw_tulip(size):
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)

def draw_flower(size):
    for _ in range(4):
        draw_tulip(size)
        turtle.right(90)

def draw_tulip_field(num_flowers, size):
    for _ in range(num_flowers):
        draw_flower(size)
        turtle.right(360 / num_flowers)

def main():
    turtle.speed(1)
    draw_tulip_field(10, 50)
    turtle.done()

if __name__ == "__main__":
    main()