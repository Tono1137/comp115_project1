import turtle
import random

pye = turtle.Turtle()

wn = turtle.Screen()

wn.bgcolor("black")

wn.setup(width=800, height=600)

pye.speed(0)

pye.up()

def make_star(num):

    for i in range(num):

        radius = 0.26
        if (i%20 == 0):
            radius = 1.2
        elif (i%30 == 0):
            radius = 0.8

        x = random.randrange(-380,380,1)
        y = random.randrange(-280,280,1)

        pye.up()

        pye.goto(x,y)

        randnum = random.randrange(0,15,1)

        pye.begin_fill()

        pye.down()
        pye.begin_fill()

        pye.color(starcolor[randnum])
        pye.circle(radius)
        pye.end_fill()
        pye.up()
    
def interloper():
    x = -30
    y = 220
    r = 3
    h = 30 #Heading

    pye.goto(x,y)

    pye.setheading(h)

    pye.color("steelblue4")

    pye.begin_fill()

    pye.circle(-r*4,75)
    pye.circle(-r*2,90)
    pye.circle(-r*4,75)

    pye.end_fill()


    pye.begin_fill()
    pye.color("paleturquoise3")
    pye.circle(-r*4,15)
    pye.circle(-r*2,90)
    pye.circle(-r*4,15)
    pye.end_fill()
    
    pye.goto((x),(y-r*1.5))
    pye.setheading(h-180)
    ice(r)

    pye.goto((x-r),(y-r*3))
    pye.setheading(h+90)
    ice(r)


    pye.color("royalblue3")

    pye.goto((x+r*2),(y+r/1.5))
    pye.setheading(h-30)
    ice(r)

    pye.goto((x+r*4),(y-r/4))
    pye.setheading(h+190)
    ice(r)

    pye.goto((x+r*5),(y-r*2))
    pye.setheading(h+140)
    ice(r*1.5)

    pye.goto((x+r*6),(y-r*2))
    pye.setheading(h+150)
    ice(r/2)

    pye.goto((x+r*4),(y-r*4.5))
    pye.setheading(h+160)
    ice(r*1.3)

    pye.goto((x+r*2),(y-r*3.5))
    pye.setheading(h-45)
    ice(r)

    pye.up()

def bramble():
    x = 280
    y = -50
    r = 13

    pye.setheading(0)
# main planet body
    pye.color("gray10")
    pye.goto(x,y)
    pye.down()
    pye.begin_fill()
    pye.circle(r)
    pye.end_fill()
    pye.goto((x-r/3),(y+r/2))
    pye.color("lavenderblush")
    pye.begin_fill()
    pye.circle(r/5)
    pye.end_fill()
    pye.up()

# ice cloud
    pye.color("lightblue1")
    pye.goto((x+r/3),(y-r/5))
    ice(r)

    pye.goto((x-r/1.5),(y+r*3))
    ice(r/3)

    pye.goto((x+r*1.5),(y+r))
    pye.setheading(90)
    ice(r/3)

    pye.goto((x+r),(y+r*2.5))
    ice(r/1.5)

    pye.goto((x-r*2),(y+r*1.3))
    ice(r/2.5)
        
def ice(r):
    
    pye.down()
    pye.begin_fill()
    pye.forward(r)
    pye.right(90)
    pye.forward(r)
    pye.right(90)
    pye.forward(r*1.5)
    pye.right(90)
    pye.forward(r/10)
    pye.left(90)
    pye.forward(r)
    pye.right(120)
    pye.forward(r/2)
    pye.right(60)
    pye.forward(r/1.5)
    pye.left(39)
    pye.forward(r/1.3)
    pye.end_fill()
    pye.up()
    pye.goto(200,200)

def deep():

    x = 200
    y = 65

    pye.setheading(0)
# planet circle
    pye.goto(x,y)
    pye.color("darkolivegreen")
    pye.down()
    pye.begin_fill()
    pye.circle(60)
    pye.end_fill()
    pye.up()

# latitudinal lines
    pye.pensize(5)
    pye.color("darkolivegreen4")
    pye.setheading(0)
    pye.circle(60,-110)
    pye.down()
    pye.setheading(275)
    pye.circle(85,75)
    pye.up()

    pye.pensize(5)
    pye.color("darkolivegreen4")
    pye.setheading(20)
    pye.circle(60,30)
    pye.down()
    pye.setheading(340)
    pye.circle(120,-55)
    pye.up()    

    pye.pensize(5)
    pye.color("darkolivegreen4")
    pye.setheading(220)
    pye.circle(60,-30)
    pye.down()
    pye.setheading(280)
    pye.circle(85,65)
    pye.up()

    pye.pensize(5)
    pye.color("darkolivegreen4")
    pye.setheading(75)
    pye.circle(60,35)
    pye.down()
    pye.setheading(350)
    pye.circle(30,-70)
    pye.up()


    p = 15 # size
    d= 40 # heading

