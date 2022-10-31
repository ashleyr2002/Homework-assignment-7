#Homework 1
# definite loop vs Indefinite loop

# A definite loop is a loop that runs the segment of code described
#within it for a predefined number of times.
#An indefinite loop is a loop that keeps
#running until it finds some condition to stop.

#for loop vs. While loop

#A for loop is used under the condition when
#the number of iterations is predifined in the condition part.
#The while loop is the opposite of a for loop and is used when
#the number of iterations is not predefined we can use while loop.

#interactive loop vs. Sentinel loop

#Interactive loops are loops that interact with the user to determine the
#repetition of a part of a program.
#A sentinal loop processes data until it finds a mark where to stop.

#sentinel loop vs. End-of-file loop

#A sentinel loop works on data whose value should be different from
#sentinel value.
#A end-of-file loop terminates when it detects the end of file.

#Homework 2
#On attached pdf



#Homework 3
#(a)
n = int(input("Enter value for n: "))
i = 1
total = 0
while(i<=n):
    total += i
    i += 1
print(total)
print()
 #(c)
n = int(input("Enter value for n: "))
total = 0
while(n!=999):
    total += n
    n = int(input("Enter value for n: "))
print(total)
print()


#Homework 4
nterms = int(input("How many terms? "))

 

n1, n2 = 0, 1

count = 0

 

if nterms <= 0:

   print("Please enter a positive integer")

elif nterms == 1:

   print("Fibonacci sequence upto",nterms,":")

   print(n1)

else:

   print("Fibonacci sequence:")

   while count < nterms:

       print(n1)

       nth = n1 + n2

       n1 = n2

       n2 = nth

       count += 1

#Homework 5
def main():
   print("")
   inNumber = eval(input("Please enter a number: "))
   print("")

   count = 0
   print(inNumber)
   while inNumber != 1:
      if(inNumber % 2 == 0):
         take =inNumber//2
         print(take)
         inNumber = take
         count = count + 1
      else:
         take = inNumber*3 + 1
         print(take)
         inNumber = take
         count = count + 1

   print("")
   print(str(count)+ 'computations preformed!')
   print("")

main()
