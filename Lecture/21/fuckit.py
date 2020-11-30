# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

'''
def solution(S, K):
    j = ''
    S = S.split('-')
    for i in range(len(S)):  
        print(str(S[i]))
        j += str(S[i])
    print(j)
    j = list(j)
    if len(j) % 2 == 0:
        print(j[0:len(j):K])
        print(j[K:-2])
    print(j[0:4])
    
    #print(S)
    # write your code in Python 3.6
    pass

solution("2-4A0r7-4k",4)
j = ''
'''
def solution(stores, houses):
    returnlist = []
    index = 0
    for house in houses:
        stores.append(house)
        for i in range(1,len(stores)):
            x = stores[i]
            j = i-1
            while j >= 0 and stores[j] > x:
                stores[j+1] = stores[j]
                j -= 1
            stores[j+1] = x
            index = stores.index(house)
        if stores[index] != stores[-1] and stores[index] != stores[0]:
            if abs(stores[index+1] - stores[index]) < abs(stores[index-1] - stores[index]):
                returnlist.append(stores[index + 1])
            elif abs(stores[index+1] - stores[index]) >= abs(stores[index-1] - stores[index]):
                returnlist.append(stores[index -1])
            else:
                returnlist.append(stores[index])
    return returnlist
print(solution([1,5,20,11,16],[5,10,17]))