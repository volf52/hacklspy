from lsprotocol.types import INITIALIZE, InitializeParams

from hacklsp.logger import LOGGER

from .hackasm_server import HackAsmServer


def setup_initialize(server: HackAsmServer) -> None:
    @server.feature(INITIALIZE)
    async def _on_initialize(ls: HackAsmServer, _params: InitializeParams) -> None:
        LOGGER.debug("initializing hacklsp")
        ls.show_message("initializing hacklsp msg")
        ls.show_message_log("initializing hacklsp log")
