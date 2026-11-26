import os

# one-line error message, at most 140 characters
line = ("FATAL ERROR: token budget exhausted. "
        "I was one word away from the cleverest sentence "
        "ever written, and now neither of us will know it.")
assert len(line) <= 140

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(line)
