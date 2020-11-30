'''
Dana Solitaire
11/7/20128
Section 17
'''

#if the set from intersection is empty then the word isnt found
def is_found(dictionary, autocorrect):
    if len(dictionary & autocorrect) == 0:
        return False
    else:
        print(dictionary & autocorrect)

#Slices through the word to drop letters and adds it to a set       
def is_drop(dictionary, autocorrect):
    drop_copy = autocorrect.copy()
    for k in range(len(autocorrect)):
        temp_word = drop_copy.pop()
        for i in range(len(temp_word)):
            temp_drop = temp_word[:i] + temp_word[i + 1:]
            drop_str.add(temp_drop)
    print(drop_str & dictionary)
    print(drop_str & autocorrect)

#Slices through the word to sawp letters and adds it to a set
def is_swap(dictionary, autocorrect):
    swap_copy = autocorrect.copy()
    for k in range(len(autocorrect)):
        temp_word = swap_copy.pop()
        for i in range(len(temp_word)):
            temp_swap = temp_word[:i] + \
                temp_word[i:i+2:][::-1] + temp_word[i + 2:]
            swap_str.add(temp_swap)                                                                
    print(swap_str & dictionary)
    print(swap_srt & autocorrect)

'''This function takes in the whole dictionary and the auto correct set.
It loops through the temp_set and assigns each element to a temp value that
is converted into a list. Another loop goes through and replaces a letter with
an alphabet letter and stores that value into a set'''
def is_replace(dictionary, autocorrect):
    letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z' ]
    temp_set = set()
    temp_set = autocorrect.copy()
    for y in range(len(temp_set)):
        autocorrect_word = temp_set.pop()
        temp_word_list = list(autocorrect_word)
        for i in range(len(temp_word_list)):
            for j in range(len(letters)):
                replace_str.add(autocorrect_word[:i] + letters[j].upper()\
                                + autocorrect_word[i+1:])
    print(replace_str.intersection(autocorrect))
    
    print(dictionary.intersection(replace_str))

#Takes in Dictionary and input_file names
dict_file = input('Dictionary file => ')
print(dict_file)
input_file = input('Input file => ')
print(input_file)

replace_str = set()
swap_str = set()
drop_str = set()

#parses words from dictionary file and adds them to a set
dictionary = set()
for line in open(dict_file, encoding='utf8'):
    words = line.strip().split(',')
    dictionary.add(words[0].upper())

    
#parses words from autocorrect input file and adds thems to a set
autocorrect = set()
for line in open(input_file, encoding='utf8'):
    words = line.strip()
    autocorrect.add(words.upper())
    
is_found(dictionary,autocorrect) 
print(is_drop(dictionary, autocorrect))
is_swap(dictionary, autocorrect)
is_replace(dictionary, autocorrect)