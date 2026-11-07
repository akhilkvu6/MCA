package com.example.integrated.app1.v3;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    EditText etUser, etPass;
    Button btnLogin;
    SharedPreferences sp;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        etUser = findViewById(R.id.etUser);
        etPass = findViewById(R.id.etPass);
        btnLogin = findViewById(R.id.btnLogin);

        sp = getSharedPreferences("AuthSession", MODE_PRIVATE);

        // Check if already logged in
        if (sp.getBoolean("isLoggedIn", false)) {
            Toast.makeText(this, "Welcome back, " + sp.getString("user", ""), Toast.LENGTH_SHORT).show();
        }

        btnLogin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String user = etUser.getText().toString().trim();
                String pass = etPass.getText().toString().trim();

                if (user.equals("admin") && pass.equals("1234")) {
                    SharedPreferences.Editor ed = sp.edit();
                    ed.putString("user", user);
                    ed.putBoolean("isLoggedIn", true);
                    ed.apply();
                    Toast.makeText(MainActivity.this, "Session Saved", Toast.LENGTH_SHORT).show();
                } else {
                    Toast.makeText(MainActivity.this, "Invalid Credentials", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
}