# starts drawing probe cannon 
    pye.goto(x-100,y+100)
    pye.color("burlywood1")
    pye.down()
    pye.setheading(d)
    pye.begin_fill()
    pye.forward(p*1.5)
    pye.right(85)
    pye.forward(p/2)
    pye.left(90)
    pye.forward(p/4)
    pye.left(90)
    pye.forward(p*1.5)
    pye.left(90)
    pye.forward(p/4)
    pye.left(90)
    pye.forward(p/2)
    pye.right(85)
    pye.forward(p*1.5)
    pye.left(85)
    pye.forward(p/4)
    
    pye.end_fill()
    pye.up()

def hollow():

    x = 45
    y = 0
    r = 25

    pye.setheading(0)
    pye.pensize(1)

# main planet body
    pye.goto(x,y)
    pye.color("darkslateblue")
    pye.down()
    pye.begin_fill()
    pye.circle(r)
    pye.end_fill()
    pye.up()

# polar ice caps
    pye.circle(r,-30)
    pye.color("whitesmoke")
    pye.down()
    pye.begin_fill()
    pye.circle(r,60)
    pye.end_fill()
    pye.up()

    pye.circle(r,120)
    pye.down()
    pye.begin_fill()
    pye.circle(r,60)
    pye.end_fill()
    pye.up()

# hollow's lantern
    pye.goto(x+r,y+(r+10))
    pye.color("orangered2")
    pye.down()
    pye.begin_fill()
    pye.circle(r/4)
    pye.end_fill()
    pye.up()
    
def hearth():   

    x = -65
    y = -10 

    r = 30 # scale

    
    f=0
    a=5
    b=0
    degree = 30
    # for fibonacci river

    pye.setheading(0)
# main planet
    pye.goto(x,y)
    pye.color("darkolivegreen4")
    pye.down()
    pye.begin_fill()
    pye.circle(r)
    pye.end_fill()
# rivers
    pye.color("cornflowerblue")
    pye.left(90)
    pye.pensize(r/10)
    pye.forward(r/4)
    pye.right(45)
    pye.circle(r/4,120)

    pye.right(110)
    pye.circle(-r/2,130)
    pye.up()

    pye.goto(x-(r/10),y+(r/1.5))
    pye.down()
    pye.setheading(60)
    for i in range(5):
    
        pye.circle(a*(r/18),-degree)#A*5.5

        f = a

        a = a+b

        b = f

        if (i%2 == 0):
            degree *= -1
            degree += 90

    pye.up()
    



    # attlerock
    pye.color("gray40")
    pye.goto(x,y-(r/1.5))
    pye.down()
    pye.begin_fill()
    pye.circle(r/3)
    pye.end_fill()
    pye.up()

def twins():

    
    x = -170
    y = -10
    r = 20
    
    pye.setheading(-135)
# ember twin (orange)
    pye.color("chocolate2")
    pye.up()
    pye.goto(x,y)
    pye.down()
    pye.begin_fill()
    pye.circle(r,180)
    pye.end_fill()
    pye.left(90)
    pye.forward(r)
    pye.pensize(r/2)
    pye.right(90)
    pye.forward(r/5)
    pye.pensize(1)
    pye.right(90)
    pye.forward(r)
    pye.left(90)
    pye.begin_fill()
    pye.circle(r,180)
    pye.end_fill()
# sand column
    pye.up()
    pye.forward(r/10)
    pye.down()
    pye.right(90)
    pye.color("cornsilk2")
    pye.pensize(r/2)
    pye.forward(r*2)
# ash twin (grey)
    pye.color("cornsilk3")
    pye.pensize(1)
    pye.right(90)
    pye.begin_fill()
    pye.circle(r)
    pye.end_fill()
    pye.up()

def sun(s):
    
    pen = 10
    size = 200
    sun_color = ["orangered2","orange2","gold"]
    for i in range(3):
        pye.pensize(pen)
        pye.goto(-460,size*-1)
        pye.color(sun_color[i])
        pye.setheading(0)
        pye.begin_fill()
        pye.down()
        pye.circle(size,180)
        pye.end_fill()
        pye.up()

        pen += 10
        size -= 20*s
        s += 1
    

starcolor = ["whitesmoke","white","lightyellow","chocolate","tomato",
             "orangered","lightsalmon","sandybrown","darkorange","goldenrod",
             "peru","peachpuff","seashell","cornflowerblue","lightblue","lightcyan"]




make_star(250)

bramble()

deep()

hollow()

hearth()

twins()

interloper()


sun(1)







wn.exitonclick()