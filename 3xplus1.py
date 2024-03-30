n = int(input()) # 27 is a good one

length = 1
max_number = 1

while n != 1:
    if n % 2 == 0: # Divide by two
        n = int(n/2)
    else: # Multiply by 3 sum 1
        n = n*3 + 1
    length += 1
    if n > max_number:
        max_number = n
    print(n)

print(f'It took {length} numbers to get to 1! Max: {max_number}')