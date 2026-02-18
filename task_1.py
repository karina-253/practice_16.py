from typing import Optional, List


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

def get_check_number() -> Optional[int]:
    """
     A function for entering a verification number(strictly one).

    Returns:
        Optional[int]: Integer if the input is correct,
        None in case of any input error
    """

    checking_num = input('Введите число для проверки: ').strip().split()

    if not checking_num:
        print('Введена пустая строка')
        return None

    elif len(checking_num) != 1:
        print('Ошибка. Нужно ввести одно число')
        return None

    try:
        return int(checking_num[0])
    except ValueError:
        print('Ошибка. Введите целое число')
        return None

def main() -> None:
    """
    The main function of the program.
    Gets a sequence of numbers and a verification number from the user,
    determines whether the verification number belongs to the set of repeated numbers.

    Returns:
        None
    """
    numbers = get_numbers()
    check_num = get_check_number()

    if numbers is None or check_num is None:
        print('Ошибка ввода')
        return

    duplicates = len(numbers) != len(set(numbers))
    is_repeated = numbers.count(check_num) > 1

    print('YES' if duplicates and is_repeated else 'NO')

if __name__ == '__main__':
    main()
