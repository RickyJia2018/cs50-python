


''' lesson 1
# docs.python.org/3/library/stdtypes.html#string-methods

name = input("What's your name?\n")

# Remove whitespace from str
name = name.strip().title()

print("hello my \"friend\"",name)
print(f'Bye my "friend" {name}')



'''





'''lesson 2
x = input("input x ")
y = input("input y ")
print(f"sum of {x} and {y} is {int(x)+int(y)}")

z = 999.4
z = round(z) #round up to int   四舍五入
print(f"{z:,}")  # print out "1,000"

z = 1.66666666
print(f"{z:.3f}") #round to 3 digits
'''


def hello(str="Jodn Doe"): 
    print("hello ",str)

name = input("What is your name?")

#must define fun before calling
hello(name)


# see solution on calculator.py