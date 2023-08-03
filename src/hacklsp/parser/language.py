from pathlib import Path

from tree_sitter import Language

SO_FILE = "hackasm-treesitter.so"

hackasm_ts_pth = (
    Path(__file__) / ".." / ".." / ".." / ".." / "tree-sitter-hackasm"
).resolve()

Language.build_library(SO_FILE, [str(hackasm_ts_pth)])

HACKASM_LANG = Language(SO_FILE, "hackasm")
