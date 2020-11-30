'''
Dana Solitaire
Section 17
11/24/2018

This class creates a Universe object which is the envirnoment where the simulation
will take place.
'''

class Universe(object):
    #Assigning variables
    
    def __init__(self, name, rewards, portals):
        # str
        self.name = name
        # [x, y, points, name]
        self.rewards_list = rewards
        # [from_x, from_y, to_name, to_x, to_y]
        self.portals_list = portals
        
    #This function adds the original index of the end reward
    def index_rewards(self):
        for i in range(len(self.rewards_list)):
            self.rewards_list[i].append(i)
            
    #Prints out universe info 
    def __str__(self):
        '''This function prints out the Universe object'''
        print('Universe: {} ({} rewards and {} portals)'\
              .format(self.name, len(self.rewards_list),\
                      len(self.portals_list)))
        print('Rewards:')
        if len(self.rewards_list) == 0:
            print('None')
        else:
            for reward in self.rewards_list:
                print('at ({},{}) for {} points: {}'.format(reward[0],\
                                        reward[1], reward[2], reward[3]))
        print('Portals:')
        if len(self.portals_list) == 0:
            print('None')
        else:
            for portal in self.portals_list:
                print('{}:({},{}) -> {}:({},{})'.format(self.name, portal[0],\
                                portal[1], portal[2], portal[3], portal[4]))
        return ''
        