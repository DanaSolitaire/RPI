import math as m

area = m.pi* pow(5,2)
area2 = round(m.pi *(32**2), 2)

out_string = 'Area 1 = {0:.2f}'.format(area)
#print(out_string)

out_string2 = 'Area 2 = '+str(area2)
print(out_string+'\n'+
      out_string2)