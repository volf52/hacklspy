from hacklsp.langserver import init_server
from hacklsp.parser import (
    HACKASM_TS_PATH,
    SO_FILE,
    Queries,
    build_lang,
    init_hackasm_parser,
)

print("Setting up hackasm treesitter...")
lang = build_lang(SO_FILE, HACKASM_TS_PATH)
parser = init_hackasm_parser(lang)
queries = Queries(lang)
print("Initializing server...")
LANG_SERVER = init_server(parser, queries)
print("Starting the server...")
LANG_SERVER.start_io()
