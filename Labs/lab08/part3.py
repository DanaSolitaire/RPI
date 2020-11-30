fname = ['wrpi.txt','allclubs.txt']
k = []
def get_info(descript):
    info2 = set()
    clubinfo = ''
    descript = descript.replace(',',' ').replace('.',' ').replace('(',' ')\
              .replace(')',' ').replace('"',' ').lower()
    clubinfo = (descript.strip().split(' '))
    for i in range(len(clubinfo)):
        if len(clubinfo[i]) >= 4 and clubinfo[i].isalpha():
            info2.add(clubinfo[i])
    return info2

r = set() 
club1set = set()
for line in open(fname[0], encoding="ISO-8859-1"):
        words = line.strip().split('|')
        name = words[1].strip().split(',')
        dinfo = ''
        for i in range(len(name)):
            dinfo += name[i]    
        club1set = (get_info(dinfo)) 
        
for line in open(fname[1], encoding="ISO-8859-1"):   
        words1 = line.strip().split('|')
        title = words1[0]
        #print(title)
        name1 = words1[1].strip().split(',')
        #print(name1)
        dinfo1 = ''
        for m in range(len(name1)):
            dinfo1 += name1[m]
        j = (get_info(dinfo1))
        if j.difference(club1set):
            length = len(j.intersection(club1set))
            #print(length)
            k.append((length,title))
            k.sort(reverse = True)
        #k.append(j)    


print('Comparing clubs '+fname[0].rstrip('.txt')+' and '+fname[1].rstrip('.txt')+':\n') 
print(k[0:5])
#print('Same words: ',k[0].intersection(k[1]))
#print('\nUnique to '+fname[0].rstrip('.txt')+': ',club1set.difference(k[4]))
#print('\nUnique to '+fname[1].rstrip('.txt')+': ',k[4].difference(club1set))
#print(k[1])