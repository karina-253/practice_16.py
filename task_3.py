from typing import Optional,Set


def sladkoezhkin_love() -> Optional[Set[str]]:
    """
    Requests the preferences of a Sweet Tooth.

    Returns:
        Optional[Set[str]]: A variety of foods that a sweet tooth likes,
                           None in case of any error
    """

    try:
        prefs_sladk = input('Введите предпочтения Сладкоежкина: ').strip().split()
        return set(prefs_sladk)
    except Exception as e:
        print(f'Ошибка ввода: {e}')
        return None


def friends_count() -> Optional[int]:
    """
    Requests the number of friends of a Sweet Tooth.

    Returns:
        Optional[int]: Number of friends (positive integer),
                      None if the input is incorrect
    """

    try:
        num = int(input('Введите количество друзей Сладкоежкина: ').strip())

        if num <= 0:
            print('Количество должно быть положительным')
            return None
        return num
    except ValueError:
        print('Ошибка. Введите целое число')
        return None

def frineds_love(friends_quantity: int) -> Set[str]:
    """
    Requests the preferences of all friends and returns the combined set.

    Args:
        friends_quantity: Number of friends

    Returns:
        Set[str]: A set of all the products that friends like
                 (empty set if friends don't have preferences)
    """

    all_friends_prefs = set()

    for num in range(1, friends_quantity + 1):
        friend_pref = set(input(f'Предпочтения друга {num}: ').strip().split())
        all_friends_prefs |= friend_pref
    return all_friends_prefs


def main() -> None:
    """
    The main function of the program.
    """
    sladk_goods = sladkoezhkin_love()
    if sladk_goods is None:
        print('Ошибка при вводе предпочтений Сладкоежкина')
        return

    friends_amount = friends_count()
    if friends_amount is None:
        print('Ошибка при вводе количества друзей')
        return

    friends_goods = frineds_love(friends_amount)

    only_sladk = sladk_goods - friends_goods
    print(f'\nКоличество продуктов только для Сладкоежкина: {len(only_sladk)}')


if __name__ == '__main__':
    main()
