#Homework 1

#If is first tested in an if-elif-if code, If this method fails
#then in that case the first elif would be tested, but you could use the try
#block first but you may get an error

#Homework 2
print("This program will be calculating your grade")

 

scores=int(input("Enter current grade for Computer Science: "))

if scores>90:

    grade='A'

elif scores>80:

    grade='B'

elif scores>=70:

    grade='C'

elif scores>60:

    grade='D'

else:

    grade='F'

 

print("\nGrade is: " + grade)
#Homework 3


def babysitting():
    print("Enter times using 24 hour format")
    start=input("Starting Time (hh:mm) :")
    end = input("Ending time (hh:mm):")
    start1=start.split(":")
    end1=end.split(":")
    for i in range(len(start1)):
        start1[i]=int(start1[i])
        end1[i]=int(end1[i])

    if end1[0]<21:
        payment=((end1[0]-start1[0])*2.5)+((end1[1]-start1[1])*2.5/60)

    if end1[0]>=21:
        payment= ((21-start1[0])*2.5) +((end1[0]-21)*1.75) - (start1[1]*2.5/60)+(end1[1]*1.75/60)

    payment = "{:.2f}".format(payment)    
    print("Total payment due : $",payment)
babysitting()


        
#Homework 4


print("This program tells your ability to run for the Senate and House")

 

age=int(input("Enter your current age: "))

if age>=30:

    eligibility='Yes!'

elif age>=25:

    eligibility='Yes!'

else:

    eligibility='No, sorry'

 

print("\nEligibility is: " + eligibility)

 

citizen=int(input("Enter how long you have been a citizen of the United States: "))

if citizen>=9:

    eligibility='Yes!'

elif citizen>=7:

    eligibility='Yes!'

else:

    eligibility='No, sorry'

 

print("\nEligibility is: " + eligibility)
 #Homework 5

try:
    x = float(input("Enter a number "))
    sum = 0
except ValueError:
    print("how many numbers do you want too average")
except ZeroDivisionError:

    print("You total number is")
    sum=sum+a
finally:
    print("There may or may not have been an exception.")
#The errors in this program are the valueerror and the zero division error.
#these errors can be caused by an unrecognized value and or if a number is
#divided by 0


