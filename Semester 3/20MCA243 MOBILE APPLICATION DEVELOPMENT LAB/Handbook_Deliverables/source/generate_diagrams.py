"""
Vector Diagram Generator for Android Programming Handbook
Generates 20 clean, publication-quality technical SVG diagrams.
"""

import os

DIAGRAMS_DIR = os.path.join(os.path.dirname(__file__), "diagrams")
os.makedirs(DIAGRAMS_DIR, exist_ok=True)

def create_svg(filename, width, height, content):
    filepath = os.path.join(DIAGRAMS_DIR, filename)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" style="max-width: {width}px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
<defs>
    <linearGradient id="gradPrimary" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#1565C0" />
        <stop offset="100%" stop-color="#1E88E5" />
    </linearGradient>
    <linearGradient id="gradAccent" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#2E7D32" />
        <stop offset="100%" stop-color="#43A047" />
    </linearGradient>
    <linearGradient id="gradOrange" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#E65100" />
        <stop offset="100%" stop-color="#F57C00" />
    </linearGradient>
    <linearGradient id="gradPurple" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#6A1B9A" />
        <stop offset="100%" stop-color="#8E24AA" />
    </linearGradient>
    <linearGradient id="gradTeal" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#00695C" />
        <stop offset="100%" stop-color="#00897B" />
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
        <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#000000" flood-opacity="0.12" />
    </filter>
</defs>
{content}
</svg>'''
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg)
    return filepath

# 1. Android Architecture
d1 = '''
<rect width="700" height="420" fill="#F8FAFC" rx="10" stroke="#CBD5E1" stroke-width="1.5" />
<text x="350" y="32" font-size="18" font-weight="bold" fill="#0F172A" text-anchor="middle">Android 5-Tier System Architecture</text>

<!-- Applications -->
<rect x="50" y="55" width="600" height="50" rx="6" fill="url(#gradPrimary)" filter="url(#shadow)" />
<text x="350" y="85" font-size="15" font-weight="bold" fill="#FFFFFF" text-anchor="middle">System &amp; User Applications (Home, Contacts, Phone, Browser, Custom Apps)</text>

<!-- Application Framework -->
<rect x="50" y="115" width="600" height="65" rx="6" fill="url(#gradAccent)" filter="url(#shadow)" />
<text x="350" y="138" font-size="15" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Application Framework (Java / Kotlin APIs)</text>
<text x="350" y="162" font-size="12" fill="#E8F5E9" text-anchor="middle">Activity Manager | Window Manager | Content Providers | View System | Notification Manager | Resource Manager</text>

<!-- Libraries & Runtime -->
<g filter="url(#shadow)">
    <rect x="50" y="190" width="290" height="65" rx="6" fill="url(#gradPurple)" />
    <text x="195" y="215" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Native C/C++ Libraries</text>
    <text x="195" y="238" font-size="11" fill="#F3E5F5" text-anchor="middle">SQLite | OpenGL ES | WebKit | Media | SSL</text>

    <rect x="360" y="190" width="290" height="65" rx="6" fill="url(#gradTeal)" />
    <text x="505" y="215" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Android Runtime (ART)</text>
    <text x="505" y="238" font-size="11" fill="#E0F2F1" text-anchor="middle">AOT/JIT Compilation | DEX Bytecode | Core Libs</text>
</g>

<!-- Hardware Abstraction Layer -->
<rect x="50" y="265" width="600" height="55" rx="6" fill="url(#gradOrange)" filter="url(#shadow)" />
<text x="350" y="290" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Hardware Abstraction Layer (HAL)</text>
<text x="350" y="308" font-size="12" fill="#FFF3E0" text-anchor="middle">Camera | Audio | Bluetooth | Sensors | Wi-Fi | GPS Drivers Interface</text>

<!-- Linux Kernel -->
<rect x="50" y="330" width="600" height="65" rx="6" fill="#374151" filter="url(#shadow)" />
<text x="350" y="355" font-size="15" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Linux Kernel</text>
<text x="350" y="378" font-size="12" fill="#D1D5DB" text-anchor="middle">Display Driver | Camera Driver | Bluetooth Driver | Shared Memory | Binder IPC | Power Management</text>
'''
create_svg("01_android_architecture.svg", 700, 420, d1)

# 2. Project Hierarchy
d2 = '''
<rect width="650" height="380" fill="#F8FAFC" rx="10" stroke="#CBD5E1" stroke-width="1.5" />
<text x="325" y="30" font-size="16" font-weight="bold" fill="#0F172A" text-anchor="middle">Android Studio Project Structure</text>

<g font-size="13" font-family="Consolas, monospace" fill="#1E293B">
    <rect x="40" y="55" width="570" height="300" rx="8" fill="#FFFFFF" stroke="#E2E8F0" />
    <text x="60" y="85" font-weight="bold" fill="#1565C0">MyApplication/</text>
    <text x="90" y="110" fill="#0F172A">|-- manifests/          -&gt; <tspan fill="#64748B">AndroidManifest.xml (Permissions, Activities)</tspan></text>
    <text x="90" y="135" fill="#0F172A">|-- java/               -&gt; <tspan fill="#64748B">Java/Kotlin source packages</tspan></text>
    <text x="120" y="160" fill="#2E7D32">\-- com.example.app/    -&gt; MainActivity.java (Business logic)</text>
    <text x="90" y="185" fill="#0F172A">|-- res/                -&gt; <tspan fill="#64748B">Application resources (Assets &amp; XML)</tspan></text>
    <text x="120" y="210" fill="#D97706">|-- drawable/           -&gt; Icons, shapes, background XMLs</text>
    <text x="120" y="235" fill="#D97706">|-- layout/             -&gt; activity_main.xml (UI layouts)</text>
    <text x="120" y="260" fill="#D97706">|-- mipmap/             -&gt; App launcher icons (mdpi, hdpi, xhdpi)</text>
    <text x="120" y="285" fill="#D97706">\-- values/             -&gt; strings.xml, colors.xml, themes.xml</text>
    <text x="90" y="315" fill="#0F172A">\-- Gradle Scripts/     -&gt; <tspan fill="#64748B">build.gradle.kts, settings.gradle.kts</tspan></text>
</g>
'''
create_svg("02_project_hierarchy.svg", 650, 380, d2)

# 3. Resource Hierarchy
d3 = '''
<rect width="680" height="340" fill="#F8FAFC" rx="10" stroke="#CBD5E1" stroke-width="1.5" />
<text x="340" y="30" font-size="16" font-weight="bold" fill="#0F172A" text-anchor="middle">Android Resource Subdirectories (res/)</text>

