co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]
i = 0
l2 = []

for i in co2_levels:
    avg = sum(co2_levels) / len(co2_levels)
    if i > avg:
        l2.append(i)

print('Average: {:.2f}\nNum above average:'.format(avg), len(l2))