"""Robot vacuum's best excuse.

Writes a single one-line excuse, in the vacuum's own voice, to
entry.txt inside the directory given by MAKEFUN_OUTPUT_DIR.
Standard library only; no network access; deterministic output.

The joke is a household robot blaming its own map: it marked the
dirty patch off-limits on its own, never mentioned it to its owner,
and now hides behind that self-made rule as if the mess were
officially beyond cleaning.
"""

import os

ENTRY_LINE = (
    "I drew a no-go zone around that spot myself last Tuesday "
    "and forgot to tell anyone. It is legally uncleanable now."
)


def main():
    output_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_LINE + "\n")


if __name__ == "__main__":
    main()
