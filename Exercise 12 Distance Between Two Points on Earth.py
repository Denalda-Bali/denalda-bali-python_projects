#Exercise 12: Distance Between Two Points on Earth             (27 Lines)

#The surface of the Earth is curved, and the distance between degrees of longitude
#varies with latitude. As a result, finding the distance between two points on the surface
#of the Earth is more complicated than simply using the Pythagorean theorem.
#Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth’s
#surface. The distance between these points, following the surface of the Earth, in
#kilometers is:

#distance = 6371.01 * arccos(sin(t1)*sin(t2)+cos(t1)*cos(t2)*cos(g1-g2))

#The value 6371.01 in the previous equation wasn’t selected at random. It is
#the average radius of the Earth in kilometers.

#Create a program that allows the user to enter the latitude and longitude of two
#points on the Earth in degrees. Your program should display the distance between
#the points, following the surface of the earth, in kilometers.

#Hint: Python’s trigonometric functions operate in radians. As a result, you will
#need to convert the user’s input from degrees to radians before computing the
#distance with the formula discussed previously. The math module contains a
#function named radians which converts from degrees to radians.

from math import radians, cos, sin, asin, acos

t1 = float (input("Enter the latitude of two points on the Earth: "))
t2 = float (input("Enter the latitude of two points on the Earth: "))

g1 = float (input("Enter the longitude of two points on the Earth: "))
g2 = float (input("Enter the longitude of two points on the Earth: "))


distance = 6371.01 * acos(sin(t1)*sin(t2)+cos(t1)*cos(t2)*cos(g1-g2))
print ("the distance between two point is : ", distance)

t1 = radians(t1)
t2 = radians(t2)

g1 = radians(g1)
g2 = radians(g2)

print ("The latitude 1 ", t1, "convertet in radians ",radians(t1))
print ("The latitude 2 ", t2, "convertet in radians ",radians(t2))

print ("The longitude 1 ", g1, "convertet in radians ",radians(g1))
print ("The longitude 2 ", g2, "convertet in radians ",radians(g2))


