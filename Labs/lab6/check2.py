import check1 as c
import lab06_util as l

fuser = input('File name: ')
print(fuser)
bd = l.read_sudoku(fuser)
lreturn = []
for i in range(9):  
    if i % 3 == 0:
        print('-' * 25)
    for j in range(9):
        if j % 3 == 0:
            print('| ', end ='')
        print(bd[i][j] + ' ', end = '') 
    print('|')
print('-' * 25) 
def vertify_board(bd):
    for k in range(9):
        for l in range(9):
            check_number = bd[k][l]
            if check_number == '.':
                return False
            else:
                lreturn.append(c.ok_to_add(bd,k,l,int(check_number)))
    for i in range (len(lreturn)):
        if lreturn[i] == 'True':
            return False
if vertify_board(bd) == False:
    print('invalid board')
    urow = input('Enter row: ')
    print(urow)
    urow = int(urow)
    ucol = input('Enter col: ')
    print(ucol)
    ucol = int(ucol)
    unumber = input('Enter val: ')
    print(unumber)
    unumber = int(unumber)
    ans = c.ok_to_add(bd, urow, ucol, unumber)
    if ans == True:
        print(ans)
        bd[urow][ucol] = str(unumber)
