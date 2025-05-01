import math

x1,y1,x2,y2 = eval(input('Enter two points:(latitude, longitude)'))

d = 6371.01 * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x2)) + math.cos(math.radians(x1)) * math.cos(math.radians(x2)) * math.cos(math.radians(y1) - math.radians(y2)))

print('The distance between the two points is', str(d), 'km')