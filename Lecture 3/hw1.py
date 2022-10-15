"""
check_data function takes two parameters - path to a file and a list of functions (validators).
You should:
- read data from file data.txt
- validate each line according to rules. Each rule is a function, that performs some specific check
- write a report to txt file and return absolute path to that file. For each line you should report 
it if it doesn't conform with at least one rule, plus add a reason - the name of a validator that
doesn't pass (if there are more than one failed rules, get the name of the first one that fails)

Valid line should have 5 elements in this order:
email, amount, currency, account, date

You should also implement at least two rules:
- validate_line should check if a line has 5 elements
- validate_date should check if a date is valid. In our case valid date will be anything that follows
the pattern DDDD-DD-DD (four digits - two digits - two digits). Date always exists in a line, even 
if this line is corrupted in some other way.
Feel free to add more rules!

For example, input lines:
foo@example.com 729.83 EUR accountName 2021-01:0
bar@example.com 729.83 accountName 2021-01-02
baz@example.com 729.83 USD accountName 2021-01-02

check_data(filepath, [validate_date, validate_line])

output lines:
foo@example.com 729.83 EUR accountName 2021-01:0 validate_date
bar@example.com 729.83 accountName 2021-01-02 validate_line
"""
from tempfile import NamedTemporaryFile
from typing import Callable, Iterable
import re
import os

def validate_line(line: str) -> bool:
    """This function checks if line has 5 elements"""
    return len(line.split()) == 5


def validate_date(line: str) -> bool:
    """This function checks if date is valid"""
    date = line.split()[-1]
    pattern=re.compile('^\d{4}-\d{2}-\d{2}$')
    return pattern.match(date) is not None



def check_data(filepath: str, validators: Iterable[Callable]) -> str:
    """This function read lines from file, checks if line is valid and reports errors"""
    with open(filepath) as data_file, open('report.txt', 'w') as report_file:
        error_lines = []
        for line in data_file:
            for validator in validators:
                if validator(line) == False:
                    error_lines.append(line.strip() + ' ' + validator.__name__ + '\n')
                    break
        error_lines[-1] = error_lines[-1].strip()
        report_file.writelines(error_lines)
        return os.path.abspath('report.txt')
