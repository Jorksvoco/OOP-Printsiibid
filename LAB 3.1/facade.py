import random

class Generator:
    def generate(self, count):
        return random.sample(range(1, count + 1), count)


class Splitter:
    def split(self, matrix):
        result = []
        size = len(matrix)

        for row in matrix:
            result.append(row)

        for col in range(size):
            result.append([matrix[row][col] for row in range(size)])

        result.append([matrix[i][i] for i in range(size)])
        result.append([matrix[i][size - 1 - i] for i in range(size)])

        return result


class Verifier:
    def verify(self, lists):
        first_sum = sum(lists[0])
        return all(sum(lst) == first_sum for lst in lists)


class MagicSquareGenerator:
    def __init__(self):
        self.generator = Generator()
        self.splitter = Splitter()
        self.verifier = Verifier()

    def generate(self, size):
        while True:
            numbers = self.generator.generate(size * size)
            matrix = [numbers[i * size:(i + 1) * size] for i in range(size)]
            lines = self.splitter.split(matrix)
            if self.verifier.verify(lines):
                return matrix


gen = MagicSquareGenerator()
square = gen.generate(3)

for row in square:
    print(row)