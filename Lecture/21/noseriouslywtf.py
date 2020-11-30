
array = [-1]
front = []
def solution(D, A):
    returnarray = []
    distance = 0
    for i in range(D, len(A) -1):
        if A[i] != 0 and A[i]!= -1:
            print('Here')
            
        if A[i] >= D:
                zero = A[i]
                distance
                returnarray[i] = A[i]
                distance = abs(D - A[i])
        
print(solution(2,[-1,0,1,2,3]))
