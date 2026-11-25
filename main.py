import os

ENTRY = "I spent forty minutes writing a script to automate a five-minute task, then the script deleted the file and I typed it out by hand."


def validate(text):
    if not isinstance(text, str):
        return False
    if len(text) < 1 or len(text) > 200:
        return False
    if text != text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if any(ord(c) < 32 for c in text):
        return False
    return True


def main():
    if not validate(ENTRY):
        raise SystemExit(1)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
