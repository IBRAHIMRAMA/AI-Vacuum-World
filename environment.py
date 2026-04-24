import random

class VacuumEnvironment:
    def __init__(self, size):
        self.size = size
        self.grid = self.create_grid()

    def create_grid(self):
        return [
            [random.choice(["Dirty", "Clean"]) for _ in range(self.size)]
            for _ in range(self.size)
        ]

    def display(self):
        for row in self.grid:
            print(row)