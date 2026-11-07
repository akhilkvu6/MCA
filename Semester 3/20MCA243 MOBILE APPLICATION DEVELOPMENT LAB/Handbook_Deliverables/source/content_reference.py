"""
Content Module: Part VI & VII - Visual Learning Aids, Quick Revision & Viva Voce
Contains complete cheat sheets, comparison tables, common error troubleshooting,
and 30 high-yield university viva examination questions with answers.
"""

def get_reference_html():
    return '''
<div class="chapter-break"></div>
<div class="chapter-header">
    <div class="part-tag">PART VII | QUICK REVISION &amp; EXAMINATION REFERENCE</div>
    <h2 class="chapter-title">HIGH-YIELD REVISION CHEAT SHEETS &amp; COMPARISON TABLES</h2>
</div>

<h3>1. Android Architecture Layer Quick Summary</h3>
<table class="academic-table">
    <tr><th>Layer</th><th>Underlying Tech</th><th>Primary Responsibilities</th><th>Key Components</th></tr>
    <tr><td><strong>Applications</strong></td><td>Java / Kotlin</td><td>User interaction &amp; presentation</td><td>Home, Phone, Custom MCA Apps</td></tr>
    <tr><td><strong>Application Framework</strong></td><td>Java APIs</td><td>High-level services &amp; management</td><td>ActivityManager, WindowManager, ContentProviders</td></tr>
    <tr><td><strong>Libraries &amp; Runtime</strong></td><td>C/C++ &amp; DEX</td><td>Native engines &amp; bytecode execution</td><td>SQLite, WebKit, OpenGL ES, ART (AOT/JIT)</td></tr>
    <tr><td><strong>Hardware Abstraction (HAL)</strong></td><td>C/C++ stubs</td><td>Device driver standardization</td><td>Camera, Audio, Bluetooth, Sensors HAL</td></tr>
    <tr><td><strong>Linux Kernel</strong></td><td>C</td><td>Hardware interface &amp; core OS services</td><td>Process management, Binder IPC, LMK, Power</td></tr>
</table>

<h3>2. Android Layout Attributes Quick Reference</h3>
<table class="academic-table">
    <tr><th>Attribute</th><th>Valid Layouts</th><th>Functional Purpose</th></tr>
    <tr><td><code>android:orientation</code></td><td>LinearLayout</td><td>Defines arrangement axis: <code>vertical</code> or <code>horizontal</code>.</td></tr>
    <tr><td><code>android:layout_weight</code></td><td>LinearLayout</td><td>Distributes surplus dimension proportionally among sibling views.</td></tr>
    <tr><td><code>android:gravity</code></td><td>View / ViewGroup</td><td>Controls alignment of <i>content inside</i> the view (e.g. text inside button).</td></tr>
    <tr><td><code>android:layout_gravity</code></td><td>Child of ViewGroup</td><td>Controls alignment of the <i>view itself</i> inside its parent container.</td></tr>
    <tr><td><code>android:layout_margin</code></td><td>All Views</td><td>Defines external spacing around the view perimeter.</td></tr>
    <tr><td><code>android:padding</code></td><td>All Views</td><td>Defines internal spacing between view boundary and its content.</td></tr>
    <tr><td><code>app:layout_constraintTop_to...</code></td><td>ConstraintLayout</td><td>Anchors the top constraint edge to a target sibling or parent boundary.</td></tr>
</table>

<h3>3. Storage Solutions Comparison Matrix</h3>
<table class="academic-table">
    <tr><th>Storage Option</th><th>Data Format</th><th>Visibility</th><th>Persistence</th><th>Typical Use Case</th></tr>
    <tr><td><strong>SharedPreferences</strong></td><td>XML Key-Value pairs</td><td>Private to app</td><td>Permanent (until cleared)</td><td>User settings, login session tokens</td></tr>
    <tr><td><strong>Internal Storage</strong></td><td>Raw binary / text files</td><td>Private to app</td><td>Permanent (until uninstalled)</td><td>Downloaded caches, private app files</td></tr>
    <tr><td><strong>External Storage</strong></td><td>Shared media files</td><td>Public / Scoped</td><td>User-managed</td><td>Photos, videos, documents, music</td></tr>
    <tr><td><strong>SQLite / Room</strong></td><td>Relational SQL tables</td><td>Private to app</td><td>Permanent structured</td><td>Complex relational catalogs, offline caching</td></tr>
</table>

<div class="chapter-break"></div>
<div class="chapter-header">
    <div class="part-tag">PART VII | UNIVERSITY EXAMINATION PREPARATION</div>
    <h2 class="chapter-title">30 HIGH-YIELD VIVA VOCE EXAMINATION QUESTIONS &amp; ANSWERS</h2>
</div>

<div class="viva-container">
    <div class="viva-item">
        <div class="viva-q">1. What is the Android Manifest file and why is it mandatory?</div>
        <div class="viva-a"><code>AndroidManifest.xml</code> is the fundamental deployment descriptor and contract of an Android application. It declares the application package name, all components (Activities, Services, Broadcast Receivers, Content Providers), required system permissions, minimum/target SDK versions, and hardware requirements. The OS refuses to execute unregistered components.</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">2. What is the role of the auto-generated R class in Android?</div>
        <div class="viva-a">The <code>R</code> class is an auto-generated Java class created by the AAPT2 tool. It maps all resources under the <code>res/</code> directory into static hexadecimal 32-bit integer constants (e.g., <code>R.id.btnLogin</code>, <code>R.layout.activity_main</code>), enabling type-safe programmatic access from Java code.</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">3. Differentiate between dp (density-independent pixels) and sp (scale-independent pixels).</div>
        <div class="viva-a">Both units scale across different hardware screen densities based on a 160 dpi baseline. However, <code>sp</code> additionally factors in the user's system-level accessibility font size preferences. Hence, <code>dp</code> is used for layout dimensions (widths, heights, margins), while <code>sp</code> is strictly reserved for text typography (<code>textSize</code>).</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">4. Explain the difference between Explicit Intent and Implicit Intent.</div>
        <div class="viva-a">An <strong>Explicit Intent</strong> explicitly specifies the exact destination target class (e.g. <code>new Intent(this, SecondActivity.class)</code>). An <strong>Implicit Intent</strong> declares a generalized action (e.g. <code>ACTION_VIEW</code>, <code>ACTION_DIAL</code>) and data URI, delegating to the Android OS to resolve the best matching external application via Intent Filters.</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">5. What happens during an Activity orientation change (portrait to landscape)?</div>
        <div class="viva-a">By default, a screen rotation constitutes a runtime configuration change. The Android OS completely tears down the active activity (executing <code>onPause &rarr; onStop &rarr; onDestroy</code>) and recreates a fresh instance from scratch (<code>onCreate &rarr; onStart &rarr; onResume</code>) to load resources from alternative qualifier folders (e.g., <code>layout-land/</code>).</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">6. How is user session state persisted across orientation changes?</div>
        <div class="viva-a">Temporary UI state can be saved in the <code>onSaveInstanceState(Bundle outState)</code> callback and restored in <code>onCreate(Bundle savedInstanceState)</code> or <code>onRestoreInstanceState()</code>. For persistent storage across app restarts, <code>SharedPreferences</code> or a database is used.</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">7. What is an Adapter and why is it necessary in Android?</div>
        <div class="viva-a">An <strong>Adapter</strong> is a structural bridge between a data source (such as an array or <code>ArrayList</code>) and an <code>AdapterView</code> (such as <code>ListView</code> or <code>Spinner</code>). It inflates and binds individual data items to child view rows on demand, recycling views to minimize memory consumption.</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">8. What is the function of android:layout_weight in LinearLayout?</div>
        <div class="viva-a"><code>layout_weight</code> specifies how remaining unused space along the layout's orientation axis should be divided among sibling views. When set to <code>0dp</code> width (horizontal) or <code>0dp</code> height (vertical) alongside weight values, views expand proportionally relative to each other.</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">9. Compare apply() versus commit() in SharedPreferences.Editor.</div>
        <div class="viva-a"><code>commit()</code> writes data synchronously to disk on the main calling thread and returns a boolean status, risking UI stuttering. <code>apply()</code> commits changes to the in-memory cache immediately and writes to disk asynchronously in a background worker thread, ensuring smooth UI performance.</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">10. What is the Golden Rule of ScrollView layout architecture?</div>
        <div class="viva-a">A <code>ScrollView</code> can host strictly <strong>one</strong> direct child view element. To place multiple widgets inside a ScrollView, all widgets must be nested inside a single parent container (such as a vertical <code>LinearLayout</code>).</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">11. Why should you never nest a ListView inside a ScrollView?</div>
        <div class="viva-a">Nesting a scrollable view inside another scrollable container causes touch event conflicts and breaks view recycling. The parent ScrollView cannot calculate the dynamic child height, resulting in the ListView rendering only one or two rows or failing to scroll.</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">12. What causes an ActivityNotFoundException in Android?</div>
        <div class="viva-a">An <code>ActivityNotFoundException</code> occurs when an implicit intent is triggered, but no installed application on the device matches the specified action, data scheme, or category. It must be guarded against using <code>try-catch</code> or <code>intent.resolveActivity()</code>.</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">13. What is an ANR error and how is it prevented?</div>
        <div class="viva-a"><strong>Application Not Responding (ANR)</strong> is a system dialog displayed when an application freezes the UI thread for longer than 5 seconds (or broadcast receiver for > 10s). It is prevented by offloading long-running tasks (network, disk I/O, heavy parsing) to background threads.</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">14. Differentiate between RadioGroup and CheckBox.</div>
        <div class="viva-a"><code>RadioGroup</code> enforces single-choice mutual exclusion among its child <code>RadioButton</code> views (selecting one deselects others). <code>CheckBox</code> allows independent multiple-choice selection, where any combination of options can be toggled simultaneously.</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">15. What is the purpose of android:exported="true" in Android 12+?</div>
        <div class="viva-a">Beginning in Android 12 (API 31), any component (Activity, Service, Receiver) containing an <code>&lt;intent-filter&gt;</code> must explicitly declare <code>android:exported="true"</code> (if accessible to outside apps/launcher) or <code>false</code> (if strictly private) to mitigate security vulnerabilities.</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">16. What is the Android Runtime (ART) Ahead-Of-Time (AOT) compilation?</div>
        <div class="viva-a">ART compiles DEX bytecode directly into native machine code (ELF binaries) during application installation (AOT) and runtime idle periods. This eliminates on-the-fly interpretation overhead, speeding up execution and conserving battery power compared to the legacy Dalvik VM.</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">17. How do you pass primitive data between Activities using Intent?</div>
        <div class="viva-a">Data is attached in the sending Activity using <code>intent.putExtra(key, value)</code> and extracted in the destination Activity via <code>getIntent().getStringExtra(key)</code>, <code>getIntExtra(key, defaultValue)</code>, or <code>getBooleanExtra(key, defaultValue)</code>.</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">18. What is the purpose of finish() in an Activity?</div>
        <div class="viva-a">Calling <code>finish()</code> explicitly terminates the current Activity instance, initiating its destruction lifecycle (<code>onPause &rarr; onStop &rarr; onDestroy</code>) and popping it off the back-stack so the user returns to the preceding screen.</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">19. What is the function of the android.permission.INTERNET declaration?</div>
        <div class="viva-a">It is a standard normal permission declared in <code>AndroidManifest.xml</code> granting the application access to open network sockets and retrieve remote web resources (e.g. via HTTP/HTTPS).</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">20. What is ViewBinding and why is it preferred over findViewById()?</div>
        <div class="viva-a">ViewBinding generates binding classes for each XML layout containing direct, null-safe, and compile-time type-safe references to all views with IDs, eliminating <code>NullPointerException</code> and <code>ClassCastException</code> risks inherent to manual <code>findViewById()</code>.</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">21. Explain the difference between match_parent and wrap_content.</div>
        <div class="viva-a"><code>match_parent</code> forces the view to expand and occupy all available space within its parent container. <code>wrap_content</code> restricts the view dimensions to only the size necessary to encompass its internal contents (e.g., text or image boundaries).</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">22. What is the difference between an Intent Action and Intent Data?</div>
        <div class="viva-a">An <strong>Action</strong> specifies the operation to be performed (e.g., <code>ACTION_VIEW</code>, <code>ACTION_SEND</code>). <strong>Data</strong> provides the URI upon which that action operates, encoded with specific schemes such as <code>https://</code> for websites or <code>tel:</code> for dialers.</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">23. How does OnItemClickListener differ from OnClickListener?</div>
        <div class="viva-a"><code>OnClickListener</code> is attached to standalone individual views (like Button, TextView). <code>OnItemClickListener</code> is attached to an AdapterView container (ListView, GridView) and provides parameters indicating the exact clicked row position (<code>position</code>) and data row ID (<code>id</code>).</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">24. What is the purpose of Logcat and the Log.d() method?</div>
        <div class="viva-a">Logcat is the system logging buffer in Android Studio. <code>Log.d(TAG, message)</code> writes debug messages tagged with an identifier, allowing developers to inspect program flow, variable states, and exception traces without displaying visual artifacts to end users.</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">25. What is the Android Binder IPC mechanism?</div>
        <div class="viva-a">Binder is a high-performance Linux kernel driver and IPC mechanism that facilitates remote procedure calls and transaction memory buffers between distinct Android processes, enabling secure communication between apps and system services.</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">26. What happens if super.onCreate() is omitted in an Activity?</div>
        <div class="viva-a">Omitting <code>super.onCreate(savedInstanceState)</code> causes the runtime framework to throw a <code>SuperNotCalledException</code>, crashing the application immediately upon launch because base framework initialization was bypassed.</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">27. What is an Intent Filter?</div>
        <div class="viva-a">An <code>&lt;intent-filter&gt;</code> is an XML declaration inside <code>AndroidManifest.xml</code> that specifies the types of implicit intents an Activity, Service, or BroadcastReceiver can respond to based on declared actions, categories, and data schemes.</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">28. How is an AlertDialog constructed in Android?</div>
        <div class="viva-a">An <code>AlertDialog</code> is instantiated using the Builder pattern: <code>new AlertDialog.Builder(context).setTitle(...).setMessage(...).setPositiveButton(...).setNegativeButton(...).show()</code>.</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">29. What is Scoped Storage in modern Android?</div>
        <div class="viva-a">Introduced in Android 10 (API 29), Scoped Storage isolates apps by giving each app private storage access while requiring the system Photo Picker or Storage Access Framework (SAF) for user-shared storage, preventing apps from scanning unrelated files across the SD card.</div>
    </div>

    <div class="viva-item">
        <div class="viva-q">30. What are the key stages in building an APK file?</div>
        <div class="viva-a">1) AAPT2 compiles XML resources into binary XML and <code>R.java</code>. 2) <code>javac</code> compiles Java code into <code>.class</code> bytecode. 3) D8 dexer converts class files into Dalvik Executable (<code>.dex</code>) format. 4) APK Packager zips DEX, resources, and assets. 5) <code>apksigner</code> signs with a digital certificate and <code>zipalign</code> optimizes alignment for memory efficiency.</div>
    </div>
</div>
'''
