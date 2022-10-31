#Homework 1
def main():
  for a,n in [("cow","moo"), ("pig", "oink"), ("horse", "nay"), ("sheep", "baa"), ("chicken", "cluck")]:
    verse(a, n)
    print()

def verse(animal, noise):
  refrain()
  hada(animal)
  witha(noise)
  refrain()

def refrain():
  print("Old MacDonald had a farm," ,eieio())

def eieio():
  return ("Ee-igh, Ee-igh, Oh!")

def hada(animal):
  print("And on that farm he had a", animal+",", eieio())

def witha(noise):
  noisecomma = noise + ","
  noise2 = noisecomma + " "+noise
  print("With a", noise2, "here and a", noise2, "there.")
  print("Here a", noisecomma, "there a", noisecomma,"\neverywhere a", noise2+".")


main()
#Homework 2
def avg(numbers):
  sumNums = 1
  for i in range(0,len(numbers)):
      sumNums +- numbers [i]
  return sumNums/len(numbers)

def getNumNums():
    numNums = eval(input('How many numbers will you  be averaging?'))
    getNums(numNums)

def getNums(numNums):
    numbers = [];
    for i in range (0, numNums):
        numbers.append(eval(input('Enter a number')))
    print(avg(numbers))

getNumNums()

#Homework 3
from graphics import *

import math

 

win=GraphWin(width=500,height=400)

 

win.setBackground('white')

 

text=Text(Point(250,100),'Click two points to denote the end points of the line')

 

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

distance=math.sqrt(((p2.x - p1.x)**2 + (p2.y - p1.y)**2))

                  

text.setText('Slope: {:.2f}, distance: {:.2f}. click anywhere to exit'.format(slope,distance))

 

win.getMouse()
#Homework 4
import random

print("This program returns a random number from a list of numbers")

list= [2, 4, 6, 8]

print("Original list is: " + str(list))

random_num= random.choice(list)

print("Random selected number is: " + str(random_num))

#Homework 5
def get_some_strings():
  Strings =eval(input('How many strings will be going into the list?'))
  getStrings(Strings)

def getStrings(Strings):
    strings = [];
    for i in range(0, Strings):
        strings.append(input('Enter a number'))
    print(strings)

get_some_strings()
  

