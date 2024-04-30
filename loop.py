
'''
for i in [0, 1, 2, 3]:
    print(i)

for _ in range(3): #for i in range(3):
    print("Meow")
print("Meow\n" * 3, end="")



i = 0
while i<10:
    print(i)
    i+=1
'''


def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(number):
    for _ in range(number):
        print("Meow")

main()