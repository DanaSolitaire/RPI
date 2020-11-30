#Importing math library for complex computation 
import math as m


#Returns the volume given the radius in inches
def find_volume_sphere(radius):
    return(4 / 3 * m.pi * pow(radius, 3))

#Returns the volume given the side     
def find_volume_cube(side):
    return (pow(side, 3))

#Returns total number of gum balls 
def total_number_gum(weekly_sales):
    return weekly_sales * 1.25


#Taking input and assigning to variables
user_radius = input('Enter the gum ball radius (in.) => ')
print(user_radius)

user_weekly_sales = input('Enter the weekly sales => ')
print(user_weekly_sales)


#Converting strings to floats 
user_radius = float(user_radius)
user_weekly_sales = float(user_weekly_sales)

# gum balls unit
total_number_gum = m.ceil(user_weekly_sales * 1.25)
side_length_gb = m.ceil(pow(total_number_gum, 1 / 3))

# inches
side_length_in = side_length_gb * user_radius * 2
volume_in = find_volume_cube(side_length_in)
'''
print(side_length_gb)
print(side_length_in)
print(total_number_gum)
'''
max_gb = find_volume_cube(side_length_gb)
extra_balls = max_gb - total_number_gum

wasted_space = volume_in - find_volume_sphere(user_radius) * total_number_gum
'''
print(wasted_space)
'''
wasted_in = volume_in - find_volume_sphere(user_radius) * find_volume_cube(side_length_gb)
'''
print(wasted_in)
#target_sales = m.sqrt(total_number_gum / number_gum_dimension)
'''

first_line = '\nThe machine needs to hold ' + str(int(side_length_gb)) \
    + ' gum balls along each edge.'
second_line = '\nTotal edge length is {:.2f} inches.'.format(side_length_in)
third_line =  '\nTarget sales were {}, but the machine will hold {} ' \
    'extra gum balls.'.format(total_number_gum, extra_balls)
fourth_line = '\nWasted space is {:.2f} cubic inches with the target number of '\
    'gum balls,'.format(wasted_space)
fifth_line = '\nor {:.2f} cubic inches if you fill up the machine.'\
    .format(wasted_in)

print(first_line, end ='')
print(second_line, end ='')
print(third_line, end ='')
print(fourth_line, end ='')
print(fifth_line, end ='')