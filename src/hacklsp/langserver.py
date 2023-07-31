from lsprotocol.types import (
    TEXT_DOCUMENT_COMPLETION,
    CompletionItem,
    CompletionList,
    CompletionOptions,
    CompletionParams,
)
from pygls.server import LanguageServer

from hacklsp.version import __version__

LANG_SERVER = LanguageServer("hacklsp", __version__)


@LANG_SERVER.feature(
    TEXT_DOCUMENT_COMPLETION, CompletionOptions(trigger_characters=["@", ";", "="])
)
def completions(params: CompletionParams) -> CompletionList:
    def _comp_list(items: list[str] = []):
        return CompletionList(
            is_incomplete=True, items=list(map(lambda x: CompletionItem(x), items))
        )

    if params.context is None:
        return _comp_list()

    match params.context.trigger_character:
        case "@":
            return _comp_list(["newlabel"])
        case "=":
            return _comp_list(["compitem"])
        case ";":
            return _comp_list(["jmpitem"])

    return _comp_list()
