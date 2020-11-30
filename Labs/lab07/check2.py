def parse_line(line):
    line = line.split('/')
    if len(line) > 3:
        line[-1] = int(line[-1].lstrip('\n'))
        line[-3] = int(line[-3])
        line[-2] = int(line[-2])
        line.append(line[0])
        line.remove(line[0])
        print(line)
    else:
        None
def get_line(fname,parno,lineno):
    para = []
    prep = []
    lines = []
    l = []
    wholeline = ''
    for line in open(fname, encoding='utf8'):
        wholeline += line 
    para = wholeline.split('\n\n')
    for i in range(len(para)):
        prep = para[i].split('\n')
        #print(prep)
        l.append(prep)
        #for j in range(len(prep)):
            #print(l[j])
    print(prep[0]  )  
    print()
    print(prep)
''' para = line.sp
        if line != '.\n':
            l =' '
            l = l.join(line)
            prep.append(l)
            print(line)
            print(l)
            
        para.append(l)
        prep = []
        
    print(para[4])
'''    
'''
        if line[0] != '\n':
            line[0] = line[0].rstrip('\n')
            if line[0] == '' and line [1] == '':
                print('no')
                line.append(line)
                l = l.join(line)
        print(l)
        
        para.append(line)
        prep = []
        
    print(para)'''
    
                
    
            
        #print(line)
    #print(para)
get_line('test.txt',1,2)
    
for line in open('1.txt'):
    parse_line(line) 
    list = []
    list.pop