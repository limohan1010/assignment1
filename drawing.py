from turtle import *

from random import randint

def draw_pikachu():
    def draw_head(center_x, center_y):
        up()
        goto(center_x, center_y)
        down()
        setheading(35)
        begin_fill()
        circle(-155, 72)
        fillcolor("#F5D142")
        
        up()
        goto(65, 125)
        down()
        setheading(305)
        circle(-155, 32)
        setheading(300)
        circle(-145, 22)
        forward(6)
        setheading(265)
        circle(-85, 75)
        
        up()
        goto(-85, -90)
        down()
        up()
        goto(-155, 115)
        down()
        setheading(245)
        circle(115, 38)
        right(12)
        forward(12)
        setheading(255)
        circle(85, 118)
        
        up()
        goto(-85, -90)
        down()
        setheading(15)
        up()
        goto(-155, 115)
        down()
        up()
        goto(center_x, center_y)
        down()
        end_fill()
        
    def draw_eyes():
        color("black","black")
        up()
        goto(-120, 35)
        down()
        begin_fill()
        setheading(5)
        circle(26)
        end_fill()
        
        color("white", "white")
        up()
        goto(-115, 58)
        down()
        begin_fill()
        setheading(5)
        circle(11)
        end_fill()
        
        color("black", "black")
        up()
        goto(35, 48)
        down()
        begin_fill()
        setheading(5)
        circle(26)
        end_fill()
        
        color("white", "white")
        up()
        goto(27, 70)
        down()
        begin_fill()
        setheading(5)
        circle(11)
        end_fill()

    def draw_cheeks():
        color("#8C4614", "#FF4601")
        up()
        goto(-120, -60)
        down()
        begin_fill()
        setheading(5)
        circle(28)
        end_fill()
        
        color("#8C4614", "#FF4601")
        up()
        goto(63, -30)
        down()
        begin_fill()
        setheading(5)
        circle(28)
        end_fill()

    def draw_nose():
        color("black", "black")
        up()
        goto(-50, 45)
        down()
        begin_fill()
        circle(8, steps=3)
        end_fill()

    def draw_mouth():
        color("black", "#FF6AB5")
        up()
        goto(-20, 30)
        down()
        begin_fill()
        setheading(265)
        forward(65)
        circle(-12, 155)
        forward(60)
        up()
        goto(-48, 29)
        down()
        end_fill()
        
        color("#8C0101", "#8C0101")
        begin_fill()
        up()
        goto(-20, 30)
        down()
        up()
        goto(-24, -8)
        down()
        up()
        goto(-62, -11)
        down()
        up()
        goto(-70, 20)
        down()
        up()
        goto(-48, 29)
        down()
        up()
        goto(-20, 30)
        down()
        end_fill()
        
    def draw_ears():
        color("black","#F5D142")
        up()
        goto(-150, 100)
        down()
        begin_fill()
        setheading(170)
        circle(-253, 53)
        right(125)
        circle(-253, 53)
        end_fill()
        
        color("black", "black")
        up()
        goto(-240, 200)
        down()
        begin_fill()
        setheading(147)
        circle(175, 28)
        left(125)
        circle(-234, 15)
        left(76)
        circle(320, 10)
        end_fill()
        
        color("black", "#F5D142")
        up()
        goto(40, 130)
        down()
        begin_fill()
        setheading(69)
        circle(-253, 53)
        right(125)
        circle(-253, 53)
        end_fill()
        
        color("black", "black")
        up()
        goto(170, 210)
        down()
        begin_fill()
        setheading(57)
        circle(175, 28)
        left(121)
        circle(234, 18)
        left(76)
        circle(-305, 10)
        end_fill()

    def draw_lightning():
        color("black", "#FFD700") 
        
        up()
        goto(120,-30)
        down()
        begin_fill()
        setheading(300)
        forward(25)
        setheading(240)
        forward(15)
        setheading(300)
        forward(20)
        setheading(0)
        forward(15)
        setheading(60)
        forward(25)
        setheading(0)
        forward(15)
        setheading(300)
        forward(20)
        end_fill()
        
        up()
        goto(-180, -30)
        down()
        begin_fill()
        setheading(240)
        forward(25)
        setheading(180)
        forward(15)
        setheading(240)
        forward(20)
        setheading(300)
        forward(15)
        setheading(240)
        forward(25)
        setheading(300)
        forward(15)
        setheading(240)
        forward(20)
        end_fill()
        

    pensize(2)
    hideturtle()
    speed(10)
    
   
    draw_head(-145, 125)
    draw_eyes()
    draw_cheeks()
    draw_nose()
    draw_mouth()
    draw_ears()
    draw_lightning()  
    done()

