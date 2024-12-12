import tests_12_3
import logging

try:
    runner1 = tests_12_3.Runner('Sasha', -5)
    tests_12_3.RunnerTest.test_walk(runner1)
    logging.info('test_walk" выполнен успешно')
except:
    logging.warning('Неверная скорость для Runner')

try:
    runner2 = tests_12_3.Runner('Sasha')
    tests_12_3.RunnerTest.test_run(runner2)
    logging.info('test_run" выполнен успешно')
except:
    logging.warning('Неверный тип данных для объекта Runner')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')