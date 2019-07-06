a = int(input('整数A：'))
b = int(input('整数B：'))

max,min = (a,b) if a > b else (b,a)
#min = a if a < b else b

print('max:',max)
print('min',min)
