# https://adventofcode.com/2021/day/1


class Application:
    def calculate(self):
        with open("./../../input_data.txt") as stream:
            num, previous_number, result_count = 0, 0, 0
            for i, line in enumerate(stream):
                num = int(line.removesuffix("\n"))

                if num > previous_number and i > 0:
                    result_count += 1
                previous_number = num

        return result_count


if __name__ == "__main__":
    app = Application()
    print(f"Result: {app.calculate()}")
