from hacklsp.parser.language import HACKASM_TS_PATH, SO_FILE, SO_FILE_PATH, build_lang


def main():
    SO_FILE_PATH.unlink(missing_ok=True)

    build_lang(SO_FILE, HACKASM_TS_PATH)
