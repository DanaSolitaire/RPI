'''
Dana Solitaire
11/7/20128
Section 17
'''
#if the set from intersection is empty then the word isnt found
def is_found(dictionary, autocorrect):
    temp = set()
    temp.add(autocorrect)
    if len(dictionary & temp) == 0:
        return False
    else:
        print(dictionary & autocorrect)
        #print(dictionary,'\t->')
        
#Takes in Dictionary and input_file names
'''
dict_file = input('Dictionary file => ')
print(dict_file)
input_file = input('Input file => ')
print(input_file)
'''
#parses words from dictionary file and adds them to a set
dictionary = set()
for line in open('words_test.txt', encoding='utf8'):
    words = line.strip()
    dictionary.add(words.upper())
print(dictionary) 
#parses words from autocorrect input file and adds thems to a set
autocorrect = []
#adds words as a set 
for line in open('input_words.txt', encoding='utf8'):
    words = line.strip()
    autocorrect.append(words.upper())
    
for i in range(len(autocorrect)):
    is_found(dictionary, autocorrect[i])
    

test = set()
test.add('motorway')
'''
    name = words[1].strip().split(',')
    dinfo = ''
    for i in range(len(name)):
        dinfo += name[i]   
    r = set()    
    r = (get_info(dinfo))
    k.append(r)
    
def found(dict_file, input_file):
    
    if 
'''