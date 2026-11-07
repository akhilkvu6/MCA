import os

theory_path = os.path.join(os.path.dirname(__file__), "content_theory.py")
with open(theory_path, "r", encoding="utf-8") as f:
    text = f.read()

# Replace selective chapter breaks in content_theory.py
# Let's replace the breaks before Chapter 3, Chapter 4, and Chapter 16-19 with clean section dividers
# Keep breaks before Chapter 1 (none), Chapter 2, Chapter 5&6, Chapter 7, Chapter 8, Chapter 11&12, Chapter 13

replacements = [
    ('<!-- CHAPTER 3 -->\n<div class="chapter-break"></div>', '<!-- CHAPTER 3 -->\n<div style="margin-top: 14px;"></div>'),
    ('<!-- CHAPTER 4 -->\n<div class="chapter-break"></div>', '<!-- CHAPTER 4 -->\n<div style="margin-top: 14px;"></div>'),
    ('<!-- CHAPTER 16, 17, 18 & 19 -->\n<div class="chapter-break"></div>', '<!-- CHAPTER 16, 17, 18 & 19 -->\n<div style="margin-top: 14px;"></div>')
]

for old, new in replacements:
    if old in text:
        text = text.replace(old, new)
        print(f"Replaced: {old[:25]}")
    else:
        print(f"Not found: {old[:25]}")

with open(theory_path, "w", encoding="utf-8") as f:
    f.write(text)

print("content_theory.py breaks optimized!")
