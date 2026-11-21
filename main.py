import os

TEXT = (
    "You lie warm under the quilt.\n"
    "The curtain lifts at the window.\n"
    "Hangs. A long while. Falls back.\n"
    "\n"
    "Under the house, the moon lifts\n"
    "the solid rock of the earth\n"
    "a foot, and sets it down,\n"
    "hills, roof, and bed,\n"
    "twice a day since the first night,\n"
    "so softly you stay asleep."
)

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(TEXT)
