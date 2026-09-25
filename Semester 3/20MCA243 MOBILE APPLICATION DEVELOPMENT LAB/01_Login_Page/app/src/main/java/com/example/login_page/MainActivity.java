package com.example.login_page;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    EditText username, password;
    Button login;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        username = findViewById(R.id.username);
        password = findViewById(R.id.password);
        login = findViewById(R.id.login);

        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                String user = username.getText().toString();
                String pass = password.getText().toString();

                if (user.isEmpty()) {
                    username.setError("Enter username");
                } else if (pass.isEmpty()) {
                    password.setError("Enter password");
                } else if (pass.length() < 6) {
                    password.setError("Password must be at least 6 characters");
                } else if (user.equals("akhil") && pass.equals("akhil@123")) {
                    Toast.makeText(MainActivity.this, "Login Successful", Toast.LENGTH_SHORT).show();
                } else {
                    Toast.makeText(MainActivity.this, "Invalid credentials", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
}
