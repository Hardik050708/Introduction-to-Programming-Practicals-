# Introduction to Programming - Practicals 1 to 10

Solutions to the supplied **LAB Manual.pdf**, numbered to match the manual.
Includes **219 standalone Python files**: 111 implementation questions,
100 practice questions, and Practical 7's 8 extra indexing/slicing questions.
All 99 viva questions have short answers in the practical folders.

## Run in Python IDLE

1. Download the repository using GitHub's **Code > Download ZIP** and extract it.
2. Open IDLE for Python 3.10 or newer.
3. Choose **File > Open** and select a `.py` question file.
4. Press **F5** (**Run > Run Module**), then answer prompts in the Shell.

Example: `practical_01/implementation/practical_01_ques_01.py`
is **Practical 1, Question 1**. Each script runs independently and uses short
comments to explain the important steps. Multi-number prompts use spaces.
Example inputs for every script are listed in [SAMPLE_INPUTS.md](SAMPLE_INPUTS.md).

## NumPy installation

Practical 6's NumPy exercises and Practical 7's NumPy slicing exercises need NumPy.
In a terminal opened in this folder, using the same Python installation as IDLE:

```sh
python -m pip install -r requirements.txt
```

On Windows, `py -m pip install -r requirements.txt` works when `py` selects
that same Python installation. All other questions use the standard library.
There is no special IDLE file format: `.py` is the correct Python source format.

## Contents

| Practical | Topic | Implementation | Practice | Extra slicing |
| --- | --- | ---: | ---: | ---: |
| [1](practical_01) | Variables, constants, types | 11 | 10 | 0 |
| [2](practical_02) | Input/output and arithmetic | 10 | 10 | 0 |
| [3](practical_03) | Conditions | 10 | 10 | 0 |
| [4](practical_04) | Loops | 10 | 10 | 0 |
| [5](practical_05) | break, continue, pass | 10 | 10 | 0 |
| [6](practical_06) | Matrices and NumPy | 12 | 10 | 0 |
| [7](practical_07) | Lists, tuples, slicing | 12 | 10 | 8 |
| [8](practical_08) | Dictionaries | 12 | 10 | 0 |
| [9](practical_09) | Functions and recursion | 12 | 10 | 0 |
| [10](practical_10) | Strings | 12 | 10 | 0 |

Each folder has `implementation/`, `practice/`, and `viva_answers.md`.
Practical 7 also has `slicing/` because its question numbering restarts there.
See [QUESTION_INDEX.md](QUESTION_INDEX.md) for a link to every program.

## Assumptions and manual corrections

- Grades use A >= 90, B >= 75, C >= 50, otherwise Fail; subjects are out of 100.
- Practical 2 uses a fixed classroom rate of INR 83 per USD, and salary has no deductions.
- Practical 2 practice Q1 uses INR 150 covering the first 100 units, plus INR 6 per extra unit.
- Practical 3 implementation Q8 treats 1000/2000 as inclusive discount thresholds;
  practice Q3 uses the manual's strict "above 2000/5000" conditions.
- Practical 3 practice Q5 charges each started parking hour, caps one day at INR 100,
  and limits input to 0-24 hours. Q6 uses child 0-12, teen 13-19, adult 20-59, senior 60+.
- Practical 3 practice Q9 uses systolic-only bands <120, 120-129, 130-139, >=140.
- Practical 5 uses demo password `python123` and PIN `123456`; day 1 is Monday for Q9.
- Practical 6 practice Q1 compares days by average across zones and also shows zone extrema.
  Q2 preserves the printed temperatures (which resemble Fahrenheit despite the Celsius label)
  and identifies the patient with the highest peak because no critical threshold is given.
- Practical 6 practice Q6 has only 24 values; it uses the requested 3x8 reshape rather
  than inventing 72 values. Q9/Q10 use seed 42 for repeatable random data.
- Practical 7 practice Q8 says 20 GPS points but prints 10; the solution uses those 10.
- Practical 9 recursion demonstrations limit input sizes to avoid recursion/execution limits.
- Practical 10 palindrome phrases ignore punctuation, spaces and case; the text analyzer
  counts words without punctuation, characters with spaces, and reports all frequency ties.
  Practice Q4 assumes an 8-character password minimum because the manual gives none.
- Demonstration errors are caught so the corrected examples can run; error text can vary by Python version.
- Array indices are 0-based; student/day/room positions are labelled as 1-based where used.

## Validation

Tested with Python 3.12 and NumPy 2.3.5. To run the checks:

```sh
python -m unittest discover -s tests -v
```

The suite executes all 219 programs with sample input and expected-output checks,
checks question coverage, and tests important boundaries and error cases.
