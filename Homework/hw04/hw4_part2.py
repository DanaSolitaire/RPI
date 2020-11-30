'''
Dana Solitaire
10/14/2018
Section 17
This program allows users to search zip code data and find distance between
two locations
'''
#Importing hw4 util provided file to call read_zip_all function
#Importing math for trig functions
import hw04_util
import math as m
#ZIP
def zip_by_location(zip_codes, location):
    ''' Given zip codes in a list and location strings upper cased for easy
    comparsion, this function finds zip codes given the city and state'''
    i = 0
    zip_code_list = []
    while i in range(len(zip_codes)):
        looped_over_zip = zip_codes[i]
        city = looped_over_zip[3].upper()
        state = looped_over_zip[4].upper()
        if city == location[0] and state == location[1]:
            zip_code_list.append(looped_over_zip[0])
        i += 1
    return zip_code_list 
        
#LOC
def location_by_zip(zip_codes, code):
    '''Given zip codes in a list and a user code, this function returns the
    state, city, and county'''
    i = 0
    while i in range(len(zip_codes)):
        looped_over_zip = zip_codes[i]
        if looped_over_zip[0] == code:
            #(latitude, longtitude, city, state, county)
            return_truple = (looped_over_zip[1], looped_over_zip[2],\
                              looped_over_zip[3], looped_over_zip[4],\
                              looped_over_zip[5])
            print(return_truple)
            return return_truple
        else:
            i += 1
            
#This function takes total zip code list, first zip and second zip as agruments             
def find_dist(zip_codes, zip_code_1, zip_code_2):
    #converts to radians
    first_zip_info = location_by_zip(zip_codes, zip_code_1)
    first_lat = m.radians(first_zip_info[0])
    first_long = m.radians(first_zip_info[1])
    second_zip_info = location_by_zip(zip_codes, zip_code_2)
    second_lat = m.radians(second_zip_info[0])
    second_long = m.radians(second_zip_info[1])
    delta_lat = second_lat - first_lat
    delta_long = second_long - first_long
    #m.sin
    
all_zip_codes = hw04_util.read_zip_all()
#Taking in user command so the program can call the appropriate function
user_command = input('Command (\'loc\', \'zip\', \'dist\', \'end\') => ')
print(user_command)
user_command = user_command.upper()
#while loop runs until user_command is 'end'
while user_command != 'END':
    #Comparing user_command with function calls and calling appropriate functions
    if user_command == 'LOC':
        user_loc = input('Enter a ZIP code to lookup => ')
        print(user_loc)
        returned_info = location_by_zip(all_zip_codes, user_loc)
        lat = returned_info[0]
        lat_degrees = int(lat//1)
        lat_minutes = lat_degrees % 60
        lat_seconds = lat_minutes % 60
        if lat > 0:
            direction_lat = 'S'
        else:
            direction_lat = 'N'
        
        long = returned_info[1]
        long_degrees = long//1
        long_minutes = long_degrees % 60
        long_seconds = long_minutes % 60
        if long > 0:
            direction_long = 'W'
        else:
            direction_long = 'E'
        println1 = 'ZIP code ' + str(user_loc) + ' is in ' + returned_info[2]\
            + ', ' + returned_info[3] + ', ' + returned_info[4] + ','
        println2 = 'coordinates: (0'+ str(int(lat_degrees)) + '\xb0' \
            + str(lat_minutes) + "\'{:.2f}\"" + direction_lat + ',0'\
            + str(int(long_degrees)) + '\xb0' + str(long_minutes)\
            + '\'{:.2f}\"' + direction_long + ")"
        print(println1)
        print(println2.format(lat_seconds, long_seconds))
            
                
    elif user_command == 'ZIP':
        user_city = input('Enter a city name to lookup => ')
        print(user_city)
        user_state = input('Enter the state name to lookup => ')
        print(user_state)
        user_city = user_city.upper()
        user_state = user_state.upper()
        user_location = (user_city, user_state)
        returned_codes = zip_by_location(all_zip_codes, user_location)
        #This part allows zip codes to be printed without '' and []
        print_codes = ''
        i = 0
        for i in range(len(returned_codes)):
            if returned_codes[i] != returned_codes[-1]:
                print_codes += ' ' + str(returned_codes[i]) + ','
            else:
                print_codes += ' ' + str(returned_codes[i])
        print('The following ZIP code(s) found for ' + \
              #This line ensures name of city/state will be printed properly
              user_city.lower().capitalize() + ', '\
              + user_state + ':' + print_codes)
        
    elif user_command == 'DIST':
        user_zip_code1 = input('Enter the first ZIP code => ')
        print(user_zip_code1)
        user_zip_code1 = int(user_zip_code1)
        user_zip_code2 = input('Enter the second ZIP code => ')
        #print(user_zip_code2)
        #user_zip_code2 = int(user_zip_code2)
        #find_dist(user_zip_code1, user_zip_code2)
        
    elif user_command == 'END':
        return_t = True
    else:
        print('Invalid command, ignoring')
    #if return_t == True:
     #   aasd= 0
    #takes in user command at end of block so it can be compared     
    user_command = input('Command (\'loc\', \'zip\', \'dist\', \'end\') => ')
    print(user_command)
    user_command = user_command.upper()
print('\nDone')
