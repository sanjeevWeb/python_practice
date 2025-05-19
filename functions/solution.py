# 3. Polymorphism in Functions
def multiply (p1,p2):
    return p1 * p2


print(multiply(2,3))
print(multiply(2,'3'))
print(multiply('a',3))

# default value function

def greet(name="User"):
    return 'Hello'+ " " + name


print(greet("Anil"))
print(greet())

# lambda function

cube = lambda x: x ** 3

print(cube(3))

print("i got the biometrics today")