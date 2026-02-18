from typing import Optional, Set


def string_in_set(entry: str) -> Optional[Set[int]]:
    """
    Reads a string from the user and converts it into a set of integers.

    Args:
        entry (str): An input prompt displayed to the user

    Returns:
        Optional[Set[int]]: A set of integers if the input is correct,
        None in case of an error
    """
    try:
        nums = input(entry).strip().split()
        return set(map(int, nums))
    except ValueError:
        print('Ошибка. Введите целые числа через пробел')
        return None
    except Exception as e:
        print(f'Ошибка ввода: {e}')
        return None


def read_number(entry: str) -> Optional[int]:
    """
    Reads a single integer from the user.

    Args:
        entry (str): An input prompt displayed to the user

    Returns:
        Optional[int]: Integer if the input is correct,
        None in case of error (non-numeric value, empty input)
    """
    try:
        return int(input(entry).strip())
    except ValueError:
        print('Ошибка. Введите целое число')
        return None
    except Exception as e:
        print(f'Ошибка ввода: {e}')
        return None


def main() -> None:
    """The main function of a program"""

    set_1 = string_in_set('Введите элементы 1го множества: ')
    if set_1 is None:
        return

    set_2 = string_in_set('Введите элементы 2го множества: ')
    if set_2 is None:
        return

    num = read_number('Введите число для проверки: ')
    if num is None:
        return

    intersection = set_1 & set_2

    if num in intersection:
        print('Принадлежит')
    else:
        print('Не принадлежит')


if __name__ == '__main__':
    main()
  
