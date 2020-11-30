'''
Dana Solitaire
Section 17
9/20/2018

This program parses constitution text from constitution.py and formats it into
readable text. This program also outputs the index of the start and end of
article 1. The program outputs the number of times an inputed word appears in
the text.
'''

#Imported constitution file so I can read in the text
import constitution as const

'''
This section reads in Constitution using get_all_text and uses the replace
string funstion to format the text. This section also counts total lines in the
text.
'''

total_const = const.get_all_text()
total_const_len = len(total_const)
total_const = total_const.replace('#', '\n\n')

#you cant replace ^ on this version, but on submitty there are ^ so different line count
total_const_lines = total_const.count('\n')
total_const = total_const.replace('^', '\n')

# Article III doesn't have a period so I added one to the overall count to make up for that
article_count = total_const.count('Article.') + 1
section_count = total_const.count('Section.')
avg_length = round(total_const_len/total_const_lines)
total_const = total_const.replace('@', ' ')
index_start = total_const.find('Section')

# added 5 to end index position because delay has 5 letters
index_end = total_const.find('delay')
index_end = index_end + 5

#All print statements placed together for easy reading
print('*' * int(avg_length - 1))
print(total_const)
print('*' * int(avg_length - 1), '\n')
print('There are', article_count, 'articles and', section_count, 'sections in the United States Constitution \n')
print('Text of Article I starts at position', index_start, '(character \'S\') with the word \"Section.\"')
print('Text of Article I ends at position', index_end, '(character \'.\') with the word \"delay.\"\n')

'''
This section takes in a word from user and finds how many times it is found in the Constitution.
'''
count_word = input('Enter the word to count in the Constitution => ')
total_const = total_const.upper()
print(count_word)
count_word = count_word.upper()
print('Word', str('"'+count_word+ '"'), 'appears', total_const.count(count_word)
, 'times (without regard to case) in the text of the United States Constitution')
