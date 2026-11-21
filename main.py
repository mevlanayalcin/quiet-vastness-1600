import os

TEXT = (
    "Your father walks the lane home.\n"
    "You fall asleep warm on his shoulder.\n"
    "A slow step. A sway. Gravel under his boot.\n"
    "With each step, the whole earth\n"
    "glides twenty miles through the dark,\n"
    "so softly no leaf stirs,\n"
    "carrying the lane, him, and you\n"
    "all the way round the sun."
)

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(TEXT)
