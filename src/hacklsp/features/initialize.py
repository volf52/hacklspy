from lsprotocol.types import INITIALIZE

from .hackasm_server import HackAsmServer


def setup_initialize(server: HackAsmServer) -> None:
    @server.feature(INITIALIZE)
    async def on_initialize():
        ...
