"""System programming 3rd labwork by Andrii Doroshenko, IO-71"""

CHUNK_OF_CODE = "int main (void) {float b, a[n12]; int n; …}"
SEPARATORS = [";", "...", "…", ", ", ":", "?"]
BRACKETS = ["(", ")", "{", "}", "[", "]"]
ARITHMETIC = ["+", "-", "*", "/", "%", "++", "--", "^", "~", ">>", "<<", "=", "+=", "-=", "*=", "/=", "%=", "<<=",
              ">>=", "&=", "^=", "|="]
LOGIC = ["==", "!=", ">", "<", ">=", "<=", "&&", "||", "!", "&", "|"]

KEYWORDS = ["auto", "break", "case", "char",
            "const", "continue", "default", "do",
            "double", "else", "enum", "extern",
            "float", "for", "goto", "if",
            "int", "long", "register", "return",
            "short", "signed", "sizeof", "static",
            "struct", "switch", "typedef", "union",
            "unsigned", "void", "volatile", "while",
            "sin", "cos", "main"]


def parser(my_str=CHUNK_OF_CODE):
    inp = my_str
    for i in [*SEPARATORS, *ARITHMETIC, *LOGIC, *BRACKETS]:
        inp = inp.replace(i, " ")
    vars = [i for i in inp.split() if (i not in KEYWORDS) and not (i.isdigit())]
    kws = [i for i in inp.split() if i in KEYWORDS]
    nums = [i for i in inp.split() if (i not in KEYWORDS) and (i.isdigit())]
    my_gen = lambda arr, searching_arr: [i for i in arr if i in searching_arr]
    ar, sep, log, br = [my_gen(i, my_str) for i in [ARITHMETIC, SEPARATORS, LOGIC, BRACKETS]]
    invalid_vars = [i for i in vars if i[0].isdigit()]
    vars = [i for i in inp.split() if (i not in KEYWORDS) and not (i.isdigit()) and (i not in invalid_vars)]
    return (vars, invalid_vars, kws, nums, ar, log, br, sep)


def console_outputer(*args):
    print(f"\nGiven statement: {CHUNK_OF_CODE}")
    print("""\nVariables and identifiers: {}
Invalid variables: {}
Programming language keywords: {}
Numbers: {}
Symbols:
    Arithmetic operators: {}
    Logic operators: {}
    Brackets: {}
    Separators: {}""".format(*[str(i)[1: -1] for i in args[0]]))


if __name__ == "__main__":
    console_outputer(parser())
