# https://adventofcode.com/2020/day/4
from dataclasses import dataclass
from typing import Optional


@dataclass
class Passport:
    """All needs to be optional because not all data are correct"""

    byr: Optional[int] = None
    iyr: Optional[int] = None
    eyr: Optional[int] = None
    hgt: Optional[str] = None
    hcl: Optional[str] = None
    ecl: Optional[str] = None
    pid: Optional[str] = None
    cid: Optional[int] = None

    def __post_init__(self) -> None:
        self.byr = int(self.byr) if self.byr else None
        self.iyr = int(self.iyr) if self.iyr else None
        self.eyr = int(self.eyr) if self.eyr else None
        self.cid = int(self.cid) if self.cid else None

    @property
    def is_valid(self) -> bool:
        if not self.byr or (self.byr < 1920 and self.byr > 2002):
            return False

        if not self.iyr or (self.iyr < 2010 and self.iyr > 2020):
            return False

        if not self.iyr or (self.iyr < 2020 and self.iyr > 2030):
            return False

        return True


class Application:
    def __init__(self) -> int:
        input_data = []
        with open("input_data.txt") as stream:
            data = stream.read()
            for item in data.split("\n\n"):
                row = item.replace("\n", " ")
                passport_items = row.split(" ")
                passports_key_value = [x.split(":") for x in passport_items]

                input_data.append(Passport(**dict(passports_key_value)))

        self.input_data = input_data

    def calculate_result(self) -> None:
        pass


if __name__ == "__main__":
    app = Application()

    print(f"Result: {app.run()}")
