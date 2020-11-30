'''
Dana Solitaire
Section 17
10/11/18
'''

#This is a program that walks a pikachu around a 150 by 150 image and simulates
#battles

def move_pokemon(row, column, direction, steps):
    #moves pokemon based on direction and steps given
    
    '''This part checks if rows and columns are within boundaries. If it is
    beyond boundaries, the value is assigned to either 0 or 150'''
    if row < 0:
        row = 0
    if row > 150:
        row = 150
    if column < 0:
        column = 0
    if column > 150:
        column = 150
    #N = x-steps, S = x+steps, W = y-steps, E = y+steps
    if direction == 'N':
        row = row - steps
    if direction == 'S':
        row = row + steps
    if direction == 'W':
        column = column - steps
    if direction == 'E':
        column = column + steps
    #checks to make sure vaules aren't above 150 and less than 0
    if row < 0:
        row = 0
    if row > 150:
        row = 150
    if column < 0:
        column = 0
    if column > 150:
        column = 150 
    return (row, column)
        
#Taking in user input for turns, how often, and name
user_turns = input('How many turns? => ')
print(user_turns)
user_turns = int(user_turns)

user_name = input('What is the name of your pikachu? => ')
print(user_name)

user_often = input('How often do we see a Pokemon (turns)? => ')
print(user_often)
user_often = int(user_often)

print('\nStarting simulation, turn 1 '+ user_name+' at (75, 75)')

i = 1
row = 75
col = 75
record = []
while i != user_turns+1:
    #takes in user direction, makes it uppercase so it's easier to compare
    user_direction = input('What direction does '+user_name+' walk? => ')
    print(user_direction)
    user_direction = user_direction.upper()
    row, col = move_pokemon(row, col, user_direction, 5)
    #Checks to see if i = often turns
    if i % user_often == 0:
        #Prints turn line and moves pokemon based on G or W
        print('Turn '+str(i)+', '+user_name+' at ('+str(row)+', '+str(col)+')')
        pokemon_type = input('What type of pokemon do you meet (W)ater, (G)round? => ')
        print(pokemon_type)
        pokemon_type = pokemon_type.upper()
        if pokemon_type == 'W':
            row, col = move_pokemon(row, col, user_direction, 1)            
            print(user_name+' wins and moves to ('+str(row)+', '+str(col)+')')
            record.append('Win')
        elif pokemon_type == 'G':
            row, col = move_pokemon(row, col, user_direction, - 10) 
            print(user_name+' runs away to ('+str(row)+', '+str(col)+')')
            record.append('Lose')
        else:
            record.append('No Pokemon')
    i+=1
    
#prints last line depending on length of user turns
if user_turns == 0:
    print(user_name+' ends up at (75, 75), Record: []')
else:
    record_print = []
    j = 0
    print(user_name+' ends up at ('+str(row)+', '+str(col)+'), Record: '+str(record))