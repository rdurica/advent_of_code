# https://adventofcode.com/2020/day/3
from dataclasses import dataclass


@dataclass
class Slop:
    right: int
    down: int


class Application:
    def __init__(self) -> None:
        result = []
        with open("input_data.txt") as stream:
            for i, line in enumerate(stream):
                text = line.removesuffix("\n")
                result.append(text * i)

        self.input_data = result

    def calculate_slop(self, slop: Slop) -> int:
        counter = 0
        down, right = slop.down, slop.right
        for _ in range(len(self.input_data) - 1):
            try:
                if self.input_data[down][right] == "#":
                    counter += 1
                right += slop.right
                down += slop.down
            except IndexError as e:
                break  # At the end

        return counter


if __name__ == "__main__":
    app = Application()

    slops = [
        Slop(1, 1),
        Slop(3, 1),
        Slop(5, 1),
        Slop(7, 1),
        Slop(1, 2),
    ]

    result = 1
    for item in slops:
        result = result * app.calculate_slop(item)

    print(f"Result: {result}")