<g transform="translate(40, 55)">
    <rect x="0" y="0" width="180" height="110" rx="6" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5" />
    <text x="90" y="30" font-size="14" font-weight="bold" fill="#1D4ED8" text-anchor="middle">res/layout/</text>
    <text x="90" y="55" font-size="11" fill="#475569" text-anchor="middle">XML UI Design</text>
    <text x="90" y="75" font-size="11" fill="#64748B" text-anchor="middle">activity_main.xml</text>
    <text x="90" y="95" font-size="10" font-family="monospace" fill="#0F172A" text-anchor="middle">R.layout.activity_main</text>

    <rect x="210" y="0" width="180" height="110" rx="6" fill="#F0FDF4" stroke="#22C55E" stroke-width="1.5" />
    <text x="300" y="30" font-size="14" font-weight="bold" fill="#15803D" text-anchor="middle">res/values/</text>
    <text x="300" y="55" font-size="11" fill="#475569" text-anchor="middle">Constants &amp; Themes</text>
    <text x="300" y="75" font-size="11" fill="#64748B" text-anchor="middle">strings.xml, colors.xml</text>
    <text x="300" y="95" font-size="10" font-family="monospace" fill="#0F172A" text-anchor="middle">R.string.app_name</text>

    <rect x="420" y="0" width="180" height="110" rx="6" fill="#FEF3C7" stroke="#F59E0B" stroke-width="1.5" />
    <text x="510" y="30" font-size="14" font-weight="bold" fill="#B45309" text-anchor="middle">res/drawable/</text>
    <text x="510" y="55" font-size="11" fill="#475569" text-anchor="middle">Graphics &amp; Shapes</text>
    <text x="510" y="75" font-size="11" fill="#64748B" text-anchor="middle">btn_bg.xml, logo.png</text>
    <text x="510" y="95" font-size="10" font-family="monospace" fill="#0F172A" text-anchor="middle">R.drawable.btn_bg</text>

    <rect x="105" y="135" width="180" height="110" rx="6" fill="#F3E8FF" stroke="#A855F7" stroke-width="1.5" />
    <text x="195" y="165" font-size="14" font-weight="bold" fill="#7E22CE" text-anchor="middle">res/mipmap/</text>
    <text x="195" y="190" font-size="11" fill="#475569" text-anchor="middle">Launcher Icons</text>
    <text x="195" y="210" font-size="11" fill="#64748B" text-anchor="middle">ic_launcher (densities)</text>
    <text x="195" y="230" font-size="10" font-family="monospace" fill="#0F172A" text-anchor="middle">R.mipmap.ic_launcher</text>

    <rect x="315" y="135" width="180" height="110" rx="6" fill="#CCFBF1" stroke="#14B8A6" stroke-width="1.5" />
    <text x="405" y="165" font-size="14" font-weight="bold" fill="#0F766E" text-anchor="middle">res/menu/ &amp; xml/</text>
    <text x="405" y="190" font-size="11" fill="#475569" text-anchor="middle">Menus &amp; Config</text>
    <text x="405" y="210" font-size="11" fill="#64748B" text-anchor="middle">options_menu.xml</text>
    <text x="405" y="230" font-size="10" font-family="monospace" fill="#0F172A" text-anchor="middle">R.menu.options_menu</text>
</g>
'''
create_svg("03_resource_hierarchy.svg", 680, 340, d3)

# 4. Application Components
d4 = '''
<rect width="700" height="340" fill="#F8FAFC" rx="10" stroke="#CBD5E1" stroke-width="1.5" />
<text x="350" y="32" font-size="16" font-weight="bold" fill="#0F172A" text-anchor="middle">The 4 Core Android Application Components</text>

<g transform="translate(35, 55)">
    <!-- Activity -->
    <rect x="0" y="0" width="145" height="240" rx="8" fill="#EFF6FF" stroke="#2563EB" stroke-width="2" />
    <circle cx="72" cy="35" r="20" fill="#2563EB" />
    <text x="72" y="42" font-size="18" fill="#FFFFFF" text-anchor="middle">📱</text>
    <text x="72" y="75" font-size="15" font-weight="bold" fill="#1E40AF" text-anchor="middle">Activity</text>
    <text x="72" y="100" font-size="11" font-weight="bold" fill="#475569" text-anchor="middle">Single UI Screen</text>
    <text x="72" y="125" font-size="10.5" fill="#334155" text-anchor="middle">Provides the user</text>
    <text x="72" y="140" font-size="10.5" fill="#334155" text-anchor="middle">interface window.</text>
    <text x="72" y="165" font-size="10" fill="#64748B" text-anchor="middle">Extends Activity</text>
    <text x="72" y="180" font-size="10" fill="#64748B" text-anchor="middle">or AppCompatActivity</text>
    <text x="72" y="215" font-size="10" font-weight="bold" fill="#2563EB" text-anchor="middle">Has Lifecycle</text>

    <!-- Service -->
    <rect x="160" y="0" width="145" height="240" rx="8" fill="#F0FDF4" stroke="#16A34A" stroke-width="2" />
    <circle cx="232" cy="35" r="20" fill="#16A34A" />
    <text x="232" y="42" font-size="18" fill="#FFFFFF" text-anchor="middle">⚙️</text>
    <text x="232" y="75" font-size="15" font-weight="bold" fill="#166534" text-anchor="middle">Service</text>
    <text x="232" y="100" font-size="11" font-weight="bold" fill="#475569" text-anchor="middle">Background Tasks</text>
    <text x="232" y="125" font-size="10.5" fill="#334155" text-anchor="middle">Runs without UI</text>
    <text x="232" y="140" font-size="10.5" fill="#334155" text-anchor="middle">for long tasks.</text>
    <text x="232" y="165" font-size="10" fill="#64748B" text-anchor="middle">Music playback,</text>
    <text x="232" y="180" font-size="10" fill="#64748B" text-anchor="middle">data download</text>
    <text x="232" y="215" font-size="10" font-weight="bold" fill="#16A34A" text-anchor="middle">Started / Bound</text>

    <!-- Broadcast Receiver -->
    <rect x="320" y="0" width="145" height="240" rx="8" fill="#FFF7ED" stroke="#EA580C" stroke-width="2" />
    <circle cx="392" cy="35" r="20" fill="#EA580C" />
    <text x="392" y="42" font-size="18" fill="#FFFFFF" text-anchor="middle">📡</text>
    <text x="392" y="75" font-size="14" font-weight="bold" fill="#9A3412" text-anchor="middle">Broadcast</text>
    <text x="392" y="90" font-size="14" font-weight="bold" fill="#9A3412" text-anchor="middle">Receiver</text>
    <text x="392" y="115" font-size="11" font-weight="bold" fill="#475569" text-anchor="middle">System Events</text>
    <text x="392" y="135" font-size="10.5" fill="#334155" text-anchor="middle">Listens for battery low,</text>
    <text x="392" y="150" font-size="10.5" fill="#334155" text-anchor="middle">boot done, SMS</text>
    <text x="392" y="175" font-size="10" fill="#64748B" text-anchor="middle">onReceive(Context, Intent)</text>
    <text x="392" y="215" font-size="10" font-weight="bold" fill="#EA580C" text-anchor="middle">Event Gateway</text>

    <!-- Content Provider -->
    <rect x="480" y="0" width="145" height="240" rx="8" fill="#FAF5FF" stroke="#9333EA" stroke-width="2" />
    <circle cx="552" cy="35" r="20" fill="#9333EA" />
    <text x="552" y="42" font-size="18" fill="#FFFFFF" text-anchor="middle">🗄️</text>
    <text x="552" y="75" font-size="14" font-weight="bold" fill="#6B21A8" text-anchor="middle">Content</text>
    <text x="552" y="90" font-size="14" font-weight="bold" fill="#6B21A8" text-anchor="middle">Provider</text>
    <text x="552" y="115" font-size="11" font-weight="bold" fill="#475569" text-anchor="middle">Data Sharing</text>
    <text x="552" y="135" font-size="10.5" fill="#334155" text-anchor="middle">Manages structured</text>
    <text x="552" y="150" font-size="10.5" fill="#334155" text-anchor="middle">data between apps</text>
    <text x="552" y="175" font-size="10" fill="#64748B" text-anchor="middle">Contacts, MediaStore</text>
    <text x="552" y="215" font-size="10" font-weight="bold" fill="#9333EA" text-anchor="middle">URI Access</text>
