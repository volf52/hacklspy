from .features import (
    HackAsmServer,
    setup_completion,
    setup_doc_close,
    setup_doc_open,
    setup_initialize,
)

# LANG_SERVER = LanguageServer("hacklsp", __version__)


def init_server() -> HackAsmServer:
    server = HackAsmServer()

    setup_initialize(server)
    setup_doc_open(server)
    setup_doc_close(server)
    setup_completion(server)

    return server
