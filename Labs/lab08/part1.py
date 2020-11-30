fname = 'csa.txt'
info = set()
info2 = set()
clubinfo = ''
lclubinfo = []
dinfo = ''

def get_info(descript):
    descript = descript.replace(',',' ').replace('.',' ').replace('(',' ')\
              .replace(')',' ').replace('"',' ').lower()
    clubinfo = (descript.strip().split(' '))
    for i in range(len(clubinfo)):
        if len(clubinfo[i]) >= 4 and clubinfo[i].isalpha():
            info2.add(clubinfo[i])
    return info2
    
for line in open(fname, encoding="ISO-8859-1"):
    words = line.strip().split('|')
    name = words[1].strip().split(',')
    for i in range(len(name)):
        dinfo += name[i] 
    k = get_info(dinfo)
print(k)
print(len(k))
    
'''for i in range(len(name)):
        clubinfo = name[i].replace(',',' ').replace('.',' ').replace('(',' ')\
              .replace(')',' ').replace('"',' ').lower()
        clubinfo = (clubinfo.strip().split(' '))
        for i in range(len(clubinfo)):
            if len(clubinfo[i]) >= 4 and clubinfo[i].isalpha():
                info.add(clubinfo[i])
    print(dinfo)
    print(info)
'''