from pathlib import Path

from tree_sitter import Language

SO_FILE_PATH = (Path(__file__).parent / "hackasm-treesitter.so").resolve()
SO_FILE = str(SO_FILE_PATH)

HACKASM_TS_PATH = str(
    (Path(__file__) / ".." / ".." / ".." / ".." / "tree-sitter-hackasm").resolve()
)


def build_lang(so_path: str, ts_path: str) -> Language:
    Language.build_library(so_path, [str(ts_path)])

    HACKASM_LANG = Language(SO_FILE, "hackasm")

    return HACKASM_LANG
