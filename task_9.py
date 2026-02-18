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


def get_number_k(k_max: int) -> Optional[int]:
    """
     A function for entering the number K (subset size).

    Args:
        k_max: Maximum allowed value for K (size of the set)

    Returns:
        Optional[int]: The number K if input is correct, None in case of error
    """

    try:
        k = int(input(f'Введите число K (от 0 до {k_max}): ').strip())

        if k < 0:
            print('Ошибка. Число K должно быть неотрицательным')
            return None

        if k > k_max:
            print(f'Ошибка. K не может быть больше длины списка')
            return None

        return k

    except ValueError:
        print('Ошибка. Введите целое число')
        return None


def get_k_subsets(nums: List[int], k: int) -> List[tuple]:
    """
    Returns all K-element subsets of the given set.

    Args:
        nums: List of integers
        k: Size of subsets

    Returns:
        List[tuple]: List of all K-element subsets
    """

    elements_sorted = sorted(nums)
    return list(combinations(elements_sorted, k))


def main() -> None:
    """
    The main function of the program.
    """

    nums = get_numbers()
    if nums is None:
        return

    k = get_number_k(len(nums))
    if k is None:
        return

    subsets = get_k_subsets(nums, k)

    for subset in subsets:
        if not subset:
            print("пустое множество")
        else:
            print(set(subset))


if __name__ == "__main__":
    main()
