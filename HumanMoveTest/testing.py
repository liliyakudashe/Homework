import unittest
from main import Student


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.runner = Student("Форест Гамп")
        self.walker = Student("Бари Ален")

    def test_walk_distance(self):
        for _ in range(10):
            self.walker.walk()
        self.assertEqual(self.walker.distance, 500, f"Дистанции не равны {self.walker.distance} != 500")

    def test_run_distance(self):
        for _ in range(10):
            self.runner.run()
        self.assertEqual(self.runner.distance, 1000, f"Дистанции не равны {self.runner.distance} != 1000")

    def test_competition(self):
        for _ in range(10):
            self.runner.run()
            self.walker.walk()
        self.assertGreater(self.runner.distance, self.walker.distance,
                           f"{self.runner.name}должен преодолеть дистанцию больше, чем {self.walker.name}")


if __name__ == "__main__":
    unittest.main()
