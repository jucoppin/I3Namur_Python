def phone_number(phone_numbers):
    return len({num[:i] for num in phone_numbers for i in range(1, len(num)+1)})