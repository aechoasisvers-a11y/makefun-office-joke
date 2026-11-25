"""The Funniest Office Joke, Judged Head to Head.

Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters, not only
white space. This entry is 86 characters.
"""

import os

ENTRY = "Our printer only jams on deadline day, so I printed my resignation — not a single jam."

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert ENTRY.strip(), "entry must not be only white space"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
