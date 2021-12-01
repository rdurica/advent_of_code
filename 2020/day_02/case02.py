# https://adventofcode.com/2020/day/2


class Application:
    def _collect_data(self) -> None:
        result = []
        with open("input_data.txt") as stream:
            for line in stream:
                data = line.replace("\n", "").replace(":", "").split(" ")
                min, max = data[0].split("-")
                result.append(
                    {
                        "min": int(min),
                        "max": int(max),
                        "letter": data[1],
                        "text": data[2],
                    }
                )

        return result

    def calculate(self):
        counter = 0
        data = self._collect_data()
        for item in data:
            first = True if item["text"][item["min"] - 1] == item["letter"] else False
            second = True if item["text"][item["max"] - 1] == item["letter"] else False

            if (first or second) and first != second:
                counter += 1

        return counter


if __name__ == "__main__":
    app = Application()
    print(f"Result: {app.calculate()}")
