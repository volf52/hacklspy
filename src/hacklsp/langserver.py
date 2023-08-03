from .features import HackAsmServer, setup_completion, setup_doc_open, setup_initialize

# LANG_SERVER = LanguageServer("hacklsp", __version__)
LANG_SERVER = HackAsmServer()

setup_initialize(LANG_SERVER)
setup_doc_open(LANG_SERVER)
setup_completion(LANG_SERVER)
