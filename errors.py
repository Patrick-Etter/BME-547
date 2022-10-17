


def function_name(n):
    try:
        from my_calculator import sqrt
    except ModuleNotFoundError:
        print('The my_calculator module is not found. Loading NumPy instead.')
        from numpy import sqrt
    answer = sqrt(n)
    return answer


def main():
    print(function_name(2))


if __name__ == '__main__':
    main()




