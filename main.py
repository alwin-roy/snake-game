import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.title("snake game")
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(snake.up, "w")
my_screen.onkey(snake.down, "s")
my_screen.onkey(snake.left, "a")
my_screen.onkey(snake.right, "d")


game_is_on = True

while game_is_on:
    my_screen.update()
    time.sleep(0.1)

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()


    for segments in snake.segments[1:]:

        if snake.head.distance(segments) < 10:
            game_is_on = False
            scoreboard.game_over()



    snake.move()









my_screen.exitonclick()