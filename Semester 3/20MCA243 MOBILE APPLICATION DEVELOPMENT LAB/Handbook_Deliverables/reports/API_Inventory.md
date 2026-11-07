# Android Framework Core API Inventory & Reference Guide
## 20MCA243 Mobile Application Development Lab

This comprehensive technical inventory documents the 30+ core Android framework APIs utilized across the **10 Original University Practical Programs**, the **5 Integrated Applications**, and their **25 Architectural Variations**.

---

## 1. UI Hierarchy & View Binding APIs

### 1.1 `setContentView(int layoutResID)`
- **Declaring Class:** `android.app.Activity` / `androidx.appcompat.app.AppCompatActivity`
- **Signature:** `public void setContentView(@LayoutRes int layoutResID)`
- **Purpose:** Inflates the specified XML layout resource file and attaches its root `ViewGroup` to the Activity's `Window` hierarchy.
- **Parameters:** `layoutResID` — A 32-bit hexadecimal integer resource pointer auto-generated in `R.layout` (e.g., `R.layout.activity_main`).
- **Return Type:** `void`
- **Execution Context:** Must be called inside `onCreate()` prior to invoking `findViewById()`.
- **Common Exception:** `android.view.InflateException` if the XML layout file contains syntax errors or unregistered custom views.
- **Example:**
  ```java
  @Override
  protected void onCreate(Bundle savedInstanceState) {
      super.onCreate(savedInstanceState);
      setContentView(R.layout.activity_main);
  }
  ```
- **Used In:** All Programs (01 through 10) & all Integrated Applications.

---

### 1.2 `findViewById(int id)`
- **Declaring Class:** `android.app.Activity` / `android.view.View`
- **Signature:** `public <T extends View> T findViewById(@IdRes int id)`
- **Purpose:** Traverses the active view hierarchy tree starting from the root node to locate and return the `View` element matching the specified resource ID.
- **Parameters:** `id` — Unique integer identifier defined in XML via `android:id="@+id/view_name"` and compiled into `R.id.view_name`.
- **Return Type:** Generic type `T extends View` (automatically cast in Java 8+). Returns `null` if no matching view is found.
- **Execution Context:** Must be invoked after `setContentView()`.
- **Common Exception:** `NullPointerException` when attempting to call methods on a view that returned `null` (e.g., if the ID belongs to a different layout).
- **Example:**
  ```java
  EditText username = findViewById(R.id.username);
  Button btnSubmit = findViewById(R.id.btnSubmit);
  ```
- **Used In:** All Programs (01 through 10) & all Integrated Applications.

---

### 1.3 `getText()`
- **Declaring Class:** `android.widget.TextView` (inherited by `EditText`, `Button`)
- **Signature:** `public CharSequence getText()`
- **Purpose:** Retrieves the current textual contents displayed inside the text view or editable input box.
- **Parameters:** None.
- **Return Type:** `CharSequence` (or `Editable` in `EditText`).
- **Execution Context:** Invoked synchronously on the UI thread, typically inside an event listener callback.
- **Common Pattern:** Requires `.toString()` to obtain a standard immutable Java `String`, and `.trim()` to strip leading/trailing whitespace.
- **Example:**
  ```java
  String input = etUsername.getText().toString().trim();
  ```
- **Used In:** Programs 01, 02, 03, 05, 06, 08, 09, 10.

---

### 1.4 `setError(CharSequence error)`
- **Declaring Class:** `android.widget.TextView` / `android.widget.EditText`
- **Signature:** `public void setError(CharSequence error)`
- **Purpose:** Displays an inline warning popup containing the error message and an error icon anchored to the right edge of the input field.
- **Parameters:** `error` — Text message describing the validation failure, or `null` to clear an existing error badge.
- **Return Type:** `void`
- **Execution Context:** Used extensively during defensive form validation before processing business logic.
- **Example:**
  ```java
  if (user.isEmpty()) {
      username.setError("Username cannot be empty");
      username.requestFocus();
      return;
  }
  ```
- **Used In:** Programs 01, 02, 03, 10, Integrated App 1, 2, 4.

---

## 2. Event Handling & Listener APIs

