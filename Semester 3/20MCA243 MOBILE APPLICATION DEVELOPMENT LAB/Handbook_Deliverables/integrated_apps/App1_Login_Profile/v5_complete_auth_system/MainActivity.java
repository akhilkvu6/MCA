package com.example.integrated.app1.v5;

import android.content.Intent;
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

        sp = getSharedPreferences("UserSession", MODE_PRIVATE);
        // Automatic login if session exists
        if (sp.getBoolean("IS_LOGGED_IN", false)) {
            navigateToProfile(sp.getString("USERNAME", ""));
            return;
        }

        setContentView(R.layout.activity_main);
        etUser = findViewById(R.id.etUser);
        etPass = findViewById(R.id.etPass);
        btnLogin = findViewById(R.id.btnLogin);

        btnLogin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String user = etUser.getText().toString().trim();
                String pass = etPass.getText().toString().trim();

                if (user.isEmpty() || pass.isEmpty()) {
                    Toast.makeText(MainActivity.this, "Fill all fields", Toast.LENGTH_SHORT).show();
                    return;
                }

                if ((user.equals("akhil") && pass.equals("akhil@123")) ||
                    (user.equals("admin") && pass.equals("1234"))) {

                    SharedPreferences.Editor editor = sp.edit();
                    editor.putString("USERNAME", user);
                    editor.putBoolean("IS_LOGGED_IN", true);
                    editor.apply();

                    navigateToProfile(user);
                } else {
                    Toast.makeText(MainActivity.this, "Invalid Username or Password", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }

    private void navigateToProfile(String username) {
        Intent intent = new Intent(MainActivity.this, ProfileActivity.class);
        intent.putExtra("USERNAME", username);
        startActivity(intent);
        finish();
    }
}