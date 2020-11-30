import lab05_util
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

print_info(restaurants[0])
print_info(restaurants[4])
print_info(restaurants[42])
