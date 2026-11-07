import fitz
import os

pdf_path = os.path.join(os.path.dirname(__file__), "..", "Android_Programming_Handbook_Second_Edition.pdf")
doc = fitz.open(pdf_path)

print(f"Total Pages: {len(doc)}")
for i, page in enumerate(doc):
    t = page.get_text().strip()
    lines = [l.strip() for l in t.split("\n") if l.strip()]
    first = lines[0] if lines else "EMPTY"
    second = lines[1] if len(lines) > 1 else ""
    third = lines[2] if len(lines) > 2 else ""
    print(f"P{i+1:02d}: {len(t):4d} chars | {first[:25]} | {second[:25]} | {third[:25]}")
