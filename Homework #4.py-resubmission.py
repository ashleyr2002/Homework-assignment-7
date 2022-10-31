#Homework 1 (c,e,g)(pg. 169/170)
#(c)
s1 = "spam"
s2 = "ni!"
print (s1[1])
#(e)
s1 = "spam"
s2 = "ni!"
print(s1[2]+s2[:2])
#(g)
s1 = "spam"
s2 = "ni!"
print(s1.upper())
#Homework 2 (a,d,e)(pg. 170)
#(a)
s1 = "spam"
s2 = "ni!"
print("NI!")
#(d)
s1 = "spam"
s2 = "ni!"
print("spam")
#(e)
s1 = "spam"
s2 = "ni!"
print(["sp","m"])
#Homework 3 (b,c,e)
#(b)
for w in "Now is the winter of our discontent...".split():
    print(w)
#(c)
for w in "Mississippi".split("i"):
    print(w, end=" ")
#(e)
msg = ""
for ch in "secret":
    msg = msg + chr(ord(ch)+1)
print(msg)
#Homework 4
print ('grades = "', end='')
grades = 60 * "F" + 10 * "D" + 10 * "C" + 10 * "B" + 10 * "A"
print(grades)
#Homework 5 (#3 pg. 171)
def main():

    num_grade = int(input("Enter grade number: "))
    grades = 60 * "F" + 10 * "D" + 10 * "C" + 10 * "B" + 10 * "A"
    print("The grade is", grades[num_grade])

main()
#Homework 6(pg. 171)
def main():

   
    phrase = input("Enter the phrase: ")

   
    phraseSplit = phrase.split()


    acronym = ""

    
    for x in phraseSplit:
        acronym = acronym + x[0].upper()

    print("The acronym for your phrase is ",acronym + ".")

main()


#Homework 7(pg. 171-172)
name= input("Enter your full name: ").lower()
print()
print (sum(ord(ch)-96 for ch in name))
