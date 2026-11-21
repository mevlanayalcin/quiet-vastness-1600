import os

TEXT = (
    "You lie back in the warm bath.\n"
    "A drop from the tap. A long while. A drop.\n"
    "Your ears go under,\n"
    "the house low and far.\n"
    "\n"
    "Half this water was made in the dark\n"
    "before the sun was lit.\n"
    "It fell in the first rain,\n"
    "filled the first sea,\n"
    "and now holds you up,\n"
    "warm to your chin."
)

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(TEXT)
