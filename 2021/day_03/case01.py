# https://adventofcode.com/2021/day/3
from parser import Parser
import numpy as np


class DiagnosticReport:
    _data: list = []
    gamma_rate: str = ""
    epsilon_rate: str = ""

    def add_entry(self, input_text: str) -> None:
        self._data.append([int(input_text[x]) for x in range(0, len(input_text))])

    @property
    def power_consumption(self) -> int:
        self._recalculate_data()

        return int(self.gamma_rate, 2) * int(self.epsilon_rate, 2)

    def _recalculate_data(self) -> None:
        """Recalculate input data"""
        data_sum_list = sum(map(np.array, self._data))
        for data_item in data_sum_list:
            if data_item > len(self._data) / 2:  # More 1 then 0
                self.gamma_rate += "1"
                self.epsilon_rate += "0"
            else:
                self.gamma_rate += "0"
                self.epsilon_rate += "1"


report = DiagnosticReport()
for item in Parser.get_input_data():
    report.add_entry(item)

print(f"Result: {report.power_consumption}")
