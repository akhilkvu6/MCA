"""
Content Module: Part I - Complete Android Theory (Chapters 1 - 19)
Second Edition: Comprehensive academic textbook format.
Single-column full-width layout, complete Android 1.0 to Android 17 version history,
SDK compilation architecture, and deep technical explanations.
"""

def get_theory_html():
    return '''
<!-- CHAPTER 1 -->
<div class="chapter-header" style="margin-top: 0;">
    <div class="part-tag">PART I | ANDROID CORE ARCHITECTURE &amp; THEORY</div>
    <h2 class="chapter-title">CHAPTER 1: INTRODUCTION TO ANDROID &amp; DEVELOPMENT ENVIRONMENT</h2>
</div>

<p class="lead-text">Android is an open-source, Linux-based mobile operating system and comprehensive software stack engineered for touchscreen mobile devices (smartphones, tablets), wearable technology (Wear OS), smart televisions (Android TV), and automotive entertainment platforms (Android Automotive). Founded by Andy Rubin in 2003 and acquired by Google in 2005, Android is maintained under the stewardship of the Open Handset Alliance (OHA) and distributed primarily under the permissive Apache 2.0 open-source license.</p>

<div class="box box-definition">
    <div class="box-title">DEFINITION | ANDROID OPERATING SYSTEM</div>
    <p><strong>Android</strong> is an open-source, multi-layered software platform comprising a modified Linux kernel, hardware abstraction layer (HAL), native C/C++ core libraries, the Android Runtime (ART) execution engine, an application framework, and pre-installed system applications, providing an abstraction barrier between mobile hardware and end-user applications.</p>
</div>

<h3>1.1 Chronological Version History: Android 1.0 through Android 17</h3>
<p>Android releases follow a disciplined progression designated by incremental API levels, numerical version strings, and historically iconic confectionery codenames. Understanding this evolutionary lineage is essential for targeting hardware capabilities and managing backward compatibility.</p>

<table class="academic-table">
    <thead>
        <tr>
            <th style="width: 10%;">Version</th>
            <th style="width: 22%;">Public Name &amp; Codename</th>
            <th style="width: 10%;">API Level</th>
            <th style="width: 8%;">Year</th>
            <th style="width: 50%;">Major Architectural Milestones &amp; Features</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Android 1.0</strong></td>
            <td>Base / "Apple Pie"</td>
            <td>API 1</td>
            <td>2008</td>
            <td>HTC Dream (G1) launch, notification pull-down drawer, WebKit browser, Android Market, SQLite integration.</td>
        </tr>
        <tr>
            <td><strong>Android 1.1</strong></td>
            <td>"Banana Bread" / "Petit Four"</td>
            <td>API 2</td>
            <td>2009</td>
            <td>Save attachments in MMS, support for showing/hiding dialer in active call, API stabilization.</td>
        </tr>
        <tr>
            <td><strong>Android 1.5</strong></td>
            <td><strong>Cupcake</strong></td>
            <td>API 3</td>
            <td>2009</td>
            <td>First public confectionery name. On-screen virtual keyboard (IME framework), video recording/playback, app widgets.</td>
        </tr>
        <tr>
            <td><strong>Android 1.6</strong></td>
            <td><strong>Donut</strong></td>
            <td>API 4</td>
            <td>2009</td>
            <td>Quick Search Box, Text-to-Speech (TTS) synthesis engine, WVGA resolution support, VPN management framework.</td>
        </tr>
        <tr>
            <td><strong>Android 2.0 / 2.1</strong></td>
            <td><strong>Eclair</strong></td>
            <td>API 5–7</td>
            <td>2009</td>
            <td>Google Maps turn-by-turn navigation, HTML5 browser support, multi-account contact sync, live wallpapers.</td>
        </tr>
        <tr>
            <td><strong>Android 2.2</strong></td>
            <td><strong>Froyo</strong> (Frozen Yogurt)</td>
            <td>API 8</td>
            <td>2010</td>
            <td>Dalvik Just-In-Time (JIT) compiler (2x–5x performance boost), USB tethering, Wi-Fi hotspot functionality, cloud messaging.</td>
        </tr>
        <tr>
            <td><strong>Android 2.3</strong></td>
            <td><strong>Gingerbread</strong></td>
            <td>API 9–10</td>
            <td>2010</td>
            <td>Native Development Kit (NDK) gaming APIs, concurrent garbage collector, Near Field Communication (NFC), front camera support.</td>
        </tr>
        <tr>
            <td><strong>Android 3.0–3.2</strong></td>
            <td><strong>Honeycomb</strong></td>
            <td>API 11–13</td>
            <td>2011</td>
            <td>Tablet-optimized holographic UI, Action Bar, Fragment framework introduced, multicore CPU hardware acceleration.</td>
        </tr>
        <tr>
            <td><strong>Android 4.0</strong></td>
            <td><strong>Ice Cream Sandwich</strong></td>
            <td>API 14–15</td>
            <td>2011</td>
            <td>Unified phone/tablet UI, Roboto typeface, Holo theme, virtual on-screen navigation keys, swipe-to-dismiss gesture.</td>
        </tr>
        <tr>
            <td><strong>Android 4.1–4.3</strong></td>
            <td><strong>Jelly Bean</strong></td>
            <td>API 16–18</td>
            <td>2012</td>
            <td>Project Butter (60 fps VSYNC rendering), expandable rich notifications, Google Now, Bluetooth Low Energy (BLE).</td>
        </tr>
        <tr>
            <td><strong>Android 4.4</strong></td>
            <td><strong>KitKat</strong></td>
            <td>API 19–20</td>
            <td>2013</td>
            <td>Project Svelte (memory footprint reduced to 512MB RAM devices), Storage Access Framework (SAF), experimental ART preview.</td>
        </tr>
        <tr>
            <td><strong>Android 5.0 / 5.1</strong></td>
            <td><strong>Lollipop</strong></td>
            <td>API 21–22</td>
            <td>2014</td>
            <td>Material Design language, Android Runtime (ART) permanently replaces Dalvik, 64-bit CPU architecture, JobScheduler.</td>
        </tr>
        <tr>
            <td><strong>Android 6.0</strong></td>
            <td><strong>Marshmallow</strong></td>
            <td>API 23</td>
            <td>2015</td>
            <td>Dynamic runtime permissions model (<code>requestPermissions</code>), Doze battery saving state, USB Type-C, Fingerprint API.</td>
        </tr>
        <tr>
            <td><strong>Android 7.0 / 7.1</strong></td>
            <td><strong>Nougat</strong></td>
            <td>API 24–25</td>
            <td>2016</td>
            <td>Multi-window split-screen multitasking, Vulkan 3D graphics API, Profile-Guided Compilation (ART JIT + AOT hybrid).</td>
        </tr>
        <tr>
            <td><strong>Android 8.0 / 8.1</strong></td>
            <td><strong>Oreo</strong></td>
            <td>API 26–27</td>
            <td>2017</td>
            <td>Project Treble (modular OS updates), mandatory Notification Channels, Picture-in-Picture (PiP), background execution limits.</td>
        </tr>
        <tr>
            <td><strong>Android 9.0</strong></td>
            <td><strong>Pie</strong></td>
            <td>API 28</td>
            <td>2018</td>
            <td>Gesture navigation bar, Display Cutout (notch) support, Adaptive Battery (on-device ML), mandatory TLS network security.</td>
        </tr>
        <tr>
            <td><strong>Android 10</strong></td>
            <td>"Quince Tart" (Android 10)</td>
            <td>API 29</td>
            <td>2019</td>
            <td>Public dessert naming retired; Scoped Storage privacy sandbox, system-wide Dark Theme, Project Mainline modular updates.</td>
        </tr>
        <tr>
            <td><strong>Android 11</strong></td>
            <td>"Red Velvet Cake" (Android 11)</td>
            <td>API 30</td>
            <td>2020</td>
            <td>Dedicated Conversations notification section, Chat Bubbles, one-time permissions, Wireless ADB debugging support.</td>
        </tr>
        <tr>
            <td><strong>Android 12 / 12L</strong></td>
            <td>"Snow Cone" (Android 12)</td>
            <td>API 31–32</td>
            <td>2021</td>
            <td>Material You dynamic color theming, Privacy Dashboard, mic/cam indicator badges, mandatory <code>android:exported</code> in manifest.</td>
        </tr>
        <tr>
            <td><strong>Android 13</strong></td>
            <td>"Tiramisu" (Android 13)</td>
            <td>API 33</td>
            <td>2022</td>
            <td>Per-app language preferences, system Photo Picker privacy, runtime Notification permission (<code>POST_NOTIFICATIONS</code>).</td>
        </tr>
        <tr>
            <td><strong>Android 14</strong></td>
            <td>"Upside Down Cake" (Android 14)</td>
            <td>API 34</td>
            <td>2023</td>
            <td>Ultra HDR image rendering, predictive back navigation gesture preview, non-linear font scaling up to 200%.</td>
        </tr>
        <tr>
            <td><strong>Android 15</strong></td>
            <td>"Vanilla Ice Cream" (Android 15)</td>
            <td>API 35</td>
            <td>2024</td>
            <td>Stable release. Default edge-to-edge layouts, Private Space isolated app profile, 16KB memory page size compatibility.</td>
        </tr>
        <tr>
            <td><strong>Android 16</strong></td>
            <td>"Baklava" (Android 16)</td>
            <td>API 36</td>
            <td>2025</td>
            <td>Scheduled H1 2025. Transition to trunk-stable engineering model, Ongoing Activity / Live Updates chips, integrated photo picker.</td>
        </tr>
        <tr>
            <td><strong>Android 17</strong></td>
            <td>Future Exploratory Milestone</td>
            <td>API 37+</td>
            <td>2026</td>
            <td>Internal AOSP development milestone advancing on-device AI integration, system modularity, and extended privacy sandboxes.</td>
        </tr>
    </tbody>
</table>

<div class="box box-concept">
    <div class="box-title">PUBLIC DESSERT NAMES VERSUS INTERNAL ENGINEERING CODENAMES</div>
    <p>From Android 1.5 (Cupcake) through Android 9 (Pie), Google utilized dessert confection names for public consumer marketing. Starting with Android 10, Google transitioned consumer branding to numerical releases (Android 10, 11, 12...) for international clarity. However, Google's internal engineering teams continue assigning alphabetical dessert codenames (Quince Tart, Red Velvet Cake, Snow Cone, Tiramisu, Upside Down Cake, Vanilla Ice Cream, Baklava) to manage branch merges within the Android Open Source Project (AOSP).</p>
</div>

<h3>1.2 The Android SDK Build Configuration Parameters</h3>
<p>Every Android Studio module declares three fundamental integer version properties inside its <code>build.gradle</code> or <code>build.gradle.kts</code> script:</p>

<div class="formula">minSdk &le; targetSdk &le; compileSdk</div>

<ul>
    <li><strong><code>compileSdk</code>:</strong> The exact Android platform SDK version used by the Gradle build system to compile the Java/Kotlin source code. It dictates which framework APIs, classes, and methods are visible to the developer at compile-time. Compiling against API 34 enables using Android 14 APIs, but does not alter runtime behavior on older devices.</li>
    <li><strong><code>minSdk</code>:</strong> The minimum API level required for a device to install and execute the application. The Google Play Store and local OS package installer (PackageManager) actively enforce this threshold, blocking devices running an earlier OS version.</li>
    <li><strong><code>targetSdk</code>:</strong> Declares the API level against which the application has been designed, implemented, and thoroughly tested. Instructs the Android OS to activate new security restrictions, permission models, and UI behavioral shifts introduced in that version (e.g., Scoped Storage on API 29, <code>android:exported</code> on API 31). Setting a higher <code>targetSdk</code> ensures modern OS compliance.</li>
</ul>

<h3>1.3 Android Studio Development Toolchain Overview</h3>
<ul>
    <li><strong>Android SDK (Software Development Kit):</strong> Core libraries (<code>android.jar</code>), build tools (AAPT2, D8), platform tools (ADB), and hardware system images.</li>
    <li><strong>Android Studio IDE:</strong> Official development environment built on JetBrains IntelliJ IDEA, providing intelligent Java code completion, graphical layout designers, and memory profilers.</li>
    <li><strong>AAPT2 (Android Asset Packaging Tool 2):</strong> Parses and compiles XML layout resources, assets, and values into binary XML and generates the static Java <code>R.java</code> class.</li>
    <li><strong>D8 / R8 Compiler:</strong> Converts compiled Java bytecode (<code>.class</code> files) into highly optimized Dalvik Executable (<code>.dex</code>) format and performs code shrinking/obfuscation.</li>
    <li><strong>Gradle Automation:</strong> Modular task-runner that manages dependencies, compiler toolchains, flavor variants, and packaging into output artifacts.</li>
    <li><strong>APK vs AAB:</strong> An <strong>APK (Android Package)</strong> is a signed ZIP archive ready for direct installation on a device. An <strong>AAB (Android App Bundle)</strong> is a publishing format uploaded to Google Play that allows Google's Dynamic Delivery system to generate customized, lightweight APKs tailored to each user's exact screen density and CPU architecture, saving ~35% storage.</li>
</ul>

<!-- CHAPTER 2 -->
<div class="chapter-break"></div>
<div class="chapter-header">
    <div class="part-tag">PART I | ANDROID CORE ARCHITECTURE &amp; THEORY</div>
    <h2 class="chapter-title">CHAPTER 2: ANDROID 5-TIER SYSTEM ARCHITECTURE</h2>
</div>

<p class="lead-text">Android's operating system architecture is organized into five modular, decoupled layers. Lower layers provide system hardware abstraction and core OS security, while upper layers expose high-level Java APIs for application development.</p>

<div class="diagram-container">
    <img src="diagrams/01_android_architecture.svg" alt="Android Architecture Diagram" class="diagram-img" style="max-height: 240px;" />
    <div class="diagram-caption">Figure 2.1: The 5-Tier Android Software Architecture Stack from Linux Kernel to Applications.</div>
</div>

<h3>2.1 Linux Kernel Layer</h3>
<p>The bedrock of Android is a specialized Linux Kernel (Long Term Support branch). It interfaces directly with device hardware and provides essential operating system capabilities:</p>
<ul>
    <li><strong>Process Isolation &amp; Sandboxing:</strong> Each Android application runs inside its own isolated process space under a distinct Linux User ID (UID). An application cannot access memory, files, or execution state belonging to another application without explicit permissions.</li>
    <li><strong>Binder IPC (Inter-Process Communication):</strong> A high-throughput kernel driver facilitating remote procedure calls (RPC) and shared memory buffer transfers between separate process boundaries.</li>
    <li><strong>Low Memory Killer (LMK):</strong> A kernel-level driver that monitors physical RAM and systematically terminates dormant background processes based on an Out-Of-Memory (OOM) score when available system RAM drops below critical thresholds.</li>
    <li><strong>Hardware Drivers:</strong> Houses hardware-specific device drivers including display drivers, camera sensor pipelines, Bluetooth, flash memory, audio DACs, and power management (Wakelocks).</li>
</ul>

<h3>2.2 Hardware Abstraction Layer (HAL)</h3>
<p>The <strong>HAL</strong> provides standard C/C++ interface contracts that hardware vendors (e.g., Qualcomm, MediaTek) implement to expose proprietary chipset capabilities to the upper Java framework without modifying framework code. Standard modules include Camera HAL, Audio HAL, Sensors HAL, and Bluetooth HAL.</p>

<h3>2.3 Native C/C++ Libraries</h3>
<p>Positioned directly above the HAL, these compiled native user-space libraries power resource-intensive subsystem tasks:</p>
<ul>
    <li><strong>SQLite:</strong> High-performance, embedded, ACID-compliant relational SQL engine used for structured persistent storage across Android apps.</li>
    <li><strong>WebKit / Blink:</strong> Native web rendering engine powering embedded <code>WebView</code> controls.</li>
    <li><strong>OpenGL ES &amp; Vulkan:</strong> Hardware-accelerated 2D/3D graphics rendering pipelines communicating directly with the mobile GPU.</li>
    <li><strong>Media Framework:</strong> Native codecs supporting hardware decode/encode of audio/video formats (H.264, VP9, AAC, MP3).</li>
    <li><strong>Bionic:</strong> Google's custom BSD-derived C standard library, engineered specifically for low memory footprints and rapid thread execution.</li>
</ul>

<h3>2.4 Android Runtime (ART)</h3>
<p>Introduced in Android 5.0 to supersede the legacy Dalvik VM, <strong>ART</strong> is the managed runtime execution engine that executes Dalvik Executable (<code>.dex</code>) bytecode. ART features:</p>
<ul>
    <li><strong>Ahead-Of-Time (AOT) Compilation:</strong> Translates DEX bytecode into native machine instructions (ELF binary) during application installation via the <code>dex2oat</code> tool, drastically reducing CPU cycles during app execution.</li>
    <li><strong>Profile-Guided JIT (Just-In-Time) Hybrid:</strong> Re-introduced in Android 7.0, ART profiles app usage dynamically, compiling frequently accessed "hot paths" to native code while storing profiles to optimize future startup.</li>
    <li><strong>Concurrent Garbage Collection (GC):</strong> Advanced compacting garbage collectors minimize application pause times, eliminating visual frame drops ("jank").</li>
</ul>

<h3>2.5 Application Framework Layer</h3>
<p>The Java/Kotlin API layer that exposes high-level operating system services to developers. Core framework managers include:</p>
<ul>
    <li><strong><code>ActivityManager</code>:</strong> Regulates the lifecycle of visual applications and manages the global navigation back stack.</li>
    <li><strong><code>WindowManager</code>:</strong> Creates and coordinates display windows, view hierarchies, and surface layouts on screen.</li>
    <li><strong><code>PackageManager</code>:</strong> Queries installed applications, inspects manifests, and validates security permissions.</li>
    <li><strong><code>NotificationManager</code>:</strong> Posts and manages user alerts in the system notification drawer.</li>
    <li><strong><code>ContentProviders</code>:</strong> Mediates secure inter-application data sharing and database querying.</li>
</ul>

<!-- CHAPTER 3 -->
<div style="margin-top: 14px;"></div>
<div class="chapter-header">
    <div class="part-tag">PART I | ANDROID CORE ARCHITECTURE &amp; THEORY</div>
    <h2 class="chapter-title">CHAPTER 3: ANDROID STUDIO PROJECT STRUCTURE</h2>
</div>

<p class="lead-text">An Android Studio project adheres to a standardized directory layout separating executable source code, XML layouts, asset binaries, and build automation scripts.</p>

<div class="diagram-container">
    <img src="diagrams/02_project_hierarchy.svg" alt="Project Hierarchy" class="diagram-img" style="max-height: 200px;" />
    <div class="diagram-caption">Figure 3.1: Standard Android Studio Project File Organization.</div>
</div>

<h3>3.1 Filesystem Anatomy</h3>
<ul>
    <li><strong><code>app/src/main/AndroidManifest.xml</code>:</strong> The central deployment descriptor and system contract. Declares the app package name, all four components (Activities, Services, Receivers, Providers), required permissions, and hardware feature requirements.</li>
    <li><strong><code>app/src/main/java/</code>:</strong> Root directory containing all Java package directories and classes (e.g., <code>com.example.login_page.MainActivity</code>).</li>
    <li><strong><code>app/src/main/res/</code>:</strong> Directory housing static application resources:
        <ul>
            <li><code>layout/</code>: XML layout files defining the visual structure of screens (e.g., <code>activity_main.xml</code>).</li>
            <li><code>values/</code>: XML files defining constants: <code>strings.xml</code> (text), <code>colors.xml</code> (palette), <code>themes.xml</code> (styles).</li>
            <li><code>drawable/</code>: Vector drawables (XML vectors) and raster graphics (PNG/JPG).</li>
            <li><code>mipmap/</code>: App launcher icons configured across screen density buckets (mdpi to xxxhdpi).</li>
        </ul>
    </li>
    <li><strong><code>build.gradle</code>:</strong> Gradle build script defining compiler target versions, external library dependencies, and build flavors.</li>
</ul>

<h3>3.2 AAPT2 and the Compiled R Class</h3>
<p>During the compilation build phase, the Android Asset Packaging Tool 2 (AAPT2) parses every file within <code>res/</code> and compiles them into a static Java class named <code>R.java</code>. Every resource declared with an ID is assigned a static final 32-bit hexadecimal integer:</p>

<div class="box box-syntax">
    <div class="box-title">SYNTAX &amp; CODE | PROGRAMMATIC RESOURCE RESOLUTION VIA R CLASS</div>
    <pre><code>// 1. Inflating an XML layout onto an Activity window
setContentView(R.layout.activity_main);

// 2. Binding a visual UI widget by its compiled hexadecimal ID
EditText etUser = findViewById(R.id.username);
Button btnLogin = findViewById(R.id.login);

// 3. Programmatically retrieving string and color values
String appTitle = getString(R.string.app_name);
int primaryColor = getColor(R.color.blue);</code></pre>
</div>

<!-- CHAPTER 4 -->
<div style="margin-top: 14px;"></div>
<div class="chapter-header">
    <div class="part-tag">PART I | ANDROID CORE ARCHITECTURE &amp; THEORY</div>
    <h2 class="chapter-title">CHAPTER 4: ANDROID RESOURCES, QUALIFIERS &amp; SIZING UNITS</h2>
</div>

<p class="lead-text">Android devices encompass a vast range of physical screen sizes, pixel densities, and language locales. To guarantee a uniform, crisp visual presentation, Android employs abstract measurement units and configuration qualifiers.</p>

<div class="diagram-container">
    <img src="diagrams/03_resource_hierarchy.svg" alt="Resource Hierarchy" class="diagram-img" style="max-height: 200px;" />
    <div class="diagram-caption">Figure 4.1: Specialization of the res/ resource hierarchy and R-class constants.</div>
</div>

<h3>4.1 Density-Independent Units: dp versus sp</h3>
<p>Hardcoding physical pixels (<code>px</code>) causes catastrophic layout variance across devices: a 100px button on a 160 dpi screen spans ~0.62 inches, but shrinks to ~0.2 inches on a 480 dpi display. Android solves this through density-independent units:</p>

<table class="academic-table">
    <thead>
        <tr><th>Dimension Unit</th><th>Full Name</th><th>Scaling Factors</th><th>Mandatory Usage Rule</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><strong><code>dp</code> / <code>dip</code></strong></td>
            <td>Density-independent Pixels</td>
            <td>Scales with screen density based on a 160 dpi baseline ($1\text{dp} = 1\text{px}$ at 160 dpi).</td>
            <td><strong>Strictly use for layout dimensions:</strong> widths, heights, margins, padding, and borders.</td>
        </tr>
        <tr>
            <td><strong><code>sp</code></strong></td>
            <td>Scale-independent Pixels</td>
            <td>Scales with screen density <em>and</em> the user's system font accessibility scaling factor.</td>
            <td><strong>Strictly reserved for typography:</strong> <code>android:textSize</code>.</td>
        </tr>
    </tbody>
</table>

<div class="box box-concept">
    <div class="box-title">MATHEMATICAL PIXEL CONVERSION FORMULA</div>
    <p>The Android OS dynamically converts <code>dp</code> into physical screen pixels (<code>px</code>) at runtime using:</p>
    <div class="formula">px = dp &times; \left(\frac{\text{dpi}}{160}\right)</div>
    <p>Baseline densities: <strong>mdpi</strong> (160 dpi, $1\times$), <strong>hdpi</strong> (240 dpi, $1.5\times$), <strong>xhdpi</strong> (320 dpi, $2\times$), <strong>xxhdpi</strong> (480 dpi, $3\times$), <strong>xxxhdpi</strong> (640 dpi, $4\times$).</p>
</div>

<h3>4.2 Resource Configuration Qualifiers</h3>
<p>The Android runtime dynamically selects alternative resources from qualified subdirectories based on active device state:</p>
<table class="academic-table">
    <thead><tr><th>Qualifier Category</th><th>Folder Syntax</th><th>Triggering Runtime Condition</th></tr></thead>
    <tbody>
        <tr><td><strong>Orientation</strong></td><td><code>res/layout-land/</code></td><td>User rotates device into landscape mode.</td></tr>
        <tr><td><strong>Night Mode</strong></td><td><code>res/values-night/</code></td><td>User enables system-wide Dark Theme (Night mode).</td></tr>
        <tr><td><strong>Smallest Width</strong></td><td><code>res/layout-sw600dp/</code></td><td>Device screen width exceeds 600dp (standard 7-inch+ tablet).</td></tr>
        <tr><td><strong>Screen Density</strong></td><td><code>res/drawable-xxhdpi/</code></td><td>High-density screen (~480 dpi) to ensure sharp bitmap rendering.</td></tr>
        <tr><td><strong>Locale / Language</strong></td><td><code>res/values-hi/</code></td><td>Device language configured to Hindi (localized UI text).</td></tr>
    </tbody>
</table>

<!-- CHAPTER 5 & 6 -->
<div class="chapter-break"></div>
<div class="chapter-header">
    <div class="part-tag">PART I | ANDROID CORE ARCHITECTURE &amp; THEORY</div>
    <h2 class="chapter-title">CHAPTERS 5 &amp; 6: APPLICATION COMPONENTS &amp; ANDROIDMANIFEST.XML</h2>
</div>

<div class="diagram-container">
    <img src="diagrams/04_app_components.svg" alt="App Components" class="diagram-img" style="max-height: 200px;" />
    <div class="diagram-caption">Figure 5.1: The Four Core Android Application Building Blocks.</div>
</div>

<h3>5.1 The Four Fundamental Application Components</h3>
<ul>
    <li><strong>1. Activity:</strong> Represents a single visual screen with an interactive user interface (subclasses <code>AppCompatActivity</code>). It serves as the primary gateway for user interaction.</li>
    <li><strong>2. Service:</strong> A background execution component that performs long-running background tasks (e.g., audio playback, file downloading, socket polling) without providing a visual user interface.</li>
    <li><strong>3. BroadcastReceiver:</strong> A gateway component that registers to receive system-wide announcements or app broadcasts (e.g., battery low, boot completed, SMS received). It has no persistent UI and executes brief logic inside <code>onReceive()</code>.</li>
    <li><strong>4. ContentProvider:</strong> Manages a secure, structured repository of persistent app data (typically SQLite) and exposes standard CRUD interfaces (<code>query</code>, <code>insert</code>, <code>update</code>, <code>delete</code>) for cross-process data sharing across applications.</li>
</ul>

<h3>6.1 The AndroidManifest.xml Deployment Contract</h3>
<p>The <code>AndroidManifest.xml</code> file is the root deployment descriptor of an Android application. The operating system inspects this manifest prior to instantiating any component. Any component not declared in the manifest cannot be executed by the OS.</p>

<div class="box box-syntax">
    <div class="box-title">SYNTAX | COMPLETE ANDROIDMANIFEST.XML WITH INTENT FILTERS</div>
    <pre><code>&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.myapp"&gt;

    &lt;!-- System Permissions Declarations --&gt;
    &lt;uses-permission android:name="android.permission.INTERNET" /&gt;

    &lt;application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:theme="@style/Theme.AppCompat.Light"&gt;

        &lt;!-- Main Launcher Activity (Entry Point) --&gt;
        &lt;activity
            android:name=".MainActivity"
            android:exported="true"&gt;
            &lt;intent-filter&gt;
                &lt;action android:name="android.intent.action.MAIN" /&gt;
                &lt;category android:name="android.intent.category.LAUNCHER" /&gt;
            &lt;/intent-filter&gt;
        &lt;/activity&gt;

        &lt;!-- Secondary Private Activity --&gt;
        &lt;activity
            android:name=".SecondActivity"
            android:exported="false" /&gt;
    &lt;/application&gt;
&lt;/manifest&gt;</code></pre>
</div>

<!-- CHAPTER 7 -->
<div class="chapter-break"></div>
<div class="chapter-header">
    <div class="part-tag">PART I | ANDROID CORE ARCHITECTURE &amp; THEORY</div>
    <h2 class="chapter-title">CHAPTER 7: ACTIVITY &amp; ACTIVITY LIFECYCLE STATE MACHINE</h2>
</div>

<p class="lead-text">An Android Activity is governed by a deterministic, callback-driven state machine managed by the Android OS framework. As the user navigates into, away from, and back to an app, the OS transitions the Activity through distinct lifecycle states, firing corresponding callback methods.</p>

<div class="diagram-container">
    <img src="diagrams/05_activity_lifecycle.svg" alt="Activity Lifecycle Flowchart" class="diagram-img" style="max-height: 240px;" />
    <div class="diagram-caption">Figure 7.1: The Android Activity Lifecycle State Machine with Return Transitions.</div>
</div>

<h3>7.1 The Seven Lifecycle Callbacks</h3>
<ul>
    <li><strong><code>onCreate(Bundle savedInstanceState)</code>:</strong> Fired when the Activity is first instantiated in memory. Perform static initializations: inflate layout via <code>setContentView()</code>, bind view variables via <code>findViewById()</code>, and configure listener callbacks.</li>
    <li><strong><code>onStart()</code>:</strong> Fired when the Activity becomes visible to the user on screen, but is not yet interactive in the foreground.</li>
    <li><strong><code>onResume()</code>:</strong> Fired when the Activity enters the active foreground running state and begins receiving user touch input.</li>
    <li><strong><code>onPause()</code>:</strong> Fired when the Activity is partially obscured (e.g., by a dialog, incoming phone call, or split-screen mode). Pause lightweight animations or commit unsaved inputs.</li>
    <li><strong><code>onStop()</code>:</strong> Fired when the Activity is completely hidden from view. Heavy background tasks should be halted and state saved to <code>SharedPreferences</code>.</li>
    <li><strong><code>onRestart()</code>:</strong> Fired when an Activity that was previously stopped transitions back toward the visible foreground prior to <code>onStart()</code>.</li>
    <li><strong><code>onDestroy()</code>:</strong> Final cleanup hook before the Activity instance is completely purged from process RAM (called via <code>finish()</code> or OS reclaiming memory).</li>
</ul>

<div class="box box-mistake">
    <div class="box-title">COMMON MISTAKE | SuperNotCalledException</div>
    <p>Every lifecycle callback implementation in Java <strong>must</strong> invoke its parent class method (e.g. <code>super.onCreate(savedInstanceState);</code>) as its very first statement. Omitting this super call causes the runtime framework to throw a fatal <code>SuperNotCalledException</code>, crashing the app.</p>
</div>

<!-- CHAPTER 8, 9 & 10 -->
<div class="chapter-break"></div>
<div class="chapter-header">
    <div class="part-tag">PART I | ANDROID CORE ARCHITECTURE &amp; THEORY</div>
    <h2 class="chapter-title">CHAPTERS 8, 9 &amp; 10: UI WIDGETS, LAYOUT MANAGERS &amp; VIEW HIERARCHY</h2>
</div>

<div class="diagram-container">
    <img src="diagrams/06_view_hierarchy.svg" alt="View Hierarchy" class="diagram-img" style="max-height: 200px;" />
    <div class="diagram-caption">Figure 8.1: View and ViewGroup Composite Tree Hierarchy.</div>
</div>

<div class="diagram-container">
    <img src="diagrams/07_layout_hierarchy.svg" alt="Layout Hierarchy" class="diagram-img" style="max-height: 200px;" />
    <div class="diagram-caption">Figure 9.1: Child Positioning Semantics across Android Layout Managers.</div>
</div>

<h3>8.1 Fundamental UI Widgets Taxonomy</h3>
<table class="academic-table">
    <thead><tr><th>UI Component</th><th>Java Class</th><th>Primary Purpose &amp; Configuration Attributes</th></tr></thead>
    <tbody>
        <tr><td><strong>TextView</strong></td><td><code>android.widget.TextView</code></td><td>Renders read-only formatted text. Key attributes: <code>android:text</code>, <code>textSize</code>, <code>textColor</code>, <code>textStyle</code>.</td></tr>
        <tr><td><strong>EditText</strong></td><td><code>android.widget.EditText</code></td><td>User text input field. Key attributes: <code>android:hint</code>, <code>inputType="textPassword|number"</code>, <code>maxLength</code>.</td></tr>
        <tr><td><strong>Button</strong></td><td><code>android.widget.Button</code></td><td>Clickable push button that triggers action callbacks. Key attribute: <code>android:text</code>.</td></tr>
        <tr><td><strong>CheckBox</strong></td><td><code>android.widget.CheckBox</code></td><td>Two-state toggle supporting independent multi-selection. Method: <code>isChecked()</code>.</td></tr>
        <tr><td><strong>RadioButton</strong></td><td><code>android.widget.RadioButton</code></td><td>Single-choice circular option button. Must be hosted inside a <code>RadioGroup</code> to enforce mutual exclusion.</td></tr>
        <tr><td><strong>Spinner</strong></td><td><code>android.widget.Spinner</code></td><td>Compact dropdown selector populated via an <code>ArrayAdapter</code>.</td></tr>
        <tr><td><strong>ListView</strong></td><td><code>android.widget.ListView</code></td><td>Vertically scrollable collection container featuring view recycling via an adapter.</td></tr>
    </tbody>
</table>

<h3>9.1 Layout Managers Overview</h3>
<ul>
    <li><strong><code>LinearLayout</code>:</strong> Arranges child elements in a single sequential direction (<code>android:orientation="vertical"</code> or <code>"horizontal"</code>). Supports proportional spacing using <code>android:layout_weight</code>.</li>
    <li><strong><code>RelativeLayout</code>:</strong> Arranges child elements relative to their parent container boundaries (e.g. <code>alignParentTop="true"</code>) or relative to sibling views (e.g. <code>layout_below="@id/header"</code>).</li>
    <li><strong><code>ConstraintLayout</code>:</strong> Flexible, flat layout manager that positions widgets using dual-axis constraints anchored to parent edges or sibling guidelines, eliminating costly view nesting.</li>
    <li><strong><code>ScrollView</code>:</strong> A container providing vertical scrolling when child content exceeds physical screen boundaries. <em>Mandatory Rule: A ScrollView can host strictly one direct child ViewGroup!</em></li>
</ul>

<h3>9.2 Core XML Layout Attribute Comparisons</h3>
<table class="academic-table">
    <thead><tr><th>Comparison</th><th>First Option</th><th>Second Option</th><th>Key Difference &amp; Usage Rule</th></tr></thead>
    <tbody>
        <tr>
            <td><strong><code>padding</code> vs <code>margin</code></strong></td>
            <td><code>android:padding</code>: Internal spacing inside view perimeter.</td>
            <td><code>android:layout_margin</code>: External spacing outside view border.</td>
            <td>Padding expands touchable area; margin creates distance between sibling views.</td>
        </tr>
        <tr>
            <td><strong><code>gravity</code> vs <code>layout_gravity</code></strong></td>
            <td><code>android:gravity</code>: Aligns content <em>inside</em> the view (e.g., text in button).</td>
            <td><code>android:layout_gravity</code>: Aligns the <em>view itself</em> inside its parent container.</td>
            <td>Gravity controls internal alignment; layout_gravity controls external container placement.</td>
        </tr>
        <tr>
            <td><strong><code>match_parent</code> vs <code>wrap_content</code></strong></td>
            <td><code>match_parent</code>: Expands view to occupy 100% of available parent dimension.</td>
            <td><code>wrap_content</code>: Shrinks view to encompass only its internal content.</td>
            <td>Use <code>match_parent</code> for full-width inputs; use <code>wrap_content</code> for buttons and labels.</td>
        </tr>
    </tbody>
</table>

<!-- CHAPTER 11 & 12 -->
<div class="chapter-break"></div>
<div class="chapter-header">
    <div class="part-tag">PART I | ANDROID CORE ARCHITECTURE &amp; THEORY</div>
    <h2 class="chapter-title">CHAPTERS 11 &amp; 12: EVENT HANDLING &amp; INTENT MESSAGING</h2>
</div>

<div class="diagram-container">
    <img src="diagrams/08_explicit_intent.svg" alt="Explicit Intent" class="diagram-img" style="max-height: 200px;" />
    <div class="diagram-caption">Figure 12.1: Explicit Intent Navigation between Activity 1 and Activity 2.</div>
</div>

<div class="diagram-container">
    <img src="diagrams/09_implicit_intent.svg" alt="Implicit Intent" class="diagram-img" style="max-height: 200px;" />
    <div class="diagram-caption">Figure 12.2: Implicit Intent Resolution through the Android OS PackageManager.</div>
</div>

<h3>11.1 Event Handling Architecture</h3>
<p>User interactions (taps, text input, selections) generate asynchronous event objects dispatched to registered listener interfaces:</p>

<div class="box box-syntax">
    <div class="box-title">SYNTAX | ANONYMOUS ONCLICKLISTENER REGISTRATION</div>
    <pre><code>Button btn = findViewById(R.id.btnSubmit);
btn.setOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View v) {
        // Asynchronous touch callback executed on the UI Thread
        Toast.makeText(MainActivity.this, "Action Triggered", Toast.LENGTH_SHORT).show();
    }
});</code></pre>
</div>

<h3>12.1 Explicit versus Implicit Intents</h3>
<table class="academic-table">
    <thead><tr><th>Criteria</th><th>Explicit Intent</th><th>Implicit Intent</th></tr></thead>
    <tbody>
        <tr><td><strong>Definition</strong></td><td>Directly designates the exact target Java class in the local package.</td><td>Declares an abstract <strong>Action</strong> and <strong>Data URI</strong> for external handling.</td></tr>
        <tr><td><strong>Syntax</strong></td><td><code>new Intent(this, SecondActivity.class)</code></td><td><code>new Intent(Intent.ACTION_VIEW, Uri.parse("https://cet.ac.in"))</code></td></tr>
        <tr><td><strong>Target Component</strong></td><td>Known, internal application screen.</td><td>Any external installed application registered to handle the action.</td></tr>
        <tr><td><strong>Security &amp; Resolution</strong></td><td>Deterministic; resolved instantly within the app sandbox.</td><td>Resolved dynamically by the OS <code>PackageManager</code> via Intent Filters.</td></tr>
        <tr><td><strong>Failure Mode</strong></td><td>Fails at compile-time if class missing.</td><td>Throws <code>ActivityNotFoundException</code> if no matching app exists (wrap in try-catch).</td></tr>
    </tbody>
</table>

<h3>12.2 Data Transfer via Intent Extras Bundle</h3>
<p>Intents transfer primitive and serializable data across Activity boundaries using an internal <code>Bundle</code> payload:</p>
<div class="box box-syntax">
    <div class="box-title">SYNTAX | ATTACHING AND EXTRACTING INTENT EXTRAS</div>
    <pre><code>// 1. Sender Activity (Packing Data)
Intent intent = new Intent(MainActivity.this, HomeActivity.class);
intent.putExtra("USER_KEY", username);
intent.putExtra("AGE_KEY", 22);
startActivity(intent);

// 2. Receiver Activity (Unpacking Data in onCreate)
Intent receivedIntent = getIntent();
String user = receivedIntent.getStringExtra("USER_KEY");
int age = receivedIntent.getIntExtra("AGE_KEY", 0); // Requires default value for primitives</code></pre>
</div>

<!-- CHAPTER 13, 14 & 15 -->
<div class="chapter-break"></div>
<div class="chapter-header">
    <div class="part-tag">PART I | ANDROID CORE ARCHITECTURE &amp; THEORY</div>
    <h2 class="chapter-title">CHAPTERS 13, 14 &amp; 15: SHAREDPREFERENCES, ADAPTERS &amp; STORAGE</h2>
</div>

<div class="diagram-container">
    <img src="diagrams/12_shared_preferences_flow.svg" alt="SharedPreferences Flow" class="diagram-img" style="max-height: 200px;" />
    <div class="diagram-caption">Figure 13.1: SharedPreferences Key-Value Storage Architecture.</div>
</div>

<div class="diagram-container">
    <img src="diagrams/13_listview_adapter.svg" alt="ListView Adapter Flow" class="diagram-img" style="max-height: 200px;" />
    <div class="diagram-caption">Figure 14.1: Adapter Bridge between Java Collections and AdapterView rows.</div>
</div>

<h3>13.1 SharedPreferences API</h3>
<p><code>SharedPreferences</code> stores primitive key-value pairs (String, int, boolean, float, long) in private XML files located under <code>/data/data/&lt;package_name&gt;/shared_prefs/</code>. Ideal for session tokens, user settings, and remember-me states.</p>

<div class="box box-syntax">
    <div class="box-title">SYNTAX | SHAREDPREFERENCES CRUD OPERATIONS</div>
    <pre><code>// Opening Preferences in Private Mode
SharedPreferences sp = getSharedPreferences("UserSession", MODE_PRIVATE);

// Writing Data
sp.edit()
  .putString("USERNAME", "akhil")
  .putBoolean("IS_LOGGED_IN", true)
  .apply(); // Asynchronous disk write (safe for UI thread)

// Reading Data (with fallback defaults)
String user = sp.getString("USERNAME", "Guest");
boolean logged = sp.getBoolean("IS_LOGGED_IN", false);

// Clearing Session Data
sp.edit().clear().apply();</code></pre>
</div>

<h3>14.1 The Adapter Pattern &amp; View Recycling</h3>
<p>An <strong>Adapter</strong> acts as a structural bridge between an in-memory data collection (such as an <code>ArrayList&lt;String&gt;</code>) and an <code>AdapterView</code> (such as <code>ListView</code> or <code>Spinner</code>). To conserve memory, Android recycles views: rather than creating 1,000 views for a 1,000-item list, the framework only instantiates enough views to fill the physical screen (~10 views) and re-binds them as the user scrolls.</p>

<h3>15.1 Android Storage Options Comparison</h3>
<table class="academic-table">
    <thead><tr><th>Storage Mechanism</th><th>Data Format</th><th>File Visibility</th><th>Lifecycle Persistence</th><th>Ideal Use Case</th></tr></thead>
    <tbody>
        <tr><td><strong>SharedPreferences</strong></td><td>Key-Value XML</td><td>Private to App</td><td>Persistent until app data cleared.</td><td>User preferences, flags, auth tokens.</td></tr>
        <tr><td><strong>Internal Storage</strong></td><td>Raw files / caches</td><td>Private to App</td><td>Persistent until uninstalled.</td><td>Private app documents, temporary cache files.</td></tr>
        <tr><td><strong>External Storage</strong></td><td>Scoped Media files</td><td>Public / Scoped</td><td>Persistent (user-managed).</td><td>Photos, videos, shared PDF documents.</td></tr>
        <tr><td><strong>SQLite / Room</strong></td><td>Relational SQL DB</td><td>Private to App</td><td>Persistent structured data.</td><td>Complex datasets, offline caching, catalogs.</td></tr>
    </tbody>
</table>

<!-- CHAPTER 16, 17, 18 & 19 -->
<div style="margin-top: 14px;"></div>
<div class="chapter-header">
    <div class="part-tag">PART I | ANDROID CORE ARCHITECTURE &amp; THEORY</div>
    <h2 class="chapter-title">CHAPTERS 16 - 19: FORMS, MENUS, PERMISSIONS &amp; DEBUGGING</h2>
</div>

<h3>16.1 Form Validation Best Practices</h3>
<p>Defensive validation prevents invalid data submissions and avoids runtime exceptions:</p>
<div class="box box-syntax">
    <div class="box-title">SYNTAX | INPUT VALIDATION AND VISUAL ERROR BADGES</div>
    <pre><code>String user = etUser.getText().toString().trim();
String pass = etPass.getText().toString();

if (user.isEmpty()) {
    etUser.setError("Username is required");
    etUser.requestFocus();
    return;
}
if (pass.length() &lt; 4) {
    etPass.setError("Password must be at least 4 characters");
    etPass.requestFocus();
    return;
}</code></pre>
</div>

<h3>17.1 Dialogs and Menus</h3>
<ul>
    <li><strong>AlertDialog:</strong> Modal popup dialog constructed using the builder pattern:
        <pre><code>new AlertDialog.Builder(this)
    .setTitle("Exit Application")
    .setMessage("Are you sure you want to log out?")
    .setPositiveButton("Yes", (dialog, which) -> finish())
    .setNegativeButton("No", null)
    .show();</code></pre>
    </li>
    <li><strong>Notification Channels (API 26+):</strong> All notifications must be posted to a registered <code>NotificationChannel</code> specifying importance levels.</li>
</ul>

<h3>18.1 Android Security &amp; Permissions</h3>
<ul>
    <li><strong>Normal Permissions:</strong> Declared in <code>AndroidManifest.xml</code> (e.g. <code>INTERNET</code>). Automatically granted at install time.</li>
    <li><strong>Dangerous Permissions:</strong> Access sensitive hardware or user data (e.g. <code>CAMERA</code>, <code>ACCESS_FINE_LOCATION</code>). Must be requested dynamically at runtime using <code>requestPermissions()</code> on API 23+.</li>
</ul>

<h3>19.1 Debugging with Logcat</h3>
<p>Logcat records system and application diagnostic output across five priority levels:</p>
<ul>
    <li><code>Log.v(TAG, msg);</code> &mdash; <strong>Verbose:</strong> Detailed low-level diagnostic tracing.</li>
    <li><code>Log.d(TAG, msg);</code> &mdash; <strong>Debug:</strong> General developer diagnostic information.</li>
    <li><code>Log.i(TAG, msg);</code> &mdash; <strong>Info:</strong> Informational application milestones.</li>
    <li><code>Log.w(TAG, msg);</code> &mdash; <strong>Warning:</strong> Non-fatal unexpected conditions.</li>
    <li><code>Log.e(TAG, msg);</code> &mdash; <strong>Error:</strong> Critical exceptions and application errors.</li>
</ul>
'''
