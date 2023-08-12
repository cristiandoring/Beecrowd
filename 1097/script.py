i = 1
j = 7
for c in range(0,5):
    
    print(f'I={i}',end=' ')
    print(f'J={j}')
    print(f'I={i}',end=' ')
    print(f'J={j-1}')
    print(f'I={i}',end=' ')
    print(f'J={j-2}')
    i += 2
    j += 2
