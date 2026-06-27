#variables
x=100
y=x

print("Before:")
print("x =", x)
print("y =",y)

y=200

print("\nAftre:")
print("x =",x)
print("y =", y)

# Mutable example
number=[1, 2, 3]

copy = number

copy.append(4)

print("\nList:")
print(number)
print(copy)