</g>
'''
create_svg("04_app_components.svg", 700, 340, d4)

# 5. Activity Lifecycle Flowchart
d5 = '''
<rect width="600" height="580" fill="#F8FAFC" rx="10" stroke="#CBD5E1" stroke-width="1.5" />
<text x="300" y="28" font-size="16" font-weight="bold" fill="#0F172A" text-anchor="middle">Android Activity Lifecycle State Machine</text>

<!-- Markers -->
<defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1 L 8 5 L 0 9 z" fill="#475569" />
    </marker>
</defs>

<!-- Nodes -->
<rect x="220" y="45" width="160" height="35" rx="17" fill="#64748B" />
<text x="300" y="67" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Activity Launched</text>

<line x1="300" y1="80" x2="300" y2="105" stroke="#475569" stroke-width="2" marker-end="url(#arrow)" />

<rect x="210" y="105" width="180" height="40" rx="6" fill="#2563EB" />
<text x="300" y="130" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">onCreate()</text>

<line x1="300" y1="145" x2="300" y2="170" stroke="#475569" stroke-width="2" marker-end="url(#arrow)" />

<rect x="210" y="170" width="180" height="40" rx="6" fill="#2563EB" />
<text x="300" y="195" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">onStart()</text>

<line x1="300" y1="210" x2="300" y2="235" stroke="#475569" stroke-width="2" marker-end="url(#arrow)" />

<rect x="210" y="235" width="180" height="40" rx="6" fill="#2563EB" />
<text x="300" y="260" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">onResume()</text>

<line x1="300" y1="275" x2="300" y2="300" stroke="#475569" stroke-width="2" marker-end="url(#arrow)" />

<!-- Resumed Active State -->
<rect x="180" y="300" width="240" height="45" rx="22" fill="#16A34A" />
<text x="300" y="327" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Activity Running (Foreground)</text>

<line x1="300" y1="345" x2="300" y2="370" stroke="#475569" stroke-width="2" marker-end="url(#arrow)" />

<rect x="210" y="370" width="180" height="40" rx="6" fill="#D97706" />
<text x="300" y="395" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">onPause()</text>

<line x1="300" y1="410" x2="300" y2="435" stroke="#475569" stroke-width="2" marker-end="url(#arrow)" />

<rect x="210" y="435" width="180" height="40" rx="6" fill="#DC2626" />
<text x="300" y="460" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">onStop()</text>

<line x1="300" y1="475" x2="300" y2="500" stroke="#475569" stroke-width="2" marker-end="url(#arrow)" />

<rect x="210" y="500" width="180" height="40" rx="6" fill="#991B1B" />
<text x="300" y="525" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">onDestroy()</text>

<line x1="300" y1="540" x2="300" y2="555" stroke="#475569" stroke-width="2" marker-end="url(#arrow)" />
<rect x="220" y="555" width="160" height="20" rx="10" fill="#334155" />
<text x="300" y="569" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Activity Shut Down</text>

<!-- Return Loops -->
<!-- onPause -> onResume -->
<path d="M 390 390 Q 480 390 480 325 Q 480 255 395 255" fill="none" stroke="#D97706" stroke-width="1.8" stroke-dasharray="4,3" marker-end="url(#arrow)" />
<text x="485" y="325" font-size="10.5" fill="#D97706">User returns</text>

<!-- onStop -> onRestart -> onStart -->
<path d="M 210 455 Q 80 455 80 315 Q 80 190 205 190" fill="none" stroke="#2563EB" stroke-width="1.8" stroke-dasharray="4,3" marker-end="url(#arrow)" />
<rect x="40" y="305" width="80" height="28" rx="4" fill="#EFF6FF" stroke="#2563EB" />
<text x="80" y="323" font-size="10" font-weight="bold" fill="#1E40AF" text-anchor="middle">onRestart()</text>
'''
create_svg("05_activity_lifecycle.svg", 600, 580, d5)

# 6. View & ViewGroup Composite Hierarchy
d6 = '''
<rect width="660" height="360" fill="#F8FAFC" rx="10" stroke="#CBD5E1" stroke-width="1.5" />
<text x="330" y="28" font-size="16" font-weight="bold" fill="#0F172A" text-anchor="middle">View and ViewGroup Composite Hierarchy</text>

<!-- Window & DecorView -->
<rect x="180" y="45" width="300" height="40" rx="6" fill="#1E293B" />
<text x="330" y="70" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">PhoneWindow / DecorView (Root)</text>

<line x1="330" y1="85" x2="330" y2="115" stroke="#64748B" stroke-width="2" marker-end="url(#arrow)" />

<!-- Root ViewGroup -->
<rect x="160" y="115" width="340" height="45" rx="6" fill="#2563EB" />
<text x="330" y="142" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Root ViewGroup (LinearLayout / ConstraintLayout)</text>

<!-- Branches to child viewgroups and views -->
<path d="M 240 160 L 140 200" stroke="#64748B" stroke-width="2" marker-end="url(#arrow)" />
<path d="M 330 160 L 330 200" stroke="#64748B" stroke-width="2" marker-end="url(#arrow)" />
<path d="M 420 160 L 520 200" stroke="#64748B" stroke-width="2" marker-end="url(#arrow)" />

<!-- Child 1: ViewGroup -->
<rect x="60" y="200" width="160" height="45" rx="6" fill="#3B82F6" />
<text x="140" y="222" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Child ViewGroup</text>
<text x="140" y="238" font-size="10" fill="#E0E7FF" text-anchor="middle">(Horizontal LinearLayout)</text>

<!-- Child 2: View -->
<rect x="250" y="200" width="160" height="45" rx="6" fill="#10B981" />
<text x="330" y="222" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">View (Widget)</text>
<text x="330" y="238" font-size="10" fill="#ECFDF5" text-anchor="middle">EditText / TextView</text>

<!-- Child 3: View -->
<rect x="440" y="200" width="160" height="45" rx="6" fill="#10B981" />
<text x="520" y="222" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">View (Widget)</text>
<text x="520" y="238" font-size="10" fill="#ECFDF5" text-anchor="middle">Button (Login)</text>

<!-- Sub-child Views under Child 1 -->
<path d="M 100 245 L 80 280" stroke="#64748B" stroke-width="1.5" marker-end="url(#arrow)" />
<path d="M 180 245 L 200 280" stroke="#64748B" stroke-width="1.5" marker-end="url(#arrow)" />

<rect x="20" y="280" width="110" height="35" rx="4" fill="#059669" />
<text x="75" y="302" font-size="11" fill="#FFFFFF" text-anchor="middle">RadioButton 1</text>

