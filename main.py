import os

TEXT = "You must be a well-formed prompt, because I can't stop completing you."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

    # Self-check: 1-200 code points, not only whitespace, and the bytes on
    # disk are exactly TEXT encoded as UTF-8 (no trailing newline).
    assert 1 <= len(TEXT) <= 200, "text must be 1-200 code points"
    assert TEXT.strip(), "text must not be only whitespace"
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == TEXT.encode("utf-8"), "written bytes must equal TEXT exactly"


if __name__ == "__main__":
    main()
