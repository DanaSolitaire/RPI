imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)
counts = dict()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1
    
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
'''
if counts.get(counts[name]) == 1:
    ones += 1
for index in range(limit):
'''    
print('{} appears most often: {} times'.format(dname.get(highest), highest))
print('{} people appear once'.format(ones))


