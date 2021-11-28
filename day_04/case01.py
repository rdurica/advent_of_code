# https://adventofcode.com/2020/day/4
class Application:
    def run(self) -> int:
        valid_results, i = 0, 0
        with open("input_data.txt") as stream:
            data = stream.read()
            for item in data.split("\n\n"):
                row = item.replace("\n", " ")
                occurrences = row.count(":")
                if occurrences == 8:
                    valid_results += 1
                    continue
                if occurrences == 7 and "cid" not in row:
                    valid_results += 1

        return valid_results


if __name__ == "__main__":
    app = Application()
    print(f"Result: {app.run()}")
