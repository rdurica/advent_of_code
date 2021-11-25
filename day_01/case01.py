# https://adventofcode.com/2020/day/1


class Application:
    def _collect_data(self) -> None:
        result = []
        with open("input_data.txt") as stream:
            for line in stream:
                result.append(line.replace("\n", ""))

        return result

    def calculate(self):
        data = self._collect_data()
        a, b = 0, 0
        for x in data:
            for y in data:
                if int(x) + int(y) == 2020:
                    a, b = int(x), int(y)

        return a * b


if __name__ == "__main__":
    app = Application()
    print(f"Result: {app.calculate()}")
