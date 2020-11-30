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
def get_response_time(beach):
    
    d1 = float(beach[0]) *3
    
    d2 = float(beach[1])
    
    h = float(beach[2])
    h = h *3
    
    v_sand = float(beach[3])
    v_sand = (5280 * float(v_sand))/3600
    
    n = float(beach[4])
    
    theta1 = float(beach[5])
    
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
    return t

'''The print line includes formating that outputs t as a one decimal number'''
