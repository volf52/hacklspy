from lsprotocol.types import (
    TEXT_DOCUMENT_DID_CHANGE,
    TEXT_DOCUMENT_DID_CLOSE,
    TEXT_DOCUMENT_DID_OPEN,
    TEXT_DOCUMENT_DID_SAVE,
    WORKSPACE_DID_RENAME_FILES,
    DidChangeTextDocumentParams,
    DidCloseTextDocumentParams,
    DidOpenTextDocumentParams,
    DidSaveTextDocumentParams,
    DocumentSelector,
    Position,
    PositionEncodingKind,
    Range,
    RenameFilesParams,
    SaveOptions,
    TextDocumentSaveRegistrationOptions,
    WorkspaceDidRenameFilesNotification,
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

    @server.feature(TEXT_DOCUMENT_DID_SAVE)
    async def _on_doc_save(ls: HackAsmServer, params: DidSaveTextDocumentParams):
        doc_uri = params.text_document.uri
        txt = ls.workspace.get_document(doc_uri).source
        await ls.replace_doc(doc_uri, txt)

    # @server.feature(TEXT_DOCUMENT_DID_CHANGE)
    # async def _on_doc_update(ls: HackAsmServer, params: DidChangeTextDocumentParams):
    #     doc_uri = params.text_document.uri
    #     new_text = ls.workspace.get_document(doc_uri).source
    #     await ls.replace_doc(doc_uri, new_text)

    @server.feature(WORKSPACE_DID_RENAME_FILES)
    async def _on_doc_rename(ls: HackAsmServer, params: RenameFilesParams):
        for rename in params.files:
            await ls.rename_doc(rename.old_uri, rename.new_uri)
