# champanze proof
print("Test anti chimpanze")

value: str = input("Veuillez entrer un nombre:")
while not value.isdigit():
    value = input("Veuillez entrer un nombre:")

my_number: int = int(value)
print(f"Vous n'êtes pas un chimpanze : {my_number}")