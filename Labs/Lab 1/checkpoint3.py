base10size = int(input("Disk size in GB => "))
base2size = int( (base10size * (10**9) / 2**30) )
lost_size = int(base10size -base2size)

print(base10size)
print(base10size,"GB in base 10 is actually",base2size,"GB in base 2,",lost_size,"GB less than advertised.")
print("Input: ", base10size * '*');print("Actual:", base2size * '*')
