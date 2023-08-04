from lsprotocol.types import (
    TEXT_DOCUMENT_HOVER,
    Hover,
    HoverParams,
    MarkupContent,
    MarkupKind,
    Range,
)

from .descriptions import DESCRIPTIONS
from .hackasm_server import HackAsmServer


def get_desc(txt: str) -> str:
    abc = DESCRIPTIONS.get(txt)
    if abc is None:
        return ""

    return abc.desc


def setup_hover(server: HackAsmServer) -> None:
    @server.feature(TEXT_DOCUMENT_HOVER)
    async def _on_hover(ls: HackAsmServer, params: HoverParams) -> Hover | None:
        doc_uri = params.text_document.uri
        pos = params.position

        details = await ls.get_hovered_node_details(doc_uri, pos)
        if details is None:
            return None

        hover_range = Range(details.start_pos, details.end_pos)

        content = MarkupContent(MarkupKind.PlainText, details._type)
        match details._type:
            case "@":
                content = MarkupContent(MarkupKind.PlainText, "A-Instruction Start")
            case ";" | "=":
                content = MarkupContent(
                    MarkupKind.PlainText, "Separator for C-Instruction"
                )
            case "label_ident":
                content = MarkupContent(
                    MarkupKind.Markdown, f"Label\n---\nValue: {details.txt}"
                )
            case "jump" | "comp" | "dest":
                title = details._type.title()
                desc = get_desc(details.txt)
                content = MarkupContent(MarkupKind.Markdown, f"{title}\n---\n{desc}")

        return Hover(content, hover_range)
