import os

TEXT = (
    "You are small in the warm bath.\n"
    "Your mother pours a cup over your back.\n"
    "Dip. A slow pour. A long while.\n"
    "Half that water was made in the dark\n"
    "before the sun was lit.\n"
    "It fell in the first rain,\n"
    "filled the first sea,\n"
    "and now runs warm over you.\n"
    "She dips the cup again."
)

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(TEXT)
