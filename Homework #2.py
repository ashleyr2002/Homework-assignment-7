import math as math 
#Question 1
for i in range (5):
    print (i * i)
for d in [3,1,4,1,5]:
    print(d, end=" ")
for i in range(4):
    print("Hello")
for i in range (5):
    print (i, 2**i)
#Question 2
ans = eval("4.0 / 10.0 + 3.5 * 2") 
print (ans)
ans = eval ("abs(4 - 20//3) ** 3")
print (ans)
ans = eval("3 * 10 // 3 + 10 % 3")
print (ans)
#Question 3
n = 2
n*(n-1)/2
print(n*(n-1)/2)
r = 4
4*math.pi*r**2
print (4*math.pi*r**2)
#Question 4
for i in [1,3,5,7,9] :
    print (i, ":" , i**3)
    print(i)
x = 2
y = 10
for j in range (0, y, x):
      print (j , end=" ")
      print (x + y)
print ("done")
#Question 5
def main():
    print("This program will calculate the slope of a line through 2 points.")
    print()
    ptx1, pty1 = eval(input("Input the first x and y point separated by a comma "))
    ptx2, pty2 = eval(input("Input the second x and y point separated by a comma "))
    slopey = pty2 - pty1
    slopex = ptx2 - ptx1

    print("The slope is", slopey, '/', slopex)


main()
#Question 6
x1=int(input("enter x1 : "))

x2=int(input("enter x2 : "))

y1=int(input("enter y1 : "))

y2=int(input("enter y2 : "))

result= ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)

print("distance between",(x1,x2),"and",(y1,y2),"is : ",result)

