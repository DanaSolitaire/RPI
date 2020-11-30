fname = ['wrpi.txt','csa.txt']
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

for line in open(fname[0], encoding="ISO-8859-1"):
        words = line.strip().split('|')
        name = words[1].strip().split(',')
        dinfo = ''
        for i in range(len(name)):
            dinfo += name[i]   
        r = set()    
        r = (get_info(dinfo))
        k.append(r)
        
for line in open(fname[1], encoding="ISO-8859-1"):
        words1 = line.strip().split('|')
        name1 = words1[1].strip().split(',')
        dinfo1 = ''
        j = set()
        for m in range(len(name1)):
            dinfo1 += name1[m]
        j = set()
        j = (get_info(dinfo1))
        k.append(j)    
print('Comparing clubs '+fname[0].rstrip('.txt')+' and '+fname[1].rstrip('.txt')+':\n')    
print('Same words: ',k[0].intersection(k[1]))
print('\nUnique to '+fname[0].rstrip('.txt')+': ',k[0].difference(k[1]))
print('\nUnique to '+fname[1].rstrip('.txt')+': ',k[1].difference(k[0]))
'''
for i in range(2):  
    for line in open(fname[i], encoding="ISO-8859-1"):
        words = line.strip().split('|')
        name = words[1].strip().split(',')
    print(name)
r = (get_info(name[0]))
print(r)  
k.append(r)
    #print(k)
#print(file1,'\n\n')
'''
'''        for i in range(len(name)):
            dinfo += name[i] 
        print('doone')       
        r = (get_info(dinfo))
        k.append(r)
    print('doone')

print(k)'''