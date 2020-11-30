'''
Dana Solitaire
Section 17
10/28/2018
'''
import random as r

#This function randomally selects and returns a direction
def move_trainer():
    directions = ['N', 'E', 'S', 'W']
    direction = r.choice(directions)
    value = r.random()
    return (direction, value)
'''
This function should create a list of num_false boolean
False values followed by num_true boolean True values, and then use random.choice() to choose and a value from this boolean list
'''
def throw_pokeball(num_false, num_true):
    num_bool_list = num_false *[False] + num_true*[True]
    return r.choice(num_bool_list)

#Taking input for size and probability
size = input('Enter the integer grid size => ')
print(size)
size = int(size)
prob = input('Enter a probability (0.0 - 1.0) => ')
print(prob)
prob = float(prob)

#Assigning values
row = size // 2
column = size // 2
random_bool_list = []
num_bool_list =[]
seed = 11 * size
r.seed(seed)
falses = 3
trues = 1
turn = 0
number_caught = 0
number_missed = 0
while 0 < row < size -1 and 0 < column < size -1:
    turn += 1
    trainer_truple = move_trainer()
    if trainer_truple[0] == 'N':
        row = row - 1
    if trainer_truple[0] == 'S':
        row = row + 1
    if trainer_truple[0] == 'W':
        column = column - 1
    if trainer_truple[0] == 'E':
        column = column + 1
    if prob >= trainer_truple[1]:
        print('Saw a pokemon at turn {}, location ({}, {})'.\
              format(turn, row, column))
        outcome = throw_pokeball(falses, trues)
        if outcome == True:
            print('Caught it!')
            trues += 1
            number_caught += 1
        else:
            print('Missed ...')
            number_missed += 1
#Formating print statements
print('Trainer left the field at turn {}, location ({}, {}).'\
      .format(turn, row, column))
print('{} pokemon were seen, {} of which were captured.'\
      .format(number_caught+number_missed, number_caught))