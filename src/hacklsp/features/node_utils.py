from dataclasses import dataclass
from typing import Callable

from lsprotocol.types import Position
from tree_sitter import Node


@dataclass
class NodeDetails:
    start_pos: Position
    end_pos: Position
    _type: str
    txt: str


def check_children(node: Node, pred: Callable[[Node], bool]) -> Node:
    # Make certain we are getting the correct child
    for child in node.children:
        if pred(child):
            return child
    return node


def traverse_tree(node: Node, pred: Callable[[Node], bool]) -> Node | None:
    if pred(node):
        return check_children(node, pred)

    for child in node.children:
        res = traverse_tree(child, pred)
        if res is not None:
            return check_children(res, pred)

    return None
