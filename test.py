def celsius_to_fahrenheit(degree: int) -> float:
    """Convert degrees Celius to degrees Fahrenheit."""
    return (degree * 9 / 5) + 32


def fuel_needed(distance: int, mpg: int) -> float:
    return distance / mpg


def total_fuel_cost(distance: int, mpg: int, price_per_gallon: int) -> float:
    return fuel_needed(distance=distance, mpg=mpg) * price_per_gallon


# print(total_fuel_cost(distance=300, mpg=25, price_per_gallon=4))


def fib(n: int) -> int:
    print(f"fib({n})")
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# print(fib(3))


def testage(age: int = 4) -> int:
    age = age + 1
    return age


# print(testage(1))


def countup(n: int) -> None:
    count = 0
    while count <= n:
        print(f"Count is {count}")
        count += 1


def countdown(n: int) -> None:
    count = n
    while count >= 0:
        print(f"Count is {count}")
        count -= 1


def summation(list_1: list[int]):
    i: int = 0
    while i < len(list_1):
        if i != 0:
            list_1[i] = list_1[i] + list_1[i - 1]
        i += 1


# values: list[int] = [1, 2, 3, 4]


def sum2(list2: list[int]) -> list[int]:
    i = 1
    while i < len(list2):
        list2[i] = list2[i] + list2[i - 1]
        i += 1
    return list2


def reverse(word: str) -> str:
    i = 0
    result = ""
    while i < len(word):
        result = word[i] + result
        i += 1
    return result


def countdowntime(seconds: int) -> None:
    print("T minus")
    while seconds > 0:
        print(seconds)
        seconds = seconds - 1
    print(f"countdown{seconds}")


def si(x: int) -> int:
    if x >= 2:
        return 1
    else:
        return 1 + si(x=x + 1)


def si2changetowhile(x: int) -> int:
    count = 0
    while count < 2:
        count += 1
    return count


def gen(stop: int) -> list[int]:
    i = 0
    acc = []
    while i < stop:
        acc.append(i)
        i += 1
    return acc


def triangle(n: int) -> str:
    i = 1
    line = ""
    while i <= n:

        line += "*"
        print(line)
        i += 1

    return line


def sum2d(xs):
    total = 0
    row_i = 0
    while row_i < len(xs):
        col_i = 0
        while col_i < len(xs[row_i]):
            total += xs[row_i][col_i]
            print(total)
            col_i += 1
        print(total)
        row_i += 1
    return total


# values: list[list[int]] = [[1, 2, 3], [3, 4, 5]]


ice_cream: dict[str, int] = {
    "chocolate": "a",
    "vanilla": 8,
    "strawberry": 4,
}


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def dist_from_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def translate_x(self, dx: float) -> None:
        self.x += dx

    def translate_y(self, dy: float) -> None:
        self.y += dy


pt: Point = Point(2.0, 1.0)
