'''
Template program for Lecture 20 exercises.
'''

def linear_search( x, L ):
    for index in range(len(L)-1):
        if L[index] == x :
            return L.index(L[index])
        elif L[index] < x and L[index+1] > x:
            return L.index(L[index+1])
        elif L[0] > x:
            return 0
        elif L[-1] < x:
            return L.index(L[-1])+1
    else:
        return -1
# replace with your code


if __name__ == "__main__":
    #  Get the name of the file containing data
    fname = input('Enter the name of the data file => ')
    print(fname)

    #  Open and read the data values
    in_file = open(fname,'r')
    values = []
    for line in in_file:
        v = float(line)
        values.append(v)

    #  Search for each value requested by the user until -1 is entered
    x = 0
    while x != -1:
        x = float(input("Enter a value to search for ==> "))
        print(x)
        if x != -1:
            loc = linear_search(x, values )
            print(loc)