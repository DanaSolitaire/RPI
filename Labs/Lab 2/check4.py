first_name = input('Please enter your first name: ')
last_name = input('Please enter your last name: ')

hello_len =  7
last_name_len = len(last_name)+1
last_name = last_name +'!'
first_name_len = len(first_name)


max_len = max(hello_len, last_name_len, first_name_len)

print(str(2 * '*') +str((max_len) * '*') + str(3 * '*'))
print(str(2* '*') , 'Hello, '+str((max_len - (hello_len)) * ' ') + str(2* '*'))
print(str(2* '*') , first_name+str((max_len - (first_name_len)) * ' ')+str(2* '*'))
print(str(2* '*') , last_name +str((max_len - (last_name_len)) * ' ')+ str(2* '*'))
print(str(2 * '*') + str((max_len) * '*')+str(3 * '*'))

