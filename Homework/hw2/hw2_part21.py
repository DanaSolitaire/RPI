import track as t
import math as m


available_tracks = t.get_number_of_tracks()
'''
das
'''
def calculate_curve(track, speed):
      letter_count = track.count('B') + track.count('E') \
            + track.count('N') + track.count('D')
      distance = letter_count * .25
      if distance == 0:
            return(0, 0)
      else:
            time = (speed / distance) 
            time = pow(time,-2) * time
            time = time * 3600
            return (distance,time)
  
  
def calculate_straight(track, speed):
      letter_count = track.count('S') + track.count('T') + track.count('R')\
            + track.count('A') + track.count('I') + track.count('G')\
            + track.count('H')
      distance = letter_count * .25
      if distance == 0:
            return(0, 0)
      else:
            time = (speed / distance) 
            time = pow(time,-2) * time
            time = time * 3600
            return (distance, time)
      
user_track = input('Select a track between 1 and ' + str(available_tracks) + ' => ')
print(user_track)

curved_speed = input('Speed on curved segments (MPH) => ')
print(curved_speed)

straight_speed = input('Speed on straight segments (MPH) => ')
print(straight_speed)

curved_speed = float(curved_speed)
straight_speed = float(straight_speed)

user_track = t.get_track(int(user_track))
print('Track: \n'+ user_track)
user_track = user_track.upper()
dis_curve, time_curve = calculate_curve(user_track, curved_speed)
dis_straight, time_straight = calculate_straight(user_track, straight_speed)
total_distance = dis_curve + dis_straight
total_time = time_curve + time_straight

if dis_curve == 0:
      avg_speed = (straight_speed)
      if avg_speed >= 120:
            print('is {:.2f} miles long.' \
            ' You raced it in {:.2f} seconds at an average speed of {:.2f}' \
            ' MPH \nWow, what a car!\
            '.format(total_distance, total_time, avg_speed))  
      elif avg_speed >= 60 and avg_speed <= 120:
            print('is {:.2f} miles long.' \
            ' You raced it in {:.2f} seconds at an average speed of {:.2f}' \
            ' MPH \nGetting there.\
            '.format(total_distance, total_time, avg_speed))            
      else:
            print('is {:.2f} miles long.' \
            ' You raced it in {:.2f} seconds at an average speed of {:.2f}' \
            ' MPH \nKind of slow.\
            '.format(total_distance, total_time, avg_speed))            
      
if dis_straight == 0:
      avg_speed = curved_speed
      if avg_speed >= 120:
            print('is {:.2f} miles long.' \
            ' You raced it in {:.2f} seconds at an average speed of {:.2f}' \
            ' MPH \nWow, what a car!\
            '.format(total_distance, total_time, avg_speed))  
      elif avg_speed >= 60 and avg_speed <= 120:
            print('is {:.2f} miles long.' \
            ' You raced it in {:.2f} seconds at an average speed of {:.2f}' \
            ' MPH \nGetting there.\
            '.format(total_distance, total_time, avg_speed))            
      else:
            print('is {:.2f} miles long.' \
            ' You raced it in {:.2f} seconds at an average speed of {:.2f}' \
            ' MPH \nKind of slow.\
            '.format(total_distance, total_time, avg_speed))      
else:      
      avg_speed = ( (curved_speed + straight_speed) / 2)
      if avg_speed >= 120:
            print('is {:.2f} miles long.' \
            ' You raced it in {:.2f} seconds at an average speed of {:.2f}' \
            ' MPH \nWow, what a car!\
            '.format(total_distance, total_time, avg_speed))  
      elif avg_speed >= 60 and avg_speed <= 120:
            print('is {:.2f} miles long.' \
            ' You raced it in {:.2f} seconds at an average speed of {:.2f}' \
            ' MPH \nGetting there.\
            '.format(total_distance, total_time, avg_speed))            
      else:
            print('is {:.2f} miles long.' \
            ' You raced it in {:.2f} seconds at an average speed of {:.2f}' \
            ' MPH \nKind of slow.\
            '.format(total_distance, total_time, avg_speed))