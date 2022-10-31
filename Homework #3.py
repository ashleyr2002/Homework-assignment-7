from graphics import *
win = GraphWin()
#Homework question 1(pg.81 #13)
def main():
    print("This program adds series of numbers entered by the user")
    num = eval(input("How many numbers do you want to sum? "))
    x = 0
    s = 0
    while x < num:
        x += 1
        s += eval(input("Enter a number: "))
    print("The total value of your", num, "numbers is ", s)
main()
#Homework question 2(pg.81 #14)
def main() :
     n = int (input ("How many numbers are to be summed: ") ) 
     sum=0
     for i in range(n) :
        a = int (input ("Please enter number  : ") ) 
        sum=sum+a
     print ("Average of a series of numbers :",sum/n) 

main()
#Homework question 3(pg. 125 a-g)
#a - A set point at (130, 130) on the window

#b - A blue circle with a red outline at a point.

#c - A blue, red and green rectangle at a specific point with a width of 3.

#d - A red line with an arrow at the end that is set to start and end at
# a specific point.

#e - An oval centered at a specific point with a fixed radius.

#f - An orange polygon that is centered with specific points.

#g - Text printed as "Hello World!", that has courier font, has a font size of
#16 and set to italic

#Homework question 4(pg. 128 #3) 
#A circle with a red color that is at a particular point listed in the code,
#if the user clicks on a blank space, the circle with move to that spot and
#it closes the program

#Homework question 5(pg. 126 #2)
def main():
    win = GraphWin('Archery Target',200,200)
center = Point(100,100)

w = Circle(center, 80)
w.setFill('white')
w.draw(win)

bl = Circle(center, 60)
bl.setFill('black')
bl.draw(win)

b = Circle(center, 40)
b.setFill('blue')
b.draw(win)

r = Circle(center, 20)
r.setFill('red')
r.draw(win)

y = Circle(center, 10)
y.setFill('yellow')
y.draw(win)

win.getMouse() 
win.close()

main()

#Homework question 6(pg. 126 #3)
circ=Circle(Point(100,100), 50)
win=GraphWin()
circ.setFill('yellow')
circ.setOutline('black')
circ.draw(win)

leftEye=Circle(Point(130,100), 5)
leftEye.setFill('black') 
leftEye.setOutline('white')
leftEye.draw(win)
rightEye=Circle(Point(70,100), 5)
rightEye.setFill('black')
rightEye.setOutline('white')
rightEye.draw(win)

Line(Point(90,120), Point(110,120)).draw(win)

#Homework question 7(pg. 126 #8)
import math
def main():
    win=GraphWin(width=400,height=200)
    win.setBackground('white')
    text=Text(Point(200,50),'Click Me!')
    text.draw(win)
    p1=win.getMouse()
    p2=win.getMouse()
    line=Line(p1,p2)
    line.draw(win)
    midX=(p1.x+p2.x)/2
    midY=(p1.y+p2.y)/2
    dot=Circle(Point(midX,midY),3)
    dot.setFill('cyan')
    dot.draw(win)
    dx=abs(p1.x-p2.x)
    dy=abs(p1.y-p2.y)
    slope=dy/dx
    length=math.sqrt(dx*dx+dy*dy)
    text.setText('Slope: {:.2f}, length: {:.2f}. click anywhere to exit'.format(slope,length))
    win.getMouse()


main()