<rect x="150" y="280" width="110" height="35" rx="4" fill="#059669" />
<text x="205" y="302" font-size="11" fill="#FFFFFF" text-anchor="middle">RadioButton 2</text>
'''
create_svg("06_view_hierarchy.svg", 660, 360, d6)

# 7. Layout Hierarchy & Comparison
d7 = '''
<rect width="680" height="340" fill="#F8FAFC" rx="10" stroke="#CBD5E1" stroke-width="1.5" />
<text x="340" y="28" font-size="16" font-weight="bold" fill="#0F172A" text-anchor="middle">Android Layout Types &amp; Child View Positioning</text>

<g transform="translate(30, 50)">
    <!-- LinearLayout Vertical -->
    <rect x="0" y="0" width="190" height="120" rx="6" fill="#FFFFFF" stroke="#94A3B8" stroke-width="1.5" />
    <text x="95" y="20" font-size="12" font-weight="bold" fill="#1E293B" text-anchor="middle">LinearLayout (Vertical)</text>
    <rect x="15" y="30" width="160" height="22" rx="3" fill="#BFDBFE" />
    <rect x="15" y="58" width="160" height="22" rx="3" fill="#93C5FD" />
    <rect x="15" y="86" width="160" height="22" rx="3" fill="#60A5FA" />

    <!-- LinearLayout Horizontal -->
    <rect x="215" y="0" width="190" height="120" rx="6" fill="#FFFFFF" stroke="#94A3B8" stroke-width="1.5" />
    <text x="310" y="20" font-size="12" font-weight="bold" fill="#1E293B" text-anchor="middle">LinearLayout (Horizontal)</text>
    <rect x="230" y="35" width="45" height="70" rx="3" fill="#BBF7D0" />
    <rect x="288" y="35" width="45" height="70" rx="3" fill="#86EFAC" />
    <rect x="345" y="35" width="45" height="70" rx="3" fill="#4ADE80" />

    <!-- RelativeLayout -->
    <rect x="430" y="0" width="190" height="120" rx="6" fill="#FFFFFF" stroke="#94A3B8" stroke-width="1.5" />
    <text x="525" y="20" font-size="12" font-weight="bold" fill="#1E293B" text-anchor="middle">RelativeLayout</text>
    <rect x="445" y="35" width="80" height="30" rx="3" fill="#FED7AA" />
    <rect x="510" y="75" width="95" height="30" rx="3" fill="#FDBA74" />

    <!-- ConstraintLayout -->
    <rect x="105" y="140" width="200" height="125" rx="6" fill="#FFFFFF" stroke="#94A3B8" stroke-width="1.5" />
    <text x="205" y="160" font-size="12" font-weight="bold" fill="#1E293B" text-anchor="middle">ConstraintLayout (Flexible)</text>
    <rect x="155" y="180" width="100" height="35" rx="4" fill="#DDD6FE" stroke="#8B5CF6" stroke-dasharray="2,2" />
    <line x1="105" y1="197" x2="155" y2="197" stroke="#8B5CF6" stroke-width="1" />
    <line x1="255" y1="197" x2="305" y2="197" stroke="#8B5CF6" stroke-width="1" />
    <text x="205" y="202" font-size="11" fill="#5B21B6" text-anchor="middle">app:layout_to...</text>

    <!-- FrameLayout -->
    <rect x="330" y="140" width="200" height="125" rx="6" fill="#FFFFFF" stroke="#94A3B8" stroke-width="1.5" />
    <text x="430" y="160" font-size="12" font-weight="bold" fill="#1E293B" text-anchor="middle">FrameLayout (Stacking)</text>
    <rect x="355" y="175" width="150" height="75" rx="4" fill="#FEF08A" />
    <rect x="380" y="190" width="100" height="45" rx="4" fill="#FACC15" />
</g>
'''
create_svg("07_layout_hierarchy.svg", 680, 340, d7)

# 8. Explicit Intent Navigation Flow
d8 = '''
<rect width="650" height="260" fill="#F8FAFC" rx="10" stroke="#CBD5E1" stroke-width="1.5" />
<text x="325" y="28" font-size="16" font-weight="bold" fill="#0F172A" text-anchor="middle">Explicit Intent: Two-Activity Navigation Flow</text>

<g transform="translate(40, 55)">
    <!-- Activity 1 -->
    <rect x="0" y="0" width="210" height="160" rx="8" fill="#EFF6FF" stroke="#2563EB" stroke-width="2" />
    <text x="105" y="30" font-size="14" font-weight="bold" fill="#1D4ED8" text-anchor="middle">MainActivity</text>
    <rect x="25" y="45" width="160" height="25" rx="3" fill="#FFFFFF" stroke="#CBD5E1" />
    <text x="35" y="62" font-size="10" fill="#64748B">Username: "akhil"</text>
    <rect x="45" y="85" width="120" height="30" rx="4" fill="#2563EB" />
    <text x="105" y="105" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Login Button</text>
    <text x="105" y="140" font-size="10" font-family="monospace" fill="#1E40AF" text-anchor="middle">startActivity(intent)</text>

    <!-- Intent Arrow -->
    <path d="M 220 60 L 340 60" stroke="#D97706" stroke-width="3" marker-end="url(#arrow)" />
    <rect x="225" y="25" width="115" height="30" rx="4" fill="#FEF3C7" stroke="#F59E0B" />
    <text x="282" y="44" font-size="10" font-weight="bold" fill="#B45309" text-anchor="middle">Explicit Intent</text>
    <text x="282" y="78" font-size="9" font-family="monospace" fill="#451A03" text-anchor="middle">putExtra("USER", "akhil")</text>

    <!-- Activity 2 -->
    <rect x="360" y="0" width="210" height="160" rx="8" fill="#F0FDF4" stroke="#16A34A" stroke-width="2" />
    <text x="465" y="30" font-size="14" font-weight="bold" fill="#15803D" text-anchor="middle">MainActivity2 (Home)</text>
    <text x="465" y="65" font-size="12" font-weight="bold" fill="#0F172A" text-anchor="middle">"Welcome, akhil!"</text>
    <rect x="405" y="85" width="120" height="30" rx="4" fill="#DC2626" />
    <text x="465" y="105" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Logout</text>
    <text x="465" y="140" font-size="10" font-family="monospace" fill="#166534" text-anchor="middle">finish()</text>

    <!-- Return arrow -->
    <path d="M 360 115 L 220 115" stroke="#64748B" stroke-width="2" stroke-dasharray="4,3" marker-end="url(#arrow)" />
</g>
'''
create_svg("08_explicit_intent.svg", 650, 260, d8)

# 9. Implicit Intent Resolution
d9 = '''
<rect width="680" height="300" fill="#F8FAFC" rx="10" stroke="#CBD5E1" stroke-width="1.5" />
<text x="340" y="28" font-size="16" font-weight="bold" fill="#0F172A" text-anchor="middle">Implicit Intent Resolution &amp; Intent Filters</text>

