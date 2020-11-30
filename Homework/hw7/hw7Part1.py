'''
Dana Solitaire
11/15/2018
Section 15
'''

#This function checks if word is already in dictionary and prints if it is
def is_found(dictionary, autocorrect_word):
    if autocorrect_word in dictionary:
        spaces = (15  - len(autocorrect_word)) * ' '
        print('{}'.format(autocorrect_word.lower())+ spaces +\
              ' -> {}'.format(autocorrect_word.lower()) + spaces+ ' :FOUND')
        return True

'''This function uses string slicing to insert a letter in the word
and then checks if that word exists in the dictionary. If it does then the word
and frequency gets added to a returned dictionary'''   
def is_insert(dictionary, autocorrect_word):
    insert_dict = dict()
    temp_word = autocorrect_word
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z' ]
    for i in range(len(temp_word)):
            for j in range(26):
                temp_insert = temp_word[:i] + temp_word[i] + letters[j].upper()\
                    + temp_word[i+1:]
                if temp_insert in dictionary:
                    insert_dict[temp_insert.lower()] = dictionary.get(temp_insert)
    return insert_dict

'''Slices through the word to drop letters, if the word is in the dictionary
then the function adds it to a returned dictionary with the frequency as the
value'''     
def is_drop(dictionary, autocorrect_word):
    drop_dict = dict()
    for i in range(len(autocorrect_word)):
        temp_word = autocorrect_word[:i] + autocorrect_word[i + 1:]
        if temp_word in dictionary:
            drop_dict[temp_word.lower()] = dictionary.get(temp_word)
    return drop_dict

'''Slices through the word to replace letters with letters from
user_key_file, if the word is in dictionary then
add word to returned dictionary with value as frequency'''
def is_replace(dictionary, autocorrect_word, keyboard):
    replace_keyboard = keyboard.copy()
    replace_dict = dict()
    temp_word = autocorrect_word
    for i in range(len(temp_word)):
        for vals in replace_keyboard:
            for j in range(len(vals)):
                temp_replace = temp_word[:i] + vals[j].upper() + temp_word[i+1:]
                if temp_replace in dictionary:
                    replace_dict[temp_replace.lower()] =  dictionary.get(temp_replace)
    return(replace_dict)

'''Slices through the word to sawp letters, if the word is in dictionary then
add word to returned dictionary with value as frequency'''
def is_swap(dictionary, autocorrect_word):
    swap_dict = dict()
    temp_word = autocorrect_word
    for i in range(len(autocorrect_word)):
            temp_swap = temp_word[:i] + \
                temp_word[i:i+2:][::-1] + temp_word[i + 2:]
            if temp_swap in dictionary:
                swap_dict[temp_swap.lower()] =  dictionary.get(temp_swap)
    return swap_dict

#Taking in user input
user_dict_file = input('Dictionary file => ')
print(user_dict_file)
user_input_file = input('Input file => ')
print(user_input_file)
user_key_file = input('Keyboard file => ')
print(user_key_file)
dictionary_main = dict()
keyboard_dict = dict()
autocorrect = set()

#Parses dictionary file into dictionary
for line in open(user_dict_file, encoding='utf8'):
    words = line.strip().split(',')
    dictionary_main[words[0].upper()] = words[1]

#Parses keyboard from file into dictionary
for line in open(user_key_file, encoding='utf8'):
    words = line.split(' ')
    letters = words[1:-1]
    letters.append(words[-1].rstrip('\n'))
    keyboard_dict[words[0]] = letters

#parses words from autocorrect input file and adds thems to a set
for line in open(user_input_file, encoding='utf8'):
    words = line.strip().upper()
    match_words = dict()
    top_three_matches = []
    match_words_set = set()
    if not is_found(dictionary_main, words):
        match_words.update(is_drop(dictionary_main, words))
        match_words.update(is_insert(dictionary_main, words))
        match_words.update(is_swap(dictionary_main, words))
        match_words.update(is_replace(dictionary_main, words, keyboard_dict))
        if len(match_words) == 0:
            spaces = (15  - len(words)) * ' '
            print('{}'.format(words.lower())+ spaces +\
              ' -> {}'.format(words.lower()) + spaces+ ' :NO MATCH')
        else:
            for correct_word in match_words:
                match_words_set.add((match_words.get(correct_word), correct_word))
            top_three_matches = list(match_words_set)
            top_three_matches.sort(reverse = True)
            top_three_matches = top_three_matches[:3]
            for i in range (len(top_three_matches)):
                if top_three_matches[i] != top_three_matches[-1]:
                    if top_three_matches[i][0] == top_three_matches[i+1][0]:
                        if top_three_matches[i][1] > top_three_matches[i+1][1]:
                            bigger = top_three_matches[i]
                            smaller = top_three_matches[i+1]
                            top_three_matches[i] = smaller
                            top_three_matches[i+1] = bigger        
            for i in range(len(top_three_matches)):
                    spaces1 = (15  - len(words)) * ' '
                    spaces2 = (15  - len(top_three_matches[i][1]))* ' '
                    print('{}'.format(words.lower())+ spaces1 +\
                          ' -> {}'.format(top_three_matches[i][1]) + spaces2 + ' :MATCH {}'.format(i+1))