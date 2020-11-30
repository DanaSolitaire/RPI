'''
Dana Solitaire
Section 17
11/24/2018

This class will track individuals moving along the universe and log their 
awards and total points. Most of the needed functions are in this class because 
it's easier to understand.
'''
import math as m

class Person(object):
    #Initalizes person object with attributes
    #(str, float, str, float, float, float, float, str, list, bool)
    def __init__(self, name, radius, home_universe, x, y, dx, dy,\
             current_universe, rewards):
        self.name = name
        self.radius = radius
        self.home_universe = home_universe
        self.x = float(x)
        self.y = float(y)
        self.dx = float(dx)
        self.dy = float(dy)
        self.current_universe = current_universe
        self.points = 0
        # [x, y, points, name, index]
        self.rewards = rewards
        #Stores dx and dy when stopped
        self.dx_stop = dx
        self.dy_stop = dy
        #Bool to check if person has stopped
        self.stop = False
        #Str that can contain name of other person collided with
        self.crashed_with = ''
        
    def __str__(self):
        #This function prints out person info
        print('{} of {} in universe {}'.format(self.name, self.home_universe,\
            self.current_universe))
        print(4 * ' ' +\
              'at ({:.1f},{:.1f}) speed ({:.1f},{:.1f}) with {} rewards and {} points'.\
            format(self.x, self.y, self.dx_stop, self.dy_stop,\
                   len(self.rewards), self.points))
        return ''
    #Simple function adds speed to position
    def move(self):
            self.x += self.dx
            self.y += self.dy

    #This checks if the center if the person is at or pass the borders
    def check_edges(self, step):
        if self.dx == 0 and self.dy == 0:
            return 0
        elif self.x >= 1000 or self.x <= 0 or\
             self.y <= 0 or self.y >= 1000:
            print('{} stopped at simulation step {} at location ({:.1f},{:.1f})\n'\
                  .format(self.name, step + 1, self.x, self.y))
            self.stop = True
            #Storing dx and dy
            self.dx_stop = self.dx
            self.dy_stop = self.dy
            #This ensures that move can be called and this person will not move
            self.dx = 0
            self.dy = 0
            
                  #(object, int)
    #Checks if abs of dx and dy are less than 10, if so it stores the values,
    #sets stop bool to True, and sets dx and dy to zero
    def check_speed(self, step):
        if self.dx == 0 or self.dy ==0:
            return
        elif abs(self.dx) < 10 or abs(self.dy) < 10:
            print('{} stopped at simulation step {} at location ({:.1f},{:.1f})\n'\
                  .format(self.name, step, self.x, self.y))
            self.stop = True
            self.dx_stop = self.dx
            self.dy_stop = self.dy
            self.dx = 0
            self.dy = 0
    
                #(object, int, list of list)
    #This function checks if reward is within person radius
    def near_reward(self, step, rewards):
        for reward in rewards.copy():
            distance = m.sqrt((self.x - reward[0]) ** 2\
                          + (self.y - reward[1]) ** 2)
            if distance <= self.radius:
                print('{} picked up "{}" at simulation step {}'\
                      .format(self.name, reward[3], step))
                #This adds rewards to the list of rewards person has
                self.rewards.append(reward)
                self.points += reward[2]
                #Removes the reward from the overall reward list for that universe
                rewards.remove(reward)
                n = len(self.rewards)
                #Reassigns dx and dy
                self.dx = self.dx - (n % 2) * (n / 6) * self.dx
                self.dy = self.dy - ((n + 1) % 2) * (n / 6) * self.dy
                #Prints output
                print('{} of {} in universe {}'.format(self.name, \
                    self.home_universe, self.current_universe))
                print(4 * ' ' +\
                      'at ({:.1f},{:.1f}) speed ({:.1f},{:.1f}) with {} rewards and {} points\n'.\
                    format(self.x, self.y, self.dx, self.dy,\
                           len(self.rewards), self.points))
                
                   #(self, int, list)
    '''This function takes the step number and portals list from universe'''
    def near_portal(self, step, portals):
        for portal in portals:
            #Calculates the distance
            distance = m.sqrt((self.x - portal[0]) ** 2\
                          + (self.y - portal[1]) ** 2)
            if distance <= self.radius:
                print('{} passed through a portal at simulation step {}'\
                      .format(self.name, portal[3], step))
                self.current_universe = portal[3]
                self.x = portal[3]
                self.y = portal[4]
                #print('{} of {} in universe {})
                
    #This function checks if person is colliding with other people in universe
    def check_crash(self, people_list, rewards, step):
        for second_person in people_list:
            #Calculates distance
            distance = m.sqrt((self.x - second_person.x) ** 2\
                          + (self.y - second_person.y) ** 2)
            #This if statement skips thefunction if person is
            #colliding with itself
            if distance == 0:
                pass
            #This line checks if the person is within range of another person
            #and that it hasn't already crashed with the same person
            elif distance <= self.radius and self.crashed_with != second_person.name:            
                print('{} and {} crashed at simulation step {} in universe {}'\
                      .format(self.name, second_person.name,\
                              step,self.current_universe))
                #Assigns crashed_with to other person's name
                self.crashed_with = second_person.name
                second_person.crashed_with = self.name
                if len(self.rewards) != 0:
                    self_temp = self.rewards[0]
                    print('{} dropped "{}", reward returned to {} at ({},{})'\
                          .format(self.name, self_temp[3], \
                                  self.current_universe, self_temp[0], \
                                  self_temp[1]))
                    rewards.insert(self_temp[4], self_temp)
                    self.rewards.pop(0)
                    self.points -= self_temp[2]
                    n = len(self.rewards) 
                    #Changes the speed only if reward is dropped
                    self.dx = -(self.dx + (n % 2) * (n/6) * self.dx)
                    self.dy = -(self.dy + ((n + 1) % 2) * (n/6)* self.dy)
                    self.move()         
                if len(second_person.rewards) != 0:
                    temp_reward = second_person.rewards[0]
                    print('{} dropped "{}", reward returned to {} at ({},{})'\
                          .format(second_person.name, temp_reward[3], \
                                  second_person.current_universe, \
                                  temp_reward[0], temp_reward[1]))
                    rewards.insert(temp_reward[4],temp_reward)
                    second_person.rewards.pop(0)
                    second_person.points -= temp_reward[2]
                    n = len(second_person.rewards)
                    second_person.dx = -(second_person.dx + \
                                         (n%2)* (n/6)*second_person.dx)
                    second_person.dy = -(second_person.dy + \
                                         ((n+ 1) % 2)* (n/  6)\
                                         * second_person.dy)
                    second_person.move()
                #Printing output
                print('{} of {} in universe {}'.format(self.name, \
                    self.home_universe, self.current_universe))
                print(4 * ' ' +\
                      'at ({:.1f},{:.1f}) speed ({:.1f},{:.1f}) with {} rewards and {} points\n'.\
                    format(self.x, self.y, self.dx, self.dy,\
                           len(self.rewards), self.points))          
                print('{} of {} in universe {}'.format(second_person.name, \
                    second_person.home_universe, \
                    second_person.current_universe))
                print(4 * ' ' +\
                      'at ({:.1f},{:.1f}) speed ({:.1f},{:.1f}) with {} rewards and {} points\n'.\
                    format(second_person.x, second_person.y, second_person.dx, \
                           second_person.dy, len(second_person.rewards), \
                           second_person.points))
    
    #Overriding the less than function to compare persons based on points            
    def __lt__(self, other):
        return self.points < other.points
    
    
    