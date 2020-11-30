#Converts celsius to fahrenheit

def convert2fahren(c):
    return float((c * (9/5)+ 32))

temp = (convert2fahren(0))
temp2 = (convert2fahren(32))
temp3 = (convert2fahren(100))

print('0 ->',temp ,'\n32 ->',temp2 ,'\n100 ->',temp3)