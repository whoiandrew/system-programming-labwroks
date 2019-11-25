"""System programming 5th labwork
Task: syntax and lexis analyser for given Pascal chunk of code with pointer on the error
by Andrii Doroshenko (@whoinadrew), IO-71"""

from termcolor import colored

STATEMENT = "if (a>b) then begin a:=b; end;"

RESERVED_STATEMENT = "if (a>b) then begin a:=b; end;"
SEPARATORS = [";", ", ", ".", ":", "?"]
SEPARATORS_NO_SEMI = [", ", ".", "?"]
BRACKETS = ["(", ")", "{", "}", "[", "]"]
LOGIC = [":=", "==", "!=", ">", "<", ">=", "<=", "&&", "||", "!", "&", "|", "="]

KEYWORDS = ["and", "array", "begin", "case", "const", "div", "do", "downto", "else", "end", "file", "for", "function",
            "goto", "if", "in", "label", "mod", "nil", "not", "of", "or", "packed", "procedure", "program", "record",
            "repeat", "set", "then", "to", "type", "until", "var", "while", "with"]

TREE = ["_prgm", "_block", "_compound_statement",
        "_if_node", "_if_without_else", "_if_with_else",
        "_for_node", "_statement", "_statement_body",
        "_assignment", "_bool_expression", "_bool_factor",
        "_expression", "_term", "_signed_factor",
        "_unsigned"]

ARITHMETIC = ["+", "-", "*", "/", "%"]
BRACKETS_DICT = {
    "{": "}",
    "[": "]",
    "(": ")"
}

my_tree = [TREE[0], TREE[1]]


def find_nth(s, x, n=0, overlap=False):
    l = 1 if overlap else len(x)
    i = -l
    for c in range(n + 1):
        i = s.find(x, i + l)
        if i < 0:
            break
    return i


def tree_builder(t=TREE, mt=my_tree, s=STATEMENT):
    if ("if" in s) and ("else" not in s):
        mt.extend((t[3], t[4]))
    if ("if" in s) and ("else" in s):
        mt.extend((t[3], t[5]))
    if ":=" in s:
        mt.append(t[9])


words = []

tree_builder()


def lexis_analyser(s=STATEMENT):
    global words
    errors = []
    for i in [*SEPARATORS, *ARITHMETIC, *LOGIC, *BRACKETS]:
        s = s.replace(i, " ")
        words = s.split()
    s = [i for i in s.split() if i not in KEYWORDS]
    for i in s:
        if not i[0].isalpha():
            errors.append(f"{i} - incorrect name for value, index({STATEMENT.index(i)})")
    if errors:
        return errors


def syntax_analyser(s=STATEMENT):
    global words
    errors = []
    opening_brackets = [i for i in s if (i in BRACKETS_DICT.keys())]
    closing_brackets = [i for i in s if i in BRACKETS_DICT.values()]

    # checks parentheses
    flag = 0
    cut_opening_s = []
    for i in range(len(opening_brackets)):
        cut_opening_s.append(s[s.index(opening_brackets[i]):])

    for i in range(len(cut_opening_s)):
        if (BRACKETS_DICT[cut_opening_s[i][0]]) not in cut_opening_s[i]:
            errors.append(f"{cut_opening_s[i][0]} is undefined symbol, index ({len(s) - len(cut_opening_s[i]) + 1})")
            flag = 1

    cut_closing_s = []
    for i in range(len(closing_brackets)):
        cut_closing_s.append(s[: s.index(closing_brackets[i]) + 1])

    for i in range(len(closing_brackets)):
        for k, w in BRACKETS_DICT.items():
            if k not in cut_closing_s[i] and w is closing_brackets[i][-1]:
                errors.append(f"{w} is undefined symbol, index({len(cut_closing_s[i]) + 1})")
                flag = 1

    errors = list(set(errors))

    # begin-end checker
    if (" begin " in s) and (("end" not in s[s.index(" begin "):]) or ("end" not in words)) and ("end." not in s) and (
            "end" not in words):
        errors.append(
            f"expected \"end\" after \"begin\" in begin-end block, index({RESERVED_STATEMENT.index('end')})")
    if ("end" in s) and (" begin " not in s[:s.index("end")]) and ("begin" not in words):
        errors.append(
            f"expected \"begin\" before \"end\" in begin-end block, index({RESERVED_STATEMENT.index('begin')})")

    # if-then checker
    if ("if " in s) and (" then " not in s[s.index("if "):]) and ("then" not in words):
        errors.append(f"expected \"then\" after \"if\" in if-then block, index({RESERVED_STATEMENT.index('then')})")
    if (" then " in s) and ("if " not in s[:s.index(" then ")]) and ("if" not in words):
        errors.append(f"expected \"if\" before \"then\" in if-then block, index({RESERVED_STATEMENT.index('if')})")

    # semicolons which needed
    semicolon_indexes = []
    nosp_indexes = []
    no_sp_s = s.replace(" ", "")
    for i in range(s.count(";")):
        semicolon_indexes.append(find_nth(s, ";", i))
        nosp_indexes.append(find_nth(no_sp_s, ";", i))
    try:
        if no_sp_s[-1] != ";":
            errors.append(f"missing semicolon after end in index({len(s.rstrip())})")
        else:
            nosp_indexes[-1] = ""
    except IndexError:
        pass

    if "end" == words[-1] and (no_sp_s.index("end") - 1 not in nosp_indexes):
        errors.append(f"missing semicolon after assignment in index({s.index(words[-1]) - 1})")

    for i in range(len(nosp_indexes)):
        if "end" == words[-1] and (no_sp_s.index("end") - 1 == nosp_indexes[i]):
            nosp_indexes[i] = ""

    # extra symbols checker
    for i in range(len(semicolon_indexes)):
        if nosp_indexes[i] != "":
            errors.append(f"unsigned ;, index({semicolon_indexes[i]})")

    # logic_if
    if flag != 1:
        parentheses_body = s[s.index("(") + 1: s.index(")")]
        if parentheses_body and [i for i in parentheses_body if i != " "]:
            if parentheses_body.strip()[0] in LOGIC:
                errors.append(f"missing argument before logic, index({s.index('(') + 1})")
            if parentheses_body.strip()[-1] in LOGIC:
                errors.append(f"missing argument before logic, index({s.index(')')})")
            if parentheses_body.strip()[0].isalpha() and parentheses_body.strip()[-1].isalpha() and " " in (
                    parentheses_body[
                    parentheses_body.index(parentheses_body.strip()[0]): parentheses_body.index(
                        parentheses_body.strip()[-1])]) and not [i for i in LOGIC if i in parentheses_body]:
                errors.append(f"wrong expression in 'if()', index({s.index('(') + 2})")
        else:
            errors.append(f"condition is empty index({s.index('(') + 1})")

    for i in range(len(s)):
        if s[i] in SEPARATORS_NO_SEMI and s[s.index("end") + 3] != s[i]:
            errors.append(f"undefined {s[i]} in index({s.index(s[i])})")

    if errors:
        errors = colored(errors, "red")
    # analyser_ending
    if not errors:
        for i in range(len(my_tree)):
            print("\t" * i + my_tree[i])
    else:
        print("\nsyntax analyser result")
        print(f"\n{errors}")


if __name__ == "__main__":
    print(f"Given:\n\t{STATEMENT}")
    lxs_an = lexis_analyser()
    if lxs_an is None:
        syntax_analyser()
    else:
        print(f"Lexis analyser relust: \n {lxs_an}")
