# https://adventofcode.com/2021/day/3
class DiagnosticReport:
    source_data: list = []
    gamma: str = ""
    epsilon: str = ""
    gamma_rate: str = None
    epsilon_rate: str = None
    power_consumption: int = 0

    def add_entry(self, entry: str):
        self.source_data.append([int(entry[x]) for x in range(0, len(entry))])

    def calculate_rates(self) -> int:
        for i in range(0, len(self.source_data[0])):
            bit_0, bit_1 = 0, 0
            for item in self.source_data:
                if item[i] == 0:
                    bit_0 += 1
                else:
                    bit_1 += 1

            if bit_1 > bit_0:
                self.gamma += "1"
                self.epsilon += "0"
            else:
                self.gamma += "0"
                self.epsilon += "1"

        self.gamma_rate = int(self.gamma, 2)
        self.epsilon_rate = int(self.epsilon, 2)
        self.power_consumption = self.gamma_rate * self.epsilon_rate


class Parser:
    def data_generator(self) -> tuple[str, int]:
        with open("input_data.txt") as stream:
            for line in stream:
                yield line.removesuffix("\n")


parser = Parser()
report = DiagnosticReport()
for item in parser.data_generator():
    report.add_entry(item)

report.calculate_rates()

print(f"Result: {report.power_consumption}")
