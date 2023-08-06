from dataclasses import dataclass

from tree_sitter import Language
from tree_sitter.binding import Query


@dataclass
class Queries:
    LABEL_QUERY: Query

    def __init__(self, lang: Language):
        self.LABEL_QUERY = lang.query("(label_def (label_ident) @label)")
