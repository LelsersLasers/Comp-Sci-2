class Student:
    def __init__(self, name: str, graduation_year: int):
        self.name: str = name
        self.graduation_year: int = graduation_year
        self.major: str = "Undecided"

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    def get_graduation_year(self) -> int:
        return self.graduation_year

    def set_graduation_year(self, graduation_year: int) -> None:
        self.graduation_year = graduation_year

    def get_major(self) -> str:
        return self.major

    def set_major(self, major: str) -> None:
        self.major = major

    def to_string(self) -> str:
        return "Name: %s, Graduation Year: %i, Major: %s" % (
            self.name,
            self.graduation_year,
            self.major,
        )


def main():
    millan = Student("Millan", 2024)
    millan.set_major("Computer Science")

    jerry = Student("Jerry", 2024)
    jerry.set_major("Computer Science")

    print(millan.to_string())
    print(jerry.to_string())


main()
