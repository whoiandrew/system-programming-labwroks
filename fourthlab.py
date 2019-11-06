"""System programming 4th labwork
Task: syntax analyser for given C statement
by Andrii Doroshenko (@whoinadrew), IO-71"""

from thirdlab import KEYWORDS, LOGIC, SEPARATORS, BRACKETS
from termcolor import colored

STATEMENT = "b+=a[--n];"
ARITHMETIC = ["+", "-", "*", "/", "%"]
BRACKETS_DICT = {
    "{": "}",
    "[": "]",
    "(": ")"
}


def is_not_english(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return True
    else:
        return False


def my_analyser(s=STATEMENT.replace(" ", "")):
    inp = STATEMENT

    for i in [*SEPARATORS, *ARITHMETIC, *LOGIC, *BRACKETS]:
        inp = inp.replace(i, " ")

    invalid_vars = [i for i in inp.split() if (i not in KEYWORDS) and not (i.isdigit()) and i[0].isdigit()]
    errors, alphas = list(), [i for i in STATEMENT if i.isalpha()]

    for i in STATEMENT:
        if is_not_english(i):
            errors.append(f"non latin character \"{i}\" in the program")

    if s[-1] != ";":
        errors.append("expected \";\" at the end of the line")
    brackets = [i for i in s if (i in BRACKETS_DICT.keys()) or (i in BRACKETS_DICT.values())]

    for i in range(len(BRACKETS_DICT)):
        if list(BRACKETS_DICT.keys())[i] in brackets and list(BRACKETS_DICT.values())[i] not in brackets:
            errors.append(f"missing \"{list(BRACKETS_DICT.values())[i]}\"")
        elif list(BRACKETS_DICT.values())[i] in brackets and list(BRACKETS_DICT.keys())[i] not in brackets:
            errors.append(f"missing \"{list(BRACKETS_DICT.keys())[i]}\"")

    after_equals_token = s.index("=") + 1
    if s[after_equals_token] in ARITHMETIC and not s[after_equals_token + 1].isalpha():
        errors.append(f"token {s[after_equals_token]} couldn't be before \"=\" token")

    print(f"\nChunk of code:\n{STATEMENT}\n")

    for i in invalid_vars:
        errors.append(f"wrong name, {i} couldn't starts with a digit")
    if len(errors) != 0:
        for i in errors:
            print(colored(f"EXCEPTION: {i}", "red"), end="\n")
    else:
        print(colored("No errors found", "green"))


if __name__ == "__main__":
    my_analyser()
