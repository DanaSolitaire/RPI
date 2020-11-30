imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)
movies = dict()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    movie = words[1].strip()
    
    if movie in movies:
        movies[movie].add(name)
    else:
        movies[movie] = set()
        movies[movie].add(name)

unique = dict()

for name in movies:
    length = len(movies[name])
    if length in unique:
        unique[length].append(name)
    else:
        unique[length] = []
        unique[length].append(name)
    
    '''if length is 1:
        unique[length].append(name)
    else:
        unique[length] = []
        unique[length].append(name)
        
        #print(len(movies[name]))
        #print(name, movies[name])
'''        
#print(unique)
max_num = max(unique.keys())
print(max_num)
k = unique.get(max_num)
for i in range(len(k)):
    print(k[i])
print(len(unique.get(1)))

'''    
for index in range(len(movies)):
    
dname = dict()
names = sorted(counts)
limit = (len(names))
highest = 0
ones = 0
for index in range(limit):
    name = names[index]
    dname[counts[name]] = name
    svalues = sorted(dname.keys())
    if counts.get(name) == 1:
        ones += 1    
    #ones += svalues.count(1)    
highest = max(dname.keys())

if counts.get(counts[name]) == 1:
    ones += 1
for index in range(limit):
   
print('{} appears most often: {} times'.format(dname.get(highest), highest))
print('{} people appear once'.format(ones))
'''

