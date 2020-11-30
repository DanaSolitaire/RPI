'''
Dana Solitaire
Section 17
9/20/2018

This program takes a word, # of columns, and # of rows and creates a '***' grid.
Part b  has CS1 printed in the middle of the grid and part c adds special characters
to create a pattern'''

'''Taking input from user and assigning it to appropriate variables. Converted string inputs
to ints for number for rows and columns'''

word = input('Word => ')
print(word)
columns = int(input('#columns => '))
print(columns)
rows = int(input('#rows => '))
print(rows)

'''Printing out basic grid'''

print('Your word is: '+ word)
print('\n(a)')
print(rows * (('*** ' * int(columns - 1)) + '***' +'\n'), end='')

'''Printing out grid with CS1 in the middle'''

print('\n(b)')
columns_middle = int((columns/2))
rows_middle = int(rows/2)
print((rows_middle *(('*** ' * int(columns - 1)) + '***'+ '\n')), end='')
print((('*** ' * columns_middle) +'CS1 ' +
       ('*** ' * int(columns_middle - 1)) + '***' + '\n'), end='')
print(rows_middle *(('*** ' * int(columns - 1)) + '***' + '\n'))

'''Printing out grid with CS1 pattern'''

print('(c)')
print((('*** ' * columns_middle) +' ^  ' + ('*** ' * int(columns_middle - 1))
       + '***' + '\n'), end='')

print((('*** ' * (columns_middle - 1)) +' /  ' + '*** '+ ' \  ' +
       ('*** ' * (columns_middle - 2)) + '***' + '\n'), end='')

print((rows_middle -2)*(('*** ' * (columns_middle - 1)) +' |  ' +
                        '*** '+ ' |  ' + ('*** ' * (columns_middle - 2)) + '***' + '\n'), end='')

print((('*** ' * (columns_middle - 1)) +' |  ' + 'CS1 '+ ' |  ' +
       ('*** ' * (columns_middle - 2)) + '***' + '\n'), end='')

print((rows_middle -2)*(('*** ' * (columns_middle - 1))
                        +' |  ' + '*** '+ ' |  ' + ('*** ' * (columns_middle - 2)) + '***' + '\n'), end='')

print((('*** ' * (columns_middle - 1)) +' \  ' + '*** '+ ' /  ' +
       ('*** ' * (columns_middle - 2)) + '***' + '\n'), end='')

print((('*** ' * columns_middle) +' v  ' + ('*** ' * int(columns_middle - 1))
       + '***' + '\n'), end='')
