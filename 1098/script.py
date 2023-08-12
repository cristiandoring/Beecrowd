i = 0
j = 1

for c in range(0,11):
    if c == 0 or c == 5 or c == 10:
        print(f'I={i:.0f}',end=' ')
        print(f'J={j:.0f}')
        print(f'I={i:.0f}',end=' ')
        print(f'J={j+1:.0f}')
        print(f'I={i:.0f}',end=' ')
        print(f'J={j+2:.0f}')
    else:
    
        print(f'I={i:.1f}',end=' ')
        print(f'J={j:.1f}')
        print(f'I={i:.1f}',end=' ')
        print(f'J={j+1:.1f}')
        print(f'I={i:.1f}',end=' ')
        print(f'J={j+2:.1f}')
    i += 0.2
    j += 0.2