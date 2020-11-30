l = []
line = ''
line2 = ''
line3 = ''
for u in range(9):
    for i in range(9):
        print((str(u)+','+str(i)) + ' ', end = '')
        if (i+1) % 3 == 0:
            print(' ', end='')
    if (u+1) % 3 == 0:
            print(' ')
    print()
    
for u in range(9):
    for i in range(9):
        if 2 == u:
            print((str(2)+','+str(i)) + ' ', end = '')
print()
for u in range(9):
    for i in range(9):
        if 5 == i:
            print(str(u)+','+str(5) +' ', end = '')
print('\n$')           
for u in range(3,6):
    for i in range(3,6):
        print((str(i)+','+str(u)) + ' ', end = '')
        if (i+1) % 3 == 0:
            print(' ', end='')
    if (u+1) % 3 == 0:
            print(' ')
    print()


'''
    #line += add+' '
    for j in range(9):
        add2= str(j)
        line2 += add2 + ' '   
    l.append(line2)
    line2 = '' 
    
prep = line+ ',' +line2
print(prep)
line = '' 
line2 = ''
'''
