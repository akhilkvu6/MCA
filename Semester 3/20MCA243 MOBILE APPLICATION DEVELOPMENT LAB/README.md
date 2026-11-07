<div align="center">

# 📱 20MCA243 - Mobile Application Development Lab

### Master of Computer Applications (MCA) — Semester 3
**College of Engineering Trivandrum (CET)** | APJ Abdul Kalam Technological University (KTU)

<img src="https://img.shields.io/badge/Course-20MCA243-blue?style=for-the-badge">
<img src="https://img.shields.io/badge/Semester-3-purple?style=for-the-badge">
<img src="https://img.shields.io/badge/Lab%20Programs-10%2F10-brightgreen?style=for-the-badge">
<img src="https://img.shields.io/badge/Status-Complete-success?style=for-the-badge">

---

### 📖 Lab Record Experiments • Android Studio • Java & XML

</div>

---

## 📑 Index of Lab Experiments

| # | Program Name | Aim / Description | Key Components | Source Code |
|:---:|:---|:---|:---|:---:|
| **01** | [**Login Page**](./01_Login_Page) | Design a Login UI with username & password validation and Toast notifications | `LinearLayout`, `EditText`, `Button`, `Toast` | [`MainActivity.java`](./01_Login_Page/app/src/main/java/com/example/login_page/MainActivity.java) |
| **02** | [**Simple Calculator**](./02_Simple_Calculator) | Arithmetic calculator supporting Addition, Subtraction, Multiplication, and Division with crash guards | `LinearLayout`, `GridLayout`, `Button`, `EditText` | [`MainActivity.java`](./02_Simple_Calculator/app/src/main/java/com/example/simple_calculator/MainActivity.java) |
| **03** | [**Explicit Intent**](./03_Intent) | Two-activity navigation passing login data via `Intent.putExtra()` and returning via Logout | `Intent`, `Bundle`, `ConstraintLayout`, `TextView` | [`MainActivity.java`](./03_Intent/app/src/main/java/com/example/intent/MainActivity.java) |
| **04** | [**Activity Life Cycle**](./04_Activity_Life_Cycle) | Demonstrate all 7 Activity lifecycle callbacks using onscreen status, `Log.d`, and Toasts | `onCreate`, `onStart`, `onResume`, `onPause`, `onStop`, `onDestroy`, `onRestart` | [`MainActivity.java`](./04_Activity_Life_Cycle/app/src/main/java/com/example/activity_life_cycle/MainActivity.java) |
| **05** | [**Checkbox & Radiobutton**](./05_Checkbox_and_Radiobutton) | User registration form handling Single Selection (`RadioGroup`) and Multi-Selection (`CheckBox`) | `RadioGroup`, `RadioButton`, `CheckBox`, `Button` | [`MainActivity.java`](./05_Checkbox_and_Radiobutton/app/src/main/java/com/example/checkbox_and_radiobutton/MainActivity.java) |
| **06** | [**Implicit Intent**](./06_Implicit_Intent) | Trigger Android system applications (CET Website, Dialer, Email, Maps, Share Text, SMS) | `Intent.ACTION_VIEW`, `ACTION_DIAL`, `ACTION_SENDTO`, `ACTION_SEND` | [`MainActivity.java`](./06_Implicit_Intent/app/src/main/java/com/example/implicit_intent/MainActivity.java) |
| **07** | [**List View**](./07_List_View) | Display a collection of student names using `ArrayAdapter` and handle item selection | `ListView`, `ArrayAdapter<String>`, `OnItemClickListener` | [`MainActivity.java`](./07_List_View/app/src/main/java/com/example/list_view/MainActivity.java) |
| **08** | [**Scroll View**](./08_Scroll_View) | Create a vertically scrollable container dynamically loaded with 20+ view items | `ScrollView`, `LinearLayout`, Dynamic `TextView` generation | [`MainActivity.java`](./08_Scroll_View/app/src/main/java/com/example/scroll_view/MainActivity.java) |
| **09** | [**Spinner**](./09_Spinner) | Dropdown selection component with fruit list and live display via `OnItemSelectedListener` | `Spinner`, `ArrayAdapter<String>`, `OnItemSelectedListener` | [`MainActivity.java`](./09_Spinner/app/src/main/java/com/example/spinner/MainActivity.java) |
| **10** | [**Shared Preferences**](./10_Shared_Preferences) | Persistent key-value storage across application restarts (Write, Read, and Clear) | `SharedPreferences`, `SharedPreferences.Editor` | [`MainActivity.java`](./10_Shared_Preferences/app/src/main/java/com/example/shared_preferences/MainActivity.java) |

---

## 📂 Repository Structure

```text
20MCA243 MOBILE APPLICATION DEVELOPMENT LAB/
├── 01_Login_Page/                 # App 1: Login validation & Toasts
├── 02_Simple_Calculator/          # App 2: Arithmetic Calculator
├── 03_Intent/                     # App 3: Explicit Intent & Navigation
├── 04_Activity_Life_Cycle/        # App 4: Android Lifecycle callbacks
├── 05_Checkbox_and_Radiobutton/   # App 5: Selection controls (Radio & CheckBox)
├── 06_Implicit_Intent/            # App 6: System actions & Implicit Intents
├── 07_List_View/                  # App 7: ListView with ArrayAdapter
├── 08_Scroll_View/                # App 8: Vertical ScrollView
├── 09_Spinner/                    # App 9: Dropdown fruit Spinner
├── 10_Shared_Preferences/         # App 10: Persistent local storage
└── README.md                      # Lab documentation index
```

---

## 🛠 Prerequisites & Tools

- **IDE**: Android Studio (Koala / Ladybug or newer)
- **Programming Language**: Java 11 / Java 17
- **Target SDK**: Android 14 / Android 15 (API 34 / API 35+)
- **Minimum SDK**: API 24 (Android 7.0 Nougat)

---

## 🚀 How to Run in Android Studio

1. **Launch Android Studio**.
2. Click **File** > **Open...**
3. Browse to this directory and select any individual project folder (e.g. `01_Login_Page` or `10_Shared_Preferences`).
4. Wait for Gradle sync to complete.
5. Select an Android Virtual Device (AVD Emulator) or connect a physical device via USB debugging.
6. Click the green **Run (▶)** button or press `Shift + F10`.

---

<div align="center">

**MCA Semester 3 • 20MCA243 Mobile Application Development Lab**  
*College of Engineering Trivandrum (CET)*

</div>
