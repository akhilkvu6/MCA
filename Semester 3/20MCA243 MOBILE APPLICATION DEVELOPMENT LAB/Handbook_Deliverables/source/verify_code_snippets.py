import fitz
import os

pdf_path = os.path.join(os.path.dirname(__file__), "..", "Android_Programming_Handbook_Second_Edition.pdf")
doc = fitz.open(pdf_path)

full_text = ""
for page in doc:
    full_text += page.get_text() + "\n"

# Exact code snippets directly from the workspace projects
real_code_checks = [
    # Login (01_Login_Page)
    "package com.example.login_page;",
    "username = findViewById(R.id.username);",
    "username.setError(\"Enter username\");",
    "Toast.makeText(MainActivity.this, \"Login Successful\", Toast.LENGTH_SHORT).show();",
    
    # Calculator (02_Simple_Calculator)
    "package com.example.simple_calculator;",
    "firstNumber = currentText;",
    "b12.setOnClickListener(opListener);",
    "bac.setOnClickListener(new View.OnClickListener()",
    "double num1 = Double.parseDouble(firstNumber);",
    "android:id=\"@+id/t1\"",
    
    # Intent (03_Intent)
    "package com.example.intent;",
    "Intent intent = new Intent(MainActivity.this, MainActivity2.class);",
    "intent.putExtra(\"USER\", username);",
    "String username = getIntent().getStringExtra(\"USER\");",
    "welcomeText.setText(\"Welcome, \" + username",
    
    # Activity Lifecycle (04_Activity_Life_Cycle)
    "package com.example.activity_life_cycle;",
    "updateStatus(\"Created\");",
    "updateStatus(\"Restarted\");",
    "Log.d(TAG, state);",
    
    # Selection Controls (05_Checkbox_and_Radiobutton)
    "package com.example.checkbox_and_radiobutton;",
    "int selectedId = radioGroup.getCheckedRadioButtonId();",
    "result.append(\"Gender: Not Selected\\n\");",
    "Toast.makeText(MainActivity.this, \"Submitted Successfully\", Toast.LENGTH_SHORT).show();",
    
    # Implicit Intent (06_Implicit_Intent)
    "package com.example.implicit_intent;",
    "Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(\"https://www.cet.ac.in\"));",
    "Intent intent = new Intent(Intent.ACTION_DIAL, Uri.parse(\"tel:9876543210\"));",
    "Toast.makeText(MainActivity.this, \"Opening CET Website...\", Toast.LENGTH_SHORT).show();",
    
    # ListView (07_List_View)
    "package com.example.list_view;",
    "ArrayAdapter<String> adapter = new ArrayAdapter<>(",
    "Toast.makeText(MainActivity.this, \"Name Clicked: \" + arr[position], Toast.LENGTH_SHORT).show();",
    
    # ScrollView (08_Scroll_View)
    "package com.example.scroll_view;",
    "<ScrollView",
    
    # Spinner (09_Spinner)
    "package com.example.spinner;",
    "s.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener()",
    "t.setText(\"Selected Fruit: \" + selected);",
    
    # SharedPreferences (10_Shared_Preferences)
    "package com.example.shared_preferences;",
    "SharedPreferences sp = getSharedPreferences(PREF_NAME, MODE_PRIVATE);",
    "Toast.makeText(MainActivity.this, \"Data Saved Successfully\", Toast.LENGTH_SHORT).show();",
    "txtStatus.setText(\"Status: SharedPreferences cleared\");"
]

all_passed = True
clean_full = " ".join(full_text.split())

for check in real_code_checks:
    clean_check = " ".join(check.split())
    if clean_check in clean_full:
        print(f"[PASSED] Found workspace snippet: {check[:45]}...")
    else:
        print(f"[FAILED] MISSING workspace snippet: {check}!")
        all_passed = False

if all_passed:
    print(f"\nALL {len(real_code_checks)} REAL WORKSPACE CODE SNIPPETS 100% VERIFIED IN PDF!")
else:
    print("\nSOME WORKSPACE CODE SNIPPETS WERE NOT FOUND!")
