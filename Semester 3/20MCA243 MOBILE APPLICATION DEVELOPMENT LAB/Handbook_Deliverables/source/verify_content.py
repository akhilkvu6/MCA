import fitz
import os

pdf_path = os.path.join(os.path.dirname(__file__), "..", "Android_Programming_Handbook_Second_Edition.pdf")
doc = fitz.open(pdf_path)

full_text = ""
for i, page in enumerate(doc):
    full_text += f"\n--- PAGE {i+1} ---\n" + page.get_text()

checks = [
    "PROGRAM 01: USER LOGIN PAGE",
    "PROGRAM 02: SIMPLE CALCULATOR",
    "PROGRAM 03: EXPLICIT INTENT",
    "PROGRAM 04: ACTIVITY LIFE CYCLE",
    "PROGRAM 05: SELECTION CONTROLS",
    "PROGRAM 06: IMPLICIT INTENTS",
    "PROGRAM 07: LISTVIEW",
    "PROGRAM 08: SCROLLVIEW",
    "PROGRAM 09: DROPDOWN SPINNER",
    "PROGRAM 10: SHAREDPREFERENCES",
    "APPLICATION 1: ENTERPRISE AUTHENTICATION",
    "APPLICATION 2: STUDENT REGISTRATION",
    "APPLICATION 3: ITEM SELECTION & SHOPPING",
    "APPLICATION 4: USER REGISTRATION & PROFILE",
    "APPLICATION 5: MULTI-PAGE UNIVERSITY PORTAL",
    "30. What are the key stages in building an APK file?"
]

all_passed = True
for c in checks:
    pos = full_text.find(c)
    if pos != -1:
        page_num = full_text[:pos].count("--- PAGE ")
        print(f"[PASSED] '{c}' found on Page {page_num}")
    else:
        print(f"[FAILED] '{c}' NOT FOUND!")
        all_passed = False

if all_passed:
    print("\nALL 16 MAJOR PROGRAM & APPLICATION CHECKPOINTS PASSED!")
else:
    print("\nSOME CHECKPOINTS FAILED!")
