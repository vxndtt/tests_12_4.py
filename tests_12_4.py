import tests_12_3
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')

    runner1 = tests_12_3.Runner('Sasha', -5)
    print(tests_12_3.RunnerTest.test_walk(runner1))

    runner2 = tests_12_3.Runner(5)
    print(tests_12_3.RunnerTest.test_run(runner2))
