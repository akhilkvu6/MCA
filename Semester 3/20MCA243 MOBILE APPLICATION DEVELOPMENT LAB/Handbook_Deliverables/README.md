<div align="center">

# 📱 20MCA243 Android Programming Theory & Practical Handbook
### Second Edition — Code Readability & Layout Redesign

### Master of Computer Applications (MCA) — Semester 3
**College of Engineering Trivandrum (CET)** | APJ Abdul Kalam Technological University (KTU)

<img src="https://img.shields.io/badge/Course-20MCA243-blue?style=for-the-badge">
<img src="https://img.shields.io/badge/Edition-Second%20Edition-purple?style=for-the-badge">
<img src="https://img.shields.io/badge/Handbook%20Pages-60%20Pages%20(Cap%20Compliant)-success?style=for-the-badge">
<img src="https://img.shields.io/badge/Original%20Programs-10%2F10%20Unabridged-brightgreen?style=for-the-badge">
<img src="https://img.shields.io/badge/Integrated%20Apps-5%20(25%20Variations)-success?style=for-the-badge">
<img src="https://img.shields.io/badge/Vector%20Diagrams-20%20Assets-orange?style=for-the-badge">

---

### 📖 Complete Academic Textbook • Practical Reference • Viva Voce Guide

</div>

---

## 🌟 Major Highlights of the Second Edition

The **Second Edition** addresses code compression, line clipping, and layout issues from the first edition:

1. **Dedicated Full-Width Code Pages:** Complete Java and XML files use the full printable page width (186mm) with dark slate header bars (`File: app/src/...`), clean Consolas/JetBrains Mono typography (8pt, 1.32 line height), 4-space tab indentation, and `white-space: pre-wrap; word-break: break-word;` to eliminate horizontal clipping.
2. **Single-Column Full-Width Theory:** Theory, architecture, syntax breakdowns, tables, and diagrams utilize the full page width rather than cramped narrow dual columns.
3. **100% Unabridged Real Code:** All 10 practical programs are dynamically loaded directly from the verified workspace directories (`01_Login_Page` to `10_Shared_Preferences`), including the complete 228-line Calculator layout and 169-line Java file, and both activities for Intent.
4. **Android 1.0 to Android 17 Version History:** Chronological master table covering release names, internal dessert codenames, API levels (API 1 to 36+), release years, milestone features, and the build inequality $\text{minSdk} \le \text{targetSdk} \le \text{compileSdk}$.
5. **Comprehensive Framework API Inventory:** Dedicated reference in `reports/API_Inventory.md` documenting 30+ core Android APIs with signatures, parameters, return types, lifecycle execution context, and exceptions.
6. **3-Stage Dynamic Data Pedagogy:** Predefined $\to$ User Input $\to$ Dynamic Runtime Updates across practicals and integrated apps.
7. **Strict 60-Page Budget Compliance:** Exactly **60 A4 portrait pages**, with zero orphaned or blank pages (<100 characters).

---

## 📂 Deliverables Directory Structure

```text
Handbook_Deliverables/
├── Android_Programming_Handbook_Second_Edition.pdf    # Master 60-Page Publication-Grade PDF
├── Android_Programming_Complete_Theory_and_Practical_Handbook.pdf  # Synchronized Master PDF
│
├── reports/                                          # Quality Control & Auditing Documentation
│   ├── First_Edition_Audit.md                        # Comprehensive defect and layout audit of Edition 1
│   ├── API_Inventory.md                              # Complete 30+ Android Framework API Guide
│   └── Final_QC_Report.md                            # PyMuPDF Automated and Visual Inspection Report
│
├── source/                                           # Editable source files & generator toolchain
│   ├── build_handbook.py                             # Master automated compilation & QC script
│   ├── book_source.html                              # Full semantic academic HTML source
│   ├── content_theory.py                             # Part I: Theory (Chapters 1 to 19)
│   ├── content_java.py                               # Part II: Java fundamentals
│   ├── content_practicals.py                         # Part III: 10 Original university programs
│   ├── content_integrated.py                         # Part IV & V: 5 Apps (25 variations)
│   ├── content_reference.py                          # Part VI & VII: Quick revision & 30 Viva Qs
│   ├── generate_diagrams.py                          # Standalone vector SVG generator
│   ├── generate_integrated_apps.py                   # Integrated applications source generator
│   ├── verify_content.py                             # Automated content and page checkpoint verification
│   ├── verify_code_snippets.py                       # Automated workspace code assertion test suite
│   ├── qc_report.txt                                 # PyMuPDF visual inspection report
│   ├── qc_renders/                                   # High-resolution rendered page proof images
│   └── diagrams/                                     # 20 Standalone vector SVG diagram assets
│       ├── 01_android_architecture.svg to 20_portal_navigation.svg
│
└── integrated_apps/                                  # Organized source code for 25 variations
    ├── App1_Login_Profile/                           # 5 Variations (v1 to v5)
    ├── App2_Student_Registration/                    # 5 Variations (v1 to v5)
    ├── App3_Item_Shopping/                           # 5 Variations (v1 to v5)
    ├── App4_User_Profile_Manager/                    # 5 Variations (v1 to v5)
    └── App5_MultiPage_Portal/                        # 5 Variations (v1 to v5)
```

