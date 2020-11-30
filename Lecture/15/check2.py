fname = input('Data file name: ').strip()
print(fname)
prefix = input('Prefix: ')
print(prefix)
name_set = set ()
count = set()
for line in open(fname, encoding="ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip().split(',')
    name = name[0]    
    if name not in name_set : 
        name_set.add(name)
        if name.startswith(prefix):
            count.add(name)
        
    
        
print(len(name_set),'last names')
print(len(count),'start with',prefix)