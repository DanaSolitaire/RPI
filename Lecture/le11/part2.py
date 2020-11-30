dale_hd = input('Enter Dale\'s height: ')
print(dale_hd)
dale_hd = int(dale_hd)
erin_he = input('Enter Erin\'s height: ')
print(erin_he)
erin_he = int(erin_he)
sam_hs = input('Enter Sam\'s height: ')
print(sam_hs)
sam_hs = int(sam_hs)

list1 = [dale_hd, erin_he, sam_hs]
list1.sort()
list1.reverse()
list2 = []
i = 0
for i in range(3):
    if list1[i] == dale_hd:
        list2.append('Dale')
    elif list1[i] == erin_he:
        list2.append('Erin')
    else:
        list2.append('Sam')
        
for j in range(3):
    print(list2[j])
