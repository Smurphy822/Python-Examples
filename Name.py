#Cameron Murphy
#9/18

#get a users name
##def get_name():
#step one ask user for a name
    ##name=input("What's your name?")
#step two display the name back for the user
    ##print("The name you entered was",name)
#step 3 verify the name
    ##input("Is this correct yes or no?")

##print("This is our function.")
##get_name()


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

AreaOfCircle()
