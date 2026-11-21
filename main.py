import os

TEXT = (
    "Your father walks the lane home.\n"
    "You fall asleep warm on his shoulder.\n"
    "A slow step. A sway. Gravel under his boot.\n"
    "Between two steps, the whole earth\n"
    "glides twenty miles round the sun,\n"
    "as it has since the first night,\n"
    "so gently no leaf stirs,\n"
    "carrying him, carrying you."
)

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(TEXT)
