from tree_sitter import Language, Parser


def init_hackasm_parser(lang: Language) -> Parser:
    HACKASM_PARSER = Parser()

    HACKASM_PARSER.set_language(lang)

    return HACKASM_PARSER