### 2.1 `setOnClickListener(View.OnClickListener l)`
- **Declaring Class:** `android.view.View`
- **Signature:** `public void setOnClickListener(@Nullable View.OnClickListener l)`
- **Purpose:** Registers an asynchronous callback listener to be invoked whenever the user taps or clicks on the view.
- **Parameters:** `l` — An implementation of the `View.OnClickListener` interface defining the `onClick(View v)` callback.
- **Return Type:** `void`
- **Execution Context:** Bound during activity initialization (`onCreate()`). Executes on the Main (UI) Thread.
- **Example:**
  ```java
  login.setOnClickListener(new View.OnClickListener() {
      @Override
      public void onClick(View view) {
          Toast.makeText(MainActivity.this, "Logging in...", Toast.LENGTH_SHORT).show();
      }
  });
  ```
- **Used In:** Programs 01, 02, 03, 05, 06, 08, 10, all Integrated Applications.

---

### 2.2 `setOnItemSelectedListener(AdapterView.OnItemSelectedListener listener)`
- **Declaring Class:** `android.widget.AdapterView` (inherited by `Spinner`, `ListView`)
- **Signature:** `public void setOnItemSelectedListener(AdapterView.OnItemSelectedListener listener)`
- **Purpose:** Registers a callback listener to capture selection changes in dropdown spinners or AdapterView containers.
- **Parameters:** `listener` — Implementation of `AdapterView.OnItemSelectedListener`, containing `onItemSelected()` and `onNothingSelected()`.
- **Return Type:** `void`
- **Execution Context:** Invoked automatically by the system when an item is selected or initial layout settles.
- **Example:**
  ```java
  spinner.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
      @Override
      public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
          String selectedItem = parent.getItemAtPosition(position).toString();
          Toast.makeText(MainActivity.this, "Selected: " + selectedItem, Toast.LENGTH_SHORT).show();
      }
      @Override
      public void onNothingSelected(AdapterView<?> parent) {}
  });
  ```
- **Used In:** Program 09 (Spinner), Integrated App 2 (Student Registration).

---

### 2.3 `setOnItemClickListener(AdapterView.OnItemClickListener listener)`
- **Declaring Class:** `android.widget.AdapterView` (inherited by `ListView`, `GridView`)
- **Signature:** `public void setOnItemClickListener(AdapterView.OnItemClickListener listener)`
- **Purpose:** Registers a callback invoked when a specific row item in an AdapterView is clicked.
- **Parameters:** `listener` — Implementation containing `onItemClick(AdapterView<?> parent, View view, int position, long id)`.
- **Return Type:** `void`
- **Used In:** Program 07 (ListView), Integrated App 3 (Shopping Cart).

---

## 3. Feedback & Notification APIs

### 3.1 `Toast.makeText(Context context, CharSequence text, int duration)`
- **Declaring Class:** `android.widget.Toast`
- **Signature:** `public static Toast makeText(Context context, CharSequence text, @Duration int duration)`
- **Purpose:** Factory method that instantiates a transient floating popup message for brief user feedback.
- **Parameters:**
  - `context`: The application or activity environment (`MainActivity.this` or `getApplicationContext()`).
  - `text`: The message string to be displayed.
  - `duration`: Display duration constant (`Toast.LENGTH_SHORT` = ~2 seconds, `Toast.LENGTH_LONG` = ~3.5 seconds).
- **Return Type:** A configured `Toast` instance.
- **Execution Context:** Must call `.show()` to schedule display on the system window manager.
- **Common Mistake:** Forgetting `.show()`, which constructs the Toast in memory without rendering it.
- **Example:**
  ```java
  Toast.makeText(MainActivity.this, "Login Successful", Toast.LENGTH_SHORT).show();
  ```
- **Used In:** All Programs (01 through 10) & all Integrated Applications.

---

### 3.2 `Log.d(String tag, String msg)`
- **Declaring Class:** `android.util.Log`
- **Signature:** `public static int d(String tag, String msg)`
- **Purpose:** Emits a debug log message into the system Logcat buffer, viewable in Android Studio.
- **Parameters:**
  - `tag`: Identifies the source component (conventionally class name or static constant).
  - `msg`: The diagnostic message text.
- **Return Type:** Integer representing the number of bytes written to the log buffer.
- **Example:**
  ```java
  Log.d("LifecycleEvent", "onStart() invoked: Activity is becoming visible.");
  ```
