package com.example.integrated.app2.v1;
import android.os.Bundle;
import android.widget.EditText;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    EditText etName, etRoll, etAge;
    @Override
    protected void onCreate(Bundle b) {
        super.onCreate(b);
        setContentView(R.layout.activity_main);
        etName = findViewById(R.id.etName);
        etRoll = findViewById(R.id.etRoll);
        etAge = findViewById(R.id.etAge);
    }
}