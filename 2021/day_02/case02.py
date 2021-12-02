# https://adventofcode.com/2021/day/2


class Possition:

    depth, horizontal_pos, aim = 0, 0, 0

    def move(self, direction: str, units: int) -> None:
        if direction == "down":
            self._move_down(units)
        if direction == "forward":
            self._move_forward(units)
        if direction == "up":
            self._move_up(units)

    @property
    def actual_coordinates(self) -> int:
        return self.depth * self.horizontal_pos

    def _move_forward(self, units: int) -> None:
        self.horizontal_pos += units
        self.depth += self.aim * units

    def _move_up(self, units: int) -> None:
        self.aim -= units

    def _move_down(self, units: int) -> None:
        self.aim += units


class Parser:
    def data_generator(self) -> tuple[str, int]:
        with open("input_data.txt") as stream:
            for line in stream:
                direction, units = line.split(" ")
                yield direction, int(units)


parser = Parser()
position = Possition()

for direction, units in parser.data_generator():
    position.move(direction, units)

print(f"Result: {position.actual_coordinates}")
