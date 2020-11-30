""" 
    This is the skeleton to demonstrate how to put Lab 10 together. 
    It provides an example to show the use of doctest. Note the function,
    addone(x) presented below has an additional 4 lines after 
    the normal function description. The lines beginning with '>>>'
    indicate examples of how the function can be called, and 
    the lines immediately after represent the expected return
    from the call. So, for example, 'addone(1)' should return '2'
    and 'addone(0) should return 1. These lines provide examples
    for a potential user of the lab10 module, but more importantly
    for this lab, they work with the doctest module to allow us to
    do automated testing. 
    
    Look at the file 'test_driver.py' for an example of how to use
    this testing information. Then come back here and change 
    the answer for one or both of the addone examples to 
    an incorrect value and run the testing again to see how a failing
    test is reported.
"""
import random as r
import time as t
def closest1():
    max_num = 0
    x = []
    '''
    closest1(x) returns truple of two closest values in a given list
    using double for loops and doesnt check pairs twice

    >>> closest1([1,3,5,2,7,23])
    (3, 2)
    >>> closest1([34,23,7,2,9,28])
    (7, 9)
    >>> closest1([2,3])
    (2, 3)
    >>> closest1([])
    (None, None)
    '''
    s1 = t.time()
    
    while max_num < 100:
        x.append(r.uniform(0.0, 1000.0))  
        max_num += 1
    k = dict()
    if len(x) < 1:
        return (None, None)
    else:
        for index in x:
            for compare in range(x.index(index), len(x)):
                if index != x[compare]:
                    k[abs(index - x[compare])] = (index, x[compare])
                
        t1 = t.time() - s1
        
        print(k.get(min(k)),'time {} secs'.format(t1))

    
def closest2():
    '''
    closest2(x) returns truple of two closest values in a given list
    using sort and one for loop. The difference is stored using a dict

    >>> closest2([1,3,5,2,7,23])
    (2, 3)
    >>> closest2([34,23,7,2,9,28])
    (7, 9)
    >>> closest2([2,3])
    (2, 3)
    >>> closest2([2,2,2])
    (2, 2)
    ''' 
    max_num = 0
    list_c = []
    s1 = t.time()
    while max_num < 100:
        list_c.append(r.uniform(0.0, 1000.0))  
        max_num += 1
        
    if len(list_c) < 2:
        return (None, None)    
    k = dict()
    fun_list = list_c.copy()
    fun_list.sort()
    low = fun_list[0]
    for i in range(len(fun_list) - 1):
        low = abs(fun_list[i] - fun_list[i+1])
        k[low] = (fun_list[i], fun_list[i+1])
    t1 = t.time() -s1
    print(k.get(min(k)),'time {} secs'.format(t1))

if __name__ == "__main__":
    (closest1())
    (closest2())
    pass
