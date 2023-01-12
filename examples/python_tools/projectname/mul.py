from .add import add


def mul(a: int, b: int) -> int:
    return a * b


def mul_add(a: int, b: int) -> int:
    return a * add(a, b)


def main():
    print(mul(10, 20))


if __name__ == "__main__":
    main()
