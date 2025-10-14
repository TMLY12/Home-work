import random

def get_numbers_ticket(min_number: int, max_number: int, quantity: int) -> list:
    if (
        not isinstance(min_number, int)
        or not isinstance(max_number, int)
        or not isinstance(quantity, int)
        or min_number < 1
        or max_number > 1000
        or min_number > max_number
        or quantity < 1
        or quantity > (max_number - min_number +1)
    ):
        return []
    numbers = random.sample(range(min_number, max_number+1), quantity)
    return sorted(numbers)
lottery_numbers = get_numbers_ticket(1,49,6)
print("Ваші лотерейні числа:", lottery_numbers)