def draw_spiral():
    bgcolor('white')
    x = 200
    speed(0)
    penup()
    goto(-100, 50)
    pendown()
    while x > 0:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        colormode(255)
        pencolor(r, g, b)
        fd(x)
        rt(90.990)
        x = x - 1
    
    while x < 400:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        colormode(255)
        pencolor(r, g, b)
        fd(x)
        rt(90.990)
        x = x + 1

    exitonclick()


def draw_python():
    import turtle as t
    t.setup(800, 300, 200, 200)
    t.penup()
    t.fd(-150)
    t.pendown()
    t.seth(-40)
    t.pensize(25)
    t.pencolor("purple")
    for i in range(4):
        t.circle(40, 80)
        t.circle(-40, 80)
    t.circle(40, 80 / 2)
    t.fd(40)
    t.circle(16, 180)
    t.fd(40 * 2 / 3)
    t.done()


def draw_flower():

    setup(600, 800, 0, 0)
    speed(0)
    penup()  
    seth(90) 
    fd(340)  
    seth(0)
    pendown()  

    speed(5)  
    begin_fill() 
    fillcolor('red')  
    circle(50, 30) 

    for i in range(10):
        fd(1)
        left(10)  
    circle(40, 40)

    for i in range(6):
        fd(1)
        left(3)
    circle(80, 40)

    for i in range(20):
        fd(0.5)
        left(5)
    circle(80, 45)

    for i in range(10):
        fd(2)
        left(1)
    circle(80, 25)

    for i in range(20):
        fd(1)
        left(4)
    circle(50, 50)


    circle(120, 55)

    speed(3)

    seth(-90)
    fd(70)

    right(150) 
    fd(20)

    left(140)
    circle(140, 90)

    left(30)
    circle(160, 100)

    left(130)
    fd(25)

    penup()
    right(150)
    circle(40, 80)
    pendown()

    left(115)
    fd(60)

    penup()
    left(180)
    fd(60)
    pendown()

    end_fill()

    right(120)
    circle(-50, 50)
    circle(-20, 90)

    speed(1)
    fd(75)

    speed(1)
    circle(90, 110)

    penup()
    left(162)
    fd(185)
    left(170)
    pendown()
    circle(200, 10)
    circle(100, 40)
    circle(-52, 115)
    left(20)
    circle(100, 20)
    circle(300, 20)
    speed(1)
    fd(250)

    penup()
    speed(2)
    left(180)
    fd(250)
    circle(-300, 7)
    right(80)
    circle(200, 5)
    pendown()

    left(60)
    begin_fill()
    fillcolor('green')
    circle(-80, 100)
    fd(10)
    left(20)
    circle(-63, 127)
    end_fill()

    penup()
    left(50)
    fd(20)
    left(180)

    pendown()
    circle(200, 25)

    penup()
    right(150)

    fd(180)

    right(40)
    pendown()
    begin_fill()
    fillcolor('green')
    circle(-100, 80)
    right(150)
    fd(10)
    left(60)
    circle(-80, 98)
    end_fill()

    penup()
    left(60)
    fd(13)
    left(180)

    pendown()
    speed(1)
    circle(-200, 23)

    exitonclick()  

print("----- Welcome to the drawing system ----")
while True:
    a = input("---- Please select what you want to draw:\n"
              " (1 for python, 2 for flowers， 3 for spiral, 4 for pikachu)\n"
              "Your selection is: ")
    try:
        a = eval(a)
        if a == 1:
            draw_python()
        elif a == 2:
            draw_flower()
        elif a == 3:
            draw_spiral()
        elif a == 4:
            draw_pikachu()
        else:
            print("Please input the value in [1,2,3,4]")
    except:
        print("Please input the value in [1,2,3,4]")


