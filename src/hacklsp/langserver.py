from tree_sitter import Parser

from .features import (
    HackAsmServer,
    setup_completion,
    setup_doc_crud,
    setup_hover,
    setup_initialize,
)
from .parser.queries import Queries

# LANG_SERVER = LanguageServer("hacklsp", __version__)


def init_server(parser: Parser, queries: Queries) -> HackAsmServer:
    server = HackAsmServer(parser, queries)

    setup_initialize(server)
    setup_doc_crud(server)
    setup_completion(server)
    setup_hover(server)

    return server
