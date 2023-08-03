from tree_sitter import Parser

from .language import HACKASM_LANG

HACKASM_PARSER = Parser()

HACKASM_PARSER.set_language(HACKASM_LANG)
