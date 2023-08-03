from dataclasses import dataclass
from enum import Enum

KeywordType = Enum("KeywordType", ["Register", "Jump"])


@dataclass
class KeywordData:
    _type: KeywordType
    desc: str

    @classmethod
    def register(cls, desc: str):
        return cls(_type=KeywordType.Register, desc=desc)

    @classmethod
    def jump(cls, desc: str):
        return cls(_type=KeywordType.Jump, desc=desc)


KEYWORDS: dict[str, KeywordData] = {
    "A": KeywordData.register("Address Register"),
    "M": KeywordData.register("Memory Register"),
    "D": KeywordData.register("Data Register"),
    "JMP": KeywordData.jump("Unconditional Jump"),
    "JEQ": KeywordData.jump("Jump if Equal"),
    "JNE": KeywordData.jump("Jump if Not Equal"),
    "JLT": KeywordData.jump("Jump if Less Than"),
    "JGT": KeywordData.jump("Jump if Greater Than"),
    "JGE": KeywordData.jump("Jump if Greater or Equal"),
    "JLE": KeywordData.jump("Jump if Less than or Equal"),
}
