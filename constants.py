CHUNK_OF_CODE = "if (a>b) then begin a:=b; end;"
PASKAL_KEYWORDS = ["if", "else", "then", "end", "begin", "and", "array", "asm", "break", "case", "const", "constructor",
                   "continue", "destructor", "div", "do", "downto", "else", "end", "false", "file", "for", "function",
                   "goto", "if", "implementation", "in", "inline", "interface", "label", "mod", "nil", "not", "object",
                   "of", "on", "operator", "or", "packed", "procedure", "program", "record", "repeat", "set", "shl",
                   "shr", "string", "then", "to", "true", "type", "unit", "until", "uses", "var", "while", "with",
                   "xor"]

CONSTRUCTIONS = [["if", "then"],
                 ["begin", "end"]]


# for i in PASKAL_KEYWORDS:
#     if i in CHUNK_OF_CODE:
#         CHUNK_OF_CODE = CHUNK_OF_CODE.replace(i, " ")
#
# print(CHUNK_OF_CODE)
