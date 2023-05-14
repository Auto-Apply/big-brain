import random


def create_random_val(min_val: float, max_val: float):
    mean = (min_val + max_val) / 2
    std_dev = (max_val - min_val) / 6
    amount = abs(random.gauss(mean, std_dev))
    amount = min(max_val, max(min_val, amount))
    return amount
