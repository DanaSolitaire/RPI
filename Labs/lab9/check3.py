from Date import Date as d
import statistics as s
temp = []
for line in open('birthdays.txt', encoding='utf8'):
    temp_line = line.strip('\n').split(' ')
    temp_date = d(temp_line[0], temp_line[1], temp_line[2])
    temp.append(temp_date)
    
temp1 = [] 
temp2 = dict()
lowestbd = temp[0]
highestbd = temp[0]
mostmonth = temp[0].month
for i in range(len(temp)):
    if temp[i] < lowestbd:
        lowestbd = temp[i]
    if temp[i] > highestbd:
        highestbd = temp[i]
    temp1.append(temp[i].month)
    
    
print(lowestbd)
print(highestbd)
#print(temp1)
month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July',\
                    'August','September', 'October', 'November', 'December' ]

print(month_names[int(s.mode(temp1))-1])