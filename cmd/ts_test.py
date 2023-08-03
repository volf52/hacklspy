from hacklsp.parser import HACKASM_LANG, HACKASM_PARSER

# with open("./data/testfile.hasm", "rb") as fp:
#     source = fp.read()

with open("./data/sum_to_100.hasm", "rb") as fp:
    source = fp.read()

parsed = HACKASM_PARSER.parse(source)
query = HACKASM_LANG.query("(label_def (label_ident) @name)")

captures = query.captures(parsed.root_node)

for cap, _ in captures:
    print(cap.text.decode())

print(captures)
