# there is no score - keeping or timer

# import required modules
import random
import turtle


# use the Screen() method of the turtle class to change background
turtle.Screen().bgcolor("green")
screen = turtle.Screen()

# make the hero of the game and set his properties
ted = turtle.Turtle()
ted.penup()
ted.shape("turtle")
ted.turtlesize(3,3)
ted.goto(-300, 300)
ted.color("blue")
ted.speed(7)

# make the enemy turtles
enemy = []
for i in range(10):
    enemy.append(turtle.Turtle())
    enemy[i].penup()
    enemy[i].speed(1)
    enemy[i].shape("turtle")
    enemy[i].color("red")

def move(i):
    i.goto(random.randint(-500,500),random.randint(-500,500))

screen.onclick(ted.goto)

while True:
    for i in enemy:
        move(i)
        if (ted.distance(i) < 100):
            i.hideturtle()
            enemy.remove(i)
            i.goto(-500, 500)
    if(len(enemy) < 1):
        break

    
    
turtle.Screen().mainloop()