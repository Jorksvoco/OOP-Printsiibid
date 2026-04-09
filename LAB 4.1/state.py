import unittest


class CombinationLock:
    def __init__(self, combination):
        self.combination = combination
        self.status = 'LOCKED'
        self.entered = []

    def enter_digit(self, digit):
        self.entered.append(digit)
        length = len(self.entered)

        if self.entered != self.combination[:length]:
            self.status = 'ERROR'
        elif self.entered == self.combination:
            self.status = 'OPEN'
        else:
            self.status = ''.join(str(d) for d in self.entered)


#test
class FirstTestSuite(unittest.TestCase):
    def test_success(self):
        cl = CombinationLock([1, 2, 3, 4, 5])
        self.assertEqual('LOCKED', cl.status)
        cl.enter_digit(1)
        self.assertEqual('1', cl.status)
        cl.enter_digit(2)
        self.assertEqual('12', cl.status)
        cl.enter_digit(3)
        self.assertEqual('123', cl.status)
        cl.enter_digit(4)
        self.assertEqual('1234', cl.status)
        cl.enter_digit(5)
        self.assertEqual('OPEN', cl.status)

    def test_failure(self):
        cl = CombinationLock([1, 2, 3, 4, 5])
        cl.enter_digit(1)
        cl.enter_digit(2)
        cl.enter_digit(9)
        self.assertEqual('ERROR', cl.status)


if __name__ == '__main__':
    unittest.main()