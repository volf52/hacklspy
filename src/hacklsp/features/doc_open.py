from lsprotocol.types import TEXT_DOCUMENT_DID_OPEN, DidOpenTextDocumentParams

from .hackasm_server import HackAsmServer


def setup_doc_open(server: HackAsmServer) -> None:
    @server.feature(TEXT_DOCUMENT_DID_OPEN)
    async def _on_doc_open(ls: HackAsmServer, params: DidOpenTextDocumentParams):
        doc_uri = params.text_document.uri
        doc_text = params.text_document.text

        ls.add_doc(doc_uri, doc_text)
