"""
Content Module: Part III - 10 Original University Practical Programs (20MCA243)
Second Edition: Dedicated Full-Width Code Pages, Dynamic Workspace Loading,
Complete 17 Academic Sections, and 3-Stage Predefined-Input-Dynamic Variations.
"""

import os
import html

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))

def read_workspace_file(proj_folder, rel_path):
    """Safely reads source code from the actual workspace project and returns escaped HTML."""
    full_path = os.path.join(WORKSPACE_ROOT, proj_folder, rel_path)
    if not os.path.exists(full_path):
        return f"<!-- File not found: {full_path} -->"
    with open(full_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    return html.escape(content)

def make_code_card(title, file_rel_path, content):
    """Generates a dedicated full-width code block with a prominent dark slate header bar."""
    return f'''
<div class="full-code-container">
    <div class="code-file-header">
        <span class="file-icon">&#128196;</span> {title} &mdash; <code>{file_rel_path}</code>
    </div>
    <pre class="full-code-block"><code>{content}</code></pre>
</div>
'''

def get_practicals_html():
    p1_xml = read_workspace_file("01_Login_Page", "app/src/main/res/layout/activity_main.xml")
    p1_java = read_workspace_file("01_Login_Page", "app/src/main/java/com/example/login_page/MainActivity.java")

    p2_xml = read_workspace_file("02_Simple_Calculator", "app/src/main/res/layout/activity_main.xml")
    p2_java = read_workspace_file("02_Simple_Calculator", "app/src/main/java/com/example/simple_calculator/MainActivity.java")

    p3_xml1 = read_workspace_file("03_Intent", "app/src/main/res/layout/activity_main.xml")
    p3_java1 = read_workspace_file("03_Intent", "app/src/main/java/com/example/intent/MainActivity.java")
    p3_xml2 = read_workspace_file("03_Intent", "app/src/main/res/layout/activity_main2.xml")
    p3_java2 = read_workspace_file("03_Intent", "app/src/main/java/com/example/intent/MainActivity2.java")

    p4_xml = read_workspace_file("04_Activity_Life_Cycle", "app/src/main/res/layout/activity_main.xml")
    p4_java = read_workspace_file("04_Activity_Life_Cycle", "app/src/main/java/com/example/activity_life_cycle/MainActivity.java")

    p5_xml = read_workspace_file("05_Checkbox_and_Radiobutton", "app/src/main/res/layout/activity_main.xml")
    p5_java = read_workspace_file("05_Checkbox_and_Radiobutton", "app/src/main/java/com/example/checkbox_and_radiobutton/MainActivity.java")

    p6_xml = read_workspace_file("06_Implicit_Intent", "app/src/main/res/layout/activity_main.xml")
    p6_java = read_workspace_file("06_Implicit_Intent", "app/src/main/java/com/example/implicit_intent/MainActivity.java")

    p7_xml = read_workspace_file("07_List_View", "app/src/main/res/layout/activity_main.xml")
    p7_java = read_workspace_file("07_List_View", "app/src/main/java/com/example/list_view/MainActivity.java")

    p8_xml = read_workspace_file("08_Scroll_View", "app/src/main/res/layout/activity_main.xml")
    p8_java = read_workspace_file("08_Scroll_View", "app/src/main/java/com/example/scroll_view/MainActivity.java")

    p9_xml = read_workspace_file("09_Spinner", "app/src/main/res/layout/activity_main.xml")
    p9_java = read_workspace_file("09_Spinner", "app/src/main/java/com/example/spinner/MainActivity.java")

    p10_xml = read_workspace_file("10_Shared_Preferences", "app/src/main/res/layout/activity_main.xml")
    p10_java = read_workspace_file("10_Shared_Preferences", "app/src/main/java/com/example/shared_preferences/MainActivity.java")

    return f'''
<!-- ============================================================== -->
<!-- PROGRAM 01: USER LOGIN PAGE WITH VALIDATION & TOAST           -->
<!-- ============================================================== -->
<div class="chapter-break"></div>
<div class="chapter-header">
    <div class="part-tag">PART III | 10 ORIGINAL UNIVERSITY PRACTICAL PROGRAMS (20MCA243)</div>
    <h2 class="chapter-title">PROGRAM 01: USER LOGIN PAGE WITH VALIDATION &amp; TOAST NOTIFICATIONS</h2>
</div>

<h3>1. Aim</h3>
<p>To design an interactive user authentication screen using <code>LinearLayout</code>, capture user credentials via <code>EditText</code>, perform defensive input validation with visual error badges (<code>setError()</code>), and provide immediate transient feedback using Android <code>Toast</code> notifications.</p>

<h3>2. Theoretical Principles</h3>
<p>User authentication interfaces require structured vertical stacking of form controls and defensive client-side validation. In Android, <code>LinearLayout</code> coordinates children along a single vertical axis. Input strings extracted via <code>getText().toString().trim()</code> are validated against emptiness and credential requirements. When validation fails, <code>setError()</code> anchors a warning popup to the offending widget. Upon successful authentication, <code>Toast.makeText().show()</code> displays a floating message that automatically dismisses without disrupting the underlying Activity lifecycle.</p>

<h3>3. Components &amp; APIs Used</h3>
<ul>
    <li><strong>Layout Container:</strong> <code>LinearLayout</code> (vertical orientation, centered gravity, 30dp padding).</li>
    <li><strong>Widgets:</strong> <code>TextView</code> (header), <code>EditText</code> (username), <code>EditText</code> (password with <code>android:inputType="textPassword"</code>), <code>Button</code> (login trigger).</li>
    <li><strong>Core APIs:</strong> <code>setContentView()</code>, <code>findViewById()</code>, <code>setOnClickListener()</code>, <code>getText().toString().trim()</code>, <code>isEmpty()</code>, <code>setError()</code>, <code>Toast.makeText(..., Toast.LENGTH_SHORT).show()</code>.</li>
</ul>

<h3>4. Program Algorithm</h3>
<ol class="algo-list">
    <li><strong>Step 1:</strong> Launch the Activity and inflate <code>activity_main.xml</code> via <code>setContentView()</code> in <code>onCreate()</code>.</li>
    <li><strong>Step 2:</strong> Bind Java widget references (<code>username</code>, <code>password</code>, <code>login</code>) using <code>findViewById()</code>.</li>
    <li><strong>Step 3:</strong> Attach an asynchronous <code>View.OnClickListener</code> to the login button.</li>
    <li><strong>Step 4:</strong> In <code>onClick()</code>, extract string contents: <code>user = username.getText().toString().trim()</code> and <code>pass = password.getText().toString()</code>.</li>
    <li><strong>Step 5:</strong> If <code>user.isEmpty()</code>, execute <code>username.setError("Enter username")</code> and return.</li>
    <li><strong>Step 6:</strong> If <code>pass.isEmpty()</code>, execute <code>password.setError("Enter password")</code> and return.</li>
    <li><strong>Step 7:</strong> Compare credentials against authorized pairs (e.g. <code>admin/1234</code> or <code>akhil/akhil@123</code>).</li>
    <li><strong>Step 8:</strong> If matching, display <code>Toast.makeText(..., "Login Successful", Toast.LENGTH_SHORT).show()</code>; otherwise show <code>"Invalid credentials"</code>.</li>
</ol>

<div class="diagram-container">
    <img src="diagrams/16_login_flowchart.svg" alt="Login Flowchart" class="diagram-img" style="max-height: 220px;" />
    <div class="diagram-caption">Figure P1.1: Program 01 Logic Flowchart.</div>
</div>

<!-- DEDICATED FULL-WIDTH CODE PAGES -->

<!-- Continuous Natural Flow -->

{make_code_card("XML Layout Implementation", "01_Login_Page/app/src/main/res/layout/activity_main.xml", p1_xml)}
{make_code_card("Java Source Code Implementation", "01_Login_Page/app/src/main/java/com/example/login_page/MainActivity.java", p1_java)}

<!-- DETAILED WALKTHROUGH & EXAMINATION REVIEW -->

<!-- Continuous Natural Flow -->

<h3>5. Detailed Code Walkthrough</h3>
<ul>
    <li><strong>Lines 21–23:</strong> <code>findViewById()</code> resolves the R-class integer tokens (<code>R.id.username</code>, <code>R.id.password</code>, <code>R.id.login</code>) to concrete in-memory view instances created by AAPT2.</li>
    <li><strong>Line 25:</strong> <code>login.setOnClickListener(...)</code> registers an anonymous inner class implementing <code>View.OnClickListener</code>. The framework dispatches touch events to <code>onClick(View view)</code> on the Main UI Thread.</li>
    <li><strong>Lines 29–30:</strong> <code>username.getText().toString().trim()</code> safely extracts user input, converting the editable buffer to an immutable String and stripping extraneous whitespace.</li>
    <li><strong>Lines 32–35:</strong> Defensive guards check <code>isEmpty()</code>. If blank, <code>setError()</code> displays an inline warning badge and pops a focus indicator.</li>
    <li><strong>Lines 36–41:</strong> <code>user.equalsIgnoreCase(...)</code> performs case-insensitive username comparison combined with strict case-sensitive password verification, triggering appropriate Toast messages.</li>
</ul>

<h3>6. Practical Variations (Predefined &rarr; User Input &rarr; Dynamic State)</h3>
<ul>
    <li><strong>Variation 1.1 (Predefined Credentials Check):</strong> Directly validating against static constants inside the Java file (as implemented above).</li>
    <li><strong>Variation 1.2 (Dynamic Length &amp; Character Validation):</strong> Enhancing validation to enforce a minimum 8-character password constraint:
        <pre><code>if (pass.length() &lt; 8) {{ password.setError("Password must be at least 8 characters"); return; }}</code></pre>
    </li>
    <li><strong>Variation 1.3 (Dynamic Credential Registration):</strong> Storing newly registered users dynamically into a collection (<code>HashMap&lt;String, String&gt;</code>) so newly registered accounts can authenticate immediately at runtime.</li>
</ul>

<h3>7. Common Mistakes &amp; Viva Focus Points</h3>
<div class="box box-mistake">
    <div class="box-title">COMMON MISTAKE | Forgetting .show() on Toast</div>
    <p>Writing <code>Toast.makeText(this, "Success", Toast.LENGTH_SHORT);</code> creates the Toast object in memory but fails to display it on screen. Calling <code>.show()</code> is mandatory to register the toast with the system NotificationManager service.</p>
</div>
<div class="box box-exam-tip">
    <div class="box-title">VIVA FOCUS | android:inputType="textPassword"</div>
    <p>Setting <code>inputType="textPassword"</code> masks keystrokes with dots and disables dictionary word suggestions, clipboard history previews, and third-party keyboard telemetry for security.</p>
</div>

<!-- ============================================================== -->
<!-- PROGRAM 02: SIMPLE CALCULATOR WITH ARITHMETIC OPERATIONS       -->
<!-- ============================================================== -->
<div class="chapter-break"></div>
<div class="chapter-header">
    <div class="part-tag">PART III | 10 ORIGINAL UNIVERSITY PRACTICAL PROGRAMS (20MCA243)</div>
    <h2 class="chapter-title">PROGRAM 02: SIMPLE CALCULATOR WITH ARITHMETIC OPERATIONS</h2>
</div>

<h3>1. Aim</h3>
<p>To implement a full-featured arithmetic calculator application in Android using nested horizontal and vertical <code>LinearLayout</code> containers, capturing numeric input through an interactive grid of buttons, handling four basic arithmetic operations (+, -, *, /), and performing defensive division-by-zero checks.</p>

<h3>2. Theoretical Principles</h3>
<p>A responsive calculator UI requires proportional distribution of buttons across the screen. This is achieved using nested <code>LinearLayout</code> containers with <code>android:layout_weight="1"</code> and <code>android:layout_width="0dp"</code> / <code>android:layout_height="0dp"</code>. The calculator state machine maintains two double-precision operands and an active operator symbol (+, -, *, /). Defensive checks catch empty operand entries and prevent runtime <code>ArithmeticException</code> or <code>Infinity</code> values when dividing by zero.</p>

<h3>3. Components &amp; APIs Used</h3>
<ul>
    <li><strong>Layout:</strong> Root vertical <code>LinearLayout</code> hosting an <code>EditText</code> display and 5 nested horizontal <code>LinearLayout</code> button rows.</li>
    <li><strong>Widgets:</strong> <code>EditText</code> (input/output screen with <code>inputType="numberDecimal"</code>), 16 numeric and operational <code>Button</code> controls (0-9, ., +, -, *, /, =, C).</li>
    <li><strong>Core APIs:</strong> <code>Double.parseDouble()</code>, <code>String.valueOf()</code>, <code>setText()</code>, <code>setSelection()</code>, <code>setError()</code>, <code>Toast.makeText()</code>.</li>
</ul>

<h3>4. Program Algorithm</h3>
<ol class="algo-list">
    <li><strong>Step 1:</strong> Inflate <code>activity_main.xml</code> in <code>onCreate()</code> and bind references to the display <code>EditText (t1)</code> and all 16 buttons.</li>
    <li><strong>Step 2:</strong> Attach click listeners to digit buttons (0–9) that append their respective characters to the display string.</li>
    <li><strong>Step 3:</strong> When an operator button (+, -, *, /) is clicked, parse the current display text into <code>firstOperand</code>, record the operator character, and clear the display for the next number.</li>
    <li><strong>Step 4:</strong> When the equals button (=) is clicked, parse the current display text into <code>secondOperand</code>.</li>
    <li><strong>Step 5:</strong> Evaluate the operation using a <code>switch-case</code> structure. If the operator is division (/) and <code>secondOperand == 0</code>, display an error Toast ("Cannot divide by zero!").</li>
    <li><strong>Step 6:</strong> Render the calculated result back to the display <code>EditText</code>. When Clear (C) is pressed, reset all operands and clear the display.</li>
</ol>

<div class="diagram-container">
    <img src="diagrams/07_layout_hierarchy.svg" alt="Layout Hierarchy" class="diagram-img" style="max-height: 200px;" />
    <div class="diagram-caption">Figure P2.1: Proportional Layout Weight Architecture in Calculator Grid.</div>
</div>

<!-- DEDICATED FULL-WIDTH CODE PAGES -->

<!-- Continuous Natural Flow -->

{make_code_card("Complete XML Layout Source Code (228 Lines)", "02_Simple_Calculator/app/src/main/res/layout/activity_main.xml", p2_xml)}


<!-- Continuous Natural Flow -->

{make_code_card("Complete Java Source Code (169 Lines)", "02_Simple_Calculator/app/src/main/java/com/example/simple_calculator/MainActivity.java", p2_java)}

<!-- DETAILED WALKTHROUGH & EXAMINATION REVIEW -->

<!-- Continuous Natural Flow -->

<h3>5. Detailed Code Walkthrough</h3>
<ul>
    <li><strong>XML Grid Layout:</strong> The display <code>EditText</code> is assigned <code>android:layout_weight="2"</code>, allocating double the vertical proportion compared to each button row (<code>weight="1"</code>). Within each row, buttons specify <code>android:layout_width="0dp"</code> and <code>android:layout_weight="1"</code>, guaranteeing exactly 25% horizontal width for each of the 4 columns across all screen sizes.</li>
    <li><strong>Numeric Input Handling:</strong> Each numeric button appends its character to <code>t1.getText()</code> and positions the cursor at the end via <code>t1.setSelection(t1.getText().length())</code>.</li>
    <li><strong>Operator Processing:</strong> When an operation button is pressed, the text is converted into a <code>double</code> via <code>Double.parseDouble(t1.getText().toString())</code> and stored in <code>firstNum</code>. The active operator (+, -, *, /) is saved in a <code>char</code> variable.</li>
    <li><strong>Defensive Division Guard:</strong> Before computing division, the code explicitly verifies <code>if (secondNum == 0)</code> to prevent displaying <code>Infinity</code> or NaN, notifying the user via a Toast.</li>
</ul>

<h3>6. Practical Variations</h3>
<ul>
    <li><strong>Variation 2.1 (Two Independent EditText Operands):</strong> Rather than a single sequential display, provide two distinct <code>EditText</code> inputs (Operand 1 and Operand 2) with 4 calculation buttons.</li>
    <li><strong>Variation 2.2 (Scientific Math Extension):</strong> Incorporating <code>Math.sqrt()</code>, <code>Math.pow()</code>, and percentage calculations.</li>
    <li><strong>Variation 2.3 (Calculation History Log):</strong> Storing previous calculation strings in an <code>ArrayList&lt;String&gt;</code> and displaying them in a popup dialog or secondary Activity.</li>
</ul>

<h3>7. Common Mistakes &amp; Viva Focus Points</h3>
<div class="box box-mistake">
    <div class="box-title">COMMON MISTAKE | Double.parseDouble() on Empty String</div>
    <p>Invoking <code>Double.parseDouble("")</code> when the user taps an operator button before entering numbers throws an unhandled <code>NumberFormatException</code>, crashing the app. Always check <code>t1.getText().toString().isEmpty()</code> first.</p>
</div>
<div class="box box-exam-tip">
    <div class="box-title">VIVA FOCUS | android:layout_width="0dp" with layout_weight</div>
    <p>Setting <code>width="0dp"</code> bypasses the initial measuring pass by the parent LinearLayout. The layout engine calculates dimensions strictly based on the assigned weight ratio, improving UI rendering performance.</p>
</div>

<!-- ============================================================== -->
<!-- PROGRAM 03: EXPLICIT INTENT & TWO-ACTIVITY NAVIGATION          -->
<!-- ============================================================== -->
<div class="chapter-break"></div>
<div class="chapter-header">
    <div class="part-tag">PART III | 10 ORIGINAL UNIVERSITY PRACTICAL PROGRAMS (20MCA243)</div>
    <h2 class="chapter-title">PROGRAM 03: EXPLICIT INTENT &amp; TWO-ACTIVITY NAVIGATION</h2>
</div>

<h3>1. Aim</h3>
<p>To implement screen-to-screen navigation between two Activities using an <strong>Explicit Intent</strong>, transferring user credentials from <code>MainActivity</code> to <code>MainActivity2</code> (Homepage) via an Intent Extras <code>Bundle</code>, and providing a Logout mechanism to terminate the session.</p>

<h3>2. Theoretical Principles</h3>
<p>An <strong>Explicit Intent</strong> explicitly specifies the target component class (e.g., <code>new Intent(this, MainActivity2.class)</code>). Data is transferred across process boundaries by bundling key-value pairs into the Intent using <code>putExtra(key, value)</code>. In the destination Activity, <code>getIntent().getStringExtra(key)</code> extracts the payload. Calling <code>finish()</code> pops the secondary Activity off the back-stack, returning the user to the caller.</p>

<h3>3. Components &amp; APIs Used</h3>
<ul>
    <li><strong>Components:</strong> <code>MainActivity</code> (Login screen), <code>MainActivity2</code> (Home dashboard screen).</li>
    <li><strong>Manifest Declarations:</strong> Both Activities registered in <code>AndroidManifest.xml</code>.</li>
    <li><strong>Core APIs:</strong> <code>Intent</code>, <code>putExtra()</code>, <code>getIntent()</code>, <code>getStringExtra()</code>, <code>startActivity()</code>, <code>finish()</code>.</li>
</ul>

<h3>4. Program Algorithm</h3>
<ol class="algo-list">
    <li><strong>Step 1:</strong> In <code>MainActivity</code>, collect username and password from <code>EditText</code> controls upon button click.</li>
    <li><strong>Step 2:</strong> Validate inputs. If credentials match, instantiate an Explicit Intent targeting <code>MainActivity2.class</code>.</li>
    <li><strong>Step 3:</strong> Attach user data: <code>intent.putExtra("username", user);</code> and invoke <code>startActivity(intent);</code>.</li>
    <li><strong>Step 4:</strong> In <code>MainActivity2.onCreate()</code>, extract the bundle: <code>String user = getIntent().getStringExtra("username");</code>.</li>
    <li><strong>Step 5:</strong> Render the welcome banner on a <code>TextView</code>: <code>"Welcome, " + user</code>.</li>
    <li><strong>Step 6:</strong> When the user clicks the "Logout" button in <code>MainActivity2</code>, invoke <code>finish();</code> to return to the login screen.</li>
</ol>

<div class="diagram-container">
    <img src="diagrams/08_explicit_intent.svg" alt="Explicit Intent" class="diagram-img" style="max-height: 200px;" />
    <div class="diagram-caption">Figure P3.1: Explicit Intent Navigation and Bundle Transfer.</div>
</div>

<!-- DEDICATED FULL-WIDTH CODE PAGES -->

<!-- Continuous Natural Flow -->

{make_code_card("MainActivity XML Layout", "03_Intent/app/src/main/res/layout/activity_main.xml", p3_xml1)}
{make_code_card("MainActivity Java Source Code", "03_Intent/app/src/main/java/com/example/intent/MainActivity.java", p3_java1)}


<!-- Continuous Natural Flow -->

{make_code_card("MainActivity2 XML Layout (Homepage)", "03_Intent/app/src/main/res/layout/activity_main2.xml", p3_xml2)}
{make_code_card("MainActivity2 Java Source Code (Homepage)", "03_Intent/app/src/main/java/com/example/intent/MainActivity2.java", p3_java2)}

<!-- DETAILED WALKTHROUGH & EXAMINATION REVIEW -->

<!-- Continuous Natural Flow -->

<h3>5. Detailed Code Walkthrough</h3>
<ul>
    <li><strong>Navigation Initiation:</strong> <code>Intent intent = new Intent(MainActivity.this, MainActivity2.class);</code> explicitly couples the source context to the target class token.</li>
    <li><strong>Data Transport:</strong> <code>intent.putExtra("username", user);</code> packs the string into an internal IPC parcelable map.</li>
    <li><strong>Data Retrieval:</strong> In <code>MainActivity2</code>, <code>getIntent().getStringExtra("username")</code> queries the incoming intent. If no key matches, it safely returns <code>null</code>.</li>
    <li><strong>Session Termination:</strong> In <code>MainActivity2</code>, the logout button triggers <code>finish()</code>, popping <code>MainActivity2</code> from the task stack and cleanly revealing <code>MainActivity</code> beneath it.</li>
</ul>

<h3>6. Practical Variations</h3>
<ul>
    <li><strong>Variation 3.1 (Multi-Field Bundle Passing):</strong> Packaging multiple fields (Email, Phone, Role) inside a standalone <code>Bundle</code> object:
        <pre><code>Bundle b = new Bundle(); b.putString("U", u); b.putInt("AGE", 22); intent.putExtras(b);</code></pre>
    </li>
    <li><strong>Variation 3.2 (ActivityResultLauncher Navigation):</strong> Using modern <code>registerForActivityResult</code> to launch a child activity and receive return data back.</li>
    <li><strong>Variation 3.3 (Clear Task Backstack):</strong> Applying <code>FLAG_ACTIVITY_NEW_TASK | FLAG_ACTIVITY_CLEAR_TASK</code> on logout to completely prevent returning to the dashboard via the device Back button.</li>
</ul>

<!-- ============================================================== -->
<!-- PROGRAM 04: ACTIVITY LIFE CYCLE CALLBACKS & LOGCAT             -->
<!-- ============================================================== -->
<div class="chapter-break"></div>
<div class="chapter-header">
    <div class="part-tag">PART III | 10 ORIGINAL UNIVERSITY PRACTICAL PROGRAMS (20MCA243)</div>
    <h2 class="chapter-title">PROGRAM 04: ACTIVITY LIFE CYCLE CALLBACKS &amp; LOGCAT TRACING</h2>
</div>

<h3>1. Aim</h3>
<p>To demonstrate and observe the complete Android Activity lifecycle callback progression (<code>onCreate</code>, <code>onStart</code>, <code>onResume</code>, <code>onPause</code>, <code>onStop</code>, <code>onDestroy</code>, <code>onRestart</code>) through synchronized <code>Toast</code> popups and system <code>Logcat</code> messages.</p>

<h3>2. Theoretical Principles</h3>
<p>The Android operating system governs Activity lifecycles via an event-driven state machine. When an Activity transitions between states, the framework invokes corresponding callback methods. Observing these callbacks in Logcat provides insight into application initialization, resource management during interruptions (e.g. incoming calls), and memory cleanup when navigating away.</p>

<h3>3. Components &amp; APIs Used</h3>
<ul>
    <li><strong>Callbacks:</strong> <code>onCreate()</code>, <code>onStart()</code>, <code>onResume()</code>, <code>onPause()</code>, <code>onStop()</code>, <code>onRestart()</code>, <code>onDestroy()</code>.</li>
    <li><strong>Core APIs:</strong> <code>Log.d(TAG, message)</code>, <code>Toast.makeText().show()</code>, <code>super.onCallback()</code>.</li>
</ul>

<div class="diagram-container">
    <img src="diagrams/05_activity_lifecycle.svg" alt="Activity Lifecycle" class="diagram-img" style="max-height: 200px;" />
    <div class="diagram-caption">Figure P4.1: Activity Lifecycle Callback Transitions.</div>
</div>

<!-- DEDICATED FULL-WIDTH CODE PAGES -->

<!-- Continuous Natural Flow -->

{make_code_card("XML Layout Source Code", "04_Activity_Life_Cycle/app/src/main/res/layout/activity_main.xml", p4_xml)}
{make_code_card("Java Source Code Implementation", "04_Activity_Life_Cycle/app/src/main/java/com/example/activity_life_cycle/MainActivity.java", p4_java)}

<!-- DETAILED WALKTHROUGH & EXAMINATION REVIEW -->

<!-- Continuous Natural Flow -->

<h3>4. Detailed Code Walkthrough</h3>
<ul>
    <li><strong>Callback Sequence at App Launch:</strong> <code>onCreate() &rarr; onStart() &rarr; onResume()</code>. The Activity is now in the active, foreground running state.</li>
    <li><strong>Pressing Home Button:</strong> <code>onPause() &rarr; onStop()</code>. The Activity is hidden and pushed to the background stack.</li>
    <li><strong>Returning from Background:</strong> <code>onRestart() &rarr; onStart() &rarr; onResume()</code>. The Activity resumes interactive operation without executing <code>onCreate()</code> again.</li>
    <li><strong>Screen Orientation Change:</strong> <code>onPause() &rarr; onStop() &rarr; onDestroy() &rarr; onCreate() &rarr; onStart() &rarr; onResume()</code>. The OS destroys and completely recreates the Activity to reload resources for the new configuration!</li>
</ul>

<h3>5. Practical Variations</h3>
<ul>
    <li><strong>Variation 4.1 (State Preservation via onSaveInstanceState):</strong> Saving counters or draft text across screen rotations:
        <pre><code>@Override protected void onSaveInstanceState(Bundle out) {{ super.onSaveInstanceState(out); out.putInt("COUNT", count); }}</code></pre>
    </li>
    <li><strong>Variation 4.2 (On-Screen Event History Log):</strong> Appending each lifecycle transition string into a dynamic <code>TextView</code> or <code>ListView</code>.</li>
    <li><strong>Variation 4.3 (Sensor &amp; Camera Lifecycle Management):</strong> Registering a sensor listener in <code>onResume()</code> and unregistering it in <code>onPause()</code> to conserve battery.</li>
</ul>

<!-- ============================================================== -->
<!-- PROGRAM 05: SELECTION CONTROLS (CHECKBOX & RADIOGROUP)         -->
<!-- ============================================================== -->
<div class="chapter-break"></div>
<div class="chapter-header">
    <div class="part-tag">PART III | 10 ORIGINAL UNIVERSITY PRACTICAL PROGRAMS (20MCA243)</div>
    <h2 class="chapter-title">PROGRAM 05: SELECTION CONTROLS (CHECKBOX &amp; RADIOGROUP)</h2>
</div>

<h3>1. Aim</h3>
<p>To design an interactive student survey screen using selection controls: single-choice mutually exclusive gender selection using <code>RadioGroup</code> / <code>RadioButton</code>, and multiple-choice language proficiency selection using independent <code>CheckBox</code> controls.</p>

<h3>2. Theoretical Principles</h3>
<p>Selection controls capture discrete categorical choices. A <code>RadioGroup</code> acts as a ViewGroup container enforcing mutual exclusion: checking one <code>RadioButton</code> automatically deselects all others. Its selected state is queried via <code>getCheckedRadioButtonId()</code>. In contrast, <code>CheckBox</code> controls operate independently, allowing any combination of zero, one, or multiple selections, evaluated individually using <code>isChecked()</code>.</p>

<!-- DEDICATED FULL-WIDTH CODE PAGES -->

<!-- Continuous Natural Flow -->

{make_code_card("XML Layout Implementation", "05_Checkbox_and_Radiobutton/app/src/main/res/layout/activity_main.xml", p5_xml)}
{make_code_card("Java Source Code Implementation", "05_Checkbox_and_Radiobutton/app/src/main/java/com/example/checkbox_and_radiobutton/MainActivity.java", p5_java)}

<!-- DETAILED WALKTHROUGH & EXAMINATION REVIEW -->

<!-- Continuous Natural Flow -->

<h3>3. Detailed Code Walkthrough</h3>
<ul>
    <li><strong>Single-Choice Gender Evaluation:</strong> <code>int selectedId = radioGroup.getCheckedRadioButtonId();</code> retrieves the ID of the selected button. If valid, <code>findViewById(selectedId).getText()</code> extracts the chosen gender label.</li>
    <li><strong>Multi-Choice CheckBox Accumulation:</strong> Using a <code>StringBuilder</code>, each <code>CheckBox</code> is checked via <code>isChecked()</code>. If true, its label is appended.</li>
    <li><strong>Validation:</strong> If no radio button is selected (<code>selectedId == -1</code>), the app prompts the user to select their gender before submitting.</li>
</ul>

<h3>4. Practical Variations (Predefined &rarr; User Input &rarr; Dynamic State)</h3>
<ul>
    <li><strong>Variation 5.1 (Static Form Submission):</strong> As implemented, collecting choices on button click.</li>
    <li><strong>Variation 5.2 (Real-Time Reactive Toggling):</strong> Using <code>setOnCheckedChangeListener</code> on checkboxes to update an on-screen preview dynamically without needing a submit button.</li>
    <li><strong>Variation 5.3 (Dynamic Options Ingestion):</strong> Inflating RadioButtons and CheckBoxes dynamically at runtime from a database or array of strings.</li>
</ul>

<!-- ============================================================== -->
<!-- PROGRAM 06: IMPLICIT INTENT & SYSTEM ACTIONS                  -->
<!-- ============================================================== -->
<div class="chapter-break"></div>
<div class="chapter-header">
    <div class="part-tag">PART III | 10 ORIGINAL UNIVERSITY PRACTICAL PROGRAMS (20MCA243)</div>
    <h2 class="chapter-title">PROGRAM 06: IMPLICIT INTENTS &amp; SYSTEM INTEGRATIONS</h2>
</div>

<h3>1. Aim</h3>
<p>To demonstrate the execution of <strong>Implicit Intents</strong> in Android by launching external system applications: opening an institution website (<code>ACTION_VIEW</code> to CET website), dialing telephone numbers (<code>ACTION_DIAL</code>), dispatching emails (<code>ACTION_SENDTO</code>), and launching maps.</p>

<h3>2. Theoretical Principles</h3>
<p>An <strong>Implicit Intent</strong> specifies an abstract action and a standardized data URI rather than a destination class. The Android OS <code>PackageManager</code> inspects all installed apps' <code>&lt;intent-filter&gt;</code> declarations to determine compatible targets. If multiple apps match, the OS presents a system disambiguation dialog (chooser).</p>

<div class="diagram-container">
    <img src="diagrams/09_implicit_intent.svg" alt="Implicit Intent" class="diagram-img" style="max-height: 200px;" />
    <div class="diagram-caption">Figure P6.1: Implicit Intent Resolution Mechanism.</div>
</div>

<!-- DEDICATED FULL-WIDTH CODE PAGES -->

<!-- Continuous Natural Flow -->

{make_code_card("XML Layout Implementation", "06_Implicit_Intent/app/src/main/res/layout/activity_main.xml", p6_xml)}
{make_code_card("Java Source Code Implementation", "06_Implicit_Intent/app/src/main/java/com/example/implicit_intent/MainActivity.java", p6_java)}

<!-- DETAILED WALKTHROUGH & EXAMINATION REVIEW -->

<!-- Continuous Natural Flow -->

<h3>3. Detailed Code Walkthrough</h3>
<ul>
    <li><strong>Browser Launch:</strong> <code>new Intent(Intent.ACTION_VIEW, Uri.parse("https://cet.ac.in"))</code> opens the URL in Chrome or default browser.</li>
    <li><strong>Phone Dialer:</strong> <code>new Intent(Intent.ACTION_DIAL, Uri.parse("tel:9876543210"))</code> pre-fills the dialer pad without requiring dangerous call permissions.</li>
    <li><strong>Defensive Handling:</strong> All implicit calls are wrapped in <code>try-catch (ActivityNotFoundException e)</code> to guard against devices lacking matching handlers (e.g., tablets with no telephony dialer).</li>
</ul>

<!-- ============================================================== -->
<!-- PROGRAM 07: LISTVIEW & ARRAYADAPTER IMPLEMENTATION            -->
<!-- ============================================================== -->
<div class="chapter-break"></div>
<div class="chapter-header">
    <div class="part-tag">PART III | 10 ORIGINAL UNIVERSITY PRACTICAL PROGRAMS (20MCA243)</div>
    <h2 class="chapter-title">PROGRAM 07: LISTVIEW &amp; ARRAYADAPTER IMPLEMENTATION</h2>
</div>

<h3>1. Aim</h3>
<p>To populate an Android <code>ListView</code> with a collection of academic course elements using an <code>ArrayAdapter&lt;String&gt;</code>, recycle list row views, and handle item selection events using <code>OnItemClickListener</code>.</p>

<h3>2. Theoretical Principles</h3>
<p>An <code>AdapterView</code> displays repetitive collection data using the Adapter structural pattern. An <code>ArrayAdapter</code> binds an in-memory array or <code>ArrayList</code> to individual row layouts (e.g. <code>android.R.layout.simple_list_item_1</code>). Item click events are captured via <code>OnItemClickListener</code>, providing the clicked position index and row ID.</p>

<div class="diagram-container">
    <img src="diagrams/13_listview_adapter.svg" alt="ListView Adapter" class="diagram-img" style="max-height: 200px;" />
    <div class="diagram-caption">Figure P7.1: Adapter Bridge between Java Collections and AdapterView rows.</div>
</div>

<!-- DEDICATED FULL-WIDTH CODE PAGES -->

<!-- Continuous Natural Flow -->

{make_code_card("XML Layout Implementation", "07_List_View/app/src/main/res/layout/activity_main.xml", p7_xml)}
{make_code_card("Java Source Code Implementation", "07_List_View/app/src/main/java/com/example/list_view/MainActivity.java", p7_java)}

<!-- DETAILED WALKTHROUGH & EXAMINATION REVIEW -->

<!-- Continuous Natural Flow -->

<h3>3. Dynamic Data Variation (Predefined &rarr; User Input &rarr; Dynamic State)</h3>
<p>In standard university practicals, a predefined static array is used. Here is the progressive 3-stage dynamic variation:</p>
<div class="box box-example">
    <div class="box-title">3-STAGE DYNAMIC DATA | USER-ENTERED ITEMS IN LISTVIEW</div>
    <pre><code>// Stage 1: Dynamic ArrayList Collection
ArrayList&lt;String&gt; courseList = new ArrayList&lt;&gt;();
courseList.add("MCA - Mobile App Development");
courseList.add("M.Tech - Cloud Computing");

ArrayAdapter&lt;String&gt; adapter = new ArrayAdapter&lt;&gt;(this, 
    android.R.layout.simple_list_item_1, courseList);
listView.setAdapter(adapter);

// Stage 2 &amp; 3: Capturing User Input and Dynamically Updating View
btnAdd.setOnClickListener(new View.OnClickListener() {{
    String newItem = etInput.getText().toString().trim();
    if (!newItem.isEmpty()) {{
        courseList.add(newItem);               // Add to collection
        adapter.notifyDataSetChanged();        // Notify adapter to re-render!
        etInput.setText("");                   // Clear input box
    }}
}});</code></pre>
</div>

<!-- ============================================================== -->
<!-- PROGRAM 08: SCROLLVIEW WITH DYNAMIC VIEW POPULATION           -->
<!-- ============================================================== -->
<div class="chapter-break"></div>
<div class="chapter-header">
    <div class="part-tag">PART III | 10 ORIGINAL UNIVERSITY PRACTICAL PROGRAMS (20MCA243)</div>
    <h2 class="chapter-title">PROGRAM 08: SCROLLVIEW WITH DYNAMIC VIEW POPULATION</h2>
</div>

<h3>1. Aim</h3>
<p>To implement an Android <code>ScrollView</code> container hosting a vertical layout of interactive elements, demonstrating dynamic programmatic view addition at runtime and adhering to the single direct child ViewGroup constraint.</p>

<div class="diagram-container">
    <img src="diagrams/15_scrollview_hierarchy.svg" alt="ScrollView Hierarchy" class="diagram-img" style="max-height: 200px;" />
    <div class="diagram-caption">Figure P8.1: ScrollView Single-Child ViewGroup Hierarchy.</div>
</div>

<!-- DEDICATED FULL-WIDTH CODE PAGES -->

<!-- Continuous Natural Flow -->

{make_code_card("XML Layout Implementation", "08_Scroll_View/app/src/main/res/layout/activity_main.xml", p8_xml)}
{make_code_card("Java Source Code Implementation", "08_Scroll_View/app/src/main/java/com/example/scroll_view/MainActivity.java", p8_java)}

<!-- DETAILED WALKTHROUGH & EXAMINATION REVIEW -->

<!-- Continuous Natural Flow -->

<h3>2. Theoretical Golden Rule of ScrollView</h3>
<div class="box box-remember">
    <div class="box-title">THE GOLDEN RULE OF SCROLLVIEW</div>
    <p>A <code>ScrollView</code> can host strictly <strong>one</strong> direct child view or layout container. Placing multiple widgets directly inside a ScrollView produces an <code>IllegalStateException: ScrollView can host only one direct child</code>. Always wrap multiple widgets in a single parent <code>LinearLayout</code>.</p>
</div>

<!-- ============================================================== -->
<!-- PROGRAM 09: DROPDOWN SPINNER & ONITEMSELECTEDLISTENER          -->
<!-- ============================================================== -->
<div class="chapter-break"></div>
<div class="chapter-header">
    <div class="part-tag">PART III | 10 ORIGINAL UNIVERSITY PRACTICAL PROGRAMS (20MCA243)</div>
    <h2 class="chapter-title">PROGRAM 09: DROPDOWN SPINNER &amp; ONITEMSELECTEDLISTENER</h2>
</div>

<h3>1. Aim</h3>
<p>To implement a compact dropdown <code>Spinner</code> selector populated with catalog items using an <code>ArrayAdapter&lt;String&gt;</code>, capturing user item selections via <code>OnItemSelectedListener</code> and displaying visual feedback.</p>

<div class="diagram-container">
    <img src="diagrams/14_spinner_adapter.svg" alt="Spinner Adapter Flow" class="diagram-img" style="max-height: 200px;" />
    <div class="diagram-caption">Figure P9.1: Spinner Data Binding via ArrayAdapter.</div>
</div>

<!-- DEDICATED FULL-WIDTH CODE PAGES -->

<!-- Continuous Natural Flow -->

{make_code_card("XML Layout Implementation", "09_Spinner/app/src/main/res/layout/activity_main.xml", p9_xml)}
{make_code_card("Java Source Code Implementation", "09_Spinner/app/src/main/java/com/example/spinner/MainActivity.java", p9_java)}

<!-- DETAILED WALKTHROUGH & EXAMINATION REVIEW -->

<!-- Continuous Natural Flow -->

<h3>2. Dynamic Spinner Variation: User Input to Dynamic Collection</h3>
<div class="box box-concept">
    <div class="box-title">DYNAMIC SPINNER DATA FLOW | PREDEFINED &rarr; USER INPUT &rarr; ADAPTER UPDATE</div>
    <p>The standard lab program uses a static array. Below is the full implementation that takes user input from an <code>EditText</code> and appends it dynamically:</p>
    <pre><code>// 1. Dynamic ArrayList backing
ArrayList&lt;String&gt; fruitList = new ArrayList&lt;&gt;();
fruitList.add("Apple");
fruitList.add("Mango");

ArrayAdapter&lt;String&gt; adapter = new ArrayAdapter&lt;&gt;(this, 
    android.R.layout.simple_spinner_item, fruitList);
adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
spinner.setAdapter(adapter);

// 2. Dynamic Input Capture &amp; Validation
btnAddFruit.setOnClickListener(new View.OnClickListener() {{
    String fruit = etNewFruit.getText().toString().trim();
    if (fruit.isEmpty()) {{
        etNewFruit.setError("Enter fruit name");
        return;
    }}
    fruitList.add(fruit);                  // Stage 3: Dynamic Data Update
    adapter.notifyDataSetChanged();       // Immediately reflects in Spinner dropdown!
    etNewFruit.setText("");                // Clear input field
    Toast.makeText(MainActivity.this, "Added: " + fruit, Toast.LENGTH_SHORT).show();
}});</code></pre>
</div>

<!-- ============================================================== -->
<!-- PROGRAM 10: SHAREDPREFERENCES PERSISTENT KEY-VALUE STORAGE     -->
<!-- ============================================================== -->
<div class="chapter-break"></div>
<div class="chapter-header">
    <div class="part-tag">PART III | 10 ORIGINAL UNIVERSITY PRACTICAL PROGRAMS (20MCA243)</div>
    <h2 class="chapter-title">PROGRAM 10: SHAREDPREFERENCES PERSISTENT KEY-VALUE STORAGE</h2>
</div>

<h3>1. Aim</h3>
<p>To demonstrate local client-side persistent storage in Android by creating, reading, updating, and clearing key-value pairs (Username, Email) using the <code>SharedPreferences</code> and <code>SharedPreferences.Editor</code> APIs.</p>

<div class="diagram-container">
    <img src="diagrams/12_shared_preferences_flow.svg" alt="SharedPreferences Flow" class="diagram-img" style="max-height: 200px;" />
    <div class="diagram-caption">Figure P10.1: SharedPreferences Key-Value Storage Architecture.</div>
</div>

<!-- DEDICATED FULL-WIDTH CODE PAGES -->

<!-- Continuous Natural Flow -->

{make_code_card("XML Layout Implementation", "10_Shared_Preferences/app/src/main/res/layout/activity_main.xml", p10_xml)}
{make_code_card("Java Source Code Implementation", "10_Shared_Preferences/app/src/main/java/com/example/shared_preferences/MainActivity.java", p10_java)}

<!-- DETAILED WALKTHROUGH & EXAMINATION REVIEW -->

<!-- Continuous Natural Flow -->

<h3>2. Detailed Code Walkthrough</h3>
<ul>
    <li><strong>Opening Storage:</strong> <code>SharedPreferences sp = getSharedPreferences("MyPrefs", MODE_PRIVATE);</code> opens an XML file stored in private app data storage.</li>
    <li><strong>Saving Data:</strong> <code>sp.edit().putString("name", name).putString("email", email).apply();</code> stages the key-value edits and persists them asynchronously.</li>
    <li><strong>Reading Data:</strong> <code>sp.getString("name", "");</code> extracts the string with an empty fallback default.</li>
    <li><strong>Clearing Data:</strong> <code>sp.edit().clear().apply();</code> wipes all stored keys, resetting the state.</li>
</ul>

<h3>3. Viva Focus: apply() versus commit()</h3>
<table class="academic-table">
    <thead><tr><th>Criteria</th><th>apply()</th><th>commit()</th></tr></thead>
    <tbody>
        <tr><td><strong>Thread Execution</strong></td><td>Asynchronous (writes to disk in background worker thread).</td><td>Synchronous (writes to disk on calling thread).</td></tr>
        <tr><td><strong>Return Value</strong></td><td><code>void</code> (fire-and-forget).</td><td><code>boolean</code> (returns true if write succeeded).</td></tr>
        <tr><td><strong>UI Thread Impact</strong></td><td>Completely safe for Main UI thread; zero frame drops.</td><td>Can block UI thread during heavy disk I/O (risk of ANR).</td></tr>
    </tbody>
</table>
'''
