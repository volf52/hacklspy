from typing import Callable

from lsprotocol.types import Position
from pygls.server import LanguageServer
from tree_sitter import Node, Parser, Tree

from hacklsp.parser import Queries
from hacklsp.version import __version__

from .node_utils import NodeDetails, traverse_tree


class HackAsmServer(LanguageServer):
    __slots__ = "ts_trees", "parser", "queries"

    ts_trees: dict[str, Tree]
    parser: Parser
    queries: Queries

    def __init__(self, parser: Parser, queries: Queries):
        super().__init__("hasklsp", __version__)
        self.ts_trees = dict()
        self.parser = parser
        self.queries = queries

    async def add_doc(self, uri: str, text: str) -> None:
        tree = self.parser.parse(text.encode())
        self.ts_trees[uri] = tree

    async def remove_doc(self, uri: str) -> None:
        if self.ts_trees.get(uri) is not None:
            del self.ts_trees[uri]

    async def rename_doc(self, old_uri: str, new_uri: str) -> None:
        tree = self.ts_trees.get(old_uri)
        if tree is not None:
            self.ts_trees[new_uri] = tree
            del self.ts_trees[old_uri]

    async def replace_doc(self, uri: str, text: str) -> None:
        # old_tree = self.ts_trees.get(uri)
        # tree = HACKASM_PARSER.parse(text.encode(), old_tree=old_tree)
        tree = self.parser.parse(text.encode())
        self.ts_trees[uri] = tree

    async def update_doc(self, uri: str) -> None:
        tree = self.ts_trees.get(uri)
        if tree is None:
            return

    async def get_labels_for_doc(self, uri: str) -> list[str]:
        tree = self.ts_trees.get(uri)
        if tree is None:
            return []

        captures = self.queries.LABEL_QUERY.captures(tree.root_node)
        labels = []
        for cap, _ in captures:
            labels.append(cap.text.decode())

        return labels

    async def get_hovered_node_details(
        self, uri: str, pos: Position
    ) -> NodeDetails | None:
        node = self.__get_node_on_pos(uri, pos)
        if node is None:
            return None

        start_line, start_char = node.start_point
        end_line, end_char = node.end_point
        start_pos = Position(start_line, start_char)
        end_pos = Position(end_line, end_char)
        node_type = node.type
        node_text = node.text.decode()

        return NodeDetails(start_pos, end_pos, node_type, node_text)

    def __get_node_on_pos(self, uri: str, pos: Position):
        line = pos.line
        character = pos.character

        def is_in_range(node: Node):
            start_line, start_char = node.start_point
            end_line, end_char = node.end_point

            return line in range(start_line, end_line + 1) and character in range(
                start_char, end_char
            )

        return self.__get_node_satisfying_cond(uri, is_in_range)

    def __get_node_satisfying_cond(
        self, uri: str, fn: Callable[[Node], bool]
    ) -> Node | None:
        tree = self.ts_trees.get(uri)
        if tree is None:
            return None
        # Root node not used to prevent matching source_file on line_start
        for node in tree.root_node.children:
            if (res := traverse_tree(node, fn)) is not None:
                return res