---

## 📘 Contents Covered in the Handbook

### Part I: Complete Android Theory (Chapters 1 – 19)
- **Ch 1:** Introduction to Android, history, evolution, Android 1.0–17 timeline, Android Studio, AVD, Gradle, APK vs AAB, and SDK compilation rules.
- **Ch 2:** Android 5-Tier Architecture (Linux Kernel, HAL, Native Libraries, ART, Application Framework).
- **Ch 3:** Android Project Structure, file tree anatomy, R-class bridging (`setContentView` & `findViewById`).
- **Ch 4:** Android Resources, qualifiers, density units (`dp` vs `sp`), math conversion formula.
- **Ch 5 & 6:** Application Components (Activity, Service, Receiver, Provider) & `AndroidManifest.xml`.
- **Ch 7:** Activity Lifecycle State Machine, 7 core callbacks, loopback transitions, process death, Logcat logging.
- **Ch 8 & 9:** 21 UI Widgets & Layout Managers (`LinearLayout`, `RelativeLayout`, `ConstraintLayout`, `ScrollView`).
- **Ch 10:** View and ViewGroup Composite Tree Hierarchy.
- **Ch 11 & 12:** Event-driven programming, Explicit & Implicit Intents, Data passing via Extras Bundle.
- **Ch 13:** SharedPreferences API, persistent key-value storage, `apply()` vs `commit()`, session cleanup.
- **Ch 14:** Adapters and Collections (`ArrayAdapter`, `BaseAdapter`, view recycling, `AdapterView`).
- **Ch 15 & 16:** Storage options, SQLite/Room overview, Forms and defensive input validation.
- **Ch 17:** Menus (Options, Context, Popup), Dialogs (`AlertDialog`), and Notification Channels.
- **Ch 18 & 19:** Android security permissions model, Debugging techniques, and APK build process.

### Part II: Java Programming Fundamentals for Android
- Inheritance (`AppCompatActivity`), Interface listeners (`View.OnClickListener`), Collections (`ArrayList<E>`), and defensive exception handling (`try-catch`).

### Part III: 10 Original University Practical Programs (20MCA243)
Every program documented across **17 mandatory academic sections**:
1. Program 01: User Login Page with Validation & Toast Notifications (Page 17)
2. Program 02: Simple Calculator with Full Arithmetic Operations (Pages 20–26, 397 lines of code unabridged)
3. Program 03: Explicit Intent & Two-Activity Navigation (Pages 27–31, both Activities & layouts included)
4. Program 04: Activity Life Cycle Callbacks & Logcat Tracing (Pages 32–34)
5. Program 05: Selection Controls (CheckBox & RadioGroup) (Pages 35–37)
6. Program 06: Implicit Intents & System Integrations (CET Website, Dialer, Email, Maps, Share, SMS) (Pages 38–41)
7. Program 07: ListView & ArrayAdapter Implementation (Pages 42–43)
8. Program 08: ScrollView with Dynamic View Population (Pages 44–45)
9. Program 09: Dropdown Spinner & OnItemSelectedListener (Pages 46–48)
10. Program 10: SharedPreferences Persistent Key-Value Storage (Pages 49–52)

### Part IV & V: 5 Integrated Android Applications (25 Variations)
- **App 1:** Enterprise Authentication & Profile Manager (Variations 1.1 to 1.5, Page 53)
- **App 2:** Student Registration & Academic Profile System (Variations 2.1 to 2.5, Page 54)
- **App 3:** Item Selection & Shopping Cart Management (Variations 3.1 to 3.5, Page 55)
- **App 4:** User Registration & Profile Settings Manager (Variations 4.1 to 4.5, Page 56)
- **App 5:** Multi-Page University Portal & Utilities Hub (Variations 5.1 to 5.5, Page 57)

### Part VI & VII: Visual Learning Aids, Revision & Viva Voce
- 20 standalone technical vector SVG diagrams.
- Quick revision comparison matrices and attribute cheat sheets (Page 58).
- **30 High-Yield Viva Voce Examination Questions & Answers** (Pages 58–60).

---

## 🖨 Typesetting & Printing Specifications

- **Format:** A4 Portrait (`margin: 13mm 11mm 15mm 11mm`)
- **Typography:** Georgia (Academic Body, 9.5pt) & Consolas / JetBrains Mono (Code Listings, 8pt)
- **Layout:** Direct Start on Page 1 (No Table of Contents or Index), Single-Column Theory, Dedicated Full-Width Code Pages with dark slate header bars.
- **Total Pages:** Exactly **60 Pages** (Zero empty or orphaned pages).
