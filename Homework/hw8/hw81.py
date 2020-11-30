

'''
def near_reward(person):
    x = person.get('x')
    y = person.get('y')
    for reward in rewards:
        distance = m.sqrt((x - reward.x) ** 2 + (person.y - reward.y))
    dx = person.get('dx')
    dy = person.get('dy')
    n = person.get('rewards')
    n = n[0]
    person['dx'] = dx - (n % 2)* (n / 6) * dx
    person['dy'] = dy - ((n + 1) % 2)* (n / 6)* dy
    return person
'''
#Printing info read from user
def info_print(universe_list, people_list):
    print('All universes')
    print('-' * 40)
    for uni in universe_list:
        print(uni)
    print('All individuals')
    print('-'* 40)
    for person in people_list:
        print(person, end='')
        
def new_portal(person):
    pass
def collision_check(person, people_list):
    pass

def move(person):
    #if person.get('dx') person.get('dy') < 10:  
    pass
 

if __name__ == "__main__":
    user_file = input('Input file => ')
    print(user_file)
    #Assigning needed variables 
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
    print(info_print(universes, individuals_list))
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
    
    person.move()
    person.check_edges(step)
    person.near_reward(step, rewards)
    person.check_speed(step)
    person.check_crash(individuals_list, rewards, step)
    person.check_speed(step)    
    
 
    for person in individuals_list:
        person.check_edges(0)
        person.check_speed(0)
        if person.stop == True:
            stop.add(person)    