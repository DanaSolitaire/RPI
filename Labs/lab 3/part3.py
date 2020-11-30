def pop(bpop, fpop):
    bpop_next = max((10 * bpop) / (1 + 0.1*bpop) - (.05*bpop*fpop),0)
    fpop_next = max((.4 * fpop + .02 * (fpop) * (bpop)), 0)
    return( bpop_next, fpop_next)
    
bpop = int(input('Number of bunnies ==> '))
print(bpop)
fpop = int(input('Number of foxes ==> '))
print(fpop)

print('Year 1:', bpop,fpop)

print('Year 2:',bpop, fpop)
bpop, fpop = pop(bpop,fpop)

print('Year 3:',int(bpop), int(fpop))

bpop, fpop = pop(bpop,fpop)
print('Year 4:',int(bpop), int(fpop))

bpop, fpop = pop(bpop,fpop)
print('Year 5:',int(bpop), int(fpop))


