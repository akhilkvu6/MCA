package com.example.shared_preferences;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private static final String PREF_NAME = "MyPrefs";
    private static final String KEY_USER = "username";
    private static final String KEY_EMAIL = "email";

    EditText etUsername, etEmail;
    Button btnWrite, btnRead, btnClear;
    TextView txtStatus;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        etUsername = findViewById(R.id.et_username);
        etEmail = findViewById(R.id.et_email);
        btnWrite = findViewById(R.id.btn_write);
        btnRead = findViewById(R.id.btn_read);
        btnClear = findViewById(R.id.btn_clear);
        txtStatus = findViewById(R.id.txt_status);

        // Prefill default sample data from record
        etUsername.setText("demo1po");
        etEmail.setText("demo1@gmail.com");

        // Write to SharedPreferences
        btnWrite.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String user = etUsername.getText().toString().trim();
                String email = etEmail.getText().toString().trim();

                if (user.isEmpty() || email.isEmpty()) {
                    Toast.makeText(MainActivity.this, "Please enter both fields", Toast.LENGTH_SHORT).show();
                    return;
                }

                SharedPreferences sp = getSharedPreferences(PREF_NAME, MODE_PRIVATE);
                SharedPreferences.Editor editor = sp.edit();
                editor.putString(KEY_USER, user);
                editor.putString(KEY_EMAIL, email);
                editor.apply();

                txtStatus.setText("Written Data:\nUsername: " + user + "\nEmail: " + email);
                Toast.makeText(MainActivity.this, "Data Saved Successfully", Toast.LENGTH_SHORT).show();
            }
        });

        // Read from SharedPreferences
        btnRead.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                SharedPreferences sp = getSharedPreferences(PREF_NAME, MODE_PRIVATE);
                String user = sp.getString(KEY_USER, null);
                String email = sp.getString(KEY_EMAIL, null);

                if (user != null && email != null) {
                    txtStatus.setText("Loaded from SharedPreferences:\nUsername: " + user + "\nEmail: " + email);
                    Toast.makeText(MainActivity.this, "Data Loaded", Toast.LENGTH_SHORT).show();
                } else {
                    txtStatus.setText("Status: No data found in SharedPreferences");
                    Toast.makeText(MainActivity.this, "No saved data found", Toast.LENGTH_SHORT).show();
                }
            }
        });

        // Clear SharedPreferences
        btnClear.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                SharedPreferences sp = getSharedPreferences(PREF_NAME, MODE_PRIVATE);
                SharedPreferences.Editor editor = sp.edit();
                editor.clear();
                editor.apply();

                txtStatus.setText("Status: SharedPreferences cleared");
                Toast.makeText(MainActivity.this, "Data Cleared", Toast.LENGTH_SHORT).show();
            }
        });
    }
}
