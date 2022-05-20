# https://adventofcode.com/2021/day/2


class Parser:
    @staticmethod
    def get_input_data() -> str:
        with open("./../../input_data.txt") as stream:
            for line in stream:
                yield line.removesuffix("\n")