- **Used In:** Program 04 (Activity Lifecycle), Program 06, Program 10.

---

## 4. Intent & Inter-Component Navigation APIs

### 4.1 `new Intent(Context packageContext, Class<?> cls)` [Explicit Intent]
- **Declaring Class:** `android.content.Intent`
- **Signature:** `public Intent(Context packageContext, Class<?> cls)`
- **Purpose:** Constructs an explicit intent directly addressing a specific application component class to launch.
- **Parameters:**
  - `packageContext`: Calling Activity context (`this` or `MainActivity.this`).
  - `cls`: Destination component class token (e.g., `SecondActivity.class`).
- **Return Type:** Explicit `Intent` instance.
- **Example:**
  ```java
  Intent intent = new Intent(MainActivity.this, MainActivity2.class);
  startActivity(intent);
  ```
- **Used In:** Program 03 (Explicit Intent), all Integrated Applications.

---

### 4.2 `new Intent(String action, Uri uri)` [Implicit Intent]
- **Declaring Class:** `android.content.Intent`
- **Signature:** `public Intent(String action, Uri uri)`
- **Purpose:** Constructs an implicit intent declaring an abstract action and target data URI, delegating to the Android OS to resolve the matching application.
- **Parameters:**
  - `action`: Intent action string (e.g., `Intent.ACTION_VIEW`, `Intent.ACTION_DIAL`, `Intent.ACTION_SEND`).
  - `uri`: Data resource identifier constructed via `Uri.parse("https://cet.ac.in")` or `Uri.parse("tel:9876543210")`.
- **Return Type:** Implicit `Intent` instance.
- **Common Exception:** `ActivityNotFoundException` if no installed application can handle the action and URI. Must wrap in `try-catch`.
- **Example:**
  ```java
  Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://cet.ac.in"));
  try {
      startActivity(intent);
  } catch (ActivityNotFoundException e) {
      Toast.makeText(this, "No browser installed", Toast.LENGTH_SHORT).show();
  }
  ```
- **Used In:** Program 06 (Implicit Intent), Integrated App 5 (University Portal).

---

### 4.3 `putExtra(String name, String value)`
- **Declaring Class:** `android.content.Intent`
- **Signature:** `public Intent putExtra(String name, String value)`
- **Purpose:** Bundles a key-value pair of primitive or serializable data into the intent's `Bundle` payload for cross-activity transmission.
- **Parameters:**
  - `name`: Unique lookup key string.
  - `value`: Data value to transport.
- **Return Type:** The same `Intent` object (method chaining).
- **Extraction API:** `getIntent().getStringExtra("KEY_NAME")` or `getIntExtra("KEY_NAME", defaultValue)`.
- **Example:**
  ```java
  // Sender
  intent.putExtra("USER_NAME", user);
  startActivity(intent);

  // Receiver in SecondActivity
  String receivedUser = getIntent().getStringExtra("USER_NAME");
  ```
- **Used In:** Program 03 (Intent), Integrated Apps 1, 2, 3, 4, 5.

---

### 4.4 `startActivity(Intent intent)` & `finish()`
- **Declaring Class:** `android.app.Activity`
- **Signatures:**
  - `public void startActivity(Intent intent)`
  - `public void finish()`
- **Purpose:** `startActivity()` launches a new Activity; `finish()` terminates the current Activity and removes it from the task back stack.
- **Used In:** Program 03, Program 06, all Integrated Applications.

---

## 5. Persistence: SharedPreferences APIs

### 5.1 `getSharedPreferences(String name, int mode)`
- **Declaring Class:** `android.content.Context`
- **Signature:** `public SharedPreferences getSharedPreferences(String name, int mode)`
- **Purpose:** Retrieves or creates an XML file in private app storage (`/data/data/<package>/shared_prefs/`) for persistent key-value storage.
- **Parameters:**
  - `name`: Preferences file name (e.g., `"UserPrefs"`).
  - `mode`: Operating mode (typically `Context.MODE_PRIVATE` = `0`).
- **Return Type:** A thread-safe `SharedPreferences` instance.
- **Used In:** Program 10 (SharedPreferences), Integrated Apps 1, 4.

