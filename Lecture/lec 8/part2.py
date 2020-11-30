values = [ 14, 10, 8, 19, 7, 13 ]

nv = input('Enter a value: ')
print(nv)
nv2 = input('Enter another value: ')
print(nv2)

nv, nv2 = int(nv) , int(nv2)
values.append( nv)
values.insert(2, nv2)
print(values[3] , values[-1])

diff = max(values) - min(values)
avg = sum(values) / len(values)
values.sort()
med = (values[3] + values[4]) / 2

print('Difference: {}'.format(diff))
print('Average: {:.1f}'.format(avg))
print('Median: {:.1f}'.format(med))






'''
Enter a value: 15
Enter another value: 23
8 15
Difference: 16
Average: 13.6
Median: 13.5
'''