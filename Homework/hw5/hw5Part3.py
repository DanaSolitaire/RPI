'''
Dana Solitaire
Section 17
11/1/2018
'''
import random as r
'''This program runs the pokemon simulations a user-specified number of times
and outputs summary statistics'''

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

def run_one_simulation(grid, prob, size):
    #Assigning values
    row = size // 2
    column = size // 2
    random_bool_list = []
    num_bool_list =[]
    falses = 3
    trues = 1
    turn = 0
    #While loop runs simulation until trainer has left grid
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
            outcome = throw_pokeball(falses, trues)
            if outcome == True:
                trues += 1
                grid[row][column] += 1
            else:
                grid[row][column] -= 1
    return turn

#Taking in size, prob, and number of simulations
size = input('Enter the integer grid size => ')
print(size)
size = int(size)
prob = input('Enter a probability (0.0 - 1.0) => ')
print(prob)
prob = float(prob)
num_sim = input('Enter the number of simulations to run => ')
print(num_sim)
num_sim = int(num_sim)

#Setting the seed outside the run_one_simulation function so the
#same seed is used
seed = 11 * size
r.seed(seed)

#Creating a grid 
grid = []
for i in range(size):
    grid.append([0] * size)
grid_count = grid.copy()

#Running the simulation a user given number of times
numbers = []
num_turns = []
for i in range(num_sim):
    num_turns.append(run_one_simulation(grid, prob, size))
print()

#formats the printing and adds values into numbers list for statistics
for i in range(len(grid)):
    for j in range(len(grid)):
        numbers.append(grid[i][j])
        print('{:5d}'.format(grid[i][j]), end = '')
    print()

#Formating print statements
print('Average number of turns in a simulation was {:.2f}'.\
      format(sum(num_turns) / len(num_turns)))
print('Maximum number of turns was {} in simulation {}'.\
      format(max(num_turns), num_turns.index(max(num_turns)) + 1))
print('Minimum number of turns was {} in simulation {}'.\
      format(min(num_turns), num_turns.index(min(num_turns)) + 1))
print('Best net missed pokemon versus caught pokemon is {}'.\
      format(max(numbers)))
print('Worst net missed pokemon versus caught pokemon is {}'.\
      format(min(numbers)))