'''
Dana Solitaire
Section 17
11/7/2018
'''
#Importing textwrap for use in printing the beast set in find_beasts function
import textwrap as t
all_beasts = []

'''Takes in user title as string and all_titles as a list with (str, set)
compares title and prints beasts set of that tile and assumes user_title is titled'''
def find_beasts(user_title, all_titles):
    temp_list = []
    beast_line = ''
    for i in range(len(all_titles)):
        if user_title == all_titles[i][0].title():
            print('\nFound the following title:', all_titles[i][0])
            #printing beasts set using text wrap for clean formating
            find_beasts_set = all_titles[i][1]
            #poping beasts out of copy so master set isn't changed
            #print formating
            temp_list = list(find_beasts_set.copy())
            temp_list.sort()
            temp_list.reverse()
            for k in range(len(temp_list)):
                beast_line += (temp_list.pop()) + ', '
            c = beast_line.rstrip(', ')
            lines = t.wrap(c,40)
            print('Beasts in this title: ',end ='')
            for h in range(len(lines)):
                print(lines[h])
            for j in range(len(all_titles)):
                continue
            return True
        
'''This function uses str.find to compare titles in str title to user given 
title. Returns title if it exists in title list '''       
def find_title(user_title):
    for  i in range(len(str_titles)):
        check_against = (str_titles[i].lower())
        if str(check_against.find(user_title)) != str(-1):
            temp_user_title = check_against
            return (temp_user_title)
        
def common_titles(common_title, all_titles):
    temp_list = []
    temp_title_set = set()
    common_line = ''
    for i in range(len(all_titles)):
        #checks if common_title equals the title at i in all_titles
        if common_title == all_titles[i][0].title():
            common_beasts_set = all_titles[i][1]
            for i in range(len(all_titles)):
                intersection = common_beasts_set.intersection(all_titles[i][1])
                if len(intersection) != len(common_beasts_set) and \
                   len(intersection) != 0:
                    temp_title_set.add(all_titles[i][0])
            if len(temp_title_set) == 0:
                print('\nOther titles containing beasts in common: ')               
            else:
                temp_list = list(temp_title_set.copy())
                temp_list.sort()
                temp_list.reverse()
                for k in range(len(temp_list)):
                    common_line += (temp_list.pop()) + ', '
                c = common_line.rstrip(', ')
                lines = t.wrap(c, 40)                
                print('\nOther titles containing beasts in common: ', end='')
                for h in range(len(lines)):
                    print(lines[h])                

def only_beasts(only_title, all_titles):
    beasts = set()
    only_all_titles = all_titles.copy()
    compared_beast_set = set()
    only_line = ''
    for i in range(len(all_titles)):
        #checks if common_title equals the title at i in all_titles
        if only_title == all_titles[i][0]:
            compared_beast_set = only_all_titles[i][1]
        #only adds a title's beast if the title doesnt equal compared_beast_set
        #title. This statment adds all beasts into one set
        if only_all_titles[i][1] != only_all_titles[-1][1]:
            temp_beast_set = only_all_titles[i][1]
            if len(temp_beast_set) != 0:
                beasts.add(temp_beast_set.pop())
    difference = compared_beast_set.difference(beasts)
    if len(difference) == 0:
        print('\nBeasts appearing only in this title: ')               
    else:
        temp_list = list(difference.copy())
        temp_list.sort()
        temp_list.reverse()
        for k in range(len(temp_list)):
            only_line += (temp_list.pop()) + ', '
            c = only_line.rstrip(', ')
            lines = t.wrap(c, 40)                
        print('\nBeasts appearing only in this title: ', end='')
        for h in range(len(lines)):
            print(lines[h])

allTitles = []
allWords = []
str_titles = []

'''Reads in file and parses the line into (str(title), set(beasts)) 
that is added to a total list of all titles and beasts'''
for line in open('titles.txt', encoding='utf8'):
    words = line.strip().split('|')
    allTitles.append(words[0])
    str_title = (words[0])
    str_titles.append(str_title)
    title = words[0].strip()
    tmpWords = []
    for word in title:
        tmpWords.append(word.lower())
    allWords.append(tmpWords)
    beasts = set()
    for i in range(1,len(words)):
        beasts.add(words[i])
    title_truple = (title,beasts)
    all_beasts.append(title_truple)

#Taking in user given title and lower so I can compare uniformly 
user_title = input('Enter a title (stop to end) => ')
print(user_title)
user_title = user_title.lower()
if user_title is 'stop':
    print('stop')
else:
    while (user_title != 'stop'):
        user_title = find_title(user_title)
        if user_title == ' ' or type(user_title) is not str:
            print('\nThis title is not found!')
        else:
            returned_bool = find_beasts(user_title.title(), all_beasts)
            if returned_bool !=  True:
                print('\nThis title is not found!')
            else:
                common_titles(user_title.title(), all_beasts)
                only_beasts(user_title.title(), all_beasts)
        user_title = input('\nEnter a title (stop to end) => ')
        print(user_title)
        user_title = user_title.lower()
        if user_title is 'stop':
            print('stop')                                                                       