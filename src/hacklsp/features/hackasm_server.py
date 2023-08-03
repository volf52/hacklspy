from pygls.server import LanguageServer
from tree_sitter import Tree

from hacklsp.parser import HACKASM_LANG, HACKASM_PARSER
from hacklsp.version import __version__

LABEL_QUERY = HACKASM_LANG.query("(label_def (label_ident) @label)")


class HackAsmServer(LanguageServer):
    __slots__ = "ts_trees"

    ts_trees: dict[str, Tree]

    def __init__(self):
        super().__init__("hasklsp", __version__)
        self.ts_trees = dict()

    def add_doc(self, uri: str, text: str) -> None:
        tree = HACKASM_PARSER.parse(text.encode())
        self.ts_trees[uri] = tree

    def get_labels_for_doc(self, uri: str) -> list[str]:
        tree = self.ts_trees.get(uri)
        if tree is None:
            return []

        captures = LABEL_QUERY.captures(tree.root_node)
        labels = []
        for cap, _ in captures:
            labels.append(cap.text.decode())

        return labels
