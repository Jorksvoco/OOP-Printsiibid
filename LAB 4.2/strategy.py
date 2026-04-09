import cmath
import unittest


class DiscriminantStrategy:
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        return b*b - 4*a*c


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        d = b*b - 4*a*c
        return float('nan') if d < 0 else d


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        d = self.strategy.calculate_discriminant(a, b, c)
        sqrt_d = cmath.sqrt(d)
        return ((-b + sqrt_d) / (2*a), (-b - sqrt_d) / (2*a))


#testnäide
class TestSolver(unittest.TestCase):
    def test_ordinary_positive(self):
        solver = QuadraticEquationSolver(OrdinaryDiscriminantStrategy())
        r1, r2 = solver.solve(1, 10, 16)
        self.assertAlmostEqual(r1.real, -2)
        self.assertAlmostEqual(r2.real, -8)

    def test_ordinary_negative_discriminant(self):
        solver = QuadraticEquationSolver(OrdinaryDiscriminantStrategy())
        r1, r2 = solver.solve(1, 4, 5)
        self.assertNotEqual(r1.imag, 0)  # kompleksarv

    def test_real_negative_discriminant(self):
        solver = QuadraticEquationSolver(RealDiscriminantStrategy())
        r1, r2 = solver.solve(1, 4, 5)
        self.assertTrue(cmath.isnan(r1))
        self.assertTrue(cmath.isnan(r2))


if __name__ == '__main__':
    unittest.main()