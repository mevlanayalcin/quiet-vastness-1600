import os

TEXT = (
    "You fall asleep under the quilt.\n"
    "Your mother's warm hand rests on your back.\n"
    "A rise. A long while. A fall.\n"
    "Under you, the moon lifts\n"
    "solid rock a foot and lowers it,\n"
    "hills, house, and bed,\n"
    "so softly nothing stirs,\n"
    "twice a day since the first night.\n"
    "Her hand stays."
)

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(TEXT)
