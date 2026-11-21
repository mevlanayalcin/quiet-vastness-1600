import os

TEXT = (
    "The light on this sill left its star before the first fern opened. "
    "It crossed all that dark at one even pace, and now it lies on "
    "warm wood beside a pear. More is on the way, and has been "
    "since before the hills."
)

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(TEXT)
