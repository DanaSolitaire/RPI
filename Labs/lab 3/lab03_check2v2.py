def find_skew(name, time1, time2, time3, time4, time5):
    avg = (time1 + time2 + time3 + time4 + time5)/5
    var = (time1 - avg)**2 + (time2 - avg)**2 + (time3 - avg)**2 + (time4 - avg)**2 + (time5 - avg)**2
    var /= 5
    skew = (time1 - avg)**3 + (time2 - avg)**3 + (time3 - avg)**3 + (time4 - avg)**3 + (time5 - avg)**3
    skew /= 5
    skew = skew / var**3**0.5
    return ("{0}'s running times have a skew of {1:.2f}".format(name,skew))

def part_two(name, time1, time2, time3, time4, time5):
    min_time = min(time1, time2, time3, time4, time5)
    max_time = max(time1, time2, time3, time4, time5)
    avg = (time1 + time2 + time3 + time4 + time5) - (max_time + min_time)
    avg = avg / 3
    print(name+'\'s stats-- min: '+ str(int(min_time)) + ',', 'max:', 
          str(int(max_time)) + ', avg: {:.1f}'.format(avg))
    
    

part_two('Stan', 34, 34, 35, 31, 29)
(part_two('Kyle', 30, 31, 29, 29, 28))
(part_two('Cartman', 36, 31, 32, 33, 33))   
(part_two('Bebe', 27, 29, 29, 28, 30)) 
(part_two('Kenny', 33, 32, 34, 31, 35))


'''
print(find_skew('Stan', 34, 34, 35, 31, 29)) 
print(find_skew('Kyle', 30, 31, 29, 29, 28))
print(find_skew('Cartman', 36, 31, 32, 33, 33))  
print(find_skew('Bebe', 27, 29, 29, 28, 30)) 
print(find_skew('Kenny', 33, 32, 34, 31, 35))
'''


'''    
name_1 = "Stan"
## The following are Stan's 5 latest running times for 3 miles

time1_1 = 34
time2_1 = 34
time3_1 = 35
time4_1 = 31
time5_1 = 29

name_2 = "Kyle"
## The following are Kyle's 5 latest running times for 3 miles
print(find_skew('Kyle', 30, 31, 29, 29, 28))  
time1_2 = 30
time2_2 = 31
time3_2 = 29
time4_2 = 29
time5_2 = 28

print(find_skew('Cartman', 36, 31, 32, 33, 33))  
name_3 = "Cartman"
## The following are Cartman's 5 latest running times for 3 miles
time1_3 = 36
time2_3 = 31
time3_3 = 32
time4_3 = 33
time5_3 = 33

print(find_skew('Kenny', 33, 32, 34, 31, 35))  
name_4 = "Kenny"
## The following are Kenny's 5 latest running times for 3 miles
time1_4 = 33
time2_4 = 32
time3_4 = 34
time4_4 = 31
time5_4 = 35
 
name_5 = "Bebe"
## The following are Bebe's 5 latest running times for 3 miles
time1_5 = 27
time2_5 = 29
time3_5 = 29
time4_5 = 28
time5_5 = 30

# Process results for the first person
avg = (time1_1+time2_1+time3_1+time4_1+time5_1)/5
var = (time1_1-avg)**2 + (time2_1-avg)**2 + (time3_1-avg)**2 + (time4_1-avg)**2 + (time5_1-avg)**2
var /= 5
skew = (time1_1-avg)**3 + (time2_1-avg)**3 + (time3_1-avg)**3 + (time4_1-avg)**3 + (time5_1-avg)**3
skew /= 5
skew = skew/var**3**0.5
print ("{0}'s running times have a skew of {1:.2f}".format(name_1,skew))


## Process for the second person
avg = (time1_2+time2_2+time3_2+time4_2+time5_2)/5
var = (time1_2-avg)**2 + (time2_2-avg)**2 + (time3_2-avg)**2 + (time4_2-avg)**2 + (time5_2-avg)**2
var /= 5
skew = (time1_2-avg)**3 + (time2_2-avg)**3 + (time3_2-avg)**3 + (time4_2-avg)**3 + (time5_2-avg)**3
skew /= 5
skew = skew/var**3**0.5
print ("{0}'s running times have a skew of {1:.2f}".format(name_2,skew))

## Process for the third person
avg = (time1_3+time2_3+time3_3+time4_3+time5_3)/5
var = (time1_3-avg)**2 + (time2_3-avg)**2 + (time3_3-avg)**2 + (time4_3-avg)**2 + (time5_3-avg)**2
var /= 5
skew = (time1_3-avg)**3 + (time2_3-avg)**3 + (time3_3-avg)**3 + (time4_3-avg)**3 + (time5_3-avg)**3
skew /= 5
skew = skew/var**3**0.5
print ("{0}'s running times have a skew of {1:.2f}".format(name_3,skew))


## Process for the fourth person
avg = (time1_4+time2_4+time3_4+time4_4+time5_4)/5
var = (time1_4-avg)**2 + (time2_4-avg)**2 + (time3_4-avg)**2 + (time4_4-avg)**2 + (time5_4-avg)**2
var /= 5
skew = (time1_4-avg)**3 + (time2_4-avg)**3 + (time3_4-avg)**3 + (time4_4-avg)**3 + (time5_4-avg)**3
skew /= 5
skew = skew/var**3**0.5
print ("{0}'s running times have a skew of {1:.2f}".format(name_4,skew))


## Process for the fifth person
avg = (time1_5+time2_5+time3_5+time4_5+time5_5)/5
var = (time1_5-avg)**2 + (time2_5-avg)**2 + (time3_5-avg)**2 + (time4_5-avg)**2 + (time5_5-avg)**2
var /= 5
skew = (time1_5-avg)**3 + (time2_5-avg)**3 + (time3_5-avg)**3 + (time4_5-avg)**3 + (time5_5-avg)**3
skew /= 5
skew = skew/var**3**0.5
print ("{0}'s running times have a skew of {1:.2f}".format(name_5,skew))
'''