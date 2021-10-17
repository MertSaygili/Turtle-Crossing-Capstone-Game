import turtle
from turtle import Turtle, Screen
import time, random

# Attributes
game_is_on = True
game_level = 1
movement_of_cars = 0
cars = []
car_colors = ["black", "red", "orange", "purple", "brown", "green", "darkGoldenrod", "yellow", "pink", "cyan"]
car_starting_positions_y = [230, 182, 134, 86, 38, -10, -58, -106, -154, -202]
color_number = 0
car_starting_point_x = 270
car_starting_point_y = 230
car_moves_forward = 20

# Screen settings
screen = Screen()
screen.setup(width=600, height=500)
screen.tracer(0)


turtle.listen()

def making_cars(color_number_0, i):
    global car_starting_point_y, car_starting_point_x, color_number
    car_starting_point_x_0 = random.randint(270, 800)
    car = Turtle("square")
    car.penup()
    car.color(car_colors[color_number_0])
    car.goto(car_starting_point_x_0, car_starting_positions_y[i])
    car.shapesize(0.8, 1.6)
    car.left(180)
    cars.append(car)
    color_number = color_number_0 + 1

def when_game_is_over():
    over_screen = Turtle()
    over_screen.hideturtle()
    over_screen.penup()
    over_screen.color("black")
    over_screen.write(f"Game's Over !!! ", False, "center", ("Arial", 24, "normal"))

# Lvl Design
lvl_table = Turtle()
lvl_table.penup()
lvl_table.hideturtle()
lvl_table.color("Black")
lvl_table.goto(-255, 220)
lvl_table.write(f"Level: {game_level}", False, "center", ("Arial", 12, "normal"))
# Player
player = Turtle("turtle")
player.shapesize(0.9)
player.penup()
player.goto(0, -230)
player.left(90)


def m_forward():
    player.forward(21)
def m_backward():
    player.backward(21)

screen.onkey(key="w", fun=m_forward)
screen.onkey(key="s", fun=m_backward)

# Making cars
if game_level == 1:
    for i in range(0, 10, 1):
        making_cars(color_number, i)
        if color_number == len(car_colors):
            color_number = 0


while game_is_on:
    for i in range(0, len(cars), 1):
        cars[i].forward(car_moves_forward)
        car_x_cor = cars[i].xcor()
        player_y_cor = player.ycor()
        if car_x_cor < -300:
            random_x_pos = random.randint(270, 1300)
            cars[i].goto(random_x_pos, car_starting_positions_y[i])
        if player.distance(cars[i]) <= 15:
            game_is_on = False
            when_game_is_over()
        if player_y_cor > 240:
            player.goto(0, -230)
            game_level = game_level + 1
            print(f"You've passed to {game_level}. lvl")
            lvl_table.clear()
            lvl_table.write(f"Level: {game_level}", False, "center", ("Arial", 12, "normal"))
            car_moves_forward = car_moves_forward + 10
            time.sleep(1.5)

    screen.update()
    time.sleep(0.08)


screen.exitonclick()
