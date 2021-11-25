# https://adventofcode.com/2020/day/3


class Application:
    def _collect_data(self) -> None:
        result = []
        with open("input_data.txt") as stream:
            for i, line in enumerate(stream):
                text = line.removesuffix("\n")
                result.append(text * i)

        return result

    def calculate(self) -> int:
        counter, col = 0, 3
        data = self._collect_data()

        for i in range(len(data) - 1):
            if data[i + 1][col] == "#":
                counter += 1
            col += 3

        return counter


if __name__ == "__main__":
    app = Application()
    print(f"Result: {app.calculate()}")
