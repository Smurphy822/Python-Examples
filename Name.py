#Cameron Murphy
#9/18
#get name function
import math

def getname(name):
    input_name= name
    input_name=input_name.lower()
    input_name=input_name.title

    
#step two display the name back for the user
    print("The name you entered was",input_name)
#step 3 verify the name
    input("Is this correct yes or no?")

print("This is our function.")
#get a users name
def get_name():
#step one ask user for a name
    name=input("What's your name?")
#get_name(name)


#calculate the area of a cirlce
#radius*radius*pie
def AreaOfCircle():
    pi=3.141592653
#1 get a radius
    radius=input("What is the radius?")
#2 calculate the area
    radius = float(radius)
    area=radius*radius*pi
#3 display the area
    print("The area of the circle is:",area)

##AreaOfCircle()


def pythagoras_theorem(ap=1,bp=1):
    a=float(ap)
    b=float(bp)
    c=a*a+b*b
    c=math.sqrt(c)

    print("The third side is",c)


    

##pythagoras_theorem(3,4)

def add_numbers(x,y):
    num1= x
    print("num1 = x",num1)
    num2= y
    print("num2 = y",num1)
    num3= int(num1)+int(num2)
    return num3

x=1
y=9
#num4=add_numbers(x,y)
#print(num4)

def num(a,b,c,d,e,f,g,h,i,j):
    mean=float(input("How many test scores are there?"))
    average=(a+b+c+d+e+f+g+h+i+j)/mean
    return average

a=float(input("what is the first test score?"))
b=float(input("what is the second test score?"))
c=float(input("what is the third test score?"))
d=float(input("what is the fourth test score?"))
e=float(input("what is the fifth test score?"))
f=float(input("what is the sixth test score?"))
g=float(input("what is the seventh test score?"))
h=float(input("what is the eighth test score?"))
i=float(input("what is the ninth test score?"))
j=float(input("what is the tenth test score?"))

avg=num(a,b,c,d,e,f,g,h,i,j)
print("The average is",avg)























