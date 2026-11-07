"""
Content Module: Part IV & V - 5 Integrated Android Applications (25 Variations)
Exhaustive coverage of 5 progressive multi-component enterprise systems,
each featuring 5 distinct architectural variations with code and explanations.
"""

def get_integrated_html():
    return '''
<div class="chapter-break"></div>
<div class="chapter-header">
    <div class="part-tag">PART IV &amp; V | INTEGRATED MULTI-COMPONENT APPLICATIONS</div>
    <h2 class="chapter-title">APPLICATION 1: ENTERPRISE AUTHENTICATION &amp; PROFILE MANAGER</h2>
</div>

<p class="lead-text">This progressive application combines credential capture, rigorous validation, session persistence using <code>SharedPreferences</code>, cross-activity data exchange via <code>Intent</code>, and secure logout state management.</p>

<div class="diagram-container">
    <img src="diagrams/16_login_flowchart.svg" alt="Auth Flow" class="diagram-img" />
    <div class="diagram-caption">Figure IA1.1: Multi-stage Authentication and Profile Lifecycle Flowchart.</div>
</div>

<div class="two-col">
    <div class="col-left">
        <h3>Variation 1.1: Basic UI Layout</h3>
        <p>Introduces raw text capture via <code>EditText</code> and a submission <code>Button</code> without validation.</p>
        <pre><code>// Var 1.1: Extracting raw strings
String u = etUser.getText().toString();
String p = etPass.getText().toString();</code></pre>

        <h3>Variation 1.2: Validation &amp; Error Badges</h3>
        <p>Integrates <code>setError()</code> on empty fields and checks credentials with Toast feedback.</p>
        <pre><code>// Var 1.2: Validation logic
if (u.isEmpty()) etUser.setError("Required");
else if (p.isEmpty()) etPass.setError("Required");
else if (u.equals("admin") &amp;&amp; p.equals("1234")) {
    Toast.makeText(this, "Success", Toast.LENGTH_SHORT).show();
}</code></pre>

        <h3>Variation 1.3: SharedPreferences Session</h3>
        <p>Stores an <code>IS_LOGGED_IN</code> boolean flag so restarting the app remembers the active user.</p>
        <pre><code>// Var 1.3: Session write
SharedPreferences sp = getSharedPreferences("Auth", MODE_PRIVATE);
sp.edit().putString("USER", u).putBoolean("LOGGED", true).apply();</code></pre>
    </div>
    <div class="col-right">
        <h3>Variation 1.4: Explicit Intent Navigation</h3>
        <p>Passes the authenticated username to <code>ProfileActivity</code> via Intent Extras.</p>
        <pre><code>// Var 1.4: Intent data transfer
Intent intent = new Intent(this, ProfileActivity.class);
intent.putExtra("LOGGED_USER", u);
startActivity(intent);</code></pre>

        <h3>Variation 1.5: Complete Auth &amp; Profile System</h3>
        <p>The definitive production architecture incorporating auto-login checks in <code>onCreate()</code> and a complete Logout routine that wipes the session and returns to login:</p>
        <pre><code>// Var 1.5: Auto-login &amp; Logout
public class ProfileActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle b) {
        super.onCreate(b);
        setContentView(R.layout.activity_profile);
        
        Button btnLogout = findViewById(R.id.btnLogout);
        btnLogout.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                SharedPreferences sp = getSharedPreferences("Auth", MODE_PRIVATE);
                sp.edit().clear().apply(); // Wipe session
                
                Intent i = new Intent(ProfileActivity.this, MainActivity.class);
                i.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK);
                startActivity(i);
                finish();
            }
        });
    }
}</code></pre>
    </div>
</div>

<!-- APPLICATION 2 -->
<div class="chapter-break"></div>
<div class="chapter-header">
    <div class="part-tag">PART IV &amp; V | INTEGRATED MULTI-COMPONENT APPLICATIONS</div>
    <h2 class="chapter-title">APPLICATION 2: STUDENT REGISTRATION &amp; ACADEMIC PROFILE SYSTEM</h2>
</div>

<div class="diagram-container">
    <img src="diagrams/17_student_reg_flowchart.svg" alt="Student Reg Flow" class="diagram-img" />
    <div class="diagram-caption">Figure IA2.1: Student Registration Data Capture and Multi-Activity Summary Flowchart.</div>
</div>

<div class="two-col">
    <div class="col-left">
        <h3>Variation 2.1: Basic Student Form</h3>
        <p>Captures Name, University Roll Number, and Age using numeric and text <code>EditText</code> controls.</p>

        <h3>Variation 2.2: Course Selection via Spinner</h3>
        <p>Binds an academic program list (MCA, M.Tech, B.Tech) to a <code>Spinner</code> using <code>ArrayAdapter</code>.</p>
        <pre><code>String[] courses = {"MCA", "M.Tech CSE", "B.Tech"};
ArrayAdapter&lt;String&gt; adapter = new ArrayAdapter&lt;&gt;(
    this, android.R.layout.simple_spinner_dropdown_item, courses);
spCourse.setAdapter(adapter);</code></pre>

        <h3>Variation 2.3: Demographics &amp; Skills Controls</h3>
        <p>Introduces a <code>RadioGroup</code> for Gender selection (Male/Female) and independent <code>CheckBox</code> controls for elective technical skills (Java, Python, Mobile App Dev).</p>
    </div>
    <div class="col-right">
        <h3>Variation 2.4: Intent Summary Transition</h3>
        <p>Bundles validated inputs and forwards them to a read-only <code>SummaryActivity</code>.</p>

        <h3>Variation 2.5: Complete Academic Profile System</h3>
        <p>Full enterprise implementation with multi-field validation, ArrayList parceling, and styled summary card rendering:</p>
        <pre><code>// Var 2.5: Bundling complex registration payload
ArrayList&lt;String&gt; skills = new ArrayList&lt;&gt;();
if (cbWeb.isChecked()) skills.add("Web Programming");
if (cbMobile.isChecked()) skills.add("Mobile Dev");

Intent intent = new Intent(MainActivity.this, StudentSummaryActivity.class);
intent.putExtra("NAME", name);
intent.putExtra("ROLL", roll);
intent.putExtra("COURSE", course);
intent.putExtra("GENDER", gender);
intent.putStringArrayListExtra("SKILLS", skills);
startActivity(intent);</code></pre>
    </div>
</div>

<!-- APPLICATION 3 -->
<div class="chapter-break"></div>
<div class="chapter-header">
    <div class="part-tag">PART IV &amp; V | INTEGRATED MULTI-COMPONENT APPLICATIONS</div>
    <h2 class="chapter-title">APPLICATION 3: ITEM SELECTION &amp; SHOPPING CART MANAGEMENT</h2>
</div>

<div class="diagram-container">
    <img src="diagrams/18_shopping_cart_flowchart.svg" alt="Shopping Cart Flow" class="diagram-img" />
    <div class="diagram-caption">Figure IA3.1: Inventory Selection, Dynamic Totaling, and Order Checkout Pipeline.</div>
</div>

<div class="two-col">
    <div class="col-left">
        <h3>Variation 3.1: Product Selection Dropdown</h3>
        <p>Displays inventory items with unit prices in a dropdown <code>Spinner</code>.</p>

        <h3>Variation 3.2: Dynamic Cost Calculation</h3>
        <p>Computes <code>unitPrice * quantity</code> upon user input and displays running totals.</p>

        <h3>Variation 3.3: Cart Memory Storage</h3>
        <p>Appends selected product lines into a runtime Java <code>ArrayList&lt;String&gt;</code>.</p>
        <pre><code>ArrayList&lt;String&gt; cart = new ArrayList&lt;&gt;();
cart.add("Android Handbook (Qty 2) = $100");</code></pre>
    </div>
    <div class="col-right">
        <h3>Variation 3.4: Real-time ListView Rendering</h3>
        <p>Connects an <code>ArrayAdapter</code> to a <code>ListView</code>, updating the UI dynamically via <code>adapter.notifyDataSetChanged()</code>.</p>

        <h3>Variation 3.5: Complete E-Commerce Checkout</h3>
        <p>Enables adding multiple items, computing grand total with sales tax, item removal on click, and launching an Order Receipt Activity:</p>
        <pre><code>// Var 3.5: Order Dispatch
Intent checkout = new Intent(this, ReceiptActivity.class);
checkout.putStringArrayListExtra("CART_ITEMS", cartItems);
checkout.putExtra("TOTAL_AMOUNT", grandTotal);
startActivity(checkout);</code></pre>
    </div>
</div>

<!-- APPLICATION 4 -->
<div class="chapter-break"></div>
<div class="chapter-header">
    <div class="part-tag">PART IV &amp; V | INTEGRATED MULTI-COMPONENT APPLICATIONS</div>
    <h2 class="chapter-title">APPLICATION 4: USER REGISTRATION &amp; PROFILE SETTINGS MANAGER</h2>
</div>

<div class="diagram-container">
    <img src="diagrams/19_profile_manager_flowchart.svg" alt="Profile Flow" class="diagram-img" />
    <div class="diagram-caption">Figure IA4.1: Persistent Settings Sync via SharedPreferences.</div>
</div>

<div class="two-col">
    <div class="col-left">
        <h3>Variation 4.1: Contact Info Form</h3>
        <p>Captures user Full Name, Email Address, and Phone Number.</p>

        <h3>Variation 4.2: Switches &amp; Toggles</h3>
        <p>Adds modern UI toggles: <code>Switch</code> for Dark Mode and Notification preferences.</p>

        <h3>Variation 4.3: Real-Time Input Sanitization</h3>
        <p>Validates email format using Android regex pattern <code>Patterns.EMAIL_ADDRESS.matcher(email).matches()</code>.</p>
    </div>
    <div class="col-right">
        <h3>Variation 4.4: Profile Display Activity</h3>
        <p>Navigates to a formatted user card layout via Explicit Intent.</p>

        <h3>Variation 4.5: Complete Persistent Profile Manager</h3>
        <p>Synchronizes all fields to <code>SharedPreferences</code>, automatically re-populates values on app restart, and includes a full reset routine:</p>
        <pre><code>// Var 4.5: Profile Auto-Sync
SharedPreferences sp = getSharedPreferences("ProfilePrefs", MODE_PRIVATE);
// Auto-load on onCreate
etName.setText(sp.getString("NAME", ""));
swNotify.setChecked(sp.getBoolean("NOTIFY", true));

// Save on Click
sp.edit()
  .putString("NAME", etName.getText().toString())
  .putBoolean("NOTIFY", swNotify.isChecked())
  .apply();</code></pre>
    </div>
</div>

<!-- APPLICATION 5 -->
<div class="chapter-break"></div>
<div class="chapter-header">
    <div class="part-tag">PART IV &amp; V | INTEGRATED MULTI-COMPONENT APPLICATIONS</div>
    <h2 class="chapter-title">APPLICATION 5: MULTI-PAGE UNIVERSITY PORTAL &amp; UTILITIES HUB</h2>
</div>

<div class="diagram-container">
    <img src="diagrams/20_portal_navigation.svg" alt="Portal Flow" class="diagram-img" />
    <div class="diagram-caption">Figure IA5.1: Multi-Page Portal Navigation &amp; Dispatch Graph.</div>
</div>

<div class="two-col">
    <div class="col-left">
        <h3>Variation 5.1: Dashboard Navigation</h3>
        <p>Central dashboard menu navigating to independent sub-activities.</p>

        <h3>Variation 5.2: Bi-directional Activity Results</h3>
        <p>Uses <code>startActivityForResult()</code> to request feedback or settings from secondary screens.</p>

        <h3>Variation 5.3: Implicit Intent Integration Hub</h3>
        <p>Embeds CET Web Portal (<code>ACTION_VIEW</code>) and Campus Location coordinates in Google Maps (<code>geo:</code>).</p>
    </div>
    <div class="col-right">
        <h3>Variation 5.4: Portal State Caching</h3>
        <p>Caches recent user activities and visits in <code>SharedPreferences</code>.</p>

        <h3>Variation 5.5: Complete University Information Portal</h3>
        <p>A flagship enterprise portal combining explicit navigation, implicit web/map integrations, dynamic calculator utilities, profile caches, and an <code>AlertDialog</code> confirmation exit dialog:</p>
        <pre><code>// Var 5.5: Exit Confirmation Dialog
new AlertDialog.Builder(MainActivity.this)
    .setTitle("Exit Portal")
    .setMessage("Are you sure you want to exit?")
    .setPositiveButton("Yes", (d, w) -&gt; finish())
    .setNegativeButton("No", null)
    .show();</code></pre>
    </div>
</div>
'''
