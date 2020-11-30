'''
Dana Solitaire 10/28/18
Section 17
'''
import random as r


def move_trainer():
    directions = ['N', 'E', 'S', 'W']
    direction = r.choice(directions)
    value = r.random()
    print('Selected ' + direction + ', value {:.2f}'.format(value))
'''
This function should create a list of num_false boolean
False values followed by num_true boolean True values, and then use random.choice() to choose and a value from this boolean list
'''
def throw_pokeball(num_false, num_true):
    if(len(num_bool_list) != num_false + num_true):
        for i in range(num_false):
            num_bool_list.append(False)
        for i in range(num_true):
            num_bool_list.append(True)
        for i in range(num_false + num_true):   
            random_bool_list.append(r.choice(num_bool_list))
    for i in range(5):
        print('Booleans:', num_bool_list)
        if len(random_bool_list) == 1:
            print('Selected',random_bool_list[0])
        else:
            print('Selected',random_bool_list[i])
    
random_bool_list = []    
num_bool_list =[]
size = input('Enter the integer grid size => ')
print(size)
size = int(size)
F = input('Enter the integer number of Falses => ')
print(F)
F = int(F)
T = input('Enter the integer number of Trues => ')
print(T)
T = int(T)
seed = 11*size
r.seed(seed)
print('Setting seed to',seed)
for i in range(5):
    print('Directions: [\'N\', \'E\', \'S\', \'W\']')
    move_trainer()
throw_pokeball(F, T)

