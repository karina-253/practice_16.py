from typing import Optional, List
from itertools import combinations


def get_numbers() -> Optional[List[int]]:
    """
    A function for entering a sequence of numbers.

    Returns:
           Optional[List[int]]: A list of integers if the input is correct,
           None in case of an error
    """
    nums = input('Введите последовательность чисел: ').split()

    if not nums:
        print('Введена пустая строка')
        return None

    try:
        return [int(num) for num in nums]
    except ValueError:
        print('Ошибка! Введите целые числа')
        return None


def print_subsets(nums: List[int]) -> None:
    """
    Prints all subsets of the given set of numbers.

    Args:
        nums: List of integers to generate and print subsets from

    Prints:
        All subsets of the input set, each on a new line.
        Empty set is printed as "пустое множество".
    """

    if not nums:
        print("пустое множество")
        return

    for i in range(len(nums) + 1):
        for combo in combinations(nums, i):
            print(set(combo) if combo else "пустое множество")


def main():
    """
    The main function of the program.
    Gets numbers from user and displays all possible subsets.
    """

    numbers = get_numbers()

    if numbers is None:
        print('Ошибка ввода')
        return

    print_subsets(numbers)

if __name__ == "__main__":
    main()
  
