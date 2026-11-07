package com.example.checkbox_and_radiobutton;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    Button b1;
    RadioGroup rg;
    RadioButton r1, r2;
    CheckBox e, m, h;
    TextView t;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        b1 = findViewById(R.id.submit);
        rg = findViewById(R.id.rg);
        r1 = findViewById(R.id.male);
        r2 = findViewById(R.id.female);
        e = findViewById(R.id.e);
        m = findViewById(R.id.m);
        h = findViewById(R.id.h);
        t = findViewById(R.id.tv);

        // Submit Button Click
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                StringBuilder result = new StringBuilder();

                // 1. Gender check
                int selectedGenderId = rg.getCheckedRadioButtonId();
                if (selectedGenderId != -1) {
                    RadioButton selectedGender = findViewById(selectedGenderId);
                    result.append("Gender: ").append(selectedGender.getText().toString()).append("\n");
                } else {
                    result.append("Gender: Not Selected\n");
                }

                // 2. Languages check
                StringBuilder langs = new StringBuilder();
                if (e.isChecked()) {
                    langs.append("English ");
                }
                if (m.isChecked()) {
                    langs.append("Malayalam ");
                }
                if (h.isChecked()) {
                    langs.append("Hindi ");
                }

                if (langs.length() > 0) {
                    result.append("Languages Known: ").append(langs.toString().trim());
                } else {
                    result.append("Languages Known: None selected");
                }

                // Display on screen
                t.setText(result.toString());

                Toast.makeText(MainActivity.this, "Submitted Successfully", Toast.LENGTH_SHORT).show();
            }
        });
    }
}
