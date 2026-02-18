from typing import List, Tuple, Set


def solve_equality() -> List[Tuple[int, int]]:
    """
    Deciphering the equality HOD + HOD + HOD = MAT,
    where the letters must correspond to the numbers.

     Returns:
        List[Tuple[int, int]]: A list of tuples (XOD, MAT)
         for all solutions found, sorted in ascending order
     """

    decryptions = []

    for H in range(1, 10):
        for O in range(10):
            if O == H:
                continue
            for D in range(10):
                if D == H or D == O:
                    continue

                HOD = 100 * H + 10 * O + D
                MAT = 3 * HOD

                if MAT > 999:
                    continue

                M = MAT // 100
                A = (MAT // 10) % 10
                T = MAT % 10

                figures = {H, O, D, M, A, T}

                if len(figures) == 6 and M != 0:
                    decryptions.append((HOD, MAT))
    return decryptions


def main() -> None:
    """
    The main function of the program.
    Gets all solutions of the equality HOD + HOD + HOD = MAT,
    sorts them in ascending order and outputs them in the required format.
    """

    decryptions = solve_equality()

    for HOD, MAT in sorted(decryptions):
        print(f"{HOD}+{HOD}+{HOD}={MAT}")

if __name__ == "__main__":
    main()
