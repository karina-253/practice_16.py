from typing import Optional, Set


def given_number() -> Optional[int]:
    """
     A function for entering a verification number(strictly one).

    Returns:
        Optional[int]: Integer if the input is correct,
        None in case of any input error
    """

    number = input('Введите натуральное число: ').strip().split()

    if not number:
        print('Введена пустая строка')
        return None

    elif len(number) != 1:
        print('Ошибка. Нужно ввести одно число')
        return None

    try:
        num = int(number[0])
        if num <= 0:
            print('Ошибка. Число должно быть положительным')
            return None
        return num
    except ValueError:
        print('Ошибка. Введите целое число')
        return None


def eratosphen_algorithm(num: int) -> Set[int]:
    """
    Finds all the primes less than a given number using the sieve of Eratosthenes.

    Args:
        num (int): Upper bound of the search

    Returns:
        Set[int]: The set of primes less than num
    """

    if num <= 2:
        return set()

    numbers = set(range(2, num))

    for i in range(2, int(num ** 0.5) + 1):
        numbers -= set(range(i * i, num, i))
    return numbers


def main():
    num = given_number()

    if num is None:
        print('Программа завершена из-за ошибки ввода')
        return

    numbers = eratosphen_algorithm(num)
    if not numbers:
        print(f'Простых чисел меньше {num} нет')
    else:
        primes_list = sorted(numbers)
        print(primes_list)


if __name__ == '__main__':
    main()
  
