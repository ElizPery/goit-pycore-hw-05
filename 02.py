from typing import Callable
from re import findall

def generator_numbers(text: str):
    # Function takes string where float numbers are separated by space and return generator of these numbers

    for num in findall(r"\d+\.\d+", text):
        yield float(num)
    
def sum_profit(text: str, func: Callable) -> float:
    # Function takes string where float numbers are separated by space and function that create generator of these numbers
    # and return sum of these numbers as sum_profit_num

    sum_profit_num = 0

    for num in func(text):
        sum_profit_num += num
        
    return sum_profit_num

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")