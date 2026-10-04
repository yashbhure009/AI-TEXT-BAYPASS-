ZERO_WIDTH_SPACE = "\u200b"

with open("assignment.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()

stealth_text = ZERO_WIDTH_SPACE.join(raw_text)

with open("clean_assignment.txt", "w", encoding="utf-8") as file:
    file.write(stealth_text)

print("Humanized")