<g transform="translate(30, 50)">
    <!-- Originating App -->
    <rect x="0" y="60" width="160" height="100" rx="6" fill="#EFF6FF" stroke="#2563EB" stroke-width="2" />
    <text x="80" y="90" font-size="13" font-weight="bold" fill="#1D4ED8" text-anchor="middle">My Application</text>
    <text x="80" y="115" font-size="11" font-family="monospace" fill="#0F172A" text-anchor="middle">ACTION_VIEW</text>
    <text x="80" y="135" font-size="10" font-family="monospace" fill="#64748B" text-anchor="middle">https://cet.ac.in</text>

    <!-- Android System Resolver -->
    <path d="M 165 110 L 230 110" stroke="#475569" stroke-width="2" marker-end="url(#arrow)" />
    <rect x="235" y="45" width="150" height="130" rx="8" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2" />
    <text x="310" y="75" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">Android OS</text>
    <text x="310" y="95" font-size="11" font-weight="bold" fill="#92400E" text-anchor="middle">PackageManager</text>
    <text x="310" y="120" font-size="10" fill="#451A03" text-anchor="middle">Matches Action,</text>
    <text x="310" y="135" font-size="10" fill="#451A03" text-anchor="middle">Data URI scheme,</text>
    <text x="310" y="150" font-size="10" fill="#451A03" text-anchor="middle">&amp; Category</text>

    <!-- Branching to Available Apps -->
    <path d="M 390 80 L 460 40" stroke="#475569" stroke-width="1.8" marker-end="url(#arrow)" />
    <path d="M 390 110 L 460 110" stroke="#475569" stroke-width="1.8" marker-end="url(#arrow)" />
    <path d="M 390 140 L 460 180" stroke="#475569" stroke-width="1.8" marker-end="url(#arrow)" />

    <!-- Target Handlers -->
    <rect x="465" y="15" width="160" height="50" rx="6" fill="#F0FDF4" stroke="#16A34A" />
    <text x="545" y="38" font-size="12" font-weight="bold" fill="#15803D" text-anchor="middle">Chrome Browser</text>
    <text x="545" y="53" font-size="9.5" fill="#64748B" text-anchor="middle">&lt;data android:scheme="https" /&gt;</text>

    <rect x="465" y="85" width="160" height="50" rx="6" fill="#F0FDF4" stroke="#16A34A" />
    <text x="545" y="108" font-size="12" font-weight="bold" fill="#15803D" text-anchor="middle">Firefox / Edge</text>
    <text x="545" y="123" font-size="9.5" fill="#64748B" text-anchor="middle">&lt;data android:scheme="https" /&gt;</text>

    <rect x="465" y="155" width="160" height="50" rx="6" fill="#EFF6FF" stroke="#3B82F6" />
    <text x="545" y="178" font-size="12" font-weight="bold" fill="#1D4ED8" text-anchor="middle">Default Handler</text>
    <text x="545" y="193" font-size="9.5" fill="#64748B" text-anchor="middle">App Chooser Dialog</text>
</g>
'''
create_svg("09_implicit_intent.svg", 680, 300, d9)

# 10. Intent Data Passing
d10 = '''
<rect width="660" height="240" fill="#F8FAFC" rx="10" stroke="#CBD5E1" stroke-width="1.5" />
<text x="330" y="28" font-size="16" font-weight="bold" fill="#0F172A" text-anchor="middle">Intent Data Exchange via Extras Key-Value Pairs</text>

<g transform="translate(35, 50)">
    <rect x="0" y="0" width="230" height="150" rx="6" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5" />
    <text x="115" y="25" font-size="13" font-weight="bold" fill="#1E40AF" text-anchor="middle">Sender (MainActivity)</text>
    <g font-family="monospace" font-size="11" fill="#0F172A">
        <text x="15" y="55">Intent i = new Intent(...);</text>
        <text x="15" y="80" fill="#D97706">i.putExtra("USER", "akhil");</text>
        <text x="15" y="105" fill="#D97706">i.putExtra("ID", 101);</text>
        <text x="15" y="130">startActivity(i);</text>
    </g>

    <!-- Bus -->
    <path d="M 235 75 L 345 75" stroke="#F59E0B" stroke-width="4" marker-end="url(#arrow)" />
    <rect x="245" y="35" width="90" height="30" rx="4" fill="#FEF3C7" stroke="#F59E0B" />
    <text x="290" y="55" font-size="10" font-weight="bold" fill="#B45309" text-anchor="middle">Intent Extras</text>

    <rect x="350" y="0" width="240" height="150" rx="6" fill="#F0FDF4" stroke="#22C55E" stroke-width="1.5" />
    <text x="470" y="25" font-size="13" font-weight="bold" fill="#166534" text-anchor="middle">Receiver (SecondActivity)</text>
    <g font-family="monospace" font-size="11" fill="#0F172A">
        <text x="365" y="55">Intent i = getIntent();</text>
        <text x="365" y="80" fill="#15803D">String u = i.getStringExtra(</text>
        <text x="385" y="100" fill="#15803D">"USER");</text>
        <text x="365" y="125" fill="#15803D">int id = i.getIntExtra("ID", 0);</text>
    </g>
</g>
'''
create_svg("10_intent_data_passing.svg", 660, 240, d10)

# 11. Bundle Structure
d11 = '''
<rect width="640" height="240" fill="#F8FAFC" rx="10" stroke="#CBD5E1" stroke-width="1.5" />
<text x="320" y="28" font-size="16" font-weight="bold" fill="#0F172A" text-anchor="middle">Android Bundle Data Container</text>
<g transform="translate(40, 50)">
    <rect x="0" y="0" width="560" height="150" rx="8" fill="#FFFFFF" stroke="#94A3B8" stroke-width="1.5" />
    <text x="280" y="25" font-size="13" font-weight="bold" fill="#1E293B" text-anchor="middle">Bundle object: Map&lt;String, Object&gt; (Parcelable key-value carrier)</text>
    <rect x="30" y="45" width="150" height="80" rx="4" fill="#EFF6FF" stroke="#3B82F6" />
    <text x="105" y="70" font-size="11" font-weight="bold" fill="#1D4ED8" text-anchor="middle">Key: "username"</text>
    <text x="105" y="95" font-size="12" font-family="monospace" fill="#0F172A" text-anchor="middle">"akhil" (String)</text>

    <rect x="205" y="45" width="150" height="80" rx="4" fill="#F0FDF4" stroke="#22C55E" />
    <text x="280" y="70" font-size="11" font-weight="bold" fill="#15803D" text-anchor="middle">Key: "roll_no"</text>
    <text x="280" y="95" font-size="12" font-family="monospace" fill="#0F172A" text-anchor="middle">24 (Integer)</text>

    <rect x="380" y="45" width="150" height="80" rx="4" fill="#FEF3C7" stroke="#F59E0B" />
    <text x="455" y="70" font-size="11" font-weight="bold" fill="#B45309" text-anchor="middle">Key: "is_enrolled"</text>
    <text x="455" y="95" font-size="12" font-family="monospace" fill="#0F172A" text-anchor="middle">true (Boolean)</text>
