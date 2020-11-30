import lab05_util
import webbrowser as w
restaurants = lab05_util.read_yelp('yelp.txt')
def print_info(restaurant):
    name = restaurant[0]
    add = restaurant[3]
    add = add.split('+')
    if len(add) > 2:
        add[0] = add[0] + ' '+add[1]
        add[1] = add[2]
    url = restaurant[4]
    rtype = restaurant[5]
    rtype = str(rtype)
    scores = restaurant[6]
    avg = sum(scores) / len(scores)
    print(name,'('+rtype+')')
    print('\t',add[0],'\n\t',add[1])
    print('Average Score: {:.2f}'.format(avg))
    return scores

def get_info(restaurant):
    lat = restaurant[1]
    long= restaurant[2]
    add = restaurant[3]
    url = restaurant[4]  
    return lat, long, add,url

def part_2(rscores):
    if len(rscores) > 3:
        remove = min(rscores) + max(rscores)
        rscores_avg = (sum(rscores) - remove) / len(rscores)
    else:
        rscores_avg = sum(rscores) / len(rscores)
    if rscores_avg < 2:
        print('This restaurant is rated bad, based on {} reviews.'.format(len(rscores)))
    elif rscores_avg > 2 and rscores_avg < 3:
        print('This restaurant is rated average, based on {} reviews.'.format(len(rscores)))
    elif rscores_avg > 3 and rscores_avg < 4:
        print('This restaurant is rated above average, based on {} reviews.'.format(len(rscores)))
    else:
        print('This restaurant is rated very good, based on {} reviews.'.format(len(rscores)))
    return rscores

id = input('Enter id: ')
print(id)
id = int(id)
id = id-1
if id > len(restaurants):
    print('Error out of range')
else:
    s = print_info(restaurants[id])
    print()
    s = part_2(s)
    
print('What would you like to do next? \n1. Visit the homepage\n2. Show on Google Maps\
\n3. Show directions to this restaurant')
user_choice= input('Your choice(1-3)? ==> ')
print(user_choice)
user_choice = int(user_choice)
lat,long,add,url = get_info(restaurants[id])

if user_choice == 1:
    w.open(url)
elif user_choice == 2:
    w.open('http://google.com/maps/place/'+ add +"'")
elif user_choice == 3:
    w.open('http://google.com/maps/dir/110 8th ST, troy ny/'+ add+ "'")
else:
    print('Unknown value')
    
    
    
    
               
