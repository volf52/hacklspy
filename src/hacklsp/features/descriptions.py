from dataclasses import dataclass
from enum import Enum

KeywordType = Enum("KeywordType", ["Register", "Jump", "Comp"])


@dataclass
class DescData:
    _type: KeywordType
    desc: str

    @classmethod
    def register(cls, desc: str):
        return cls(_type=KeywordType.Register, desc=desc)

    @classmethod
    def jump(cls, desc: str):
        return cls(_type=KeywordType.Jump, desc=desc)

    @classmethod
    def comp(cls, desc: str):
        return cls(_type=KeywordType.Comp, desc=desc)


DESCRIPTIONS: dict[str, DescData] = {
    "A": DescData.register("Address Register"),
    "M": DescData.register("Memory Register"),
    "D": DescData.register("Data Register"),
    "JMP": DescData.jump("Unconditional Jump"),
    "JEQ": DescData.jump("Jump if Equal"),
    "JNE": DescData.jump("Jump if Not Equal"),
    "JLT": DescData.jump("Jump if Less Than"),
    "JGT": DescData.jump("Jump if Greater Than"),
    "JGE": DescData.jump("Jump if Greater or Equal"),
    "JLE": DescData.jump("Jump if Less than or Equal"),
    "0": DescData.comp("zero"),
    "1": DescData.comp("one"),
    "-1": DescData.comp("negative 1"),
    "!D": DescData.comp("bitwise not of D"),
    "!A": DescData.comp("bitwise not of A"),
    "!M": DescData.comp("bitwise not of M"),
    "-D": DescData.comp("negative D"),
    "-A": DescData.comp("negative A"),
    "-M": DescData.comp("negative M"),
    "D+1": DescData.comp("D + 1"),
    "D-1": DescData.comp("D - 1"),
    "A+1": DescData.comp("A + 1"),
    "A-1": DescData.comp("A - 1"),
    "M+1": DescData.comp("M + 1"),
    "M-1": DescData.comp("M - 1"),
    "D+A": DescData.comp("D + A"),
    "A+D": DescData.comp("A + D"),
    "D+M": DescData.comp("D + M"),
    "M+D": DescData.comp("M + D"),
    "D-A": DescData.comp("D - A"),
    "A-D": DescData.comp("A - D"),
    "D-M": DescData.comp("D - M"),
    "M-D": DescData.comp("M - D"),
    "D&A": DescData.comp("bitwise and of D & A"),
    "A&D": DescData.comp("bitwise and of A & D"),
    "D&M": DescData.comp("bitwise and of D & M"),
    "M&D": DescData.comp("bitwise and of M & D"),
    "D|A": DescData.comp("bitwise OR of D n A"),
    "A|D": DescData.comp("bitwise OR of A n D"),
    "D|M": DescData.comp("bitwise OR of A n M"),
    "M|D": DescData.comp("bitwise OR of M n D"),
}
