import os

practicals_path = os.path.join(os.path.dirname(__file__), "content_practicals.py")

with open(practicals_path, "r", encoding="utf-8") as f:
    text = f.read()

parts = text.split('<div class="chapter-break"></div>')
print(f"Total parts split by chapter-break: {len(parts)}")

rebuilt = [parts[0]]
kept_breaks = 0
removed_breaks = 0

for p in parts[1:]:
    # If the segment starts with a practical program header, keep the break
    if "PROGRAM" in p[:300]:
        rebuilt.append('<div class="chapter-break"></div>' + p)
        kept_breaks += 1
    else:
        # Otherwise, let it flow naturally without a hard page break
        rebuilt.append('\n<!-- Continuous Natural Flow -->\n' + p)
        removed_breaks += 1

print(f"Kept breaks: {kept_breaks}, Removed internal breaks: {removed_breaks}")

new_text = "".join(rebuilt)
with open(practicals_path, "w", encoding="utf-8") as f:
    f.write(new_text)

print("content_practicals.py successfully optimized!")
