
def parse_line(line):
    line = line.split('/')
    if len(line) > 3:
        line[-1] = int(line[-1].lstrip('\n'))
        line[-3] = int(line[-3])
        line[-2] = int(line[-2])
        line.append(line[0])
        line.remove(line[0])
        line = (line[0],line[1],line[2],line[3])
        print(line)
        
    
for line in open('1.txt'):
    parse_line(line) 
    list = []
    list.pop