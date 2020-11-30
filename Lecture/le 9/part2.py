census = [ 340, 589, 959, 1372, 1918, 2428, 3097, 3880, 4382, 5082, \
            5997, 7268, 9113, 10385, 12588, 13479, 14830, 16782, \
            8236, 17558, 17990, 18976, 19378 ]
avg = []
real_avg = []
i = 0
while i < len(census):
    if census[i] != census [-1]:
        avg.append(float(((census[i+1] - census[i]) / census[i]) * 100))
    i+=1

j = 0
while j < len(avg):
    if avg[j] != avg[-1]:
        real_avg.append(float((avg[j+1] + avg[j]) / 2) )
    j+=2
    
print('Average = {:.1f}%'.format((sum(real_avg)/ len(real_avg))))
    

    