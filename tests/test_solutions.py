"""Run with: python -m unittest discover -s tests -v."""
import json
import os
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
CASES = json.loads((Path(__file__).with_name('sample_cases.json')).read_text())


def execute(relative_path, data):
    return subprocess.run(
        [sys.executable, str(ROOT / relative_path)], input=data,
        text=True, capture_output=True, timeout=15, cwd=ROOT,
        env={**os.environ, 'OMP_THREAD_LIMIT': '1', 'OPENBLAS_NUM_THREADS': '1'},
    )


class SolutionTests(unittest.TestCase):
    def test_question_coverage(self):
        counts = [11, 10, 10, 10, 10, 12, 12, 12, 12, 12]
        listed = {case['file'] for case in CASES}
        actual = {str(p.relative_to(ROOT)) for p in ROOT.glob('practical_*/*/*.py')}
        self.assertEqual(listed, actual)
        self.assertEqual(len(listed), 219)
        for practical, count in enumerate(counts, 1):
            for section, size in [('implementation', count), ('practice', 10)]:
                prefix = 'ques' if section == 'implementation' else 'practice_ques'
                for question in range(1, size + 1):
                    path = f'practical_{practical:02d}/{section}/practical_{practical:02d}_{prefix}_{question:02d}.py'
                    self.assertIn(path, listed)
        self.assertEqual(len(list((ROOT / 'practical_07/slicing').glob('*.py'))), 8)


def make_case(case):
    def test(self):
        result = execute(case['file'], case['input'])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn('Traceback', result.stderr)
        self.assertTrue(case['expected'], 'Every sample needs a result assertion')
        for expected in case['expected']:
            self.assertIn(expected, result.stdout, result.stdout)
    return test


for case in CASES:
    name = case['file'].replace('/', '_').replace('.py', '')
    setattr(SolutionTests, 'test_' + name, make_case(case))


class BoundaryTests(unittest.TestCase):
    def check(self, path, data, expected, absent=None):
        result = execute(path, data)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(expected, result.stdout)
        if absent is not None:
            self.assertNotIn(absent, result.stdout)

    def test_calculator_types(self):
        path = 'practical_01/implementation/practical_01_ques_09.py'
        for data, expected in [('hello\nworld\n', 'Concatenation: helloworld'),
                               ('1\nword\n', 'Invalid combination'),
                               ('[1]\n[2]\n', 'Invalid combination'),
                               ('True\nFalse\n', 'Invalid combination')]:
            with self.subTest(data=data):
                self.check(path, data, expected)

    def test_division_zero(self):
        self.check('practical_03/implementation/practical_03_ques_07.py', '1\n0\n/\n', 'Cannot divide by zero')

    def test_grade_boundaries(self):
        path = 'practical_03/implementation/practical_03_ques_03.py'
        for marks, expected in [('90', 'Grade: A'), ('75', 'Grade: B'), ('50', 'Grade: C'),
                                ('49', 'Grade: Fail'), ('101', 'Invalid marks')]:
            with self.subTest(marks=marks):
                self.check(path, marks + '\n', expected)

    def test_leap_centuries(self):
        path = 'practical_03/implementation/practical_03_ques_06.py'
        self.check(path, '1900\n', 'Not a leap year')
        self.check(path, '2024\n', 'Leap year')

    def test_triangle_invalid(self):
        self.check('practical_03/implementation/practical_03_ques_09.py', '1 2 3\n', 'Invalid triangle')

    def test_factorial_zero_and_negative(self):
        path = 'practical_04/implementation/practical_04_ques_04.py'
        self.check(path, '0\n', 'While factorial: 1')
        self.check(path, '-1\n', 'undefined')
        self.check('practical_09/implementation/practical_09_ques_07.py', '0\n', 'Recursive: 1')

    def test_zero_digits(self):
        self.check('practical_04/implementation/practical_04_ques_07.py', '0\n', 'Total digits: 1')

    def test_prime_small_values(self):
        path = 'practical_04/implementation/practical_04_ques_08.py'
        for number in [-5, 0, 1, 4, 49]:
            with self.subTest(number=number):
                self.check(path, f'{number}\n', 'Not prime')
        self.check(path, '2\n', 'Prime')

    def test_password_lockout(self):
        self.check('practical_05/implementation/practical_05_ques_08.py', 'x\nx\nx\n', 'Access denied after 3 attempts')
        self.check('practical_05/practice/practical_05_practice_ques_05.py', 'x\n' * 5, 'Locked after 5 failed attempts')

    def test_all_invalid_sensor_readings(self):
        self.check('practical_05/practice/practical_05_practice_ques_06.py', '-1 -2\n', 'No valid readings')

    def test_zero_divisor_search(self):
        self.check('practical_05/implementation/practical_05_ques_05.py', '0\n', 'Divisor cannot be zero')
        self.check('practical_05/implementation/practical_05_ques_05.py', '101\n', 'No divisible number')

    def test_search_missing(self):
        self.check('practical_05/implementation/practical_05_ques_04.py', '1 2 3\n4\n', 'Not found')

    def test_discount_thresholds(self):
        path = 'practical_03/practice/practical_03_practice_ques_03.py'
        self.check(path, '5000\n', 'Final bill: INR 4500.00')
        self.check(path, '2000\n', 'Final bill: INR 2000.00')

    def test_loop_controls_stop_processing(self):
        self.check('practical_05/practice/practical_05_practice_ques_01.py', '90 14 80\n', 'Scan stopped at row 2', 'Scanned row 3')
        self.check('practical_05/practice/practical_05_practice_ques_09.py', '', 'Analyzing day 30', 'Analyzing day 6\n')
        self.check('practical_05/practice/practical_05_practice_ques_02.py', 'S101\n' * 60, 'Unique attendance: 1')

    def test_text_empty_and_ties(self):
        path = 'practical_10/implementation/practical_10_ques_12.py'
        self.check(path, '\n', 'No words found.')
        self.check(path, 'Cat dog\n', "Most frequent word(s): ['cat', 'dog']")
        self.check('practical_10/implementation/practical_10_ques_11.py', '!!!\n', 'Enter at least one letter or digit.')

    def test_function_menu_branches(self):
        path = 'practical_09/implementation/practical_09_ques_11.py'
        self.check(path, '1\n2 3\n', 'Sum: 5.0')
        self.check(path, '2\n1\n', 'Not prime')
        self.check(path, '3\n-2\n', 'Invalid negative integer')
        self.check(path, '4\n', 'Invalid choice')


if __name__ == '__main__':
    unittest.main()
