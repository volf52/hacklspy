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
    "!D": DescData.comp("bitwise not of Data Register"),
    "!A": DescData.comp("bitwise not of Address Register"),
    "!M": DescData.comp(r"bitwise not of Memory\[Address Register]"),
    "-D": DescData.comp("negative of Data Register"),
    "-A": DescData.comp("negative Address Register"),
    "-M": DescData.comp(r"negative Memory\[Address Register]"),
    "D+1": DescData.comp("Data Register + 1"),
    "D-1": DescData.comp("Data Register - 1"),
    "A+1": DescData.comp("Address Register + 1"),
    "A-1": DescData.comp("Address Register - 1"),
    "M+1": DescData.comp(r"Memory\[Address Register\] + 1"),
    "M-1": DescData.comp(r"Memory\[Address Register\] - 1"),
    "D+A": DescData.comp("Data Register + Address Register"),
    "A+D": DescData.comp("Address Register + Data Register"),
    "D+M": DescData.comp(r"Data Register + Memory\[Address Register]"),
    "M+D": DescData.comp(r"Memory\[Address Register] + Data Register"),
    "D-A": DescData.comp("Data Register - Address Register"),
    "A-D": DescData.comp("Address Register - Data Register"),
    "D-M": DescData.comp(r"Data Register - Memory\[Address Register]"),
    "M-D": DescData.comp(r"Memory\[Address Register] - Data Register"),
    "D&A": DescData.comp("bitwise and of Data Register & Address Register"),
    "A&D": DescData.comp("bitwise and of Address Register & Data Register"),
    "D&M": DescData.comp(r"bitwise and of Data Register & Memory\[Address Register]"),
    "M&D": DescData.comp(r"bitwise and of Memory\[Address Register] & Data Register"),
    "D|A": DescData.comp("bitwise OR of Data Register n Address Register"),
    "A|D": DescData.comp("bitwise OR of Address Register n Data Register"),
    "D|M": DescData.comp(r"bitwise OR of Address Register n Memory\[Address Register]"),
    "M|D": DescData.comp(r"bitwise OR of Memory\[Address Register] n Data Register"),
}
