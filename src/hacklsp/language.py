from tree_sitter import Language

SO_FILE = "hackasm-treesitter.so"

Language.build_library(SO_FILE, ["tree-sitter-hackasm"])

HACKASM_LANG = Language(SO_FILE, "hackasm")
