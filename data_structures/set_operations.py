odd = set(range(1,10,2))
prime = set()
for i in range(2,10):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
         prime.add(i)
print("ODD NUMBERS:",odd)
print("PRIME NUMBERS:",prime)
print("DIFFERENCE:",odd.difference(prime))
print("UNION:",odd.union(prime))
print("SYMMETRIC DIFFERENCE:",odd.symmetric_difference(prime))
print("INTERSECTION:",odd.intersection(prime))

        
            
