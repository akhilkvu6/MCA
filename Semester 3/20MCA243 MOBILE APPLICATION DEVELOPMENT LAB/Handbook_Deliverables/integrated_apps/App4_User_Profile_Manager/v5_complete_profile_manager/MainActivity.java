package com.example.integrated.app4.v5;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    EditText etFullName, etEmail, etPhone;
    Switch swDarkTheme, swNotify;
    Button btnSave, btnReset;
    SharedPreferences sp;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        etFullName = findViewById(R.id.etFullName);
        etEmail = findViewById(R.id.etEmail);
        etPhone = findViewById(R.id.etPhone);
        swDarkTheme = findViewById(R.id.swDarkTheme);
        swNotify = findViewById(R.id.swNotify);
        btnSave = findViewById(R.id.btnSave);
        btnReset = findViewById(R.id.btnReset);

        sp = getSharedPreferences("UserProfilePrefs", MODE_PRIVATE);

        // Auto-load saved settings
        etFullName.setText(sp.getString("NAME", ""));
        etEmail.setText(sp.getString("EMAIL", ""));
        etPhone.setText(sp.getString("PHONE", ""));
        swDarkTheme.setChecked(sp.getBoolean("DARK_THEME", false));
        swNotify.setChecked(sp.getBoolean("NOTIFY", true));

        btnSave.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                SharedPreferences.Editor ed = sp.edit();
                ed.putString("NAME", etFullName.getText().toString());
                ed.putString("EMAIL", etEmail.getText().toString());
                ed.putString("PHONE", etPhone.getText().toString());
                ed.putBoolean("DARK_THEME", swDarkTheme.isChecked());
                ed.putBoolean("NOTIFY", swNotify.isChecked());
                ed.apply();
                Toast.makeText(MainActivity.this, "Profile Saved & Synced", Toast.LENGTH_SHORT).show();
            }
        });

        btnReset.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                sp.edit().clear().apply();
                etFullName.setText("");
                etEmail.setText("");
                etPhone.setText("");
                swDarkTheme.setChecked(false);
                swNotify.setChecked(false);
                Toast.makeText(MainActivity.this, "Settings Reset", Toast.LENGTH_SHORT).show();
            }
        });
    }
}