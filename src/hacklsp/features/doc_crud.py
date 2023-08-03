from lsprotocol.types import (
    TEXT_DOCUMENT_DID_CLOSE,
    TEXT_DOCUMENT_DID_OPEN,
    DidCloseTextDocumentParams,
    DidOpenTextDocumentParams,
)

from .hackasm_server import HackAsmServer


def setup_doc_crud(server: HackAsmServer) -> None:
    @server.feature(TEXT_DOCUMENT_DID_OPEN)
    async def _on_doc_open(ls: HackAsmServer, params: DidOpenTextDocumentParams):
        doc_uri = params.text_document.uri
        doc_text = params.text_document.text

        await ls.add_doc(doc_uri, doc_text)

    @server.feature(TEXT_DOCUMENT_DID_CLOSE)
    async def _on_doc_close(ls: HackAsmServer, params: DidCloseTextDocumentParams):
        doc_uri = params.text_document.uri

        await ls.remove_doc(doc_uri)
