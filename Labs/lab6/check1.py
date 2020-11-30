bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

#print(len(bd))
#print(len(bd[0]))
#print(bd[0][0])
#print(bd[8][8])

def ok_to_add(bd,row, col, number):
    returnbool = True
    if row > 9 or col > 9 or number > 9:
        print('firstline')
        returnbool =  False

    if not (row == 0 and col == 0) :
        row -= 1
        col -= 1
    for j in range(9):
        if bd[row][j] == str(number):
            returnbool = False
        elif bd[j][col] == str(number):
            returnbool = False   
    box = 0
    if (row >= 0 and row <= 2) and (col >= 0 and col <=2):
        box = 1 
    elif (row >= 0 and row <= 2) and (col >= 3 and col <=5):
        box = 2
    elif (row >= 0 and row <= 2) and (col >= 6 and col <=8):
        box = 3
    elif (row >= 3 and row <= 5) and (col >= 0 and col <=2):
        box = 4
    elif (row >= 3 and row <= 5) and (col >= 3 and col <=5):
        box = 5
    elif (row >= 3 and row <= 5) and (col >= 6 and col <=8):
        box = 6
    elif (row >= 6 and row <= 8) and (col >= 0 and col <=2):
        box = 7
    elif (row >= 6 and row <= 8) and (col >= 3 and col <=5):
        box = 8
    elif (row >= 6 and row <= 8) and (col >= 6 and col <=8):
        box = 9    
    l = []
    j = 0
    if box == 1:
        for row in range(0,3):
            for col in range(0,3):
                l.append(bd[row][col])
        for i in range(len(l)):
            if l[i] != '.' and int(l[i]) == number:
                returnbool = False
                
    elif box == 2:           
        for row in range(0,3):
            for col in range(3,6):
                l.append(bd[row][col])
        for i in range(len(l)):
            if l[i] != '.' and int(l[i]) == number:
                returnbool = False

    elif box==3:        
        for row in range(0,3):
            for col in range(6,9):
                l.append(bd[row][col])
        for i in range(len(l)):
            if l[i] != '.' and int(l[i]) == number:
                returnbool = False

    elif box ==4:            
        for row in range(3,6):
            for col in range(0,3):
                l.append(bd[row][col])
        for i in range(len(l)):
            if l[i] != '.' and int(l[i]) == number:
                returnbool = False
    elif box ==5:
        for row in range(3,6):
            for col in range(3,6):
                l.append(bd[row][col])
        for i in range(len(l)):
            if l[i] != '.' and int(l[i]) == number:
                returnbool = False
    elif box ==6:
        for row in range(3,6):
            for col in range(6,9):
                l.append(bd[row][col])
        for i in range(len(l)):
            if l[i] != '.' and int(l[i]) == number:
                returnbool = False     
          
    elif box == 7:                
        for row in range(6,9):
            for col in range(0,3):
                l.append(bd[row][col])
        for i in range(len(l)):
            if l[i] != '.' and int(l[i]) == number:
                returnbool = False
      
    elif box == 8:            
        for row in range(6,9):
            for col in range(3,6):
                l.append(bd[row][col])
        for i in range(len(l)):
            if l[i] != '.' and int(l[i]) == number:
                returnbool = False

    elif box == 9:            
        for row in range(6,9):
            for col in range(6,9):
                l.append(bd[row][col])
        for i in range(len(l)):
            if l[i] != '.' and int(l[i]) == number:
                returnbool = False
                
    return( returnbool)
#ok_to_add(bd,1,8,2)