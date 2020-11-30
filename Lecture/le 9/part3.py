user_list = []
user_input = input('Enter a value (0 to end): ')
print(user_input)
user_input = int(user_input)
user_list.append(user_input)
while user_input !=0:
    user_input = input('Enter a value (0 to end): ')
    print(user_input)
    user_input = int(user_input)
    user_list.append(user_input)

 
if user_list[0] == 0:
    print('Min:',0)
    print('Max:',0)
    print('Avg:',0)
else:
    user_list.pop()
    print('Min:',min(user_list))
    print('Max:',max(user_list))
    print('Avg: {:.1f}'.format(sum(user_list) / len(user_list)))
    
    