from typing import Optional, List
from itertools import permutations


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


def get_permutations(nums: List[int]) -> List[tuple]:
    """
    Generates all permutations of the given numbers in lexicographic order.

    Args:
        nums: List of integers to permute

    Returns:
        List[tuple]: A list of tuples, where each tuple represents
        a permutation of the original numbers. Returns empty list if input is empty.
    """

    if not nums:
        return []

    nums_sorted = sorted(nums)
    if len(nums) != len(set(nums)):
        return list(set(permutations(nums_sorted)))
    return list(permutations(nums_sorted))


def main() -> None:
    """The main function of the program."""

    numbers = get_numbers()

    if numbers is None:
        print('Ошибка ввода')
        return

    perms_list = get_permutations(numbers)

    for perm in perms_list:
        print(perm)

if __name__ == "__main__":
    main()
  
