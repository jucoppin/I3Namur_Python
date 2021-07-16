from turtle import turtles


def phone_number(phone_numbers):
    return len({num[:i] for num in phone_numbers for i in range(1, len(num)+1)})
    return len({num[:i] for num in phone_numbers for i in range(1, len(num)+1)})
   # return len({num[:i] for num in phone_numbers for i in range(1, len(num)+1)})


a, b = 0
c = a / b

print(c)

print('hello')
print(phone_number("yoloh"))
def phone_number(phone_numbers):
    return len({num[:i] for num in phone_numbers for i in range(1, len(num)+1)})
