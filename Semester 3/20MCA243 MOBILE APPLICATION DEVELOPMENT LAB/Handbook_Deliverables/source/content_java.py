"""
Content Module: Part II - Java Programming Fundamentals for Android
Provides clean, focused object-oriented and event-driven Java concepts
required for Android application development.
"""

def get_java_html():
    return '''
<div class="chapter-break"></div>
<div class="chapter-header">
    <div class="part-tag">PART II | JAVA PROGRAMMING FUNDAMENTALS FOR ANDROID</div>
    <h2 class="chapter-title">JAVA OBJECT-ORIENTED &amp; EVENT-DRIVEN FOUNDATIONS</h2>
</div>

<p class="lead-text">Android native development in Java builds extensively upon Object-Oriented Programming (OOP) paradigms, polymorphic inheritance hierarchies, interface-driven callbacks, dynamic collections, and exception handling. Mastering these targeted concepts is essential for understanding how the Android framework dispatches events and orchestrates component lifecycles.</p>

<div class="two-col">
    <div class="col-left">
        <h3>1. Class Inheritance in Android</h3>
        <p>In Android, every screen is created by sub-classing framework classes:</p>
        <pre><code>// Activity Hierarchy
public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}</code></pre>
        <p>The <code>super.onCreate(savedInstanceState)</code> call is mandatory; omitting it throws a <code>SuperNotCalledException</code> runtime crash.</p>

        <h3>2. Interfaces and Callback Listeners</h3>
        <p>Asynchronous event dispatching relies on Java interfaces:</p>
        <pre><code>// Defining Interface
public interface OnClickListener {
    void onClick(View v);
}

// Anonymous Implementation in Android
button.setOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View v) {
        // Callback method invoked on touch event
    }
});</code></pre>
    </div>
    <div class="col-right">
        <h3>3. Dynamic Collections: ArrayList&lt;E&gt;</h3>
        <p>Unlike fixed-length arrays, <code>ArrayList</code> provides resizeable collections used by adapters to power dynamic lists and spinners:</p>
        <pre><code>import java.util.ArrayList;

ArrayList&lt;String&gt; fruitList = new ArrayList&lt;&gt;();
fruitList.add("Apple");
fruitList.add("Mango");
fruitList.add("Banana");

// Accessing by index
String item = fruitList.get(0); // "Apple"
int count = fruitList.size();   // 3

// Iterating collection
for (String f : fruitList) {
    Log.d("Fruit", f);
}</code></pre>

        <h3>4. Defensive Exception Handling</h3>
        <p>Mobile applications must handle parsing and activity resolution errors gracefully without terminating the process:</p>
        <pre><code>try {
    double num = Double.parseDouble(inputStr);
    Intent intent = new Intent(Intent.ACTION_VIEW, uri);
    startActivity(intent);
} catch (NumberFormatException e) {
    editText.setError("Invalid numeric format");
} catch (ActivityNotFoundException e) {
    Toast.makeText(this, "No app available", Toast.LENGTH_SHORT).show();
}</code></pre>
    </div>
</div>
'''
