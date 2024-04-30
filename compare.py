x = 1
y= 2
if x<y:
    print("x less than y")
elif x>y:
    print("x greater than y")
else:
    print("x equal to y")

#  or   and   
if x<y or x>y: # x!=y
    print("x or y?")
else:
    print("x equal to y")


def is_even(n):
    # return True if n%2==0 else False
    return n%2==0

name = input("What's your name?")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case _:
        print("Who?")