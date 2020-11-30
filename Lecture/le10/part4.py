co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]

user_p =  input('Enter the fraction: ')
print(user_p)
user_p = float(user_p)

i = 0
for i in range(len(co2_levels)):
    co2_levels[i] = co2_levels[i] * (1+ user_p)
    
print('First: {:.2f}'.format(co2_levels[0]))
print('Last: {:.2f}'.format(co2_levels[-1]))
