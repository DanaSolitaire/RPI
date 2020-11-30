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
    actual_time = l.get_response_time(beach)
    times = []
    angles = []
    angle = interval[0]
    info = []
    angle_difference = interval[1] - interval[0]
    delta_angle = angle_difference / (interval[2] -1)
    for i in range(interval[2]):
        angles.append(angle)
        beach = beach[0], beach[1], beach[2], beach[3], beach[4], angle
        time_returned = l.get_response_time(beach)
        times.append(time_returned)
        #find min time and index find angle with same index
        info.append((angles[i],times[i]))
        
        i+=1
        if angle < interval[1]:
            angle += delta_angle
    optimal_time = min(times)
    
    opt_ang_and_time = info[times.index(optimal_time)]
    difference = actual_time - optimal_time
    return [opt_ang_and_time[1], opt_ang_and_time[0], difference]

'''
This function takes a list of beaches and a intervals and finds the number of 
rescued, drowned but could have been saved, and could not save swimmers
'''
def get_stats(beaches,intervals):
    stat_list_actual = []
    stat_list_optimal = []
    rescued = []
    drowned_could = []
    drowned = []
    for i in range(len(beaches)):
        ang, time, diff = get_optimal(beaches[i], intervals)
        stat_list_optimal.append(time / 60)
        #converts optimal time in seconds to actual time in minutes
        time = (time+diff) / 60
        stat_list_actual.append(time)
    for i in range(len(stat_list_actual)):
        #comparing actual times
        if stat_list_actual[i] < 2:
            rescued.append(i)
        elif stat_list_actual[i] > 2 and stat_list_optimal[i] < 2:
            drowned_could.append(i)
        elif stat_list_optimal[i] > 2:
            drowned.append(i)
    
    print('Rescued: '+ str(len(rescued)) + '; drowned and could save: ' \
          + str(len(drowned_could)) + '; drowned and could not save: ' \
          + str(len(drowned)))
'''        
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

