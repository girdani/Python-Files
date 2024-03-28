n = int(input())
loops = 3 #Accuracy level 
aprox = 1 #Initial aproximation

for i in range(loops):
    aprox = (aprox + n/aprox)/2

print(aprox)
print(n**0.5)
# Compare the difference!