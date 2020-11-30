''' Dana Solitaire 
    Section: 17
    10/9/2018
    
    This program finds the score of a dart game and validates that a user given 
    board is legal
'''
def is_board_valid(board_specs):
    '''This function takes 7 user submitted board configuration specs and
    returns true if the board is valid. The specs are all in inches and floats
    '''
    '''This part checks if all the values are positive and not zero'''
    for specs in range (len(board_specs)):
        if board_specs[specs] != board_specs [-1]:
            if board_specs[specs] <= 0.0 :
                return False
    '''This part checks if different sections overlap each other'''
    if board_specs[2] > board_specs[1] and board_specs[4] > board_specs[2] and\
       board_specs[6] > board_specs[4] and board_specs[0] > board_specs[6]:
        return True
    else:
        return False
    
def get_score(board_config, position):
    '''This function computes the score based on the rules of dart'''
    '''This part checks if dart is within board dimensions'''
    if position[0] < 0.0:
        return 0
    if position[0] == 0:
        return 50
    if position[0] >= board_config[0]:
        return 0
    '''assigning circular wires and return 0 if dart hits it'''
    first_wire = board_config[0] / 2
    second_wire = board_config[2] / 2
    fourth_wire = board_config[4] / 2
    third_wire = fourth_wire - board_config[3]
    sixth_wire = board_config[6] / 2
    fifth_wire = sixth_wire - board_config[5]
    
    if position[0] == first_wire or position[0] == second_wire or\
       position[0] == third_wire or position[0] == fourth_wire or\
       position[0] == fifth_wire or position[0] == sixth_wire:
        return 0
    if fifth_wire > sixth_wire:
        return 0
    
    score = find_section(position)
    '''
    This part finds out whether position is inside triple or double ring
    Uses wires to figure out where the rings are and to check if position 
    is in it
    '''
    if position[0] < fourth_wire and position[0] > third_wire:
        score = score * 3
    elif position[0] < sixth_wire and position[0] > fifth_wire:
        score = score * 2
    else:
        score
        
    return score
    
   
def find_section(position):
    '''Finding which sections the position is using phi % 360 
    if 360 mod equals 90 then we are between sec 1-5
    180 = sec 15 - 20
    270 = sec 10 - 15
    0 = sec 5-10
     each section has 18 degrees inside
    '''
    angle = abs(position[1]) % 369
    if angle == 81 or angle == 171 or angle == 351 or angle == 261:
        return 0
    #Checks angle between 351 to 81 returns section number and 0 if it hits wires
    if angle < 81:
        if angle > 351 and angle < 9:
            return 5
        elif angle > 9 and angle < 27:
            return 4
        elif angle > 27 and angle < 45:
            return 3
        elif angle > 45 and angle < 63:
            return 2
        elif angle > 63 and angle < 81:
            return 1
        else:
            return 0
    #Checks angle between 261 and 351, returns section number
    if angle > 261 and angle < 351:
        if angle > 261 and angle < 279:
            return 10
        elif angle > 279 and angle < 297:
            return 9
        elif angle > 297 and angle < 315:
            return 8
        elif angle > 315 and angle < 333:
            return 7
        elif angle > 333 and angle < 350:
            return 6
        else:
            return 0
    #Checks angle between 180 and 270, returns section number
    if angle > 171 and angle < 261:
        if angle > 171 and angle < 189:
            return 15
        elif angle > 189 and angle < 207:
            return 14
        elif angle > 207 and angle < 225:
            return 13
        elif angle > 225 and angle < 243:
            return 12
        elif angle > 243 and angle < 261:
            return 11
        else: return 0
    #Checks angle between 180 and 90, returns section number
    if angle > 81 and angle < 171:
        if angle > 81 and angle < 99:
            return 20
        elif angle > 99 and angle < 117:
            return 19
        elif angle > 117 and angle < 135:
            return 18
        elif angle > 135 and angle < 153:
            return 17
        elif angle > 153 and angle < 171:
            return 16
        else:
            return 0
'''
Printing user interface and taking in user input. All values are inches 
and floats except for phi which is in degrees and int
'''
print('Please enter dart board parameters below.')
user_diameter = input('Board diameter => ')
print(user_diameter)
user_diameter = float(user_diameter)

user_inner_bulls_d = input('Inner bull\'s eye diameter => ')
print(user_inner_bulls_d)
user_inner_bulls_d = float(user_inner_bulls_d)

user_outer_bulls_d = input('Outer bull\'s eye diameter => ')
print(user_outer_bulls_d)
user_outer_bulls_d = float(user_outer_bulls_d)

user_triple_ring_width = input('Triple ring width => ')
print(user_triple_ring_width)
user_triple_ring_width = float(user_triple_ring_width)

user_triple_ring_dist = input('Distance from the center to the outside edge of \
the triple ring => ')
print(user_triple_ring_dist)
user_triple_ring_dist = float(user_triple_ring_dist)

user_double_ring_width = input('Double ring width => ')
print(user_double_ring_width)
user_double_ring_width = float(user_double_ring_width)

user_double_ring_dist = input('Distance from the center to the outside edge of the double ring => ')
print(user_double_ring_dist)
user_double_ring_dist = float(user_double_ring_dist)

user_r = input('Enter the radial coordinate (r) of the point where the dart landed => ')
print(user_r)
user_r = float(user_r)

user_phi = input('Enter the angular coordinate (phi) of the point where the dart landed => ')
print(user_phi)
user_phi = float(user_phi)

board_specs = (user_diameter, user_inner_bulls_d, user_outer_bulls_d, \
               user_triple_ring_width, user_triple_ring_dist, \
               user_double_ring_width, user_double_ring_dist)

user_position = (user_r, user_phi)

#Printing out score and converting to int if needed
if is_board_valid(board_specs) == False:
    print('Invalid dartboard parameter(s) specified.')
else:
    score = get_score(board_specs, user_position)    
    if score == None:
        print('Invalid dartboard parameter(s) specified')
    else:
        score = str(score)
        print('This throw scored '+ score +'.')