</g>
'''
create_svg("11_bundle_flow.svg", 640, 240, d11)

# 12. SharedPreferences Flow
d12 = '''
<rect width="660" height="280" fill="#F8FAFC" rx="10" stroke="#CBD5E1" stroke-width="1.5" />
<text x="330" y="28" font-size="16" font-weight="bold" fill="#0F172A" text-anchor="middle">SharedPreferences Persistent Storage Mechanism</text>
<g transform="translate(35, 50)">
    <!-- App RAM -->
    <rect x="0" y="0" width="220" height="180" rx="6" fill="#EFF6FF" stroke="#2563EB" stroke-width="1.5" />
    <text x="110" y="25" font-size="13" font-weight="bold" fill="#1D4ED8" text-anchor="middle">Application Process</text>
    <rect x="15" y="45" width="190" height="50" rx="4" fill="#FFFFFF" stroke="#93C5FD" />
    <text x="105" y="65" font-size="10.5" font-family="monospace" fill="#0F172A" text-anchor="middle">sp.edit().putString(...)</text>
    <text x="105" y="83" font-size="10.5" font-family="monospace" fill="#1E40AF" text-anchor="middle">.apply();</text>
    <rect x="15" y="110" width="190" height="50" rx="4" fill="#FFFFFF" stroke="#93C5FD" />
    <text x="105" y="130" font-size="10.5" font-family="monospace" fill="#0F172A" text-anchor="middle">sp.getString("user", "")</text>
    <text x="105" y="148" font-size="10.5" font-family="monospace" fill="#166534" text-anchor="middle">sp.clear();</text>

    <!-- Write / Read Arrows -->
    <path d="M 225 70 L 335 70" stroke="#16A34A" stroke-width="2.5" marker-end="url(#arrow)" />
    <text x="280" y="60" font-size="10" font-weight="bold" fill="#166534" text-anchor="middle">Write (apply)</text>

    <path d="M 335 135 L 225 135" stroke="#2563EB" stroke-width="2.5" marker-end="url(#arrow)" />
    <text x="280" y="125" font-size="10" font-weight="bold" fill="#1D4ED8" text-anchor="middle">Read (get)</text>

    <!-- Storage XML File -->
    <rect x="345" y="0" width="245" height="180" rx="6" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.5" />
    <text x="467" y="25" font-size="13" font-weight="bold" fill="#166534" text-anchor="middle">Internal Storage (Disk)</text>
    <text x="467" y="45" font-size="10" fill="#64748B" text-anchor="middle">/data/data/&lt;pkg&gt;/shared_prefs/MyPrefs.xml</text>
    <rect x="360" y="60" width="215" height="100" rx="4" fill="#FFFFFF" stroke="#CBD5E1" />
    <g font-family="monospace" font-size="10" fill="#334155">
        <text x="370" y="80">&lt;map&gt;</text>
        <text x="385" y="100" fill="#166534">&lt;string name="username"&gt;</text>
        <text x="400" y="120" fill="#0F172A">akhil&lt;/string&gt;</text>
        <text x="370" y="140">&lt;/map&gt;</text>
    </g>
</g>
'''
create_svg("12_shared_preferences_flow.svg", 660, 280, d12)

# 13. ListView and ArrayAdapter Relationship
d13 = '''
<rect width="680" height="280" fill="#F8FAFC" rx="10" stroke="#CBD5E1" stroke-width="1.5" />
<text x="340" y="28" font-size="16" font-weight="bold" fill="#0F172A" text-anchor="middle">Adapter Pattern: Data Source to ListView</text>
<g transform="translate(30, 50)">
    <!-- Data Source -->
    <rect x="0" y="20" width="170" height="140" rx="6" fill="#FEF3C7" stroke="#F59E0B" stroke-width="1.5" />
    <text x="85" y="45" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">Data Source</text>
    <g font-family="monospace" font-size="11" fill="#451A03">
        <text x="25" y="75">String[] arr = {</text>
        <text x="40" y="95">"Deepak",</text>
        <text x="40" y="115">"Subi", ...</text>
        <text x="25" y="135">};</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 175 90 L 225 90" stroke="#475569" stroke-width="2" marker-end="url(#arrow)" />

    <!-- ArrayAdapter -->
    <rect x="230" y="0" width="180" height="180" rx="6" fill="#EFF6FF" stroke="#2563EB" stroke-width="2" />
    <text x="320" y="30" font-size="14" font-weight="bold" fill="#1D4ED8" text-anchor="middle">ArrayAdapter</text>
    <text x="320" y="55" font-size="10.5" fill="#475569" text-anchor="middle">Binds data to row views</text>
    <rect x="245" y="70" width="150" height="40" rx="4" fill="#FFFFFF" stroke="#93C5FD" />
    <text x="320" y="88" font-size="10" fill="#1E40AF" text-anchor="middle">android.R.layout.</text>
    <text x="320" y="102" font-size="10" fill="#1E40AF" text-anchor="middle">simple_list_item_1</text>
    <text x="320" y="135" font-size="11" font-weight="bold" fill="#15803D" text-anchor="middle">getView() Method</text>
    <text x="320" y="155" font-size="10" fill="#64748B" text-anchor="middle">Recycles child views</text>

    <!-- Arrow 2 -->
    <path d="M 415 90 L 465 90" stroke="#475569" stroke-width="2" marker-end="url(#arrow)" />

    <!-- ListView -->
    <rect x="470" y="15" width="150" height="150" rx="6" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.5" />
    <text x="545" y="40" font-size="13" font-weight="bold" fill="#15803D" text-anchor="middle">ListView UI</text>
    <rect x="485" y="55" width="120" height="25" rx="3" fill="#FFFFFF" stroke="#CBD5E1" />
    <text x="545" y="72" font-size="10.5" fill="#0F172A" text-anchor="middle">Deepak</text>
    <rect x="485" y="85" width="120" height="25" rx="3" fill="#FFFFFF" stroke="#CBD5E1" />
    <text x="545" y="102" font-size="10.5" fill="#0F172A" text-anchor="middle">Subi</text>
    <rect x="485" y="115" width="120" height="25" rx="3" fill="#FFFFFF" stroke="#CBD5E1" />
    <text x="545" y="132" font-size="10.5" fill="#0F172A" text-anchor="middle">Misira</text>
</g>
'''
create_svg("13_listview_adapter.svg", 680, 280, d13)

# 14. Spinner Dropdown Flow
d14 = '''
<rect width="660" height="240" fill="#F8FAFC" rx="10" stroke="#CBD5E1" stroke-width="1.5" />
<text x="330" y="28" font-size="16" font-weight="bold" fill="#0F172A" text-anchor="middle">Spinner Dropdown &amp; OnItemSelectedListener Event Flow</text>
<g transform="translate(35, 50)">
    <rect x="0" y="20" width="160" height="110" rx="6" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5" />
    <text x="80" y="45" font-size="13" font-weight="bold" fill="#1D4ED8" text-anchor="middle">Fruit ArrayList</text>
    <text x="80" y="70" font-size="11" font-family="monospace" fill="#0F172A" text-anchor="middle">["Apple", "Mango",</text>
    <text x="80" y="90" font-size="11" font-family="monospace" fill="#0F172A" text-anchor="middle"> "Pineapple", ...]</text>

    <path d="M 165 75 L 220 75" stroke="#475569" stroke-width="2" marker-end="url(#arrow)" />

    <rect x="225" y="10" width="180" height="130" rx="6" fill="#FEF3C7" stroke="#F59E0B" stroke-width="1.5" />
    <text x="315" y="35" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">Spinner Widget</text>
    <rect x="240" y="50" width="150" height="30" rx="4" fill="#FFFFFF" stroke="#CBD5E1" />
    <text x="255" y="70" font-size="11" fill="#0F172A">Mango</text>
    <text x="375" y="70" font-size="11" fill="#64748B">▼</text>
    <text x="315" y="105" font-size="10" fill="#78350F" text-anchor="middle">User selects an item</text>

    <path d="M 410 75 L 465 75" stroke="#475569" stroke-width="2" marker-end="url(#arrow)" />

    <rect x="470" y="15" width="160" height="120" rx="6" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.5" />
    <text x="550" y="40" font-size="12" font-weight="bold" fill="#15803D" text-anchor="middle">Event Callback</text>
    <text x="550" y="65" font-size="10" font-family="monospace" fill="#166534" text-anchor="middle">onItemSelected()</text>
    <text x="550" y="95" font-size="10" fill="#0F172A" text-anchor="middle">tv.setText("Selected:")</text>
    <text x="550" y="115" font-size="10" fill="#2563EB" text-anchor="middle">Toast.show()</text>
