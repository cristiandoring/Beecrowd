X = int(input(''))
Y = int(input(''))

soma = 0

X = abs(X)
Y = abs(Y)

if X > Y:
    for i in range(Y,X):
            if i % 2 == 1:
                soma += i
elif X < Y:
    for i in range(X,Y):
           if i % 2 == 1:
               soma += i
     
print(soma)