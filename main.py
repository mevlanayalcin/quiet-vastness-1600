import os

TEXT = (
    "The porch boards hold the last of the sun.\n"
    "A cup of tea goes cool by the rail.\n"
    "\n"
    "Down the hill, the river\n"
    "turns one stone a little rounder,\n"
    "as it has each evening\n"
    "for ten thousand years,\n"
    "and will,\n"
    "for ten thousand more."
)

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(TEXT)