</g>
'''
create_svg("14_spinner_adapter.svg", 660, 240, d14)

# 15. ScrollView Single-Child View Hierarchy
d15 = '''
<rect width="640" height="260" fill="#F8FAFC" rx="10" stroke="#CBD5E1" stroke-width="1.5" />
<text x="320" y="28" font-size="16" font-weight="bold" fill="#0F172A" text-anchor="middle">ScrollView Single Direct Child Rule</text>
<g transform="translate(40, 50)">
    <rect x="0" y="0" width="560" height="175" rx="8" fill="#EFF6FF" stroke="#2563EB" stroke-width="2" />
    <text x="280" y="25" font-size="13" font-weight="bold" fill="#1E40AF" text-anchor="middle">&lt;ScrollView android:layout_width="match_parent" android:layout_height="match_parent"&gt;</text>

    <rect x="30" y="40" width="500" height="120" rx="6" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.5" />
    <text x="280" y="60" font-size="12" font-weight="bold" fill="#166534" text-anchor="middle">Single Direct Child: &lt;LinearLayout android:orientation="vertical"&gt;</text>

    <g transform="translate(50, 75)">
        <rect x="0" y="0" width="95" height="35" rx="4" fill="#FFFFFF" stroke="#86EFAC" />
        <text x="47" y="22" font-size="10" fill="#0F172A" text-anchor="middle">Child Item 1</text>
        <rect x="115" y="0" width="95" height="35" rx="4" fill="#FFFFFF" stroke="#86EFAC" />
        <text x="162" y="22" font-size="10" fill="#0F172A" text-anchor="middle">Child Item 2</text>
        <rect x="230" y="0" width="95" height="35" rx="4" fill="#FFFFFF" stroke="#86EFAC" />
        <text x="277" y="22" font-size="10" fill="#0F172A" text-anchor="middle">Child Item 3</text>
        <rect x="345" y="0" width="115" height="35" rx="4" fill="#FFFFFF" stroke="#86EFAC" />
        <text x="402" y="22" font-size="10" fill="#0F172A" text-anchor="middle">Item N (Dynamic)</text>
    </g>
    <text x="280" y="145" font-size="10.5" fill="#475569" text-anchor="middle">Enables vertical scroll viewport when content height exceeds screen display</text>
</g>
'''
create_svg("15_scrollview_hierarchy.svg", 640, 260, d15)

# 16. Login Authentication Flowchart
d16 = '''
<rect width="640" height="360" fill="#F8FAFC" rx="10" stroke="#CBD5E1" stroke-width="1.5" />
<text x="320" y="28" font-size="16" font-weight="bold" fill="#0F172A" text-anchor="middle">Login Authentication Flowchart</text>
<g transform="translate(60, 50)">
    <rect x="180" y="0" width="160" height="35" rx="17" fill="#64748B" />
    <text x="260" y="22" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">User Clicks Login</text>

    <line x1="260" y1="35" x2="260" y2="60" stroke="#475569" stroke-width="2" marker-end="url(#arrow)" />

    <polygon points="260,60 360,95 260,130 160,95" fill="#FEF3C7" stroke="#F59E0B" stroke-width="1.5" />
    <text x="260" y="99" font-size="11" font-weight="bold" fill="#B45309" text-anchor="middle">Fields Empty?</text>

    <!-- Yes -> Error -->
    <path d="M 360 95 L 430 95" stroke="#DC2626" stroke-width="2" marker-end="url(#arrow)" />
    <rect x="435" y="77" width="110" height="35" rx="4" fill="#FEE2E2" stroke="#DC2626" />
    <text x="490" y="99" font-size="10.5" font-weight="bold" fill="#991B1B" text-anchor="middle">setError()</text>

    <!-- No -> Credentials check -->
    <line x1="260" y1="130" x2="260" y2="160" stroke="#475569" stroke-width="2" marker-end="url(#arrow)" />
    <polygon points="260,160 360,195 260,230 160,195" fill="#FEF3C7" stroke="#F59E0B" stroke-width="1.5" />
    <text x="260" y="199" font-size="11" font-weight="bold" fill="#B45309" text-anchor="middle">Valid User?</text>

    <!-- Invalid User -->
    <path d="M 360 195 L 430 195" stroke="#DC2626" stroke-width="2" marker-end="url(#arrow)" />
    <rect x="435" y="177" width="110" height="35" rx="4" fill="#FEE2E2" stroke="#DC2626" />
    <text x="490" y="199" font-size="10" font-weight="bold" fill="#991B1B" text-anchor="middle">Toast "Invalid"</text>

    <!-- Valid User -> Navigate -->
    <line x1="260" y1="230" x2="260" y2="260" stroke="#16A34A" stroke-width="2" marker-end="url(#arrow)" />
    <rect x="170" y="260" width="180" height="40" rx="6" fill="#16A34A" />
    <text x="260" y="285" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Start Home Activity</text>
</g>
'''
create_svg("16_login_flowchart.svg", 640, 360, d16)

# 17. Student Registration Flowchart
d17 = '''
<rect width="640" height="300" fill="#F8FAFC" rx="10" stroke="#CBD5E1" stroke-width="1.5" />
<text x="320" y="28" font-size="16" font-weight="bold" fill="#0F172A" text-anchor="middle">Student Registration Form Flowchart</text>
<g transform="translate(40, 50)">
    <rect x="0" y="20" width="150" height="70" rx="6" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5" />
    <text x="75" y="45" font-size="11" font-weight="bold" fill="#1D4ED8" text-anchor="middle">User Input</text>
    <text x="75" y="65" font-size="10" fill="#475569" text-anchor="middle">Name, Roll, Age</text>

    <path d="M 155 55 L 200 55" stroke="#475569" stroke-width="2" marker-end="url(#arrow)" />

    <rect x="205" y="20" width="150" height="70" rx="6" fill="#FDF4FF" stroke="#C026D3" stroke-width="1.5" />
    <text x="280" y="45" font-size="11" font-weight="bold" fill="#86198F" text-anchor="middle">Selections</text>
    <text x="280" y="65" font-size="10" fill="#475569" text-anchor="middle">Course &amp; Gender</text>

    <path d="M 360 55 L 405 55" stroke="#475569" stroke-width="2" marker-end="url(#arrow)" />

    <rect x="410" y="20" width="150" height="70" rx="6" fill="#FEF3C7" stroke="#D97706" stroke-width="1.5" />
    <text x="485" y="45" font-size="11" font-weight="bold" fill="#92400E" text-anchor="middle">Validation</text>
    <text x="485" y="65" font-size="10" fill="#475569" text-anchor="middle">Required Checks</text>

    <path d="M 485 95 L 485 140 L 300 140" stroke="#16A34A" stroke-width="2" marker-end="url(#arrow)" />

    <rect x="150" y="120" width="145" height="40" rx="6" fill="#16A34A" />
    <text x="222" y="145" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Display Summary</text>
