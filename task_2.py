from typing import Optional,Set


def student_count() -> Optional[int]:
    """
    Requests the number of students from the user.

    Returns:
        Optional[int]: Number of students if the input is correct,
        None in case of any input error
    """

    try:
        num = int(input('Введите количество студентов: ').strip())
        if num <= 0:
            print('Количество должно быть положительным')
            return None
        return num
    except ValueError:
        print('Ошибка. Введите целое число')
        return None


def student_courses(student_num: int) -> Optional[Set[str]]:
    """
    Requests courses for a specific student and returns them as a set.

    Args:
        student_num: Student's number (starting from 1)

    Returns:
        Optional[Set[str]]: Multiple course names selected by the student,
        None in case of any error
    """

    try:
        courses = input(f'Курсы студента {student_num}:').strip().split()
        return set(courses)
    except Exception as e:
        print(f'Ошибка ввода: {e}')
        return None


def common_courses(amount: int) -> Set[str]:
    """
    Finds the courses that ALL students have chosen.\

    Args:
        amount: Number of students

    Returns:
        Set[str]: A set of courses shared by all students.
    """

    common = student_courses(1)
    if common is None:
        return set()

    for i in range(2, amount + 1):
        courses = student_courses(i)
        if courses is None:
            return set()

        common &= courses

        if not common:
            break

    return common

def main() -> None:
    """
    The main function of the program.
    """

    num = student_count()
    if num is None:
        return

    joint = common_courses(num)

    print(f'\nКоличество общих курсов: {len(joint)}')


if __name__ == '__main__':
    main()

