from lsprotocol.types import TEXT_DOCUMENT_DID_CLOSE, DidCloseTextDocumentParams

from .hackasm_server import HackAsmServer


def setup_doc_close(server: HackAsmServer) -> None:
    @server.feature(TEXT_DOCUMENT_DID_CLOSE)
    async def _on_doc_close(ls: HackAsmServer, params: DidCloseTextDocumentParams):
        doc_uri = params.text_document.uri

        ls.remove_doc(doc_uri)