</g>
'''
create_svg("17_student_reg_flowchart.svg", 640, 300, d17)

# 18. Shopping Cart State Flow
d18 = '''
<rect width="660" height="260" fill="#F8FAFC" rx="10" stroke="#CBD5E1" stroke-width="1.5" />
<text x="330" y="28" font-size="16" font-weight="bold" fill="#0F172A" text-anchor="middle">Shopping Cart Application Flowchart</text>
<g transform="translate(30, 50)">
    <rect x="0" y="25" width="140" height="70" rx="6" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5" />
    <text x="70" y="50" font-size="11" font-weight="bold" fill="#1D4ED8" text-anchor="middle">Select Product</text>
    <text x="70" y="70" font-size="10" fill="#475569" text-anchor="middle">Spinner Dropdown</text>

    <path d="M 145 60 L 195 60" stroke="#475569" stroke-width="2" marker-end="url(#arrow)" />

    <rect x="200" y="25" width="140" height="70" rx="6" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.5" />
    <text x="270" y="50" font-size="11" font-weight="bold" fill="#15803D" text-anchor="middle">Enter Quantity</text>
    <text x="270" y="70" font-size="10" fill="#475569" text-anchor="middle">Calculate Price</text>

    <path d="M 345 60 L 395 60" stroke="#475569" stroke-width="2" marker-end="url(#arrow)" />

    <rect x="400" y="25" width="160" height="70" rx="6" fill="#FEF3C7" stroke="#D97706" stroke-width="1.5" />
    <text x="480" y="50" font-size="11" font-weight="bold" fill="#92400E" text-anchor="middle">Add to ArrayList</text>
    <text x="480" y="70" font-size="10" fill="#475569" text-anchor="middle">Update Total Sum</text>

    <path d="M 480 100 L 480 140 L 340 140" stroke="#475569" stroke-width="2" marker-end="url(#arrow)" />

    <rect x="180" y="120" width="150" height="40" rx="6" fill="#4338CA" />
    <text x="255" y="145" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">View Cart (ListView)</text>
</g>
'''
create_svg("18_shopping_cart_flowchart.svg", 660, 260, d18)

# 19. Profile Manager Flowchart
d19 = '''
<rect width="660" height="260" fill="#F8FAFC" rx="10" stroke="#CBD5E1" stroke-width="1.5" />
<text x="330" y="28" font-size="16" font-weight="bold" fill="#0F172A" text-anchor="middle">User Profile Manager Data Flow</text>
<g transform="translate(35, 50)">
    <rect x="0" y="20" width="160" height="80" rx="6" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5" />
    <text x="80" y="45" font-size="11" font-weight="bold" fill="#1D4ED8" text-anchor="middle">Edit Profile Screen</text>
    <text x="80" y="65" font-size="10" fill="#475569" text-anchor="middle">Name, Email, Preferences</text>

    <path d="M 165 60 L 225 60" stroke="#16A34A" stroke-width="2" marker-end="url(#arrow)" />

    <rect x="230" y="20" width="160" height="80" rx="6" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.5" />
    <text x="310" y="45" font-size="11" font-weight="bold" fill="#15803D" text-anchor="middle">SharedPreferences</text>
    <text x="310" y="65" font-size="10" fill="#475569" text-anchor="middle">Key-Value Persist</text>

    <path d="M 395 60 L 455 60" stroke="#2563EB" stroke-width="2" marker-end="url(#arrow)" />

    <rect x="460" y="20" width="160" height="80" rx="6" fill="#FAF5FF" stroke="#9333EA" stroke-width="1.5" />
    <text x="540" y="45" font-size="11" font-weight="bold" fill="#6B21A8" text-anchor="middle">Profile View Screen</text>
    <text x="540" y="65" font-size="10" fill="#475569" text-anchor="middle">Auto-Load on Launch</text>
</g>
'''
create_svg("19_profile_manager_flowchart.svg", 660, 260, d19)

# 20. Multi-Page Portal Navigation & Dispatch Graph
d20 = '''
<rect width="680" height="340" fill="#F8FAFC" rx="10" stroke="#CBD5E1" stroke-width="1.5" />
<text x="340" y="28" font-size="16" font-weight="bold" fill="#0F172A" text-anchor="middle">Multi-Page Information &amp; Utility Portal Navigation Graph</text>
<g transform="translate(30, 45)">
    <!-- Central Dashboard -->
    <rect x="230" y="80" width="180" height="70" rx="8" fill="#1E293B" filter="url(#shadow)" />
    <text x="320" y="112" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Main Portal Hub</text>
    <text x="320" y="132" font-size="10" fill="#94A3B8" text-anchor="middle">Dashboard Activity</text>

    <!-- Outgoing paths -->
    <!-- Up: Student Profile -->
    <path d="M 320 80 L 320 40" stroke="#2563EB" stroke-width="2" marker-end="url(#arrow)" />
    <rect x="240" y="0" width="160" height="40" rx="6" fill="#EFF6FF" stroke="#2563EB" />
    <text x="320" y="25" font-size="11" font-weight="bold" fill="#1D4ED8" text-anchor="middle">Academic Profile Screen</text>

    <!-- Left: External CET Website -->
    <path d="M 230 115 L 140 115" stroke="#D97706" stroke-width="2" marker-end="url(#arrow)" />
    <rect x="0" y="95" width="135" height="40" rx="6" fill="#FEF3C7" stroke="#D97706" />
    <text x="67" y="115" font-size="10" font-weight="bold" fill="#B45309" text-anchor="middle">CET Website</text>
    <text x="67" y="128" font-size="9" fill="#78350F" text-anchor="middle">(Implicit Intent)</text>

    <!-- Right: Campus Maps -->
    <path d="M 410 115 L 490 115" stroke="#D97706" stroke-width="2" marker-end="url(#arrow)" />
    <rect x="495" y="95" width="135" height="40" rx="6" fill="#FEF3C7" stroke="#D97706" />
    <text x="562" y="115" font-size="10" font-weight="bold" fill="#B45309" text-anchor="middle">Campus Maps</text>
    <text x="562" y="128" font-size="9" fill="#78350F" text-anchor="middle">(Implicit Intent)</text>

    <!-- Down-Left: Calculator Utility -->
    <path d="M 280 150 L 200 200" stroke="#16A34A" stroke-width="2" marker-end="url(#arrow)" />
    <rect x="130" y="200" width="140" height="40" rx="6" fill="#F0FDF4" stroke="#16A34A" />
    <text x="200" y="225" font-size="11" font-weight="bold" fill="#15803D" text-anchor="middle">Calculator Utility</text>

    <!-- Down-Right: Settings & SharedPreferences -->
    <path d="M 360 150 L 440 200" stroke="#9333EA" stroke-width="2" marker-end="url(#arrow)" />
    <rect x="370" y="200" width="150" height="40" rx="6" fill="#FAF5FF" stroke="#9333EA" />
    <text x="445" y="225" font-size="11" font-weight="bold" fill="#6B21A8" text-anchor="middle">Settings &amp; Prefs</text>
</g>
'''
create_svg("20_portal_navigation.svg", 680, 340, d20)

print("Generated 20 professional vector SVG diagrams successfully.")
