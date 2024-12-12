import logging
import unittest
import runner_and_tournament

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runner = Runner('Sasha', 5)
            for i in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('test_walk" выполнен успешно')
        except:
            logging.warning('Неверная скорость для Runner')


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner = Runner('Kolya', 5)
            for i in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('Неверный тип данных для объекта Runner')
        except:
            logging.warning('Неверный тип данных для объекта Runner')


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = Runner('Katya')
        runner2 = Runner('Igor')
        for i in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == '__main__':
    unittest.main()


import unittest
from runner_and_tournament import *


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for item in cls.all_results:
            print(item, end = '}\n')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run1(self):
        t1 = Tournament(90, self.runner1, self.runner3)
        results = t1.start()
        TournamentTest.all_results.append(results)
        self.assertTrue(results[2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run2(self):
        t2 = Tournament(90, self.runner2, self.runner3)
        results = t2.start()
        TournamentTest.all_results.append(results)
        self.assertTrue(results[2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run3(self):
        t3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = t3.start()
        TournamentTest.all_results.append(results)
        self.assertTrue(results[3] == 'Ник')


if __name__ == '__main__':
    unittest.main()
