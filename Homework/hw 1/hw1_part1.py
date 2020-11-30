'''
Dana Solitaire
Section 17
9/20/2018

This program finds the time required for a lifeguard to reach a swimmer
'''

import math as m


'''
All values are converted into ft and or seconds except n and theta.
The program takes in all values as strings, then prints it back as strings.
then the values are converted into floats for computation


#taking input
'''
d1 = input('Enter the shortest distance from the lifeguard to water, d1 (yards) => ')
print(d1)
d1 = float(d1) *3
d2 = input('Enter the shortest distance from the swimmer to the shore, d2 (feet) => ')
print(d2)
d2 = float(d2)
h = input('Enter the lateral displacement between the lifeguard and the swimmer, h (yards) => ')
print(h)
h = float(h)
h = h *3
v_sand = input('Enter the lifeguard\'s running speed on sand, v_sand (MPH) => ') 
print(v_sand)
v_sand = float(v_sand)
v_sand = (5280 * float(v_sand))/3600
n = input('Enter the lifeguard\'s swimming slowdown factor, n => ')
print(n)
n = float(n)
theta1 = input('Enter the direction of lifeguard\'s running on sand, theta1 (degrees) => ')
print(theta1)
theta1 = float(theta1)

'''
computation

ratio is tan(theta), theta1 is converted to radians
x = the oppsite side of a right triangle where d1 is the adjacent side to theta1
l1 and l2 are the hypotenuses 
'''

ratio = m.tan(m.radians(theta1))
x = (d1 * ratio) 
l1 = m.sqrt(pow(x, 2) + pow(d1, 2))
l2 = m.sqrt(pow((h - x), 2) + pow(d2, 2))
t = (1 / v_sand) * (l1 + n * l2)

'''The print line includes formating that outputs t as a one decimal number'''

print(f'If the lifeguard starts by running in the direction with theta1 of', round(theta1), 'degrees,')
print(f'they will reach the swimmer in {t:.1f} seconds')
