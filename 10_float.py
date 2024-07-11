x = 3.3
print(x)
y = 1.1 + 2.2
print(y)

y_str = format(y, ".2g")
print(y_str)
print(type(y_str))
print(y_str == str(x))


print(y, x)

tolerance = 0.00001
print(abs(x-y) < tolerance)