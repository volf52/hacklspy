from dataclasses import dataclass

from lsprotocol.types import (
    TEXT_DOCUMENT_COMPLETION,
    CompletionItem,
    CompletionItemKind,
    CompletionList,
    CompletionOptions,
    CompletionParams,
    CompletionTriggerKind,
)

from .hackasm_server import HackAsmServer


@dataclass
class TriggerCharacter:
    AT = "@"
    SEMI = ";"
    EQ = "="


TRIGGER_CHARACTERS = [TriggerCharacter.AT, TriggerCharacter.SEMI, TriggerCharacter.EQ]
JUMP_KWS = ["JMP", "JEQ", "JLE", "JGT", "JGE", "JLE", "JNE"]

NO_COMPLETION: CompletionList = CompletionList(is_incomplete=False, items=[])

LABEL_KIND = CompletionItemKind.Constant
JUMP_KIND = CompletionItemKind.Keyword


def _comp_list(items: list[str] = []):
    CompletionItemKind.Constant
    return CompletionList(
        is_incomplete=True, items=list(map(lambda x: CompletionItem(x), items))
    )


def _jump_list() -> CompletionList:
    items = [CompletionItem(x, kind=JUMP_KIND) for x in JUMP_KWS]

    return CompletionList(is_incomplete=False, items=items)


def _label_list(ls: HackAsmServer, doc_uri: str) -> CompletionList:
    doc_labels = ls.get_labels_for_doc(doc_uri)

    completions = CompletionList(
        is_incomplete=True,
        items=[CompletionItem(label, kind=LABEL_KIND) for label in doc_labels],
    )

    return completions


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
                return _comp_list(["compitem"])
            case TriggerCharacter.SEMI:
                return _jump_list()

        return _comp_list()
