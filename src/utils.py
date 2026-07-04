def hello() -> str:
    """Функция возвращает строку hello"""
    return 'hello'


def summ(a: int | float, b: int | float) -> int | float:
    """Функция суммы двух чисел"""
    return a + b


if __name__ == "__main__":
    print(hello())
    print(summ(1, 2))
