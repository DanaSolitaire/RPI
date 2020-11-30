'''
Dana Solitaire
Section 17
11/24/2018

This program runs the simulation
'''
from Universe import *
from Person import *
import json

#This function prints out in given universes and persons info from file
def info_print(universe_list, people_list):
    print('All universes')
    print('-' * 40)
    for uni in universe_list:
        print(uni)
    print('All individuals')
    print('-'* 40)
    for person in people_list:
        print(person, end='')

#This function prints info of the person with the most points        
def end_print(people_list, step, stop):
    t = 0
    print()
    print('-' * 40 + '\nSimulation stopped at step {}'.format(step))
    print('{} individuals still moving'.format(stop))
    print('Winners:')
    #This section accounts for stimulations where all persons have no points
    for person in people_list:
        t+= person.points
    if t == 0:
        for person in people_list:
            print(person, end = '')
            print('Rewards:\n')
    else:
        print(people_list[0], end = '')
        print('Rewards:')
        for reward in people_list[0].rewards:
            print(' ' * 4 + reward[3])
        print()
        
#Returns a list of sorted persons based on points
def ranking(people):
    ranked= []
    ranked = sorted(people, reverse = True)
    return ranked

#Clears str for crashed_with. This ensures that all persons can have crashes
#with persons
def clear_crash(people_list):
    for person in people_list:
        person.crashed_with = ''

if __name__ == "__main__":
    user_file = input('Input file => ')
    print(user_file)
    #Assigning needed variables 
    stopped_people = 0
    universes = []
    rewards = []
    portals = []
    individuals_list = []
    data = json.loads(open(user_file).read())
    #data is a dict, each item contains universe and individuals info
    for key in data:
        temp_person_list = []
        universe_name = ''
        universe_name = key.get('universe_name')
        rewards = key.get('rewards')
        portals = key.get('portals')

        #Creating a Universe object and appending it to a list 
        current_uni = Universe(universe_name, rewards, portals)
        current_uni.index_rewards()
        universes.append(current_uni)
        
        #this loop creates a Person object and appends it to a list
        temp_person_list = key.get('individuals')
        for person in temp_person_list:
            new_person = Person(person[0], person[1],\
                         universe_name, person[2],\
                         person[3], person[4],\
                         person[5], universe_name, [])
            individuals_list.append(new_person)
    
    #Printing out universe and individual info from given file    
    info_print(universes, individuals_list)
    print('\nStart simulation\n' + 40 * '-')
    stop = set()
    step = 0
    for person in individuals_list:
        person.near_reward(step, rewards)
        person.check_edges(step)
        if person.stop == True:
            stop.add(person)
    #Main loop runs 100 times or
    #until the len of stopped == total person list length
    while step < 100 and (len(stop) != len(individuals_list)):
        for person in individuals_list:
            '''This layout ensures the order of the output matches the expected output
            TA's have tried to change or reduce the amount of functions call,
            but it breaks the code'''
            person.near_reward(step, rewards)
            person.check_speed(step)
            person.check_edges(step)
            person.check_crash(individuals_list, rewards, step)
            person.check_speed(step)
            person.move()
            person.check_speed(step)
            person.check_edges(step)
            person.check_crash(individuals_list, rewards, step)
            person.check_speed(step)
            #Adds person to list of stopped people
            if person.stop == True:
                stop.add(person)
        #clears all persons crashed_with str
        clear_crash(individuals_list)
        step += 1
    rank = ranking(individuals_list)
    end_print(rank, step, len(individuals_list) - len(stop))