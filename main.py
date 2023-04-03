import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from points import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(l_paddle.go_up, "w")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
        score.update_score()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
        score.update_score()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

screen.exitonclick()
