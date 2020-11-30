'''
Dana Solitaire
10/14/2018
Section 17
'''
'''
This program finds which angle the lifeguard should run to minimize
the time it takes to reach the swimmer
'''
import lifeguard as l
'''
This function finds the angle that the lifeguard reaches the swimmer in the
shortest amount of time
'''
# beach = (d_1, d_2, h, v_sand, n, theta_1)
#interval = (start_angle, end_angle, num_samples)
def get_optimal(beach,interval): 
    times = []
    angles = []
    angle = interval[0]
    angle_difference = interval[1] - interval[0]
    delta_angle = angle_difference / (interval[2] -1)
    for i in range(interval[2]):
        angles.append(angle)
        beach = beach[0], beach[1], beach[2], beach[3], beach[4], angle
        time_returned = l.get_response_time(beach)
        times.append(time_returned)
        i+=1
        if angle < interval[1]:
            angle += delta_angle
    optimal_time = min(times)
    ang_index = times.index(optimal_time)
    optimal_ang = angles[ang_index]
    actual_time = l.get_response_time(beach)
    difference = actual_time - optimal_time
    return [optimal_time, optimal_ang, difference]

'''
This function takes a list of beaches and a intervals and finds the number of 
rescued, drowned but could have been saved, and could not save swimmers
'''
def get_stats(beaches,intervals):
    rescued = 0
    drowned_could = 0
    drowned = 0
    for i in range(len(beaches)):
        if l.get_response_time(beaches[i]) <= 2 * 60:
            rescued += 1
        elif get_optimal(beaches[i], intervals)[0] <= 2 * 60:
            drowned_could += 1
        else:
            drowned += 1
    stats = (rescued, drowned_could, drowned)
    return stats

'''
    print('Rescued: '+ str(rescued) + '; drowned and could save: ' \
          + str(drowned_could) + '; drowned and could not save: ' \
          + str(drowned))
       
results = [(8, 60, 40, 6, 1.2, 30.47), 
           (8, 10, 50, 5, 2, 19.0987), 
           (18, 40, 20, 3, 1.5, 48.123), 
           (9, 10, 35, 5.5, 1.2, 45), 
           (17, 90, 150, 7, 1.1, 87.5), 
           (8, 12, 52, 6.5, 2.5, 29.0), 
           (8.9, 100, 100, 2.4, 3, 0.0), 
           (80, 52.5, 20, 4.5, 1.14, 78.55)]

thetas = (0.0, 90.0, 1000)
optimal = get_stats(results,thetas)
'''

