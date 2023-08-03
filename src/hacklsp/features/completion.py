from dataclasses import dataclass

from lsprotocol.types import (
    TEXT_DOCUMENT_COMPLETION,
    CompletionItem,
    CompletionItemKind,
    CompletionItemLabelDetails,
    CompletionList,
    CompletionOptions,
    CompletionParams,
    CompletionTriggerKind,
)

from .descriptions import DESCRIPTIONS, KeywordType
from .hackasm_server import HackAsmServer


@dataclass
class TriggerCharacter:
    AT = "@"
    SEMI = ";"
    EQ = "="


TRIGGER_CHARACTERS = [TriggerCharacter.AT, TriggerCharacter.SEMI, TriggerCharacter.EQ]
NO_COMPLETION: CompletionList = CompletionList(is_incomplete=False, items=[])

LABEL_KIND = CompletionItemKind.Constant
JUMP_KIND = CompletionItemKind.Keyword

JUMP_KWS = [
    (x, data.desc)
    for (x, data) in DESCRIPTIONS.items()
    if data._type is KeywordType.Jump
]
JUMP_COMPLETION_ITEMS = CompletionList(
    is_incomplete=False,
    items=[
        CompletionItem(x, CompletionItemLabelDetails(desc), kind=JUMP_KIND)
        for (x, desc) in JUMP_KWS
    ],
)


def _comp_list(items: list[str] = []):
    CompletionItemKind.Constant
    return CompletionList(
        is_incomplete=True, items=list(map(lambda x: CompletionItem(x), items))
    )


def _label_list(ls: HackAsmServer, doc_uri: str) -> CompletionList:
    doc_labels = ls.get_labels_for_doc(doc_uri)

    completions = CompletionList(
        is_incomplete=True,
        items=[CompletionItem(label, kind=LABEL_KIND) for label in doc_labels],
    )

    return completions


_comp_items = [
    CompletionItem(x, CompletionItemLabelDetails(f"Copy value from {x} register"))
    for x in ["A", "M", "D"]
]
_comp_items.extend(
    (
        CompletionItem(x, CompletionItemLabelDetails(f"Set dest value to {data.desc}"))
        for (x, data) in DESCRIPTIONS.items()
        if data._type is KeywordType.Comp
    )
)
COMP_COMPLETION_ITEMS = CompletionList(
    is_incomplete=False,
    items=_comp_items,
)


def setup_completion(server: HackAsmServer) -> None:
    @server.feature(
        TEXT_DOCUMENT_COMPLETION,
        CompletionOptions(trigger_characters=TRIGGER_CHARACTERS),
    )
    async def _on_completion_req(
        ls: HackAsmServer, params: CompletionParams
    ) -> CompletionList:
        if (
            params.context is None
            or params.context.trigger_kind != CompletionTriggerKind.TriggerCharacter
        ):
            return NO_COMPLETION

        doc_uri = params.text_document.uri
        match params.context.trigger_character:
            case TriggerCharacter.AT:
                return _label_list(ls, doc_uri)
            case TriggerCharacter.EQ:
                return COMP_COMPLETION_ITEMS
            case TriggerCharacter.SEMI:
                return JUMP_COMPLETION_ITEMS

        return NO_COMPLETION
