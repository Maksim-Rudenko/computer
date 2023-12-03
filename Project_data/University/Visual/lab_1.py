import matplotlib.pyplot as plt
import turtle


rectangle = [(0,0),(0,1),(1,1),(1,0),(0,0)]
hexagon = [(0,0),(0,1),(1,2),(2,1),(2,0),(1,-1),(0,0)]
l_shape = [(0,0),(0,3),(1,3),(1,1),(3,1),(3,0),(0,0)]
concave = [(0,0),(0,3),(1,3),(1,1),(2,1),(2,3),(3,3),(3,0),(0,0)]
house = [(7,7),(7,13),(11,17),(15,13),(15,7),(7,7),(9,9),(9,12),(13,12),(13,9),(9,9)]

for points in [rectangle, hexagon, l_shape, concave, house]:
    # 1. Can I get rid of the zip? plot directly by points 
    # 2. How can I make the shape complete?
    xs, ys = zip(*points)
    #plt.plot(xs, ys, 'o')
    plt.plot(xs, ys, '-')

    automin, automax = plt.xlim()
    plt.xlim(automin-0.5, automax+0.5)
    automin, automax = plt.ylim()
    plt.ylim(automin-0.5, automax+0.5)
    # Can I display the shapes 2 in 1 line?
    plt.show()







# Здесь домик рисует черепашка 
'''
house = turtle.Turtle()
house.penup()
house.goto(150, 130)
house.pendown()
#square.shape("turtle")

house.right(90)
house.forward(60)
house.right(90)
house.forward(80)
house.right(90)
house.forward(60)
house.right(45)
house.forward(pow(40 ** 2 + 40 ** 2, 0.5))
house.right(90)
house.forward(pow(40 ** 2 + 40 ** 2, 0.5))
house.penup()
house.goto(130, 120)
house.pendown()
house.right(45)
house.forward(30)
house.right(90)
house.forward(40)
house.right(90)
house.forward(30)
house.right(90)
house.forward(40)
house.penup()

turtle.exitonclick()
'''