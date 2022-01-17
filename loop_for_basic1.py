# 1-basico
# For Loop 0 to until 151
for i in range(0,151):
    print(i)

# 2-Multiplos de 5
# For Loop 5 to until 1001 increments by 5
for i in range(5,1001,5):
    print(i)

# 3-Contar, a la manera del Dojo
# For Loop 1 to until 101
for i in range(1,101):
    if i%10==0:
        print("Coding Dojo")
    elif i%5==0:
        print("Coding")
    else:
        print(i)

# 4- Whoa. Es un gran idiota
suma = 0
# For Loop 0 to until 500001
for i in range(0,500001):
    if i%2==1:
        suma += i
print(suma)

#5-Cuenta regresiva por 4
# For Loop 2018 to 0, decrement by 4
for i in range(2018,0,-4):
    print(i)

#6-Flexible Counter
lowNum=2 
highNum=9 
mult=3

for i in range(lowNum,highNum+1):
    if i%mult==0:
        print(i)   

