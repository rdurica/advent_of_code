# https://adventofcode.com/2021/day/1


class Application:
    data = []

    def __init__(self) -> None:
        with open("input_data.txt") as stream:
            for line in stream:
                num = int(line.removesuffix("\n"))
                self.data.append(num)

    def calculate(self):
        result_count = 0
        for i, _ in enumerate(self.data):
            try:
                a, b, c, d = [self.data[i + x] for x in range(1, 5)]
            except IndexError:
                break

            if (b + c + d) > (a + b + c):
                result_count += 1

        return result_count


if __name__ == "__main__":
    app = Application()
    print(f"Result: {app.calculate()}")