---

### 5.2 `SharedPreferences.Editor` (`edit()`, `putString()`, `apply()`, `commit()`)
- **Declaring Class:** `android.content.SharedPreferences.Editor`
- **Key Methods:**
  - `Editor edit()`: Opens an editing transaction.
  - `Editor putString(String key, String value)`: Stages a key-value pair.
  - `Editor remove(String key)`: Removes a specific key.
  - `Editor clear()`: Wipes all keys.
  - `void apply()`: Commits changes to in-memory cache immediately and writes to disk **asynchronously** (safe for UI thread).
  - `boolean commit()`: Writes to disk **synchronously** and returns a boolean (blocks UI thread; avoid on main thread).
- **Example:**
  ```java
  SharedPreferences sp = getSharedPreferences("UserPrefs", MODE_PRIVATE);
  sp.edit()
    .putString("NAME", name)
    .putString("EMAIL", email)
    .apply(); // Asynchronous disk write
  ```
- **Used In:** Program 10 (SharedPreferences), Integrated Apps 1, 4.

---

## 6. Adapter & Dynamic Collection APIs

### 6.1 `ArrayAdapter<T>(Context context, int resource, List<T> objects)`
- **Declaring Class:** `android.widget.ArrayAdapter<T>`
- **Signature:** `public ArrayAdapter(@NonNull Context context, @LayoutRes int resource, @NonNull List<T> objects)`
- **Purpose:** Constructs an adapter that binds an `ArrayList<T>` or array of objects to an `AdapterView` container row-by-row.
- **Parameters:**
  - `context`: Application or Activity environment.
  - `resource`: Layout resource for each row (e.g., `android.R.layout.simple_list_item_1` or `simple_spinner_dropdown_item`).
  - `objects`: The backing data collection.
- **Example:**
  ```java
  ArrayList<String> fruits = new ArrayList<>();
  fruits.add("Apple");
  fruits.add("Mango");
  ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, fruits);
  listView.setAdapter(adapter);
  ```
- **Used In:** Program 07 (ListView), Program 09 (Spinner), Integrated Apps 2, 3.

---

### 6.2 `notifyDataSetChanged()`
- **Declaring Class:** `android.widget.BaseAdapter` / `android.widget.ArrayAdapter`
- **Signature:** `public void notifyDataSetChanged()`
- **Purpose:** Notifies attached AdapterView observers that the underlying dataset has been modified (items added, removed, or edited), triggering an automatic UI re-render.
- **Execution Context:** Must be called on the UI thread whenever items are added or removed from the backing `ArrayList`.
- **Example:**
  ```java
  fruits.add(userEnteredFruit);
  adapter.notifyDataSetChanged(); // UI immediately reflects new item!
  etInput.setText(""); // Reset input field
  ```
- **Used In:** Program 07, Program 09, Integrated Apps 2, 3.

---

## 7. Activity Lifecycle Callback APIs

### 7.1 Lifecycle Callback Contract
All callbacks must chain to their superclass implementation (`super.onCallbackName()`), otherwise a `SuperNotCalledException` is thrown.

| Callback Method | Visibility & State | Mandatory Super Call | Primary Responsibility in Lab Practicals |
|---|---|---|---|
| `onCreate(Bundle b)` | Created (Not Visible) | `super.onCreate(b)` | Inflate layout (`setContentView`), bind views (`findViewById`), init listeners. |
| `onStart()` | Visible (Not Focused) | `super.onStart()` | Prepare animations, register UI observers, verify permissions. |
| `onResume()` | Active & In Focus | `super.onResume()` | Resume camera/sensors, restore form inputs, start animations. |
| `onPause()` | Partially Obscured | `super.onPause()` | Commit unsaved edits, pause animations, release camera. |
| `onStop()` | Completely Hidden | `super.onStop()` | Release heavy resources, write state to `SharedPreferences`. |
| `onRestart()` | Transitioning Stop $\to$ Start | `super.onRestart()` | Refresh dynamic list data after user returns to screen. |
| `onDestroy()` | Terminating / Finishing | `super.onDestroy()` | Nullify references, close database connections, cleanup threads. |

- **Used In:** Program 04 (Activity Life Cycle), Program 03, all Integrated Applications.
